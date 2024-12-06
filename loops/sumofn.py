# WAP to print the sum of n natural numbers using while loop and for loop.
#1.Using while loop
a=int(input("Enter the number:"))

sum=0
i=1

while i<=a:
    print(i)
    sum=sum+i;
    i=i+1
print("The sum of",a, "number is:", sum)


#2.Using for loop
# n=int(input("Enter the number:"))

# sum=0

# for i in range(1,n+1):
#     print(i)
#     sum=sum+i


# print("The total sum of", n, "number is:", sum)