#DICTIONARY - dict {}  curly brace, key-value pair

myInfo = {
    "Name": "Carl Delgado",
    "Age": 18, "Gender":
    "Male",
    "Height": 170,
    "Weight": 45
}
print(myInfo)

print(myInfo["Name"])
print(myInfo["Age"])
print(myInfo.get("Gender"))#as an alternative or another way
print(myInfo["Height"])
print(myInfo.get("Weight"))

myInfo.update({"Citezenship": "Filipino"}) #no value at the top,  if you add another another value that is not present to the first one it will create new set of values
print(myInfo)

myInfo.update({"Height": 200}) #update
print(myInfo)

myInfo["Height"] = 300 #assighned value
print(myInfo)

print(myInfo.values())
print(myInfo.keys())

#DICTIONARY - partner palagi si key-value pair, mutable, {} curly brace ang enclosure
#List -   THEN IF NAKA BRACKET [] LIST
#TUPLE - IF NAKA PARENTHESIS () TUPLE
#SET - mutable, DOES NOT ALLOW DUPLICATE,
# does not preserve the order, no append and no insert, have add,
# does not allow (listed nest or( sets of set))
# curly brace ang enclosure

#15th demo
#DICTIONARY - dict {}  curly brace, key-value pair

myInfo = {
    "Name": {
    "FirstName" :   "Carl",
    "LastName" :   "Delgado"
},
    "Age": 18,
    "Gender":"Male",
    "Cources": [
        "CMPE", "ECEN", "CMFE",
    ]
}
print(myInfo)
print(myInfo["Name"]["FirstName"])
print(myInfo["Name"]["LastName"])
print(myInfo["Cources"])
print(myInfo["Cources"][0])
print(myInfo["Name"]["FirstName"] + " " + myInfo["Name"]["LastName"])

myInfo["Name"]["FirstName"] = "Xarl"
print(myInfo["Name"]["FirstName"])
myInfo["Name"]["LastName"] = "Odagled"
print(myInfo["Name"]["LastName"])

#another demo ; same topic
#DICTIONARY

myListOfDictionary = [
    {"fruit" : "orange"},
     {"fruit" : "grapes"},
      {"fruit" : "banana"}
]
print(myListOfDictionary)
print(myListOfDictionary[1])