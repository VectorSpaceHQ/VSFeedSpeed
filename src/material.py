class Material():
    def __init__(self, material=None):
        # super().__init__()
        self.name = ''
        self.hardness = 1.0
        self.surface_speed = 1.0 #ft/min
        self.family = None
        self.species = None

        # with open("mdf_data.yaml", "r") as stream:
        # # with open("cutting_feed_speed_for_milling_aluminum.yaml", "r") as stream:
        #     try:
        #         self.material_dict = yaml.safe_load(stream)
        #     except yaml.YAMLError as exc:
        #         print(exc)


        # self.material_list_complete = pd.read_csv('./data/mdf.csv')
        # self.material_list = self.material_list_complete
        # print(self.material_list)

        # print(self.filter(self.material_list, "Material Family", "wood"))

        if material:
            self.set_material(material)

    def set_material(self, family):
        self.family = family
        # self.material_list = self.material_list[
        #     (self.material_list["material species"] == material)]

        # if len(self.material_list) == 0:
        #     print("Error: No matching materials found in database.")

    def reset(self):
        self.family = None
        self.species = None
