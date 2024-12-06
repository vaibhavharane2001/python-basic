# WAP to search for a number x in this tuple using the loop

 #[1,4,9,16,25,36,49,64,81,100]

tup=(1,4,9,16,25,36,49,64,81,100)


x=int(input("Enter the number to search in the tuple:"))
# x=49

i=0

while i< len(tup):
    
    if(tup[i]==x):
        print("found at index:",i)

        break

    else:

        print("finding.....")

    i=i+1