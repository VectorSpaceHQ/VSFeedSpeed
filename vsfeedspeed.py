#!/usr/bin/env python3
import yaml
import math
import numpy as np
import sys
import os
import csv
import pandas as pd

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

        self.load_materials()
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
        self.table_data = pd.read_csv('table_15a.csv')
        print(self.table_data)
        
    
    def connect_signals(self):
        # Populate materials listbox
        for material in self.materials:
            self.ui.material_combo_box.addItem(material)

        self.ui.material_combo_box.textActivated.connect(self.set_work_material)
        self.ui.material_combo_box.textActivated.connect(self.populate_tool_materials)
        
        self.ui.tool_diameter_input.textChanged['QString'].connect(self.set_diameter)
        self.ui.tool_teeth_input.textChanged['QString'].connect(self.set_teeth)
        self.ui.tool_material_combo_box.textActivated.connect(self.set_tool_material)
        self.ui.operation_input.textChanged['QString'].connect(self.set_operation)
        self.ui.doc_input.textChanged['QString'].connect(self.set_doc)
        self.ui.woc_input.textChanged['QString'].connect(self.set_woc)


    def populate_tool_materials(self):
        pass
        # for key,v in self.material_dict.items():
        #     print(key,v)

    def apply_filters(self):
        # self.table_data = self.table_data.filter(like=material, axis=0)
        filtered_df = self.table_data
        filtered_df = filtered_df[filtered_df['Material'] == self.material]
        filtered_df = filtered_df[filtered_df['DOC'] > self.operation.doc]

        # df_sort = filtered_df.iloc[(filtered_df['DOC']-self.operation.doc).abs().argsort()[:2]]
        # print(df_sort)
        # print()
        print(filtered_df)
            
    def set_work_material(self):
        self.material = self.ui.material_combo_box.currentText()
        self.apply_filters()
        
    def set_diameter(self):
        d = self.ui.tool_diameter_input.displayText()
        if not d:
            d = 0
        self.tool.D = float(d)
        
        self.operation.get_feedrate()

    def set_teeth(self):
        t = self.ui.tool_teeth_input.displayText()
        if not t:
            t = 0
        self.tool.nt = float(t)
        
    def set_tool_material(self):
        # self.tool_material = self.op['tool_materials']["HSS"]
        self.tool.material = self.ui.tool_material_input.displayText()
        
    def set_operation(self):
        self.operation.operation = self.ui.operation_input.displayText()
        
    def set_doc(self):
        try:
            doc = float(self.ui.doc_input.displayText())
            self.operation.doc = doc
            self.apply_filters()
        except:
            pass
        
    def set_woc(self):
        try:
            self.operation.w = float(self.ui.woc_input.displayText())
        except:
            pass
        

            
class Operation():
    def __init__(self, tool, material, width=None, doc=None):
        self.Pm = 0 # Power at motor
        self.E = 1.0 # Machine tool efficiency factor
        self.Kp = 1.0 # Power constant
        self.C = 1.0 # Feed factor
        self.Q = 1.0 # Metal removal rate
        self.W = 1.0 # Tool wear factor
        ft = 1 # feed in inch per tooth (ipt)
        nt = 1 # number of teeth per milling cutter
        self.N = 0
        self.w = 2 # cut width (in)
        self.doc = .25 # depth of cut (in)

        self.tool = tool
        self.material = material


    def calc_speed(self):
        self.N = (12 * self.s) / (math.pi * self.tool.D)
        self.N = rpm_round(self.N)
        
    def calc_feed(self):
        self.fm = self.f * self.tool.nt * self.N # milling machine table feed rate (ipm)
        
    def calc_power(self):
        self.get_power_constant()
        
        self.Q = self.fm * self.w * self.doc
        self.Pm = (self.Kp * self.C * self.Q * self.W) / self.E

    def set_operation(self):
        self.operation = ''
        
    def get_surf_speed(self):
        try:
            self.surface_speed = material.material_dict['materials'][material]['operations']['End Milling']['tool_materials']['HSS']['s']
        except:
            print("Material not found")
            
    def get_feedrate(self):
        try:
            # self.op = self.material.material_dict['materials'][self.material.material]['operations']['End Milling']
            # self.tool_material = self.op['tool_materials']["HSS"]
            self.f = self.material['f'] * 0.001 # feed (in/tooth)
            self.s = self.material['s'] # surface speed in ft/min
        except Error as e:
            print("get_feedrate failed", e)
            
    def get_power_constant(self):
        """
        Once material is known, lookup power constant
        """
        with open("power_constants.yaml", "r") as stream:            
            try:
                power_constants = yaml.safe_load(stream)
            except yaml.YAMLError as exc:
                print(exc)

        self.Kp = power_constants["Material"][self.material.material]["Brinell Hardness"][100]['Kp']

        
class Tool():
    def __init__(self, diameter=None, flutes=None):
        self.D = diameter # Diameter (inches)
        self.flutes = flutes # Number of flutes
        self.nt = flutes
        stickout = 0.0
        material = 'HSS'
        self.rpm = 0
        self.chipload = 0
        self.sf = 1

    def adjust_sf(self):
        pass
    

class Material(Tool):
    def __init__(self, material=None):
        super().__init__()
        name = ''
        hardness = 1.0
        surface_speed = 1.0 #ft/min

        # with open("material_database.yaml", "r") as stream:
        with open("cutting_feed_speed_for_milling_aluminum.yaml", "r") as stream:            
            try:
                self.material_dict = yaml.safe_load(stream)
                # print(self.material_dict)
            except yaml.YAMLError as exc:
                print(exc)
                
        if material:
            self.set_material(material)

    def set_material(self, material):
        self.material = material



def rpm_round(x):
    if x < 1000:
        return int(round(x / 10.0)) * 10
    else:
        return int(round(x / 100.0)) * 100

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


def main():
    example_3()


def example_plywood():
    mytool = tool()
    mytool.diameter = 4 / 25.4 # inches
    mytool.flutes = 2

    mymaterial = material()
    mymaterial.set_material('plywood')

    calc_speed(mymaterial, mytool)
    calc_feedrate(mymaterial, mytool)

    print(mymaterial.material, mytool.rpm, mytool.feedrate)

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
    app = QApplication(sys.argv)
    window = MainWindow(app)
    window.show()
    sys.exit(app.exec_())
    
    main()
