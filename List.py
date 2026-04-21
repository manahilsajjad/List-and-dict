My_list = ["Banana", "mango","strawberry","grapes","apple"]


print("Lenght of the list is:",len(My_list))
print("The first element of the list is:",My_list[0])
print("The last element of the list is:",My_list[-1])

My_list.append("orange")
print("The updated list is:", My_list)

My_list.remove("apple")
print("The list after removing apple is:",My_list)

My_list.sort()
print("The sorted list is:", My_list)

My_list.pop(3)
print("the list after popping element at index 3 is:",My_list)

My_list.reverse()
print(My_list)

print("Multiplaying the list:", My_list * 2)

My_list = My_list[:4]
print("Sliced list:",My_list)

My_list.clear()
print("Empty list:", My_list)