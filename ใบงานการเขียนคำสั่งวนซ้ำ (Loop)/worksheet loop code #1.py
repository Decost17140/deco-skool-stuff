print("เกมทายตัวเลข 0-100")
target = 85
guess = int
count = 0
while (target != guess):
    guess = int(input("เดาเลข :"))
    if (0 > guess > 100):
        print("ขอโทษด้วยตัวเลขไม่อยู่ในช่วงระหว่าง 0-100 กรุณาทายใหม่")
        count += 1
    elif (guess < target):
        print("ขอโทษด้วยตัวเลขมีค่าน้อยเกินไปกว่าที่ตั้งไว้ กรุณาทายใหม่")
        count += 1
    elif (guess > target):
        print("ขอโทษด้วยตัวเลขมีค่ามากเกินไปกว่าที่ตั้งไว้ กรุณาทายใหม่")
        count += 1
count += 1
print(f"ยินดีด้วยคุณทายถูก คุณทายทั้งหมด {count} ครั้ง")