print("โปรแกรมรับค่าขนาดหน้าอก เพื่อทำการตรวจสอบขนาดของเสื้อโปโล")
size = int(input("ขนาดหน้าอก:"))
if size <= 34:
    print("ได้เสื้อขนาด: XS")
elif size <= 36:
    print("ได้เสื้อขนาด: S")
elif size <= 38:
    print("ได้เสื้อขนาด: M")
elif size <= 40:
    print("ได้เสื้อขนาด: L")
else:
    print("ได้เสื้อขนาด: XL")