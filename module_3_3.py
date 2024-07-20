# 1.Функция с параметрами по умолчанию:
def print_params(a = 1, b = 'строка', c = True):
    print(a, b, c)
print_params() # Вывод на кансоль :   1 строка True
print_params(b = 25) # Вывод на кансоль : 1 25 True
print_params(c = [1,2,3]) # Вывод на кансоль : 1 строка [1, 2, 3]
# 2.Распаковка параметров:
values_list = [3, 'строчка', True]
values_dict = {'va': 2, 'lu': 'строка','es': True}
print_params(*values_list)
print_params(*values_dict)
# 3.Распаковка + отдельные параметры:
values_list_2 = [54.32, 'Строка' ]
print_params(*values_list_2, 42)