class ConfigException(Exception):
    def __init__(self, err='The config file is invalid'):
        Exception.__init__(self, err)