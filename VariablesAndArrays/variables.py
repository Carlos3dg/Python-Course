# We can not use uppercase in a variable declaration
curso_codigo_facilito = 'El curso es Python 3'
print(curso_codigo_facilito)

curso_codigo_facilito = 99
print(curso_codigo_facilito)

curso_codigo_facilito = True 
print(curso_codigo_facilito)

# TYPE OF NUMBERS
enteros = 10
floats = 9.0
complex # For precision results, most of the time used for machine learning
booleans = True # Also known like 1 and 0

# Operators
number_one = 10
number_two = 4

# Suma
result = number_one + number_two
print('Suma', result) # 14

# Resta
result = number_one - number_two
print('Resta', result) # 10

# Multiplicación
result = number_one * number_two
print('Multiplicación', result) # 40

# División
result = number_one / number_two
print('División', result) # 2.5 Returns a float num

# Division entera
result = number_one // number_two
print('División', result) # 2 Returns a whole num

# Exponencial
result = number_one ** number_two
print('Exponencial', result) # 2 number_one elevado a la number_two

# STRINGS
my_string = "Hola Mundo!" 
print(my_string) # Returns Hola Mundo!

my_string = "Hola Mundo! 'Carlos' " 
print(my_string) # Returns Hola Mundo! 'Carlos'

# Saltos de línea
my_string = """ Este es un string que contiene
            saltos de linea,
            como se puede observar """ # We insert three ''' or """ to write a string with line height

print(my_string)

my_string = '''Este es un string que contiene\nsaltos de línea,\ncomo se puede observar''' # To avoid the line heights in our code editor we can use invert slash(\) and n to make the line height
print(my_string)

# Concatenating strings
language = 'Python'
name = 'Carlos'

final_message = name + ' is learning ' + language + ' language' # First way
print(final_message) # Returns Carlos is learning Python language

final_message = "%s is learning %s language" %(name, language) # Second way
print(final_message) # Returns Carlos is learning Python language

final_message = "{} is learning {} language".format(name, language) # Third way (less recommended)
print(final_message) # Returns Carlos is learning Python language