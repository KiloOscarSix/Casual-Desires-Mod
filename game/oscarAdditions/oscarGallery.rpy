init python:
    galleryCharacter = ""
    galleryPageNumber = 1

    sceneGalleryMenuDict = {
    "galleryMenu": [
    ["{}".format(persistent.povname), "/images/Scenes/Chapter 1/c1 photo 2-5.jpg"],
    ["{}".format(persistent.vioname), "/images/Scenes/Chapter 1/c1 photo 2-5.jpg"],
    ],
    "{}".format(persistent.povname): {
    1: [
    ["galleryScene1", {"model_seduction":99}, "/images/Scenes/Chapter 1/c1 photo 2-5.jpg"],
    ["c2hottub", {}, "/images/Scenes/Chapter 2/c2 pool 8.jpg"],
    ["galleryScene3", {}, "/images/Scenes/Chapter 2/c2 laundry 7.jpg"],
    ["galleryScene4", {"c2boy_sed":99, "exh":99}, "/images/Misc/Flashback/fb1.jpg"],
    ["galleryScene5", {"boys_horny":99}, "/images/Scenes/Chapter 2/c2 dream 1.jpg"],
    ["galleryScene6", {"c2_end3":1}, "/images/Scenes/Chapter 3/c3 intro 1.jpg"],
    ["c3wind", {"exh":99}, "/images/Scenes/Chapter 3/c3 outside 4a.jpg"],
    ["galleryScene7", {"exh":99}, "/images/Scenes/Chapter 3/c3 outside 10a.jpg"],
    ],
    2: [
    ["galleryScene8", {"exh":99}, "/images/Scenes/Chapter 3/c3 pizza 6.jpg"],
    ["c3pool", {"c2poolex":1}, "/images/Scenes/Chapter 3/c3 pool 9.jpg"],
    ["c3end", {"c3pool":True, "c2_end2":1, "les":99}, "/images/Scenes/Chapter 3/c3 end 7.jpg"],
    ["galleryScene9", {"vioc":1}, "/images/Scenes/Chapter 3/c3 viosex 4.jpg"],
    ["c4bed", {"exh":99}, "/images/Scenes/Chapter 4/c4 park 1.jpg"],
    ["c4bed", {"exh":99}, "/images/Scenes/Chapter 4/c4 park 9n.jpg"],
    ["c4hroom", {}, "/images/Scenes/Chapter 4/c4 hotspring 10.jpg"],
    ],
    },
    "{}".format(persistent.vioname): {
    1: [
    ["galleryScene2", {}, "/images/Scenes/Chapter 2/c2 outside 3-15.jpg"],
    ["galleryScene10", {}, "/images/Scenes/Chapter 4/c4 vtoi 2.jpg"],
    ],
    },
    }

label galleryNameChange:
    default persistent.povname = ""
    default persistent.frname = ""
    default persistent.vioname = ""
    if persistent.povname == "":
        show heroine portrait intro
        with dissolve
        $ persistent.povname = renpy.input("What will you name the female protagonist?", default="Rita")
        hide heroine portrait intro
    if persistent.frname == "":
        show femalefriend portrait intro
        with dissolve
        $ persistent.frname = renpy.input("What will you name [persistent.povname]'s Japanese friend?", default="Haruka")
        hide femalefriend portrait intro
    if persistent.vioname == "":
        show secondary portrait intro
        with dissolve
        $ persistent.vioname = renpy.input("What will you name the secondary heroine?", default="Violet")
        hide secondary portrait intro
    return

screen sceneGalleryMenu():
    tag menu
    modal True
    add "#23272a"

    text "Oscar's Scene Gallery":
        style "modTextHeader"
        xcenter 0.5
        ycenter 165

    vbox:
        spacing 20
        pos (1868, 50)

        fixed:
            xmaximum 186
            ymaximum 76
            xanchor 1.0

            imagebutton:
                action Hide("sceneGalleryMenu"), ShowMenu("main_menu")
                idle "/oscarAdditions/images/button.png"
                hover Transform(im.MatrixColor("/oscarAdditions/images/button.png", im.matrix.brightness(0.2)))
            text "Back":
                style "modTextBody"
                xcenter 0.5
                ycenter 0.5

        imagebutton:
            action OpenURL("https://www.patreon.com/oscarsix/overview")
            idle Transform("/oscarAdditions/images/become_a_patron_button.png", zoom=0.7465437788)
            hover Transform(im.MatrixColor("/oscarAdditions/images/become_a_patron_button.png", im.matrix.brightness(0.2)), zoom=0.7465437788)
            xanchor 1.0

    vpgrid:
        cols 4
        xspacing 50
        yspacing 37
        pos (117, 360)

        for i in sceneGalleryMenuDict["galleryMenu"]:
            vbox:
                imagebutton:
                    action ShowMenu("sceneCharacterMenu"), Hide("sceneGalleryMenu"), SetVariable("galleryCharacter", i[0])
                    idle Transform(i[1], zoom=0.2)
                    hover Transform(im.MatrixColor(i[1], im.matrix.brightness(0.2)), zoom=0.2)
                text i[0]:
                    style "modTextBody"
                    xcenter 0.5

screen sceneCharacterMenu():
    tag menu
    modal True
    add "#23272a"

    text "[galleryCharacter] Scenes - Page [galleryPageNumber]":
        style "modTextHeader"
        xcenter 0.5
        ycenter 165

    vbox:
        spacing 20
        pos (1868, 50)

        fixed:
            xmaximum 186
            ymaximum 76
            xanchor 1.0

            imagebutton:
                if galleryPageNumber == 1:
                    action Hide("sceneCharacterMenu"), Show("sceneGalleryMenu")
                else:
                    action SetVariable("galleryPageNumber", galleryPageNumber - 1)
                idle "/oscarAdditions/images/button.png"
                hover im.MatrixColor("/oscarAdditions/images/button.png", im.matrix.brightness(0.2))
            text "Back":
                style "modTextBody"
                xcenter 0.5
                ycenter 0.5

        fixed:
            xmaximum 186
            ymaximum 76
            xanchor 1.0

            if galleryPageNumber != len(sceneGalleryMenuDict[galleryCharacter]):
                imagebutton:
                    action SetVariable("galleryPageNumber", galleryPageNumber + 1)
                    idle "/oscarAdditions/images/button.png"
                    hover im.MatrixColor("/oscarAdditions/images/button.png", im.matrix.brightness(0.2))
                text "Next":
                    style "modTextBody"
                    xcenter 0.5
                    ycenter 0.5

    vpgrid:
        cols 4
        xspacing 50
        yspacing 100
        pos (117, 360)

        for i in sceneGalleryMenuDict[galleryCharacter][galleryPageNumber]:
            $ scopeDict = {"povname":persistent.povname, "frname":persistent.frname, "vioname":persistent.vioname}
            $ scopeDict.update(i[1])
            imagebutton:
                action Replay(i[0], scope=scopeDict, locked=False)
                idle Transform(i[2], zoom=0.2)
                hover Transform(im.MatrixColor(i[2], im.matrix.brightness(0.2)), zoom=0.2)
