from src.utils import load_config, set_configs, load_tasksplanner_json, create_tasksnew_json, create_changedbucketes_json
from src import utils

# Função principal
def main(config_path):
    load_config(config_path)
    set_configs()
    if utils.opion_created or utils.opion_modified:
        load_tasksplanner_json()
        if utils.opion_created: create_tasksnew_json()
        if utils.opion_modified: create_changedbucketes_json()
    exit()