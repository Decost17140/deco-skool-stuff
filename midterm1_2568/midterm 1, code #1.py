hour = (int(input("จอดรถกี่ชั่วโมง=")))
minute = (int(input("จอดรถกี่นาที=")))
if hour < 0 or minute < 0:
    print("โปรดใส่ข้อมูลที่ไม่ติดลบ")
else:
    total_time = hour + (1 if minute > 0 else 0)
    chargeable_hours = max(0, total_time - 1)
    cost = chargeable_hours * 30
    print(f"ค่าจอดรถ={str(cost)}บาท")
