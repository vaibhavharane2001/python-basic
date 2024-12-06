student={
    "name":"Vaibahv",
    "class":"B.E",
    "subjects":{
        "phy":95,
        "chem":94,
        "math":93,
    }
}
print(student["subjects"])
print(student["subjects"]["phy"])
student["subjects"]["Bio"] = 90
print(student["subjects"]["Bio"])
print(student)