from tkinter import *
import random
import time;

root = Tk()
root.geometry("1600x800+0+0")
root.title("restaurant management")

text_input = StringVar()
operator = ""

Tops = Frame(root, width=1600, heigh=50, bg="powder blue", relief=SUNKEN)
Tops.pack(side=TOP)

frame1 = Frame(root, width=800, height=700, relief=SUNKEN)
frame1.pack(side=LEFT)

frame2 = Frame(root, width=300, height=700, relief=SUNKEN)
frame2.pack(side=RIGHT)



localtime = time.asctime(time.localtime(time.time()))

lblInfo = Label(Tops, font=('arial', 50, 'bold'), text="Restaurant Management System", fg="Steel Blue", bd=10,
                anchor='w')
lblInfo.grid(row=0, column=0)
lblDateTime = Label(Tops, font=('arial', 20, 'bold'), text=localtime, fg="Steel Blue", bd=10, anchor='w')
lblDateTime.grid(row=1, column=0)


def btnClick(numbers):
    global operator
    operator = operator + str(numbers)
    text_input.set(operator)


def btnClearDisplay():
    global operator
    operator = ""
    text_input.set("")


def bthEqualsInput():
    global operator
    sumup = str(eval(operator))
    text_input.set(sumup)
    operator = ""


def Ref():
    x = random.randint(39276, 1983426)
    rand.set(str(x))

    CoF = float(fries.get())
    CoD = float(drinks.get())
    CoFilet = float(filet.get())
    CoBurger = float(burger.get())
    CochicBurger = float(chicken_burger.get())
    CocheeseBurger = float(cheese_burger.get())

    CostofFries = CoF * 12.90
    CostofDrinks = CoD * 7.60
    CostofFilet = CoFilet * 33.85
    CostofBurger = CoBurger * 25.0
    CostofChicken_Burger = CochicBurger * 27.55
    CostofCheese_Burger = CocheeseBurger * 27.55

    CostofMeal = "₪", str('%.2f' % (CostofFries + CostofDrinks + CostofFilet + CostofBurger
                                    + CostofChicken_Burger + CostofCheese_Burger))
    PayTax = ((CostofFries + CostofDrinks + CostofFilet + CostofBurger
               + CostofChicken_Burger + CostofCheese_Burger) * 0.17)
    TotalCost = (CostofFries + CostofDrinks + CostofFilet + CostofBurger
                 + CostofChicken_Burger + CostofCheese_Burger)
    Ser_Charge = ((CostofFries + CostofDrinks + CostofFilet + CostofBurger
                   + CostofChicken_Burger + CostofCheese_Burger) / 10)
    Service = "₪", str('%.2f' % Ser_Charge)

    OverAllCost = "₪", str('%.2f' % (PayTax + TotalCost + Ser_Charge))
    PaidTax = "₪", str('%.2f' % PayTax)

    Service_Charge.set(Service)
    cost.set(CostofMeal)
    Tax.set(PaidTax)
    subTotal.set(CostofMeal)
    Total.set(OverAllCost)


def qExit():
    root.destroy()


def Reset():
    rand.set("")
    fries.set("")
    burger.set("")
    filet.set("")
    subTotal.set("")
    Total.set("")
    Service_Charge.set("")
    drinks.set("")
    Tax.set("")
    cost.set("")
    chicken_burger.set("")
    cheese_burger.set("")


txtDisplay = Entry(frame2, font=('arial', 20, 'bold'), textvariable=text_input, bd=15, insertwidth=2,
                   bg="powder blue", justify='right')
txtDisplay.grid(columnspan=4)

btn7 = Button(frame2, padx=16, pady=16, bd=3, fg="black", font=('arial', 20, 'bold'),
              text="7", bg="powder blue", command=lambda: btnClick(7)).grid(row=2, column=0)
btn8 = Button(frame2, padx=16, pady=16, bd=3, fg="black", font=('arial', 20, 'bold'),
              text="8", bg="powder blue", command=lambda: btnClick(8)).grid(row=2, column=1)
btn9 = Button(frame2, padx=16, pady=16, bd=3, fg="black", font=('arial', 20, 'bold'),
              text="9", bg="powder blue", command=lambda: btnClick(9)).grid(row=2, column=2)

btn4 = Button(frame2, padx=16, pady=16, bd=3, fg="black", font=('arial', 20, 'bold'),
              text="4", bg="powder blue", command=lambda: btnClick(4)).grid(row=3, column=0)
btn5 = Button(frame2, padx=16, pady=16, bd=3, fg="black", font=('arial', 20, 'bold'),
              text="5", bg="powder blue", command=lambda: btnClick(5)).grid(row=3, column=1)
btn6 = Button(frame2, padx=16, pady=16, bd=3, fg="black", font=('arial', 20, 'bold'),
              text="6", bg="powder blue", command=lambda: btnClick(6)).grid(row=3, column=2)
btn1 = Button(frame2, padx=16, pady=16, bd=3, fg="black", font=('arial', 20, 'bold'),
              text="1", bg="powder blue", command=lambda: btnClick(1)).grid(row=4, column=0)
btn2 = Button(frame2, padx=16, pady=16, bd=3, fg="black", font=('arial', 20, 'bold'),
              text="2", bg="powder blue", command=lambda: btnClick(2)).grid(row=4, column=1)
btn3 = Button(frame2, padx=16, pady=16, bd=3, fg="black", font=('arial', 20, 'bold'),
              text="3", bg="powder blue", command=lambda: btnClick(3)).grid(row=4, column=2)
btn0 = Button(frame2, padx=16, pady=16, bd=3, fg="black", font=('arial', 20, 'bold'),
              text="0", bg="powder blue", command=lambda: btnClick(0)).grid(row=5, column=0)
Addition = Button(frame2, padx=16, pady=16, bd=3, fg="black", font=('arial', 19, 'bold'),
                  text="+", bg="powder blue", command=lambda: btnClick("+")).grid(row=2, column=3)
Subtraction = Button(frame2, padx=16, pady=16, bd=3, fg="black", font=('arial', 22, 'bold'),
                     text="-", bg="powder blue", command=lambda: btnClick("-")).grid(row=3, column=3)
Multply = Button(frame2, padx=16, pady=16, bd=3, fg="black", font=('arial', 18, 'bold'),
                 text="X", bg="powder blue", command=lambda: btnClick("*")).grid(row=4, column=3)
Division = Button(frame2, padx=16, pady=16, bd=3, fg="black", font=('arial', 21, 'bold'),
                  text="/", bg="powder blue", command=lambda: btnClick("/")).grid(row=5, column=3)
btnClear = Button(frame2, padx=16, pady=16, bd=3, fg="black", font=('arial', 20, 'bold'),
                  text="C", bg="powder blue", command=btnClearDisplay).grid(row=5, column=1)
btnEqual = Button(frame2, padx=16, pady=16, bd=3, fg="black", font=('arial', 20, 'bold'),
                  text="=", bg="powder blue", command=bthEqualsInput).grid(row=5, column=2)
# =============================================================================================
# =============================================================================================
rand = StringVar()
fries = StringVar()
burger = StringVar()
filet = StringVar()
subTotal = StringVar()
Total = StringVar()
Service_Charge = StringVar()
drinks = StringVar()
Tax = StringVar()
cost = StringVar()
chicken_burger = StringVar()
cheese_burger = StringVar()

lblReference = Label(frame1, font=('arial', 16, 'bold'), text="Reference", bd=16, anchor='w')
lblReference.grid(row=0, column=0)
txtReference = Entry(frame1, font=('arial', 16, 'bold'), textvariable=rand, bd=10, insertwidth=4,
                     bg="powder blue", justify='right')
txtReference.grid(row=0, column=1)

lblFries = Label(frame1, font=('arial', 16, 'bold'), text="Large Fries", bd=16, anchor='w')
lblFries.grid(row=1, column=0)
txtFries = Entry(frame1, font=('arial', 16, 'bold'), textvariable=fries, bd=10, insertwidth=4,
                 bg="powder blue", justify='right')
txtFries.grid(row=1, column=1)

lblBurger = Label(frame1, font=('arial', 16, 'bold'), text="Burger Meal", bd=16, anchor='w')
lblBurger.grid(row=2, column=0)
txtBurger = Entry(frame1, font=('arial', 16, 'bold'), textvariable=burger, bd=10, insertwidth=4,
                  bg="powder blue", justify='right')
txtBurger.grid(row=2, column=1)

lblFilet = Label(frame1, font=('arial', 16, 'bold'), text="Filet O Meal", bd=16, anchor='w')
lblFilet.grid(row=3, column=0)
txtFilet = Entry(frame1, font=('arial', 16, 'bold'), textvariable=filet, bd=10, insertwidth=4,
                 bg="powder blue", justify='right')
txtFilet.grid(row=3, column=1)

lblChickenB = Label(frame1, font=('arial', 16, 'bold'), text="Chicken Meal", bd=16, anchor='w')
lblChickenB.grid(row=4, column=0)
txtChickenB = Entry(frame1, font=('arial', 16, 'bold'), textvariable=chicken_burger, bd=10, insertwidth=4,
                    bg="powder blue", justify='right')
txtChickenB.grid(row=4, column=1)

lblCheeseB = Label(frame1, font=('arial', 16, 'bold'), text="Cheese Meal", bd=16, anchor='w')
lblCheeseB.grid(row=5, column=0)
txtCheeseB = Entry(frame1, font=('arial', 16, 'bold'), textvariable=cheese_burger, bd=10, insertwidth=4,
                   bg="powder blue", justify='right')
txtCheeseB.grid(row=5, column=1)

lblDrinks = Label(frame1, font=('arial', 16, 'bold'), text="Drinks", bd=16, anchor='w')
lblDrinks.grid(row=6, column=0)
txtDrinks = Entry(frame1, font=('arial', 16, 'bold'), textvariable=drinks, bd=10, insertwidth=4,
                  bg="powder blue", justify='right')
txtDrinks.grid(row=6, column=1)
# =============================================================================================
# =============================================================================================



lblCost = Label(frame1, font=('arial', 16, 'bold'), text="Cost Of Meal", bd=16, anchor='w')
lblCost.grid(row=0, column=2)
txtCost = Entry(frame1, font=('arial', 16, 'bold'), textvariable=cost, bd=10, insertwidth=4,
                bg="#ffffff", justify='right')
txtCost.grid(row=0, column=3)

lblService = Label(frame1, font=('arial', 16, 'bold'), text="Service Charge", bd=16, anchor='w')
lblService.grid(row=1, column=2)
txtService = Entry(frame1, font=('arial', 16, 'bold'), textvariable=Service_Charge, bd=10, insertwidth=4,
                   bg="#ffffff", justify='right')
txtService.grid(row=1, column=3)

lblTax = Label(frame1, font=('arial', 16, 'bold'), text="State Tax", bd=16, anchor='w')
lblTax.grid(row=2, column=2)
txtTax = Entry(frame1, font=('arial', 16, 'bold'), textvariable=Tax, bd=10, insertwidth=4,
               bg="#ffffff", justify='right')
txtTax.grid(row=2, column=3)

lblSubTotal = Label(frame1, font=('arial', 16, 'bold'), text="Sub Total", bd=16, anchor='w')
lblSubTotal.grid(row=3, column=2)
txtSubTotal = Entry(frame1, font=('arial', 16, 'bold'), textvariable=subTotal, bd=10, insertwidth=4,
                    bg="#ffffff", justify='right')
txtSubTotal.grid(row=3, column=3)

lblTotal = Label(frame1, font=('arial', 16, 'bold'), text="Total Cost", bd=16, anchor='w')
lblTotal.grid(row=4, column=2)
txtTotal = Entry(frame1, font=('arial', 16, 'bold'), textvariable=Total, bd=10, insertwidth=4,
                 bg="#ffffff", justify='right')
txtTotal.grid(row=4, column=3)
# =========================================================================================================

btnTotal = Button(frame1, padx=16, pady=8, bd=16, fg="black", font=('arial', 16, 'bold'), width=5,
                  text="Total", bg="powder blue", command=Ref).grid(row=7, column=0)

btnReset = Button(frame1, padx=16, pady=8, bd=16, fg="black", font=('arial', 16, 'bold'), width=5,
                  text="Reset", bg="powder blue", command=Reset).grid(row=7, column=1)

btnExit = Button(frame1, padx=16, pady=8, bd=16, fg="black", font=('arial', 16, 'bold'), width=5,
                 text="Exit", bg="powder blue", command=qExit).grid(row=7, column=2)



root.mainloop()