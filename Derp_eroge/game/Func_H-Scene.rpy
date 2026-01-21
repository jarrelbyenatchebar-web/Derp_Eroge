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

    


        textbutton "Exit" action Return()

    add "shizuku normal":
            xalign 0.5
            yalign 0.3