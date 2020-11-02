init python:
    gr = "{color=#0f0}"

define mod = Character("OscarSix", color="#0f0")

screen modOptions():
    modal True

    add "#23272a"

    vbox:
        xcenter 0.5
        ypos 33
        spacing 33

        text "Mod Options" style "modTextHeader"

        textbutton "Change In-Game Names" action ui.callsinnewcontext("changeIngameNames") text_style "modTextButtonHeader"

        textbutton "Change Gallery Names" action ui.callsinnewcontext("changeGalleryNames") text_style "modTextButtonHeader"

    textbutton _("Return") action Hide("modOptions"):
        text_style "modTextButtonHeader"
        yanchor 1.0
        align (0.1, 0.9)

label changeGalleryNames:
    show heroine portrait intro
    with dissolve
    $ persistent.povname = renpy.input("What will you name the female protagonist?", default="Rita")
    hide heroine portrait intro
    show femalefriend portrait intro
    with dissolve
    $ persistent.frname = renpy.input("What will you name [persistent.povname]'s Japanese friend?", default="Haruka")
    hide femalefriend portrait intro
    show secondary portrait intro
    with dissolve
    $ persistent.vioname = renpy.input("What will you name the secondary heroine?", default="Violet")
    hide secondary portrait intro
    mod "Gallery names successful changed"
    return

label changeIngameNames:
    mod "Make sure to do this in the save you wish to change names for."
    show heroine portrait intro
    with dissolve
    $ povname = renpy.input("What will you name the female protagonist?", default="Rita")
    hide heroine portrait intro
    show femalefriend portrait intro
    with dissolve
    $ frname = renpy.input("What will you name [persistent.povname]'s Japanese friend?", default="Haruka")
    hide femalefriend portrait intro
    show secondary portrait intro
    with dissolve
    $ vioname = renpy.input("What will you name the secondary heroine?", default="Violet")
    hide secondary portrait intro
    mod "Names successful changed"
    return
