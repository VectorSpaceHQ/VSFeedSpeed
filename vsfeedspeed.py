#!/usr/bin/env python3
import yaml
import math
import numpy as np


class tool():
    def __init(self):
        diameter = 0.0 #inches
        stickout = 0.0
        self.flutes = 1
        material = 'HSS'
        self.rpm = 0
        self.chipload = 0
        self.sf = 1

    def adjust_sf(self):
        pass


class material():
    def __init__(self):
        name = ''
        hardness = 1.0
        surface_speed = 1.0 #ft/min

        with open("material_database.yaml", "r") as stream:
            try:
                self.material_dict = yaml.safe_load(stream)
            except yaml.YAMLError as exc:
                print(exc)

    def set_material(self, material):
        self.material = material
        print(self.material)

        try:
            self.surface_speed = self.material_dict[material]['surface_speed']
        except:
            print("Material not found")




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

def calc_speed(material, tool):
    rpm = material.surface_speed / (math.pi * tool.diameter / 12.)
    tool.rpm = rpm_round(rpm)

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
    mytool = tool()
    mytool.diameter = 4 / 25.4 # inches
    mytool.flutes = 2

    mymaterial = material()
    mymaterial.set_material('plywood')

    calc_speed(mymaterial, mytool)
    calc_feedrate(mymaterial, mytool)

    print(mymaterial.material, mytool.rpm, mytool.feedrate)




if __name__ == '__main__':
    main()
