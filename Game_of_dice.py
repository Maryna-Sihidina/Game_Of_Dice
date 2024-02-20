from tkinter import*
import random, time


def brosok():
    x = random.choice(['b1.png','b2.png','b3.png',
                       'b4.png','b5.png','b6.png'])
    return x

def img(even):
    global b1,b2
    for i in range(10):
        b1 = PhotoImage(file = (brosok()))
        b2 = PhotoImage(file = (brosok()))

        lab1['image'] = b1
        lab2['image'] = b2
        root.update()
        time.sleep(0.12)

# the window of game
root = Tk()
root.geometry('400x200')
root.title('Game of dice. Take a throw!')
root.resizable(height = False, width = False)
root.iconphoto(True, PhotoImage(file=('icon.png'))) #иконка окна

# set up the canvas game
font = PhotoImage(file=('image.png'))
Label(root, image = font).pack()

# put the first label
lab1 = Label(root)
lab1.place(relx=0.3,rely=0.5,anchor=CENTER)

#put the second label
lab2 = Label(root)
lab2.place(relx=0.7,rely=0.5,anchor=CENTER)

root.bind('<1>', img)
img('event')

root.mainloop()
