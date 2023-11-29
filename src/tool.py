#!/usr/bin/env python3

class Tool():
    def __init__(self, diameter=None, flutes=1, material=None):
        self.D = diameter # Diameter (inches)
        self.flutes = flutes # Number of flutes
        self.nt = flutes
        self.stickout = 0.0
        self.material = material
        self.rpm = 0
        self.chipload = 0
        self.sf = 1


    def adjust_sf(self):
        pass
