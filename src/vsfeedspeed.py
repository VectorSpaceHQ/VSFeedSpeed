#!/usr/bin/env python3
import yaml
import math
import numpy as np
import sys
import os
import csv
import pandas as pd
from tool import Tool
from material import Material
from operation import Operation

from PyQt5.QtWidgets import QMainWindow, QGraphicsView, QFileDialog, QApplication, QMessageBox
from mainwindow import Ui_vsfeedspeedgui


class MainWindow(QMainWindow):
    def __init__(self, app):
        QMainWindow.__init__(self)
        self.app = app
        self.ui = Ui_vsfeedspeedgui()
        self.ui.setupUi(self)

        self.tool = Tool()
        self.material = Material()
        self.operation = Operation(self.tool, self.material)

        # self.load_materials()
        self.load_table()
        self.connect_signals()

    def load_materials(self):

        with open("cutting_feed_speed_for_milling_aluminum.yaml", "r") as stream:
            try:
                self.material_dict = yaml.safe_load(stream)
                self.materials = []
                self.tool_materials = []
                for key, value in self.material_dict['materials'].items():
                    self.materials.append(key)
            except yaml.YAMLError as exc:
                print(exc)

    def load_table(self):

        self.table_data = pd.read_excel("./data/feed_speed_database.ods", engine="odf", sheet_name='non-metals')

        no_dupes = self.table_data.drop_duplicates(subset=['Material Family'])
        self.materials = no_dupes['Material Family']
        print(self.materials)


    def connect_signals(self):
        # Populate materials listbox
        for material in self.materials:
            self.ui.material_combo_box.addItem(material)

        self.ui.material_combo_box.textActivated.connect(self.set_material_family)
        self.ui.material_combo_box.textActivated.connect(self.populate_tool_materials)
        self.ui.material_combo_box.textActivated.connect(self.populate_operations)
        self.ui.material_species_combo_box.textActivated.connect(self.set_material_species)

        self.ui.tool_diameter_input.textChanged['QString'].connect(self.set_diameter)
        self.ui.tool_teeth_input.textChanged['QString'].connect(self.set_teeth)
        self.ui.tool_material_combo_box.textActivated.connect(self.set_tool_material)
        self.ui.operation_combo_box.textActivated.connect(self.set_operation)
        self.ui.doc_input.textChanged['QString'].connect(self.set_doc)
        self.ui.woc_input.textChanged['QString'].connect(self.set_woc)

        self.initialize_values()

    def initialize_values(self):
        self.ui.tool_teeth_input.setText("1")

    def populate_tool_materials(self):
        tool_materials = set(self.filtered_df['Tool Material'].tolist())
        for mat in tool_materials:
            self.ui.tool_material_combo_box.addItem(mat)

    def populate_operations(self):
        operations = set(self.filtered_df['Operation'].tolist())
        for op in operations:
            self.ui.operation_combo_box.addItem(op)

    def filter_materials(self, df):
        print("filtering materials...")
        filtered_df = df[df['Material Family'] == self.material.family]
        self.filtered_df = filtered_df

    def apply_filters(self):
        self.ui.feedrate_display.setText("N/A")
        self.ui.speed_display.setText("N/A")

        # self.table_data = self.table_data.filter(like=material, axis=0)
        filtered_df = self.table_data
        # filtered_df = filtered_df[filtered_df['Material Family'] == self.material.family]
        # filtered_df = filtered_df[filtered_df['DOC'] > self.operation.doc]

        if self.material.species:
            filtered_df = filtered_df[filtered_df['material species'] == self.material.species]

        # filter tools
        if self.tool.material:
            filtered_df = filtered_df[filtered_df['Tool Material'] == self.tool.material]

        try:
            filtered_df = filtered_df[filtered_df['Operation'] == self.operation.operation]
        except:
            pass

        filtered_df = self.filter_doc(filtered_df)
        filtered_df = self.filter_diameter(filtered_df)

        print("\nThere are {} results.".format(len(filtered_df)))
        print(filtered_df)
        self.filtered_df = filtered_df



        if len(filtered_df) == 2:
            self.interp_results(filtered_df)
        elif len(filtered_df) == 1:
            self.operation.f = float(filtered_df['Feed'])
            self.operation.ss = float(filtered_df['Speed'])


        try:
            self.set_feed_and_speed(filtered_df)
        except Exception as e:
            print("cannot calc feed and speed", e)

        # try:
        #     self.operation.calc_RPM()
        #     self.operation.calc_feedrate()
        #     self.ui.feedrate_display.setText(str(self.operation.fm))
        #     self.ui.speed_display.setText(str(self.operation.N))
        # except Exception as e:
        #     print("operation feedrate unknown", e)

    def interp_results(self, df):
        diameters = df['Cutter Diameter'].tolist()
        feeds = df['Feed'].tolist()
        speeds = df['Speed'].tolist()

        feed = np.interp(self.tool.D, diameters, feeds)
        speed = np.interp(self.tool.D, diameters, speeds)
        self.operation.f = round(feed, 4)
        self.operation.ss = round(speed, 4)

    def filter_doc(self, df):
        """
        Depth of Cut
        """
        try:
            no_dupes = df.drop_duplicates(subset=['DOC'])
            no_dupes = no_dupes.dropna(subset=['DOC'])
            docs = no_dupes['DOC'].tolist()
            doc_low = find_nearest_low(docs, self.operation.doc)
            doc_high = find_nearest_high(docs, self.operation.doc)
            df = df[(df['DOC'] == doc_low) | (df['DOC'] == doc_high)]
        except Exception as e:
            print("cant calc doc", e)
        return df

    def filter_diameter(self, df):
        try:
            no_dupes = df.drop_duplicates(subset=['Cutter Diameter'])
            no_dupes = no_dupes.dropna(subset=['Cutter Diameter'])
            diams = no_dupes['Cutter Diameter'].tolist()
            diam_low = find_nearest_low(diams, self.tool.D)
            diam_high = find_nearest_high(diams, self.tool.D)
            print(diam_low, diam_high)
            df = df[(df['Cutter Diameter'] == diam_low) | (df['Cutter Diameter'] == diam_high)]
        except Exception as e:
            print("cant calc cutter diameter", e)
        return df


    def set_material_family(self):
        # if work material changes, reset the df filters. Otherwise species disappear
        print("\n\nmaterial family changed!\n\n")
        self.filtered_df = self.table_data

        self.material.reset()
        self.material.set_material(self.ui.material_combo_box.currentText())
        self.filter_materials(self.filtered_df)
        self.populate_species()

    def populate_species(self):
        # given the current material family selection, populate dropdown with all possible species
        self.ui.material_species_combo_box.clear()
        species = set(self.filtered_df['material species'].tolist())
        for s in species:
            self.ui.material_species_combo_box.addItem(s)

    def set_material_species(self):
        print("SET MATERIAL SPECIES")
        self.material.species = self.ui.material_species_combo_box.currentText()
        self.apply_filters()


    def set_diameter(self):
        d = self.ui.tool_diameter_input.displayText()
        if not d or d == '.':
            d = 0.0

        try:
            self.tool.D = float(d)
            # update DOC accordingly
            self.set_doc(self.tool.D)
        except:
            pass
        self.apply_filters()

    def set_teeth(self):
        t = self.ui.tool_teeth_input.displayText()
        if not t:
            t = 1
        self.tool.nt = float(t)
        self.update()

    def set_tool_material(self):
        # self.tool_material = self.op['tool_materials']["HSS"]
        self.tool.material = self.ui.tool_material_combo_box.currentText()
        self.apply_filters()

    def set_operation(self):
        self.operation.operation = self.ui.operation_combo_box.currentText()
        self.apply_filters()

    def set_doc(self, doc=None):
        if doc == None:
            doc = float(self.ui.doc_input.displayText())
        else:
            self.ui.doc_input.setText(str(doc))
        try:
            self.operation.doc = doc
            self.apply_filters()
        except:
            pass

    def set_woc(self):
        try:
            self.operation.w = float(self.ui.woc_input.displayText())
        except:
            pass

    def set_feed_and_speed(self, df):
        """
        Interpolate the feed and speed, then set them in the display.
        """
        print("\n\nSetting feed and speed\n\n")

        if len(df) == 2:
            diameters = df['Cutter Diameter'].tolist()
            feeds = df['Feed'].tolist()
            speeds = df['Speed'].tolist()
            feed = np.interp(self.tool.D, diameters, feeds)
            speed = np.interp(self.tool.D, diameters, speeds)
            self.operation.f = round(feed, 4)
            self.operation.ss = round(speed, 4)
        elif len(df) == 1:
            self.operation.f = float(df['Feed'])
            self.operation.ss = float(df['Speed'])
        else:
            print("Too many results.")

        self.operation.calc_RPM()
        self.operation.calc_feedrate()

        self.ui.feedrate_display.setText(str(self.operation.fm))
        self.ui.speed_display.setText(str(self.operation.N))


    def update(self):
        self.apply_filters()














def calc_feedrate(material, tool):
    chipload = get_chipload(material, tool)
    feedrate = tool.rpm * tool.flutes * chipload
    feedrate = int(feedrate)
    tool.feedrate = feedrate



def get_chipload(material, tool):
    diameters = list(material.material_dict[material.material]['chipload'].keys())
    chiploads = list(material.material_dict[material.material]['chipload'].values())

    print(diameters, chiploads)
    chipload = np.interp(tool.diameter, diameters, chiploads)
    # for d, load in chiploads.items():
    #     if d < tool.diameter:
    #         chipload = load
    return chipload

def find_nearest_low(array, value):
    idx = 0
    max_val = 0
    for i, x in enumerate(array):
        if x == value:
            return value
        elif (value - x) > 0:
            if x > max_val:
                max_val = x
                idx = i
    return array[idx]

def find_nearest_high(array, value):
    idx = len(array)-1
    min_val = max(array)
    for i, x in enumerate(array):
        if x == value:
            return value
        if (value - x) < 0:
            if x < min_val:
                min_val = x
                idx = i
    return array[idx]

# def main():
#     example_plywood()
#     # example_3()


def example_plywood():
    mytool = Tool()
    mytool.D = 4 / 25.4 # inches diameter
    mytool.flutes = 2
    mytool.material = "HSS"

    mymaterial = Material()
    mymaterial.set_material('MDF')

    myop = Operation(mytool, mymaterial, width=mytool.D, doc=.25)

    print(mymaterial.material)
    print("Speed: {} RPM, Feedrate: {} in/min".format(myop.N, myop.fm))
    print("TEST")

def example_3():
    """
    Example 3, pg 190 Machinery's handbook Guide
    """
    mymaterial = Material('Plain Carbon Steel')
    mytool = Tool(diameter=3, flutes = 8)

    myop = Operation(mytool, mymaterial, width=2, doc=.25)
    myop.get_feedrate()
    myop.calc_speed()
    myop.calc_feed()
    print("Speed: {} RPM, Feedrate: {} in/min".format(myop.N, myop.fm))
    myop.get_power_constant()


if __name__ == '__main__':
    # example_plywood()

    app = QApplication(sys.argv)
    window = MainWindow(app)
    window.show()
    sys.exit(app.exec_())
