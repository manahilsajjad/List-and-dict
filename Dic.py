My_dict = {}
My_dict= { 1: 'apple', 2 : 'banana' }

My_dict={"name":"Manahil",1:[3,6,7]}
My_dict={"name":"John","age":12}
print(My_dict["name"])
print(My_dict.get("age"))

My_dict["age"] = 15
print(My_dict)

My_dict["adress"] = "566 Street"
print(My_dict)

My_dict.pop("name")
print(My_dict)
print("adress",My_dict.get("adress"))

My_dict.clear()
print(My_dict)