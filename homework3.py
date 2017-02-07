# Задание 1:# Написать функцию, которая выбрасывает одно из трех исключений: # ValueError, TypeError или RuntimeError случайным образом. # В месте вызова функции обрабатывать все три исключения.# Не уверен, что правильно понял задание# Придумываю функцию, при выполнении которой могут возникать разные ошибки, например: # принять список чисел, разделить каждое на введеное пользователем число и вернуть результат в виде нового списка# Вызываю функцию через try, в зависмости от вида ошибки сообщаю пользователю о проблеме.def func(l):	new_list = []	b = None	for i in l:		b = i / a 		new_list.append(int(b))	return new_listinput_list = [2, 44, 13, 5, 0, 22]try:	a = int(input('Введите значение, на которое делим объекты списка: '))	print(func(input_list))except ValueError:	print('Ошибка: делителем должно быть число')except TypeError:	print('Ошибка: проверьте - в списке не должно быть строковых значений')except Exception:	raise RuntimeError('Что-то пошло не так :(, попробуйте ещё ')# Задание 2:# Написать функцию, которая принимает на вход список, # если в списке все объекты - int, сортирует его. Иначе выбрасывает ValueErrorinput_list = [2, 44, 13, 9, 0, 22]print('Сортирую список: ', input_list) def sort_func(l):		try:		sorted_list = []		for i in l:			sorted_list.append(int(i))		sorted_list.sort()			return print('Сортированный спискок: ', sorted_list)		except ValueError:		print('Ошибка: в списке должны быть только целые числа')sort_func(input_list)# Короткий вариант с TypeError:l = [2, 'k', 13, 9, 0, 33]print('Сортирую список', l) try:	l.sort()	print('Сортированный список:', l)except TypeError as e:	print('{} - невозможно просортировать: в списке должны быть только целые числа'.format(e))# Задание 3:# Написать функцию, которая принимает словарь, # преобразует все ключи словаря к строкам и возвращает новый словарьmy_dict = {1: 'Страна', 2: 'Город', '3': 'Улица', 4.2: 'Дом'}def keys_from_int_to_str(d):		new_dict = {}	for key, value in d.items():		if isinstance (key, str):			new_dict.update({key: value})		else:			key = str(key)			new_dict.update({key: value})	return new_dictprint(keys_from_int_to_str(my_dict))# Задание 4:# Написать функцию, которая принимает список чисел и возвращает их произведениеl = input('Введите список чисел, произведение которых нужно вычислить: ').split()numbers = []try:	for i in range(len(l)):		numbers.append(float(l[i]))except ValueError:	print('Неправильный формат ввода. Просто введите числа через пробел.')else:	from functools import reduce	result = reduce(lambda a, b: a*b, numbers)	print('Произведение всех чисел списка = {}'.format (result))# Задание 5:# Написать три функции: do_work, handle_success, handle_error. # do_work(my_list, success_callback, error_callback) принимает на вход три аргумента: # список, функцию для обработки успеха и функцию для обработки ошибки. # Ее задача проверить, что все значения в списке идут по-возрастанию. # Если все верно: вызываем success_callback, иначе: error_callback. # Функция handle_success пишет в консоль информацию об успешном выполнении. # Функция handle_error выбрасывает ValueErrorinput_list = [2, 11, 9, 22]print('Проверка сортировки: ') def do_work(my_list, success_callback, error_callback):	sorted_list = []	for i in my_list:		sorted_list.append(int(i))		sorted_list.sort()		if sorted_list == my_list:		success_callback()		else:		error_callback()def handle_success():	print('Список отсортирован по возрастанию')def handle_error():	print('Список не отсортирован по возрастанию')do_work(input_list, handle_success, handle_error)# Вопрос на уточнение: чем хорошо в данном случае зашивать функции во входящие аргументы, # если можно просто вызвать глобальные функции в do_work при вызове функции не писать много аргументов ? # Например, так:input_list = [2, 7, 9, 22]print('Проверка сортировки: ') def do_work(my_list):	sorted_list = []	for i in my_list:		sorted_list.append(int(i))		sorted_list.sort()		if sorted_list == my_list:		handle_success()		else:		handle_error()def handle_success():	print('Список отсортирован по возрастанию')def handle_error():	print('Список не отсортирован по возрастанию')do_work(input_list)