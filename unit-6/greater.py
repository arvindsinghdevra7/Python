a1=int(input("Enter a Number 1:"))
a2=int(input("Enter a Number 2:"))
a3=int(input("Enter a Number 3:"))
a4=int(input("Enter a Number 4:"))

if(a1>=a2 and a1>=a3 and a1>=a4):
    print("Yes a1 is greater",a1)
elif(a2>=a1 and a2>=a3 and a2>=a4):
    print("Yes a2 is greater",a2)
elif(a3>=a2 and a3>=a1 and a3>=a4):
    print("Yes a3 is greater",a3)
elif(a4>=a2 and a4>=a3 and a4>=a1):
    print("Yes a1 is greater",a4)

else:
    print("You enter invalid number")

