init python:
    cheatMenuDict = {
    "Rita": [
    ["Preversion", "perv", 20],
    ["Sexual Experiances", "sexe", 20],
    ["Exhibition", "exh", 20],
    ["Model Seduction", "model_seduction", 20],
    ["Lesbian", "les", 20],
    ["Innocent", "inn", 20],
    ],
    "Violet": [
    ["Vio C", "vioc", 20],
    ["Vio P", "viop", 20],
    ],
    }

screen cheatMenu():
    modal True
    zorder 200

    python:
        cheatMenuList = ["Rita", "Violet"]

    default shownCheatMenu = None

    add "/modAdditions/images/cheatMenuBackground.png"
    fixed:
        xysize (1877, 99)
        pos (18, 13)

        hbox:
            xcenter 0.5
            ycenter 0.5
            spacing 100
            for i in cheatMenuList:
                textbutton i:
                    action [Function(renpy.retain_after_load), SetScreenVariable("shownCheatMenu", value=i)]
                    text_style "modTextButtonHeader"

    for i in cheatMenuList:
        if shownCheatMenu == i:
            use cheatMenuValues(cheatMenuChar=i)

    imagebutton:
        action [Hide("cheatMenu"), Hide("cheatMenuValues"), SetVariable("quick_menu", True)]
        idle "/modAdditions/images/cheatMenuBackButton.png"
        hover im.MatrixColor("/modAdditions/images/cheatMenuBackButton.png", im.matrix.brightness(0.2))
        pos (1666, 50)

screen cheatMenuValues(cheatMenuChar):
    tag cheatmenu
    zorder 199

    vbox:
        pos (100, 200)
        spacing 50

        vpgrid:
            cols 4
            spacing 50
            for x in cheatMenuDict[cheatMenuChar]:

                vbox:
                    spacing 20
                    text "[x[0]]:" style "modTextBody2"
                    fixed:
                        xysize (352, 42)

                        bar value VariableValue(x[1], x[2]):
                            left_bar Frame("gui/bar/left.png", 10, 0)
                            right_bar Frame("gui/bar/right.png", 10, 0)
                        text "{:}".format(getattr(store, x[1])) xcenter 0.5 ycenter 0.5

        if cheatMenuChar == "Rita":
            frame:
                xsize 300
                padding (20, 20)
                vpgrid:
                    cols 4
                    spacing 50
                    style_prefix "check"

                    textbutton "ModelMotive":
                        action ToggleVariable("model_motive", true_value=1, false_value=0)
