# STRINGS AS ARRAYS
my_string = 'Curso de Código facilito!'
print(my_string)

# To select a specific character in our string we add a [number character] after the name variable
print(my_string[0]) #Return the character in the position 0, in this case C.
print(my_string[1]) #Return u
print(my_string[10]) # Return ó

# To select characters from right to left
print(my_string[-1]) # Return !, in this case -1 represents the last element
print(my_string[-2]) # Return o

# To select one or more characters, in this way we create other string 
print(my_string[0:15]) # Return Curso de Código, here our firts value is the position of the character and the other one is the number of characters to read counting since the begining
print(my_string[15]) #Here the 15 is the position and represents a blank space
print(my_string[9:15]) # Código
print(my_string[-5:-1]) #Return lito

#To select characters ommiting other ones
print(my_string[0:10:2]) # Return Crod, Here we select character 0, then character 1 is omited and read next character and so on until character 10.

#To make a reverse in a string
print(my_string[::-1]) # Return !otilicaf ogidóC ed osruC

# STRING METHODS
course = 'Curso'
my_string = 'Código Facilito!'

#Format method
result = '{} de {}'.format(course, my_string)
print(result) # Return Curso de Código Facilito
result = '{a} de {b}'.format(b=course, a=my_string) #Here we changed the order, thanks to the parameters a and b
print(result) # Return Código Facilito! de Curso

#Lower method
result = result.lower()
print(result) # código facilito! de curso

#Upper method
result = result.upper()
print(result) # CODIGO FACILITO! DE CURSO

#Title method
result = result.title()
print(result) #Código Facilito! De Curso

#Find Method
result = '{} de {}'.format(course, my_string)
find = result.find('Código') #Returns the position where the character or string is ubicated in the complete string
print(find) #Return 9, this means the string Código beging in the position 9 of the complete string

#Count method
count = result.count('o') #This method counts the number of times that a specific character or string is inside the variable
print(count) # Returns 3, this example omited the ó and just counts the o without acent.

#Replace method
new_string = result.replace('Código', 'Diseño')
print(new_string) # Curso de Diseño Facilito

#Split method
#This method cuts the strings inside the variable to create an array
new_string = result.split(' ') #Here we say that split should cut the complete string in every blank space
print(new_string) #Return ['Curso', 'de', 'Código', 'Facilito' ]
