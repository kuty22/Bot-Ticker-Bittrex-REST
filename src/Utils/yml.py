import yaml

def loadYaml(config):
    with open(config, 'r') as yaml_file:
        res = yaml.load(yaml_file)
        return res
