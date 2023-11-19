import json

class JSONFileEditor:

    def __init__(self, file_path):
        self.file_path = file_path+".json"
        self.data = self._load_data()

    def _load_data(self):
        try:
            with open(self.file_path, 'r') as file:
                data = json.load(file)
            return data
        except (FileNotFoundError, json.JSONDecodeError):
            try:
                with open(self.file_path, 'w') as file:
                   data = json.load(file)
                return data
            except:
                print("Error while creating File")
                return {}

    def save(self):
        with open(self.file_path, 'w') as file:
            json.dump(self.data, file, indent=4)

    def get_value(self, key, default=None):
        return self.data.get(key, default)

    def set_value(self, key, value):
        self.data[key] = value

    def update_value(self, key, new_value):
        if key in self.data:
            self.data[key] = new_value
        else:
            raise KeyError(f"'{key}' not found in the JSON data.")
        
    def add_value(self, key, value):
        if key in self.data:
            raise KeyError(f"'{key}' already present in the JSON data.")
        else:
            self.data[key] = value
            
    def append_value(self, key, value):
        if key in self.data:
            if isinstance(self.data[key], list):
                self.data[key].append(value)
            else:
                raise TypeError(f"'{key}' is not a list in the JSON data.")
        else:
            self.data[key] = [value]

    def delete_key(self, key):
        if key in self.data:
            del self.data[key]
        else:
            raise KeyError(f"'{key}' not found in the JSON data.")

