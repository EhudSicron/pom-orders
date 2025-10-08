# 1. Create a file called config.py
# 2. Copy this code to the file (config.py)
# 3. Call this function to get values from the config.ini file (Ex. user = ConfigReader.read_config('email', 'user'))
import configparser
import os
import sys


class ConfigReader:

    @staticmethod
    def read_config(section, key):
        root_dir = sys.path[0]
        print("start url")
        print(root_dir)
        # This gets the absolute path to the directory where reader.py is located.
        script_dir = os.path.dirname(os.path.abspath(__file__))

        # Use os.path.join() to construct a platform-independent path to config.ini.
        config_path = os.path.join(script_dir, 'config.ini')
        print(config_path)


        config = configparser.ConfigParser()
        #config.read(root_dir + '\config.ini')
        config.read(config_path)
        # Check that the Section & key exists
        if config.has_section(section) and config.has_option(section, key):
            return config[section][key]
        else:
            raise KeyError(f"Section '{section}' or key '{key}' not found in config.ini")