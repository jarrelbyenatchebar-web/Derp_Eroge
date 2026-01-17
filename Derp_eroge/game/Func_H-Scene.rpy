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

        add "shizuku normal"


        textbutton "Exit" action Return()