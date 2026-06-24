class MyDict:
    def __init__(self):
        self._keys = []
        self._values = []
    
    def __getitem__(self, key):
        try:
            index = self._keys.index(key)
            return self._values[index]
        except ValueError:
            return None
    
    def __setitem__(self, key, value):
        try:
            index = self._keys.index(key)
            self._values[index] = value
        except ValueError:
            self._keys.append(key)
            self._values.append(value)
    
    def __delitem__(self, key):
        try:
            index = self._keys.index(key)
            del self._keys[index]
            del self._values[index]
        except ValueError:
            pass
    
    def keys(self):
        return self._keys
    
    def values(self):
        return self._values
    
    def items(self):
        return list(zip(self._keys, self._values))
    
    def __len__(self):
        return len(self._keys)
    
    def __contains__(self, key):
        return key in self._keys
    
    def __str__(self):
        temp = [f"{repr(k)}: {repr(v)}" for k, v in self.items()]
        return "{" + ", ".join(temp) + "}"
    
    def get(self, key, defualt=None):
        try:
            index = self._keys.index(key)
            return self._values[index]
        except ValueError:
            return defualt
    
    def pop(self, key, defualt=None):
        try:
            index = self._keys.index(key)
            value = self._values[index]
            del self._keys[index]
            del self._values[index]
            return value
        except ValueError:
            return defualt
    
    def clear(self):
        self._keys.clear()
        self._values.clear()

    def update(self, dict):
        for key, value in dict.items():
            try:
                index = self._keys.index(key)
                self._values[index] = value
            except ValueError:
                self._keys.append(key)
                self._values.append(value)
    

my_dict = MyDict()
my_dict['name'] = 'Alice'
my_dict['age'] = 30
print(my_dict['name'])  # Вернет 'Alice'
print('city' in my_dict)  # Вернет False
print(my_dict.keys())  # Вернет ['name']
print(my_dict.values())  # Вернет ['Alice']
print(my_dict)

my_dict_2 = MyDict()
my_dict_2[10] = 20
my_dict_2['age'] = 40
print(my_dict_2)
my_dict.update(my_dict_2)
print(my_dict)