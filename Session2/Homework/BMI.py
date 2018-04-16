

mass= float(input("How weigh are you? "))
height= float(input("How tall are you? "))

BMI= mass/(height**2/10000)
#print("BMI=", BMI)
if BMI<16:
    print("Severely underweight")
elif BMI<18.5:
    print("Underweight")
elif BMI<25:
    print("Normal")
elif BMI <30:
    print("Overweight")
else:
    print("Obese")
