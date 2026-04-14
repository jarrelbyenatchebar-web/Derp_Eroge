label minigame:

    window hide
    call screen mg_screen()
    window show

    return

init python:
    dragging = False
    btn_x = 400
    btn_y = 300
    vel_x = 0
    vel_y = 0
    last_x = 0
    last_y = 0

    friction = 0.9  # velocity multiplier per tick (0-1, lower = stops faster)
    throw_scale = 1.2   # throw velocity multiplier
    tick = 0.016    # 60 FPS timer

    def physics_tick():
        global btn_x, btn_y, vel_x, vel_y,last_x, last_y, dragging

        if dragging:
            mx, my = renpy.get_mouse_pos() # turns mouse position into tuple
            vel_x = (mx - last_x) * throw_scale
            vel_y = (my - last_y) * throw_scale

            btn_x = float(mx)
            btn_y = float(my)
            last_x =float(mx)
            last_y =float(my)
        else: #apply the velocity

            btn_x += vel_x
            btn_y += vel_y
            vel_x *= friction
            vel_y *= friction

            # keep the button on screen
            btn_x = max(0.0, min(btn_x, 1280.0)) # assuming button width is 100
            btn_y = max(0.0, min(btn_y, 720.0)) # assuming button height is 50

            #stops the jank
            if abs(vel_x) < 0.1:
                vel_x = 0
            if abs(vel_y) < 0.1:
                vel_y = 0

        renpy.restart_interaction() # forces the screen to update


screen mg_screen():

    vbox:
        spacing 20

        text "H-Scene Menu" size 40
        text "Affection: [Affection]" size 30
        text "Intimacy: [Lust]" size 30

    #drag button
    timer tick repeat True action Function(physics_tick)

    imagebutton:
        idle "bg_button"
        xpos int(btn_x)
        ypos int(btn_y)

        hovered SetVariable("dragging", True)
        unhovered SetVariable("dragging", False)
        action NullAction() # prevents clicks from doing anything

    
    textbutton "Exit" action Return():
        xalign 0.99
        yalign 0.1