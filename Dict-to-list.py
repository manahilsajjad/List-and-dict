def test(lst):
	result = {}
	for item in lst:
		result[item[0]] = item[1:]
	return result

students = [[1, 'James Franco', 'V'], [2, 'Ronald Weasley', 'V'], [3, 'David Miller', 'VI'], [4, 'Emma Anderson', 'VI'], [5, 'Hermione Granger', 'VII']]

print("\nOriginal list of lists:")
print(students)
print("\nConverted  lists to a dictionary:")
print(test(students))