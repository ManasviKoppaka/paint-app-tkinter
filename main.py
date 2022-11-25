from tkinter import *
from tkinter import colorchooser
root=Tk()
root.geometry("1000x600")
root.title("Paint App")

def selectCustomColor():
    selectedColor=colorchooser.askcolor(title="Select Color")
    print(selectedColor)
    if selectedColor[1]!=None:
        strokeColor.set(selectedColor[1])

strokeColor=StringVar()
strokeColor.set("black")

frame1 = Frame(root, height=100, width=1000)
frame1.grid(row=0, column=0, sticky=NW)

toolFrame = Frame(frame1, height=100, width=100, relief=SUNKEN, borderwidth=3)
toolFrame.grid(row=0, column=0)

sizeFrame = Frame(frame1, height=100, width=100, relief=SUNKEN, borderwidth=3)
sizeFrame.grid(row=0, column=1)

colorFrame = Frame(frame1, height=100, width=100, relief=SUNKEN, borderwidth=3)
colorFrame.grid(row=0, column=2)

customColorFrame = Frame(frame1, height=100, width=100, relief=SUNKEN, borderwidth=3)
customColorFrame.grid(row=0, column=3)

customButton = Button(customColorFrame, text="Custom Color", width=10, command=selectCustomColor)
customButton.grid(row=0, column=0)

blueButton = Button(colorFrame, text="Blue", bg="blue", width=10, command=lambda:strokeColor.set("blue"))
blueButton.grid(row=0, column=0)
redButton = Button(colorFrame, text="Red", bg="red", width=10, command=lambda:strokeColor.set("red"))
redButton.grid(row=1, column=0)
yellowButton = Button(colorFrame, text="Yellow", bg="yellow", width=10, command=lambda:strokeColor.set("yellow"))
yellowButton.grid(row=2, column=0)
blackButton = Button(colorFrame, text="Black", bg="black", width=10, fg="white", command=lambda:strokeColor.set("black"))
blackButton.grid(row=0, column=1)
greenButton = Button(colorFrame, text="Green", bg="green", width=10, command=lambda:strokeColor.set("green"))
greenButton.grid(row=1, column=1)
orangeButton = Button(colorFrame, text="Orange", bg="orange", width=10, command=lambda:strokeColor.set("orange"))
orangeButton.grid(row=2, column=1)

defaultButton = Button(sizeFrame, text="Default", fg="black", width=10, command=lambda:strokeSize.set(2))
defaultButton.grid(row=0, column=0)

options = [2,4,6,8,10]
strokeSize = IntVar()
sizeOptions=OptionMenu(sizeFrame, strokeSize, *options)
sizeOptions.grid(row=1, column=0)

sizeLabel = Label(sizeFrame, text="Size", width=10)
sizeLabel.grid(row=2, column=0)

pencil=Button(toolFrame, text="Pencil", fg="black", width=10, command=lambda:strokeColor.set("black"))
pencil.grid(row=0, column=0)

eraser=Button(toolFrame, text="Eraser", fg="black", width=10, command=lambda:strokeColor.set("white"))
eraser.grid(row=1, column=0)
tools=Label(toolFrame, text="Tools", fg="black", width=10)
tools.grid(row=2, column=0)

frame2 = Frame(root, height=500, width=1000, bg="yellow")
frame2.grid(row=1, column=0)

canvas = Canvas(frame2, height=500, width=1000, bg="white")
canvas.grid(row=0, column=0)

previousPoint=[0,0]
currentPoint=[0,0]


def paint(event):
    x=event.x
    y=event.y
    currentPoint[0]=x
    currentPoint[1]=y
    if not previousPoint==[0,0]:   
        canvas.create_polygon(previousPoint[0], previousPoint[1], currentPoint[0], currentPoint[1], fill=strokeColor.get(), width=strokeSize.get(), outline=strokeColor.get())
        # canvas.create_oval(x,y,x+1,y+1, fill="green", outline="green")


    previousPoint[0]=x
    previousPoint[1]=y
    if event.type=="5":
        previousPoint[0]=0
        previousPoint[1]=0



canvas.bind("<B1-Motion>",paint)
canvas.bind("<ButtonRelease-1>", paint)


root.resizable(False, False)
root.mainloop()
