

class IniPaser:
    def __init__(self, file):
        self.file = file

    def readFile(self):
        import configparser
        config = configparser.ConfigParser()
        config.read(self.file)
        result = {}
        for k, v in config.items('default'):
            result[k] = v
        return result
#
# if __name__ == '__main__':
#     parser = IniPaser('config.ini')
#     print(parser.readFile())