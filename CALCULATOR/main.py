
from tkinter import*
def click(event):
    
    text = event.widget.cget('text')
    current = display.get()
    if text == "=":
        result = eval(current)
        display.delete(0,END)
        display.insert(END, result)
    elif text== "C":
        display.delete(0,END)
    else:    
        display.insert(END,text)
root = Tk()
root.title("Calculator")
root.configure(background="grey")
display = Entry(root, font=("Arial",25))
display.pack(fill=X, padx=10, pady=10, ipady=10)
btn_frame = Frame(root)
btn_frame.pack()
button_labels = [
    "7", "8", "9","+",
    "4", "5", "6", "-",
    "1", "2", "3", "*",
    "C", "0", "=", "/",
]

i=0
for label in button_labels:
    button = Button(btn_frame, text=label,font=("Arial", 18),padx=20,pady=20,bg="grey")
    button.grid(row=i//4, column=i%4, padx=10, pady=10)
    button.bind("<Button-1>", click)
    i = i+1

root.mainloop()
