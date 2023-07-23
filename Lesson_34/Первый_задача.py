slovar = {"key1": "value1",
          "key2": "value2",
          "key3": "value3",
          "key4": "value4",
          "key5": "value5"}

# keys = list(slovar.keys())
# values = list(slovar.values())
# print(keys)
# print(values)

# ============================================
keys = []
values = []
for i in slovar:
    keys.append(i)
    values.append(slovar[i])
print(values)
print(keys)


