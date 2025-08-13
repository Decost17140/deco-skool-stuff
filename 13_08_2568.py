import tkinter as tk
root = tk.Tk()
root.title("that Hayase Yuuka simp")

mylabel = tk.Label(text="Hello World", fg="black", font="96").pack()

def showMessage():
    tk.Label(text="ชื่อ: นาย สิรวิชญ์ ว่องกีรติกุล\nชั้น: ม.5/8\n เลขที่: 28", fg="red", font="48").pack()
    
btn1 = tk.Button(root, text="Press Me!", command=showMessage).pack()

root.geometry("469x469")
root.mainloop()