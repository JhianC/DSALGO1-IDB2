#Exercise 1
wii=100
userMoney=int((input("Enter the amount of money that you have: ")))
afford=int(userMoney/wii)
additional=int(userMoney%wii)

if userMoney>=wii:
    print("You can buy", afford, "unit/s of Nintendo Wii")
    print("For an additional unit you need ",additional)

else:
    print("Insufficient Funds")

#Exercise 2
print()
factorial=1
number=int(input("Enter any number: "))
for x in range(1, (number+1)):
    factorial=factorial * x
print(factorial, "is the factorial of ", number)

#Exercise 3
print()
factor=1
number1=int(input("Enter any number: "))
for a in range(1, number1+1):
    if number1%a==0:
        print(a, "is a factor of",number1 )

#Alt Ver Exercise 3
print()
factorList=[]
number1=int(input("Enter any number: "))
for a in range(1, number1+1):
    if number1%a==0:
        factorList.append(a)
print("The factors of" ,number1, "are: ", factorList )