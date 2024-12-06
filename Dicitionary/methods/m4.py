student={
    "name":"Vaibahv",
    "class":"B.E",
    "subjects":{
        "phy":95,
        "chem":94,
        "math":93,
    }
}
print(student["name"]) # if we change name=name2 then this will give the error
print(student.get("name2")) #But in this case by changing the name=name2 will not give any type of error it will only print none.