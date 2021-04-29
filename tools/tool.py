import json
import os


class ScenarioTool:
    def __init__(self, scenario_filename):
        self.scenario_filename = scenario_filename
        self.scenario_json = None
        self.pedestrian_json = None

    def load(self):
        with open(self.scenario_filename) as scenario_fd:
            self.scenario_json = json.load(scenario_fd)

    def add_ped(self, ped_filename):
        with open(ped_filename) as ped_fd:
            file_basename= os.path.basename(self.scenario_filename)
            self.scenario_json["name"] = file_basename.split('.')[0] + "_modify"
            pedestrian_json = json.load(ped_fd)
            for target in self.scenario_json["scenario"]["topography"]["targets"]:
                pedestrian_json["targetIds"].append(target["id"])
            self.scenario_json["scenario"]["topography"]["dynamicElements"].append(pedestrian_json)

    def save(self, save_filename):
        with open(save_filename, 'w') as save_fd:
            json.dump(self.scenario_json, save_fd)


if __name__ == "__main__":
    s_tool = ScenarioTool("../scenario/MyFristScenario.scenario")
    s_tool.load()
    s_tool.add_ped("../scenario/pedestrian.json")
    s_tool.save("../scenario/MyFristScenario_Modified.scenario")
