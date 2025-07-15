print("BMI Calculator 9000")
w=float(input("กรอกน้ำหนักในหน่วยกิโลกรัม: "))
h_m=float(input("กรอกส่วนสูงในหน่วยเมตร: "))
bmi=float(w/(h_m*h_m))
print(f"BMI is: {bmi:.2f}")
if bmi < 18.5:
    print("Underweight")
elif 18.5 <= bmi < 25:
    print("Normal weight")
elif 25 <= bmi < 30:
    print("Overweight")
else:
    print("Obesity")