#Figure out a way to store 9 & 9.0 as separate values in the set.
#(you can take help of built-in data types)

#Two methods are there are as follow

set={9,"9.0"}#This is method 1
print(set)

set_x={
    ("float",9.0),#This is method 2
    ("int",9)
}

print(set_x)