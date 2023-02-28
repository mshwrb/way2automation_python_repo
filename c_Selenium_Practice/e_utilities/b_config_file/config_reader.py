from configparser import ConfigParser


def read_config(file_name, section, key):
    config = ConfigParser()
    config.read(file_name)
    return config.get(section, key)


print(read_config("config.ini", "LOCATORS LOGIN PAGE", "username__XPATH"))
print(str("username__XPATH").split("__")[1])
print(read_config("config.ini", "BASIC INFO", "explicit wait"))
