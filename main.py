# 🚨 Don't change the code below 👇
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

bmi = weight/(height*height)

if bmi < 18.5:
  print("Your BMI is %s, you are slightly underweight." %round(bmi))
elif 18.5 < bmi < 25:
  print("Your BMI is %s, you have a normal weight." %round(bmi))
elif 25 < bmi < 30:
  print("Your BMI is %s, you are slightly overweight." %round(bmi))
elif 30 < bmi < 35:
  print("Your BMI is %s, you are obese." %round(bmi))
elif bmi > 35:
  print("Your BMI is %s, you are clinically obese." %round(bmi))
else:
  print("Please enter valid inputs.")

