name=input("Enter the user's name:")
print("hello ",name)
num1 = input("Enter the value:")
unit1 = input("Which unit do you want it converted from:")
unit2 = input("Which unit do you want it converted to:")
if unit1 == "cm" and unit2 == "m":
    ans = float(num1)/100
    print(ans)
elif unit1 == "mm" and unit2 == "cm":
    ans = float(num1)/10
    print(ans)
elif unit1 == "m" and unit2 == "cm":
    ans = float(num1)*100
    print(ans)
elif unit1 == "cm" and unit2 == "mm":
    ans = float(num1)*10
    print(ans)
elif unit1 == "mm" and unit2 == "m":
    ans = float(num1)/1000
    print(ans)
elif unit1 == "m" and unit2 == "mm":
    ans = float(num1)*1000
    print(ans)
elif unit1 == "km" and unit2 == "m":
    ans = float(num1)*1000
    print(ans)
elif unit1 == "m" and unit2 == "km":
    ans = float(num1)/1000
    print(ans)
elif unit1 == "mm" and unit2 == "km":
    ans = float(num1)/1000000

    print(ans)
elif unit1 == "inch" and unit2 == "cm":
    ans = float(num1)*2.54
    print(ans)
score=int(input("enter a score between 0 and 100:"))
if score>=80:
      print("grade A")
elif score >=70 and score <80:
          print("grade B")
elif score >=60 and score <70:
          print("grade C")
elif score >=50 and score <60:
          print("grade D")
elif score >=30 and score <40:
          print("grade E")
elif score>=20:
     print("F")
name=input("Enter the user's name:")
print("Goodbye ",name)