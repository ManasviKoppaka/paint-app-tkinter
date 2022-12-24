from tkinter import *
from tkinter import colorchooser,filedialog,messagebox
import PIL.ImageGrab as ImageGrab
root=Tk()
root.geometry("1000x600")
root.title("Paint App")


def paint(event):
    x=event.x
    y=event.y
    currentPoint[0]=x
    currentPoint[1]=y
    if not previousPoint==[0,0]:   
        if brushType.get()=="caligraphy pen":
            canvas.create_polygon(previousPoint[0], previousPoint[1], currentPoint[0], currentPoint[1], fill=strokeColor.get(), width=strokeSize.get(), outline=strokeColor.get())
            canvas.create_line(currentPoint[0], currentPoint[1], currentPoint[0]+20, currentPoint[1]+20, width=3)
            # canvas.create_line(currentPoint[0]+1, currentPoint[1]+1, currentPoint[0]+20, currentPoint[1]+20, width=3)

        elif brushType.get()=="brush":
            canvas.create_polygon(previousPoint[0], previousPoint[1], currentPoint[0], currentPoint[1], fill=strokeColor.get(), width=strokeSize.get(), outline=strokeColor.get())
        elif brushType.get()=="watercolor brush":
            canvas.create_arc(currentPoint[0], currentPoint[1], currentPoint[0]+20, currentPoint[1]+20)

    previousPoint[0]=x
    previousPoint[1]=y
    if event.type=="5":
        previousPoint[0]=0
        previousPoint[1]=0

def selectCustomColor():
    selectedColor=colorchooser.askcolor(title="Select Color")
    # print(selectedColor)
    # print(selectedColor[1])
    if selectedColor[1]!=None:
        strokeColor.set(selectedColor[1])
        # print(previousCustomColor.get(), "pc1")
        # print(previousCustomColor2.get(), "pc2")
        # if previousCustomColor.get()!="white":
        previousCustomColor2.set(previousCustomColor.get())
        previousCustomColor.set(selectedColor[1])
        # print(previousCustomColor.get(), "pc1")
        previousColor["bg"]=previousCustomColor.get()
        previousColor2["bg"]=previousCustomColor2.get()
    # previousCustomColor.set(selectedColor)


previousCustomColor =  StringVar()
previousCustomColor.set("white")
previousCustomColor2 = StringVar()
previousCustomColor2.set("white")



def saveImage():
    image=filedialog.asksaveasfilename(defaultextension="jpg")
    x = root.winfo_rootx()
    y = root.winfo_rooty()
    paint = ImageGrab.grab(bbox=(x,y,x+1000,y+600))
    paint.show()



strokeColor=StringVar()
strokeColor.set("black")
strokeSizeOptions = [2,4,6,8,10]
brushTypeOptions = ["brush", "caligraphy pen", "watercolor brush"]
brushType = StringVar()
brushType.set("brush")
strokeSize = IntVar()
strokeSize.set(2)
previousPoint=[0,0]
currentPoint=[0,0]

# frames
# frame1-dashboard
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

brushFrame = Frame(frame1, height=100, width=200, relief=SUNKEN, borderwidth=3)
brushFrame.grid(row=0, column=4)

saveImageFrame = Frame(frame1, height=100, width=100, relief=SUNKEN, borderwidth=3)
saveImageFrame.grid(row=0, column=5)

# frame2-canvas
frame2 = Frame(root, height=500, width=1000, bg="yellow")
frame2.grid(row=1, column=0)

# tool frame widgets
pencil=Button(toolFrame, text="Pencil", fg="black", width=10, command=lambda:strokeColor.set("black"))
pencil.grid(row=0, column=0)
eraser=Button(toolFrame, text="Eraser", fg="black", width=10, command=lambda:strokeColor.set("white"))
eraser.grid(row=1, column=0)
tools=Label(toolFrame, text="Tools", fg="black", width=10)
tools.grid(row=2, column=0)

# size frame widgets
sizeOptions=OptionMenu(sizeFrame, strokeSize, *strokeSizeOptions)
sizeOptions.grid(row=1, column=0)
sizeLabel = Label(sizeFrame, text="Size", width=10)
sizeLabel.grid(row=2, column=0)
defaultButton = Button(sizeFrame, text="Default", fg="black", width=10, command=lambda:strokeSize.set(2))
defaultButton.grid(row=0, column=0)


# color frame buttons
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

#brushes frame widgets
brushOptions = OptionMenu(brushFrame, brushType, *brushTypeOptions)
brushOptions.grid(row=1, column=0)
brush = Label(brushFrame, text="Brushes", width=20)
brush.grid(row=2, column=0)
defalutBrush = Button(brushFrame, text="Defalut", width=20, command=lambda:brushType.set("brush"))
defalutBrush.grid(row=0, column=0)

# custom color button
customButton = Button(customColorFrame, text="Custom Color", width=10, command=selectCustomColor)
customButton.grid(row=0, column=0)
previousColor = Button(customColorFrame, text="previous", bg=previousCustomColor.get(), width=10, command=lambda:strokeColor.set(previousCustomColor.get()))
previousColor.grid(row=1, column=0)
previousColor2 = Button(customColorFrame, text="previous2", width=10, bg=previousCustomColor2.get(), command=lambda:strokeColor.set(previousCustomColor2.get()))
previousColor2.grid(row=2, column=0)


#Save Image Frame
saveImage= Button(saveImageFrame, text="Save Image", width=10, command=saveImage)
saveImage.grid(row=0, column=0)

# canvas
canvas = Canvas(frame2, height=500, width=1000, bg="white")
canvas.grid(row=0, column=0)


canvas.bind("<B1-Motion>",paint)
canvas.bind("<ButtonRelease-1>", paint)


root.resizable(False, False)
root.mainloop()
