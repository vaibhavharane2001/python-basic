# WAP to search for a number x in this tuple using the loop

 #[1,4,9,16,25,36,49,64,81,100)

tup=(1,4,9,16,25,36,49,64,81,100)

x=36
i=0
for val in tup:
    if(val==x):
        print("found at index:",i)
    i=i+1

