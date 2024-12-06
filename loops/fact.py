# WAP to find the factorial of the given number using for loop and while loop.
#1.using for loop
n=int(input("Enter the number:"))

fact=1

for i in range(1, n+1):
    fact=fact*i
print("The factorial of",n,"number is:",fact)



#2. using while loop
# n=int(input("Enter the number:"))

# fact=1
# i=1

# while i<=n:
#     print(i)
#     fact=fact*i
#     i=i+1

# print("The factorial of",n,"number is:",fact)