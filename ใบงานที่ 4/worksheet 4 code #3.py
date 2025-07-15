print("โปรแกรมคํานวนเกรด")
score = int(input("กรอกคะแนน:"))
if score >= 80:
    print("คุณได้เกรด A")
elif score >= 70 and score <= 79:
    print("คุณได้เกรด B")
elif score >= 60 and score <= 69:
    print("คุณได้เกรด C")
elif score >= 50 and score <= 59:
    print("คุณได้เกรด D")
else:
    print("คุณได้เกรด F")