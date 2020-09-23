init python:
    mod = Character("OscarSix", color="#0f0")

    gr = "{color=#0f0}"
    red = "{color=#f00}"

    def resetGalleryName():
        persistent.povname = ""
        persistent.frname = ""
        persistent.vioname = ""

screen modOptions():
    tag menu
    modal True

    add "#23272a"

    vbox:
        xcenter 0.5
        ypos 50
        spacing 100

        text "Walkthrough Options" style "modTextHeader"

        text "Turn on and off character paths" style "modTextBody" xcenter 0.5

    frame:
        xcenter 0.5
        ycenter 0.5
        padding (20, 20)
        grid 4 2:
            spacing 50
            style_prefix "check"

            textbutton "":
                action [ToggleVariable("", true_value="", false_value="")]

    textbutton "Reset Gallery Names":
        action [Function(resetGalleryName), ui.callsinnewcontext("resetGalleryNameConfirmed")]
        xcenter 0.5
        ypos 650
        text_style "modTextButtonBody"

    textbutton _("Return") action ShowMenu("save"), Hide("modWalkthroughOptions"):
        yanchor 1.0
        pos (100, 1030)
        text_style "modTextButtonHeader"

label resetGalleryNameConfirmed:
    mod "Gallery Names have been reset.\nNext time you load up the Scene Gallery you will be asked to reenter the character names."
    return
