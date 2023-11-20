
from pynput import keyboard
import tkinter as tkr

fullscreen = True
settings = True
relx = .5
rely = .354


# generate points to create polygon crosshair
# takes radius of polygon, mid x coord of canvas, mid y coord of canvas
def crosshair_points(radius, x_mid, y_mid):
    x = x_mid - 0.5*radius
    y = y_mid - 0.5*radius

    return [x, y, x+radius, y, x+radius, y+radius, x, y+radius, x, y]


# create transparent crosshair window
def run_app():
    # create window
    app = tkr.Tk()

    # edit window
    app.title("crosshair")
    app.configure(background="#ff0f0f")


    # create a canvas object within window (app) for the crosshair
    c = tkr.Canvas(app, width=100, height=100, background="#ff0f0f", highlightthickness=0)
    c.pack()

    # create crosshair in center of canvas
    points = crosshair_points(8, int(c['width'])/2, int(c['height'])/2)
    c.create_polygon(points, outline='white', fill='', smooth='true', splinesteps=20, width=1)
    c.place(relx=relx, rely=rely, anchor=tkr.CENTER)




    # create a canvas object within window (app) for the settings text
    settings_c = tkr.Canvas(app, background="#ff0f0f", highlightthickness=0)
    settings_c.pack()
    settings_c.place(relx=0.93, rely=0.18, anchor=tkr.CENTER)

    # create settings label
    text = "\n\
    SETTINGS\n\n\
    h   hide/show Settings\n\n\
    f   full screen                \n\n\
    c   change color            \n\n\
    ↑   move up                   \n\n\
    ↓   move down              \n\n\
    →   move right               \n\n\
    ←   move left                  \n\n\
        "
    label = tkr.Label(settings_c, width=25, height=17, bg="#333333", fg="white", anchor='w', text=text)
    label.pack()




    # set attributes of window (app)
    # app.overrideredirect(True)
    app.wm_attributes("-fullscreen", fullscreen)
    app.wm_attributes("-transparentcolor", "#ff0f0f")
    app.wm_attributes("-topmost", True)



    # key event handlers
    def up_press(event):
        if (settings):
            global rely
            rely -= .001
            c.place(relx=relx, rely=rely, anchor=tkr.CENTER)

    def down_press(event):
        if (settings):
            global rely
            rely += .001
            c.place(relx=relx, rely=rely, anchor=tkr.CENTER)

    def right_press(event):
        if (settings):
            global relx
            relx += .001
            c.place(relx=relx, rely=rely, anchor=tkr.CENTER)

    def left_press(event):
        if (settings):
            global relx
            relx -= .001
            c.place(relx=relx, rely=rely, anchor=tkr.CENTER)

    def hide_press(event):
        global settings
        if (settings):
            settings = False
            label.configure(background="#ff0f0f", text="")
        else:
            settings = True
            label.configure(background="#333333", text=text)

    def full_screen(event):
        global fullscreen
        if (fullscreen):
            fullscreen = False
        else:
            fullscreen = True
        app.wm_attributes("-fullscreen", fullscreen)


    # bind keys to window (app)
    app.bind("<Up>", up_press)
    app.bind("<Down>", down_press)
    app.bind("<Right>", right_press)
    app.bind("<Left>", left_press)
    app.bind("<h>", hide_press)
    app.bind("<f>", full_screen)

    # activate window (app)
    app.mainloop()

run_app()