class Config:
    def __init__(self, file):
        self.file = "./tigr/doc/" + file

    def readConfig(self):
        import os
        from pathlib import Path
        from .ini_parser import IniPaser
        from .yaml_parser import YamlParser

        file = self.file
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
        return None