#Usually:
# sum_integers_list.py
def my_sum(my_integers):
    result = 0
    for x in my_integers:
        result += x
    return result

list_of_integers = [5, 8, 1]
print(my_sum(list_of_integers))

# With *args:
# Name NOT important: *args = *integers = *opcional = *infinito
# IMPORTANT!:  unpacking operator (*)
#the iterable object isn't a list but a tuple (slicing and iteration but unmutable). 
# sum_integers_args.py
def my_sum(*args):
    result = 0
    # Iterating over the Python args tuple
    for x in args:
        result += x
    return result

print(my_sum(1, 2, 3))
