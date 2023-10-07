### Variables ###

my_string_variable = "Esto es una prueba"
print(my_string_variable)

my_int_variable = 73
print(my_int_variable)

my_bool_variable = False
print(my_bool_variable)

# Variables en una sola línea
name, surname, alias, age = "José Antonio", "García.", "Gokuto.", 14
print('Me llamo:', name, surname, 'Tengo:', age, 'años.', 'Algunos me llaman:', alias)

# Inputs
name = input('what is your name?:')
_age = input('How old are you?:')

print('Hi,', name)
print('So you are:', _age, 'I am younger')

# Concadenación de variables
print(my_string_variable, my_int_variable, my_bool_variable) 

# Algunas funciones el sistema 
print(len(my_string_variable)) # 'len' cuenta los caracteres
