import os
class Config:
    def __init__(self, file):
        self.file = file
        self.path = "./tigr/doc/"


    def readConfig(self):

        from pathlib import Path
        from .ini_parser import IniPaser
        from .yaml_parser import YamlParser
        from .ConfigException import ConfigException

        file = self.file
        if self.checkFileOrDirector() == False:
            file = self.path + self.file

        if os.path.isfile(file):
            suffix = file[file.rindex('.'):]
            if (suffix in ['.yaml', '.yml']):
                yamlParser = YamlParser(file)
                return yamlParser.readFile()
            elif (suffix == '.ini'):
                iniPaser = IniPaser(file)
                return iniPaser.readFile()
            else:
                print('The format of file should be *.ini, *.yaml or *.yml')
                raise ConfigException()
            return None
        else:
            print('The config file does not exist')
            raise ConfigException()

    def checkFileOrDirector(self):
        if os.path.isfile(self.file):
            return True
        return False