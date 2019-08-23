import yaml

class YamlParser:
    def __init__(self, file):
        self.file = file

    def readFile(self):
        try:
            f = open(self.file)
            result = yaml.safe_load(f)
            f.close()
            return result
        except FileNotFoundError:
            print('The file cannot be found')