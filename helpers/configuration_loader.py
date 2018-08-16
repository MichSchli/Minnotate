class ConfigurationLoader:

    def load(self, filename):
        configuration_dictionary = {}
        for line in open(filename, 'r'):
            line = line.strip()
            if line:
                parts = line.split("=")
                setting_name = parts[0].strip()
                setting_value = parts[1].strip()
                configuration_dictionary[setting_name] = setting_value

        return configuration_dictionary
