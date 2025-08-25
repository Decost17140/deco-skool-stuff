import tkinter as tk

root = tk.Tk()
root.title("นับเวลาถอยหลัง")
root.geometry("700x400")

count = 10

label = tk.Label(root, text="", font=("Consolas", 30))
label.pack(pady=10)

info_label = tk.Label(root, text="", font=("Consolas", 12))
info_label.pack()

def countdown():
    global count
    if count > 0:
        label.config(text=str(count))
        count -= 1
        root.after(1000, countdown)
    else:
        label.config(text="สวัสดีครับ ท่านสมาชิกชมรมคนชอบเกม")
        info = (
            "\nชื่อ - นามสกุล: สิรวิชญ์ ว่องกีรติกุล"
            "\nชื่อเล่น: เฟส"
            "\nห้องเรียน: ม.5/8"
            "\nแผนการเรียน: เทคโนโลยี"
            "\nอยากเรียนคณะ: คณะสถาปัตยกรรมศาสตร์และการออกแบบ สาขามีเดียอาตส์"
        )
        info_label.config(text=info)

countdown()

root.mainloop()