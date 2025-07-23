i=0
while(i != 101):
    print(i)
    i += 1
i=1000
while(i != -1):
    print(i)
    i -= 1
min_value = None
while(True):
    try:
        num = float(input("ใส่จำนวนจริงบวก: "))
        if num <= 0:
            break
        if min_value is None or num < min_value:
            min_value = num
    except ValueError:
        break
if min_value is not None:
    print("ค่าที่น้อยที่สุดคือ", min_value)
else:
    print("ไม่มีจำนวนจริงบวกที่ป้อนเข้ามาเลย")