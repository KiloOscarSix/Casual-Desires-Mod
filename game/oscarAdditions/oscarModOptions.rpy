init python:
    mod = Character("OscarSix", color="#0f0")

    gr = "{color=#0f0}"
    red = "{color=#f00}"

    def resetGalleryName():
        persistent.povname = ""
        persistent.frname = ""
        persistant.vioname = ""

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

            textbutton "Charm Points":
                action [ToggleVariable("CharmRoute", true_value="{color=#0f0}[Charm Route]", false_value=""), ToggleVariable("Charm_5", true_value="{color=#f00}[Charm -5]", false_value=""), ToggleVariable("Charm_1", true_value="{color=#f00}[Charm -1]", false_value=""), ToggleVariable("Charm1", true_value="{color=#0f0}[Charm +1]", false_value=""), ToggleVariable("Charm2", true_value="{color=#0f0}[Charm +2]", false_value="")]

            textbutton "Dark Points":
                action [ToggleVariable("DarkRoute", true_value="{color=#0f0}[Dark Route]", false_value=""), ToggleVariable("Dark_5", true_value="{color=#f00}[Dark -5]", false_value=""), ToggleVariable("Dark_1", true_value="{color=#f00}[Dark -1]", false_value=""), ToggleVariable("Dark1", true_value="{color=#0f0}[Dark +1]", false_value=""), ToggleVariable("Dark3", true_value="{color=#0f0}[Dark +3]", false_value=""), ToggleVariable("Dark5", true_value="{color=#0f0}[Dark +5]", false_value=""), ToggleVariable("Dark10", true_value="{color=#0f0}[Dark +10]", false_value=""), ToggleVariable("Dark12", true_value="{color=#0f0}[Dark +12]", false_value="")]

            textbutton "Janice Path":
                action [ToggleVariable("JanicePath", true_value="{color=#0f0}[Janice Path]", false_value=""), ToggleVariable("JaniceDomPath", true_value="{color=#0f0}[Janice Dom Path]", false_value="")]

            textbutton "Fran Path":
                action ToggleVariable("FranPath", true_value="{color=#0f0}[Fran Path]", false_value="")

            textbutton "Abby Path":
                action ToggleVariable("AbbyPath", true_value="{color=#0f0}[Abby Path]", false_value="")

            textbutton "Stacy Path":
                action [ToggleVariable("StacyPath", true_value="{color=#0f0}[Stacy Path]", false_value=""), ToggleVariable("StacyLovePath", true_value="{color=#0f0}[Stacy Love Path]", false_value=""), ToggleVariable("StacySubPath", true_value="{color=#0f0}[Stacy Sub Path]", false_value="")]

            textbutton "Gena Path":
                action ToggleVariable("GenaPath", true_value="{color=#0f0}[Gena Path]", false_value="")

            textbutton "Sofia Path":
                action ToggleVariable("SofiaPath", true_value="{color=#0f0}[Sofia Path]", false_value="")

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
