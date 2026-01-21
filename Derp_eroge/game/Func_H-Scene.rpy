label minigame:

    window hide
    call screen mg_screen
    window show

    return

screen mg_screen():

    vbox:
        spacing 20

        text "H-Scene Menu" size 40
        text "Affection: [Affection]" size 30
        text "Intimacy: [Lust]" size 30

    

    frame:
        xalign 0.3

        background "container_bg"

        vbox:
            add "upper_torso" yalign 0.5


    
    textbutton "Exit" action Return():
        xalign 0.99
        yalign 0.1