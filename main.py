from tkinter import *
from turtle import right, width

root = Tk()

root.title("Tkinter Canvas Bind Project")
root.geometry('1000x600')

canvas = Canvas(root,width=500,height=400,bg="orange")
canvas.grid(row=0, column=0)

#variables
hex_code=IntVar()
variable=IntVar()
operation = IntVar()
r = IntVar()
g = IntVar()
b = IntVar()
size = IntVar()

def rgb_hex(color):
    return hex(color.get())[2:].zfill(2) #zerofill

def shape_selection(event):

    global hex_code
    
    fill_col = ("#" + str(rgb_hex(r))+str(rgb_hex(g))+str(rgb_hex(b)))
    size = slider_size.get()

    if operation.get() == 1:
        canvas.create_rectangle(event.x,event.y,event.x+size,event.y+size,fill=fill_col,outline=fill_col)
    elif operation.get() == 2:
        canvas.create_oval(event.x,event.y,event.x+size,event.y+size,fill=fill_col,outline=fill_col)
    elif operation.get() == 3:
        points = [event.x,event.y,event.x+size,event.y,event.x+(size/2),event.y+size]
        canvas.create_polygon(points, fill=fill_col,outline=fill_col,width=2)
    canvas.delete(hex_code)

    hex_code = canvas.create_text(33,10,text=fill_col,font=('Arial','11'),fill=fill_col,justify=LEFT)
        
    print(fill_col)

#clear
def clear():
    canvas.delete("all")

#sliders
slider_r = Scale(root,label="Red",from_=0, to=255,bg='red', orient='horizontal',variable=r)
slider_r.grid(row=0,column=1,sticky=N,pady=70) 
 
slider_g = Scale(root,label="Green",from_=0, to=255,bg='green', orient='horizontal',variable=g)
slider_g.grid(row=0,column=2,sticky=N,pady=70) 
 
slider_b = Scale(root,label="Blue",from_=0, to=255,bg='blue', orient='horizontal',variable=b)
slider_b.grid(row=0,column=3,sticky=N,pady=70) 

slider_size = Scale(root,label="Size",from_=0, to=100,orient=HORIZONTAL,fg="black",bg="grey")
slider_size.grid(row=0,column=1,padx=10)

#clear button
clear_button = Button(root, text="Clear",command=clear,bg="orange",height=3,width=15)
clear_button.grid(row=0, column=2,sticky=S,pady=200)

#radio buttons
rectangle = Radiobutton(root,text='Square',variable=operation,value=1)
rectangle.grid(row=0, column=1,sticky=S,pady=100)

triangle = Radiobutton(text="Circle",variable=operation,value=2)
triangle.grid(row=0, column=2,sticky=S,pady=100) 

circle = Radiobutton(text="Triangle",variable=operation,value=3)
circle.grid(row=0, column=3,sticky=S,pady=100)

canvas.bind("<Button-1>",shape_selection)
canvas.update()
 
root.mainloop()