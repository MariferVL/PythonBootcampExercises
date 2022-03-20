
shopping_list = {'papas':3, 'tomates':2, 'paltas' : 0}

def add_item():
    item_name= input(">Ingrese nombre de producto a agregar: ").lower()
    quantity= int(input(">Ingrese número de unidades a agregar: "))
    if item_name in shopping_list.keys():
        shopping_list[item_name] += quantity
    else:
        shopping_list[item_name] = quantity

def add_item(item_name="", quantity=1):
    if not item_name:
        quantity = 0
    if item_name in shopping_list.keys():
        shopping_list[item_name] += quantity
    else:
        shopping_list[item_name] = quantity

add_item()
print (shopping_list)