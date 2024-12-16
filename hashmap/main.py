from ExtendedDict import ExtendedDict

# Пример использования
map = ExtendedDict()

map["value1"] = 6
map["value2"] = 7
map["value3"] = 8
map["1"] = 0
map["2"] = 3
map["3"] = 4
map["(1, 5)"] = 1
map["(5, 5)"] = 5
map["(10, 5)"] = 2

print(map.ploc[">2, >2"])
