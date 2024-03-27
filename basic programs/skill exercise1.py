'''n=int(input("Enter n value:"))
if n==0:
    print("wrong input")
else:
    for i in range(n,n+1):
        val=n*(n-1)
        print(val)'''



'''x=0
str1="thisismycountryindia"
for i in str1:
    x=x+1
    print(str1[0:x])

x=0
str1="thisismycountryindia"
for i in str1:
    x=x-1
    print(str1[0:x])'''


n=int(input("Enter n:"))
for i in range(n):
   for j in range(i-1):
     print("* ",end =" ")
   print("/n")


'''
a1=1045
a2=format(a1,'b')
print(a2)


a1="10100011110"
a2=int(format(int (a1,2),'d'))
print(a2)
'''


'''num=[10,20,30,40]
avg=sum(num)/len(num)
print(avg)


n=int(input("Enter n:"))
'''
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

num = int(input("Enter a number: "))
if num < 0:
    print("Factorial does not exist for negative numbers.")
elif num == 0:
    print("The factorial of 0 is 1")
else:
    print(f"The factorial of {num} is {factorial(num)}")




for i in range(1,8):
    print(7*i)




def main():
    input_sequence = input("Enter a sequence of comma-separated 4-digit binary numbers: ")

    binary_numbers = [num.strip() for num in input_sequence.split(',')]
    divisible_by_5_numbers = [num for num in binary_numbers if len(num) == 4 and int(num, 2) % 5 == 0]

    if divisible_by_5_numbers:
        result_sequence = ','.join(divisible_by_5_numbers)
        print(f"Numbers divisible by 5: {result_sequence}")
    else:
        print("No numbers divisible by 5 found in the input.")

if _name_ == "_main_":
    main()
