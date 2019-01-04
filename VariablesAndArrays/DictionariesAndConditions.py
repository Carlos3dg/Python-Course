""" DICTIONARIES """
# A dictionary is very similar to an object in JavaScript, these have key (properties) and values, they are declared like follow:
dictionary = { 'a' : True, 5 : 'String', 'b' : 10 }
# Dictionaries have keys and values. Keys can be strings, numbers, or whataver we want, and values also can be string, numbers and so on. Keys can't be modify
print(dictionary) # Return {'a': True, 5: 'String', 'b': 10}

# A dictionary can not has two keys named equal at the same time. If this happen the dictionary just choose the value from the last key.
dictionary = { 'a' : True, 5 : 'String', 'a' : 10 }
print(dictionary) # Return {'a': 10, 5: 'String'}
# The a key has the value of 10 and not the True.

# To add new keys to the dictionary
dictionary['c'] = 45
print(dictionary) # Return {'a': 10, 5: 'String', 'c': 45}

# To modify a value already existed 
dictionary['a'] = False
print(dictionary)# Return {'a': False, 5: 'String', 'c': 45}
# This method is the same like the last one, the only difference is that when a key is not found the key is created, in the other way the key is just modify

# To get a specific key value from the dictionary
valor = dictionary['c'] # Firts method
print(valor) # Return 45

valor = dictionary.get('c', False) # Second method
print(valor) # Return 45
# This second method returns exactly the same the only difference is that the parameters inside it are a key, used to found it in the dictionary and a value to return in case that the key is not in the found.

# To delete one key from the dictionary
del dictionary[5] # Put the key name in the [] and use the word del
print(dictionary) # Return ['a': False, 'c': 45]

# To get all keys in an object
llaves = dictionary.keys()
print(llaves) # Return dict_keys(['a', 'c'])
# To transform the last return in array
llaves = list(dictionary.keys())
print(llaves) # Return ['a', 'c']

# To get all values in an object
valores = dictionary.values()
print(valores) # Return dict_values([False, 45])
# To transform the last return in array
valores = list(dictionary.values())
print(valores) # Return [False, 45]

# To add other dictionary
dictionary2 = { 'd' : 5, 'e' : 4 }

dictionary.update(dictionary2)
print(dictionary) # Return {'a': False, 'c': 45, 'd': 5, 'e': 4}
