    ########################
    # ส่วนที่ต้องจัดเป็นอันดับ 1  #
    ######################## 
#เรียกข้อมูลที่ไม่มีอยู่ภายในเครื่องเข้ามาในโปรแกรม 

import os
from tkinter import *
from tkinter import messagebox

    ########################
    # ส่วนที่ต้องจัดเป็นอันดับ 3  #
    ######################## 

#จัดวาง Fuction     
def on_drag(e):

    global In_DisTotal

    In_Dis_Total = IN_DiSC2.get()
    IN_DiSC.set(In_Dis_Total)
    In_DisTotal.set(In_Dis_Total)
    result_Disc()
    
def OFF_entry(e):
    try:
        
        global In_DisTotal

        In_Dis_Total = IN_DiSC.get()

        if In_Dis_Total > 100:
            messagebox.showinfo("!! ʕ•ᴥ•ʔ", "กรุณาใส่ % น้อยกว่า 100")
        elif In_Dis_Total < 0:
            messagebox.showinfo("!! ʕ•ᴥ•ʔ", "กรุณาใส่ % มากกว่า   0")
    
        In_DisTotal.set(In_Dis_Total)
        IN_DiSC2.set(In_DisTotal.get())
        result_Disc()
    except:
        messagebox.showinfo("!! ʕ•ᴥ•ʔ", "กรุณาใส่ %") 

  
def result_Disc():
    try:

        global In_DisTotal

        Disc_Minus = (IN_Count.get() * In_DisTotal.get()) / 100
        Toatal = IN_Count.get() - Disc_Minus 
    
        #TERMIMAL CHECK RESULT
        Out_Toatal1.set(int(Disc_Minus))
        Out_Toatal2.set(int(Toatal))
    except:
            messagebox.showinfo("!! ʕ•ᴥ•ʔ", "อย่าใส่ราคาว่าง")


if __name__ == "__main__":

    ########################
    # ส่วนที่ต้องจัดเป็นอันดับ 2  #
    ######################## 
    #สร้างหน้าต่าง window 
    root = Tk()
    #Font 
    root.option_add("*Font", "bold 18")
    #หัวข้อ 
    root.title("Discount ʔʕ")
    #ขนาดของความกว้าง
    root.geometry("300x300")

    ########################
    #  ส่วนของการจัดวางเมนู   #
    ########################
    IN_Count = IntVar()

    Count_label = Label(root, text=" ราคาสินค้า", padx=5, pady=20)
    Count_label.grid(row=0, column=0,ipadx=0, ipady=0,sticky=W)

    Count_entry = Entry(root,textvariable=IN_Count,width=5, justify="center")
    Count_entry.grid(row=0, column=2, sticky=W ,ipadx=45)
    #bind Key เหมือน Fuction ที่มีให้อยู่แล้ว
    Count_entry.bind("<Return>", OFF_entry) #OFF_entry Fuction || <Return> รับค่าจาก Enter

    #ส่วนของการใส่ส่วนลด 1
    IN_DiSC = IntVar()
    IN_DiSC.set(50)

    DiSC_label = Label(root, text=" ส่วนลด",padx=5,pady=10)
    DiSC_label.grid(row=1, column=0, sticky=W)
    #ช่องใส่ค่า
    DiSC_entry = Entry(root, textvariable=IN_DiSC,width=5, justify="center")
    DiSC_entry .grid(row=1, column=2, sticky=W,ipadx=45)
    DiSC_entry.bind("<Return>", OFF_entry) #OFF_entry Fuction || <Return> รับค่าจาก Enter
    
    #ส่วนของตัวเลื่อนส่วนลด 2
    IN_DiSC2 = Scale(root, from_=1, to=100, orient=HORIZONTAL, length=150, width=30)
    IN_DiSC2.set(50)
    IN_DiSC2.grid(row=2, column=2 ,padx=1,pady=1,sticky=N)
    IN_DiSC2.bind('<B1-Motion>', on_drag)
    IN_DiSC2.bind('<B3-Motion>', on_drag)
    IN_DiSC2.bind('<Button-1>', on_drag)
    IN_DiSC2.bind("<Button-3>",on_drag)
    #<Button-1> คลิกซ้าย1  <B1-Motion> คลิกค้าง
    
    In_DisTotal = IntVar()
    Out_Toatal1 = IntVar()
    Out_Toatal2 = IntVar()

    #ส่วนของ Label คำตอบ 
    Discents_Label1= Label(root, text="ประหยัดไป", padx=15, pady=10)
    Discents_Label1.grid(row=3, column=0,ipadx=0, ipady=0,sticky=W)

    Discents_T1Label= Label(root, textvariable=Out_Toatal1, padx=5, pady=10)
    Discents_T1Label.grid(row=3, column=2,ipadx=45, ipady=0,sticky=N)

    Discents_Label2= Label(root, text="เหลือ", padx=15, pady=10)
    Discents_Label2.grid(row=4, column=0,ipadx=0, ipady=0,sticky=W)

    Discents_T2Label= Label(root, textvariable=Out_Toatal2, padx=5, pady=10)
    Discents_T2Label.grid(row=4, column=2,ipadx=45, ipady=0,sticky=N)

    root.mainloop()#เรียกใช่ Tkinter 
