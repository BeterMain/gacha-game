import tkinter as tk
import gachaGame

window = tk.Tk()
# Set title
window.title("Gacha Game")
# Set grid config
window.rowconfigure(0, minsize=1000, weight=1)
window.columnconfigure(1, minsize=1000, weight=1)
# Set Resize
window.resizable(width=False,height=False)
# Setting icon 
icon = tk.PhotoImage(file="Gacha Game/test pizza.png")
window.wm_iconphoto(False, icon)

# Functions
game = gachaGame.GachaGame()

def MultiSummon():
    # Clear previous
    canvas.delete('all')
    img_list = []

    # Add cards from multisummon into list
    for i in range(10):
        img_list.append(tk.PhotoImage(file=game.MultiSummon()))

    # Set width and height of canvas
    canvas['width'] = 900
    canvas['height'] = 800

    # Set starting height, width, and counter
    start_height = 0
    start_width = img_list[0].width()
    counter = 0

    # Arrange the cards to fit inside of the canvas
    for i in range(len(img_list)):
        if i % 4 == 0:
            start_height += img_list[i].height()
            counter = 0
        
        canvas.create_image(start_width * counter, start_height, anchor='sw', image=img_list[i])
        canvas.itemconfig(image_container, image=img_list[i])
        counter += 1

    # Show cards
    canvas.mainloop()
    
    

def SingleSummon():
    # set image to card
    img = tk.PhotoImage(file=game.SingleSummon()) 
    
    # Set width and height to card width and height
    canvas['width'] = img.width() 
    canvas['height'] = img.height()

    # Create new container to go ontop of the multisummon
    new = canvas.create_image(0, 0, anchor='nw', image=img)
    canvas.itemconfig(new, image=img)
    # Show card
    canvas.mainloop()
    


# Frames
leftFrame = tk.Frame(master=window, bg='blue', borderwidth=5)
rightFrame = tk.Frame(master=window, bg='purple', relief=tk.SUNKEN, borderwidth=5)
bottomFrame = tk.Frame(master=window, relief=tk.RIDGE, borderwidth=5)
topFrame = tk.Frame(master=window, relief=tk.RIDGE, borderwidth=3)

# Labels
lblTopMessage = tk.Label(master=topFrame,text="Welcome", bg='black', fg='red', width=100)
lblReactMessage = tk.Label(master=bottomFrame,text="You got this guy", bg='black', fg='red', width=30)

# Images
img = tk.PhotoImage(file='Gacha Game/test pizza.png') # create image
canvas = tk.Canvas(master=window, width=img.width(), height=img.height())
image_container = canvas.create_image(0, 0, anchor='nw', image=img)

# Buttons
btnSingle = tk.Button(master=leftFrame, width=30, height=30, bg='black', fg='red', text="Single",command=SingleSummon)
btnMulti = tk.Button(master=leftFrame, width=30, height=30,bg='black', fg='red',text="Multi", command=MultiSummon) 
btnCharacters = tk.Button(master=leftFrame, text="Characters")
btnList = [btnSingle, btnMulti]

# Pack and Grid #

# Left Frame
for i in range(len(btnList)):
    btnList[i].grid(row=i, column=0, padx=10, pady=10)

leftFrame.grid(row=0, column=0, padx=4)

# Top Frame
lblTopMessage.pack(fill=tk.BOTH, side=tk.TOP)
topFrame.grid(row=0, column=1, sticky='n')

# Right Frame
lblReactMessage.pack(fill=tk.X, side=tk.BOTTOM)
canvas.grid(row=0, column=1, padx=5, pady=5)
rightFrame.grid(row=0, column=1, sticky='nsew')

# Bottom Frame
bottomFrame.grid(row=0, column=1, sticky='s')

# Run Window
window.mainloop()