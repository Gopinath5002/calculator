from tkinter import * 
from tkinter import messagebox 

app = Tk() 
app.title("Simple Calculator") 
app.geometry("485x600") 
app.resizable(False,False) 
app.config(bg="#004C99") 

Label(app, text="CALCULATOR", width=40, height=2, fg="#FFFFFF", bg="#004C99", font=("Arial", 16, "bold")).pack() 

entry = Entry(app, width=37, state="normal", borderwidth=5, font=("Arial", 14)) 
entry.place(x=30, y=88) 

def click(number): 
    current = entry.get() 
    entry.delete(0, END) 
    entry.insert(0, current + str(number))

def calculate(): 
    expression = entry.get() 
    entry.delete(0, END) 
    try: 
        result = eval(expression) 
        entry.insert(0, result) 
    except Exception: 
        messagebox.showerror("Error", "Invalid Input") 

def clear_last(): 
    current = entry.get() 
    if current: 
        entry.delete(0, END) 
        entry.insert(0, current[:-1]) 
    else: 
        messagebox.showinfo("Info", "Already cleared") 

def clear_all(): 
    entry.delete(0, END) 

Button(app, text="1", padx=28, pady=5,font=("Arial", 20), bg="#FFFFFF", command=lambda: click("1")).place(x=30, y=150) 
Button(app, text="2", padx=28, pady=5,font=("Arial", 20), bg="#FFFFFF", command=lambda: click("2")).place(x=140, y=150)
Button(app, text="3", padx=28, pady=5,font=("Arial", 20), bg="#FFFFFF", command=lambda: click("3")).place(x=250, y=150) 
Button(app, text="4", padx=28, pady=5,font=("Arial", 20), bg="#FFFFFF", command=lambda: click("4")).place(x=30, y=230) 
Button(app, text="5", padx=28, pady=5,font=("Arial", 20), bg="#FFFFFF", command=lambda: click("5")).place(x=140, y=230) 
Button(app, text="6", padx=28, pady=5,font=("Arial", 20), bg="#FFFFFF", command=lambda: click("6")).place(x=250, y=230) 
Button(app, text="7", padx=28, pady=5,font=("Arial", 20), bg="#FFFFFF", command=lambda: click("7")).place(x=30, y=310) 
Button(app, text="8", padx=28, pady=5,font=("Arial", 20), bg="#FFFFFF", command=lambda: click("8")).place(x=140, y=310) 
Button(app, text="9", padx=28, pady=5,font=("Arial", 20), bg="#FFFFFF", command=lambda: click("9")).place(x=250, y=310) 
Button(app, text="0", padx=28, pady=5,font=("Arial", 20), bg="#FFFFFF", command=lambda: click("0")).place(x=140, y=390) 
Button(app, text=" . ", padx=20, pady=0.1,font=("Arial", 25, 'bold'), bg="#FFFFFF", command=lambda: click(".")).place(x=30, y=390) 
Button(app, text="=", padx=28, pady=5,font=("Arial", 20), bg="#FFFFFF", command=calculate).place(x=250, y=390) 
Button(app, text="+", padx=28, pady=5,font=("Arial", 20), bg="#FFFFFF", command=lambda: click("+")).place(x=360, y=150) 
Button(app, text="- ", padx=28, pady=5,font=("Arial", 20), bg="#FFFFFF", command=lambda: click("-")).place(x=360, y=230) 
Button(app, text="×", padx=28, pady=5,font=("Arial", 20), bg="#FFFFFF", command=lambda: click("*")).place(x=360, y=310) 
Button(app, text="/ ", padx=28, pady=5,font=("Arial", 20), bg="#FFFFFF", command=lambda: click("/")).place(x=360, y=390)
Button(app, text="( ", padx=28, pady=5,font=("Arial", 20), bg="#FFFFFF", command=lambda: click("(")).place(x=30, y=470) 
Button(app, text=") ", padx=28, pady=5,font=("Arial", 20), bg="#FFFFFF", command=lambda: click(")")).place(x=140, y=470) 
Button(app, text="CLEAR", padx=20, pady=19,font=("Arial", 10, 'bold'), bg="#FFFFFF", command=clear_last).place(x=250, y=470) 
Button(app, text="DELETE", padx=18, pady=19,font=("Arial", 10,'bold'), bg="#FFFFFF", command=clear_all).place(x=360, y=470) 

app.mainloop()