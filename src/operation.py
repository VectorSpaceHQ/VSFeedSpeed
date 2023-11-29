import math

class Operation():
    def __init__(self, tool, material, width=None, doc=None):
        self.Pm = 0 # Power at motor
        self.E = 1.0 # Machine tool efficiency factor
        self.Kp = 1.0 # Power constant
        self.C = 1.0 # Feed factor
        self.Q = 1.0 # Metal removal rate
        self.W = 1.0 # Tool wear factor
        self.f = .01 # feed in inch per tooth (ipt) AKA chipload
        self.N = 0
        self.w = 2 # cut width (in)
        self.doc = .25 # depth of cut (in)
        self.ss = 0 # surface speed (ipm) or Cutting speed

        self.tool = tool
        self.material = material

        # self.get_surf_speed()
        # self.calc_feed()


    def calc_RPM(self):
        if (self.tool.D == None):
            print("Error: Tool diameter is not defined")
            return

        self.N = (12 * self.ss) / (math.pi * self.tool.D)
        self.N = rpm_round(self.N)
        print("RPM: {}, diameter: {}".format(self.N, self.tool.D))

    def calc_feedrate(self):
        self.calc_RPM()
        fm = self.f * self.tool.nt * self.N # milling machine table feed rate (ipm)
        self.fm = round(fm, 1)
        print("feedrate: {}".format(self.fm))

    def calc_power(self):
        self.get_power_constant()

        self.Q = self.fm * self.w * self.doc
        self.Pm = (self.Kp * self.C * self.Q * self.W) / self.E

    def set_operation(self):
        self.operation = ''

    def get_surf_speed(self):
        try:
            material_df = self.material.material_list

            print("HERE")
            print(self.tool.material)
            material_df = material_df[(material_df["Tool Material"] == self.tool.material)]

            print(material_df)
            sys.exit()
            # self.ss = self.material.material_dict['materials'][material]['operations']['End Milling']['tool_materials']['HSS']['s']
            # self.f = self.material.material_dict['materials'][material]['operations']['End Milling']['tool_materials']['HSS']['s']
            self.ss = self.material['s']
            self.f = self.material['f']
        except:
            print("Material not found. Surface speed and or chipload not acquired.")

    def get_feedrate(self):
        try:
            # self.op = self.material.material_dict['materials'][self.material.material]['operations']['End Milling']
            # self.tool_material = self.op['tool_materials']["HSS"]
            self.f = self.material['f'] * 0.001 # feed (in/tooth)
            self.s = self.material['s'] # surface speed in ft/min
        except Exception as e:
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


def rpm_round(x):
    if x < 1000:
        return int(round(x / 10.0)) * 10
    else:
        return int(round(x / 100.0)) * 100
