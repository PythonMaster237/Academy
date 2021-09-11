entry_list = [3, 4, 1, 7, 9, 'Ore', 5]


def stepin(list_int, power):
	list_int = []

	for row in entry_list:
		if type(row) is int:
			list_int.append(row**power)

	return list_int

print(stepin(entry_list, 2))