from tkinter import *
import random

main_window = Tk()
main_window.title('Python With Python')
main_window.iconbitmap(r'icons/snake.ico')
# main_window.overrideredirect(True)# to hide window bar
main_window.geometry('1200x700')# sets window geometry
main_window.resizable(0,0)# fixed window
main_window.rowconfigure(10, minsize=50)
main_window.columnconfigure(10, minsize=50)

# creating a canvas for to hold onStart, onGame, onGameEnd
main_window.canvas = Canvas(main_window,
                width=1200,
                height=700,
                borderwidth=0,
                highlightthickness=0)

# for keyboard event listening, for onGame event
def onGameKey(event):
    main_window.key_pressed = event.keysym
    if main_window.previous_state != main_window.key_pressed:
        if main_window.key_pressed == 'Right':
            main_window.state = 'Right'
            main_window.bool_image_change = True
        elif main_window.key_pressed == 'Left':
            main_window.state = 'Left'
            main_window.bool_image_change = True
        elif main_window.key_pressed == 'Up':
            main_window.state= 'Up'
            main_window.bool_image_change = True
        elif main_window.key_pressed == 'Down':
            main_window.state = 'Down'
            main_window.bool_image_change = True
        else:
            main_window.state =''
        main_window.previous_state = main_window.state
    # print('pressed :'+main_window.key_pressed)

# for keyboard event listening, for onStart event
def onStartKey(event):
    if event.keysym == 'Return':
        startGame()
    elif event.keysym == 'Escape':
        quit()

# for keyboard event listening, for onGameEnd event
def onGameEndKey(event):
    if event.keysym == 'Return':
        onStart()
    if event.keysym == 'Escape':
        main_window.destroy()

# this loads up first when app launches
def onStart():
    main_window.canvas.delete('all')

    # setting-up wallpaper for onStart environment
    main_window.wall_filename = PhotoImage(file = "wallpapers/red2.png")
    image = main_window.canvas.create_image(1202, 0, anchor=NE, image=main_window.wall_filename)
    main_window.canvas.grid(row=0, column = 0)
    main_window.canvas.create_text(520, 284, text='Start', font="fantasy 27 italic bold", fill='green')
    main_window.canvas.create_text(650, 410, text='Exit', font="fantasy 27 italic bold", fill='red')
    main_window.bugg = PhotoImage(file = "wallpapers/bugg.png")
    main_window.bugr = PhotoImage(file = "wallpapers/bugr.png")
    main_window.canvas.grid(row=0, column = 0)
    start_btn = Button(text='START', command=startGame, image=main_window.bugg, bg='black')
    start_btn.configure(activebackground = "#000000", relief = FLAT)
    start_btn_window = main_window.canvas.create_window(470, 300, anchor=NW, window=start_btn)
    exit_btn = Button(text='QUIT', command=main_window.destroy, image=main_window.bugr, bg='black')
    exit_btn.configure(activebackground = "#000000", relief = FLAT)
    exit_btn_window = main_window.canvas.create_window(600, 300, anchor=NW, window=exit_btn)
    main_window.key_bind_id = main_window.bind("<Key>", onStartKey)
    variableUpdate()

# this thing loads up when gamer has pressed play button
def onGame():
    # clearing-up everything for making game environment enable
    main_window.canvas.delete('all')
    main_window.playing = True
    # setting-up wallpaper for game environment
    main_window.wall_filename = PhotoImage(file = "wallpapers/red2.png")
    main_window.head = main_window.canvas.create_image(1202, 0, anchor=NE, image=main_window.wall_filename)
    main_window.canvas.tag_raise(main_window.head)
    main_window.canvas.grid(row=0, column = 0)
    co_ords = main_window.co_ords[0]
    main_window.canvas.create_image(co_ords[0], co_ords[1], anchor=NE, image=selectTargetRandom(), tag='target')

    # setting-up spikes on edge of screen
    main_window.left_spike_filenames = ['']
    main_window.right_spike_filenames = ['']
    main_window.top_spike_filenames = ['']
    main_window.bottom_spike_filenames = ['']
    # left spikes
    gap = -32
    for i in range(0,19):
        main_window.left_spike_filenames.append(PhotoImage(file = "wallpapers/bugtop.png"))
        image = main_window.canvas.create_image(40, gap, anchor=NE, image=main_window.left_spike_filenames[i])
        gap = gap + 39
    # top spikes
    gap = 43
    for j in range(0,29):
        main_window.top_spike_filenames.append(PhotoImage(file = "wallpapers/bugright.png"))
        image = main_window.canvas.create_image(gap, -3, anchor=NE, image=main_window.top_spike_filenames[j])
        gap = gap + 41
    # right spikes
    gap = -5
    for k in range(0,23):
        main_window.right_spike_filenames.append(PhotoImage(file = "wallpapers/bugbottom.png"))
        image = main_window.canvas.create_image(1206, gap, anchor=NE, image=main_window.right_spike_filenames[k])
        gap = gap + 41
    # bottom spikes
    gap = 45
    for l in range(0,30):
        main_window.bottom_spike_filenames.append(PhotoImage(file = "wallpapers/bugleft.png"))
        image = main_window.canvas.create_image(gap, 660, anchor=NE, image=main_window.bottom_spike_filenames[l])
        gap = gap + 39

    # packing canvas into grid
    main_window.canvas.grid(row=0, column = 0)

    # setting-up different directioned heads of snake
    main_window.head_filename_l = PhotoImage(file = "wallpapers/headleft50.png")
    main_window.head_filename_u = PhotoImage(file = "wallpapers/headup50.png")
    main_window.head_filename_d = PhotoImage(file = "wallpapers/headdown50.png")
    main_window.head_filename_r = PhotoImage(file = "wallpapers/headright50.png")
    # setting-up snake head
    main_window.head = main_window.canvas.create_image(120, 30, anchor=NE, image=main_window.head_filename_r)
    # setting-up key function to keyboard event listening
    main_window.bind("<Key>", onGameKey)

# this loads up when the gane is over
def onGameEnd():
    main_window.canvas.delete("all")
    # setting-up wallpaper for onStart environment
    main_window.wall_filename = PhotoImage(file = "wallpapers/red2.png")
    image = main_window.canvas.create_image(1202, 0, anchor=NE, image=main_window.wall_filename)
    main_window.trans_filename = PhotoImage(file = "wallpapers/mini_trans50large.png")
    image = main_window.canvas.create_image(1202, 0, anchor=NE, image=main_window.trans_filename)
    main_window.canvas.create_text(590, 100, text='Game Over', font="fantasy 91 italic bold", fill='green')
    main_window.canvas.create_text(590, 300, text='Score : {}'.format(main_window.score), font="fantasy 70 italic bold", fill='darkblue')
    main_window.canvas.grid(row=0, column = 0)
    main_window.bind("<Key>", onGameEndKey)

# starts the game
def startGame():
    # calling update function to update the game environment
    onGame()
    # loops game envirionment and updates
    main_window.after(500, update)

# this updates the frames of game
def frameUpdate():
    if main_window.key_pressed == 'Return' and main_window.at_start == 1:
        main_window.canvas.move(main_window.head, main_window.x_moment_change, main_window.y_moment_change)
        main_window.at_start = 0
        # print('started moving')
    elif main_window.state == 'Right':
        main_window.canvas.move(main_window.head, main_window.x_moment_change, 0)
        main_window.x_pos = main_window.x_pos + main_window.x_moment_change
        if main_window.bool_image_change:
            main_window.canvas.itemconfig(main_window.head, image=main_window.head_filename_r)
            main_window.bool_image_change = False
        # print('moving right,', 'x :',main_window.x_pos, 'y :',main_window.y_pos)
    elif main_window.state == 'Left':
        main_window.canvas.move(main_window.head, main_window.x_moment_change-2*main_window.x_moment_change, 0)
        main_window.x_pos = main_window.x_pos + main_window.x_moment_change - 2*main_window.x_moment_change
        if main_window.bool_image_change:
            main_window.canvas.itemconfig(main_window.head, image=main_window.head_filename_l)
            main_window.bool_image_change = False
        # print('moving left', 'x :',main_window.x_pos, 'y :',main_window.y_pos)
    elif main_window.state == 'Up':
        main_window.canvas.move(main_window.head, 0, main_window.y_moment_change-2*main_window.y_moment_change)
        main_window.y_pos = main_window.y_pos + main_window.y_moment_change-2*main_window.y_moment_change
        if main_window.bool_image_change:
            main_window.canvas.itemconfig(main_window.head, image=main_window.head_filename_u)
            main_window.bool_image_change = False
        # print('moving up', 'x :',main_window.x_pos, 'y :',main_window.y_pos)
    elif main_window.state == 'Down':
        main_window.canvas.move(main_window.head, 0, main_window.y_moment_change)
        main_window.y_pos = main_window.y_pos + main_window.y_moment_change
        if main_window.bool_image_change:
            main_window.canvas.itemconfig(main_window.head, image=main_window.head_filename_d)
            main_window.bool_image_change = False
        # print('moving down', 'x :',main_window.x_pos, 'y :',main_window.y_pos)
    checkIfReach()

# checks if python reaches the target
def checkIfReach():
    if main_window.x_pos > main_window.co_ords[0][0] and main_window.y_pos > main_window.co_ords[0][1] and main_window.x_pos < main_window.co_ords[0][2] and main_window.y_pos < main_window.co_ords[0][3]:
        relpaceNewTarget()
        scoreUp()
        # print('win',main_window.score)
    elif main_window.x_pos+50 > main_window.co_ords[0][0] and main_window.y_pos+50 > main_window.co_ords[0][1] and main_window.x_pos < main_window.co_ords[0][2] and main_window.y_pos < main_window.co_ords[0][3]:
        relpaceNewTarget()
        scoreUp()
        # print('win',main_window.score)

# selects random taget objects
def selectTargetRandom():
    return main_window.target_images[random.randint(0, main_window.no_of_images-1)]

# replaces the target with new one
def relpaceNewTarget():
    main_window.canvas.delete('target')
    main_window.co_ords = []
    putCoords()
    co_ords = main_window.co_ords[0]
    main_window.canvas.create_image(co_ords[0], co_ords[1], anchor=NE, image=selectTargetRandom(), tag='target')
    # to make head visible on all
    main_window.canvas.tag_raise(main_window.head)

# calculates the score
def scoreUp():
    main_window.score = main_window.score + 10

# checks if gamer is out/not
def boolGameOver():
    if main_window.x_pos > 1197 or main_window.x_pos < 91 or main_window.y_pos > 610 or main_window.y_pos < 0:
        return True
    else:
        return False

# this function iupdates the game environment
def update():
    frameUpdate()
    if boolGameOver():
        print('game over')
        onGameEnd()
    elif main_window.key_pressed == 'Escape':
        onGameEnd()
        onStart()
    elif main_window.playing:
        # to make update function run again
        main_window.after(main_window.speed_of_snake, update)

# updates the target image
def targetImageUpdate():
    main_window.target_names = ['c', 'python', 'java']# , 'cs', 'cpp', 'java', 'asm', 'ruby', 'go', 'js', 'html', 'bf', 'php', 'swift', 'alice', 'boo', 'grass', 'grasshooper'
    main_window.target_images = []
    for name in main_window.target_names:
        image = PhotoImage(file = "wallpapers/"+name+".png")
        main_window.target_images.append(image)
    main_window.no_of_images = len(main_window.target_names)

# puts the coords for new target
def putCoords():
    x = random.randint(100, 900)
    y = random.randint(50, 500)
    # opdating coords of target
    main_window.co_ords.append([x, y, x+30, y+30])

# updates variables of game called when new game started
def variableUpdate():
    main_window.at_start = 1
    main_window.key_pressed = ''
    main_window.bool_image_change = False
    main_window.state = ''
    main_window.previous_state = ''
    main_window.playing = False
    main_window.key_bind_id = 0
    main_window.x_moment_change = 0.5
    main_window.y_moment_change = 0.5
    main_window.speed_of_snake = 1
    main_window.x_pos = 120
    main_window.y_pos = 30
    main_window.score = 0
    main_window.co_ords = []
    putCoords()

variableUpdate()
targetImageUpdate()
onStart()
main_window.mainloop()
