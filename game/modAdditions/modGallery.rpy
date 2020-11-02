init python:
    galleryItems = []

    class GalleryItem:
        def __init__(self, char, pageNum, label, thumbnail, scope=None):
            self.char = char
            self.pageNum = pageNum
            self.label = label
            if scope is None:
                scope = {}
            self.scope = scope
            self.thumbnail = "/images/{}".format(thumbnail)
            galleryItems.append(self)

    def galleryDecreasePageNumber():
        global galleryPageNumber
        galleryPageNumber -= 1

    def galleryIncreasePageNumber():
        global galleryPageNumber
        galleryPageNumber += 1

    def updateScope(newScope):
        rv = scopeDict.copy()
        rv.update(newScope)
        return rv

    def resetGalleryItems():
        global galleryItems
        galleryItems = []

default galleryPageNumber = 1
default scopeDict = {}

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

    python:
        resetGalleryItems()

        scopeDict = {"povname":persistent.povname, "frname":persistent.frname, "vioname":persistent.vioname}
        galleryMenu = [
        ["{}".format(persistent.povname), "/images/Scenes/Chapter 1/c1 photo 2-5.jpg"],
        ["{}".format(persistent.vioname), "/images/Scenes/Chapter 1/c1 photo 2-5.jpg"],
        ["Other", "/images/Scenes/Chapter 1/c1 photo 2-5.jpg"],
        ]

        Rita = GalleryItem("{}".format(persistent.povname), 1, "galleryScene1", "Scenes/Chapter 1/c1 photo 2-5.jpg", {"model_seduction":99})
        Rita = GalleryItem("{}".format(persistent.povname), 1, "c2hottub", "Scenes/Chapter 2/c2 pool 8.jpg")
        Rita = GalleryItem("{}".format(persistent.povname), 1, "galleryScene3", "Scenes/Chapter 2/c2 laundry 7.jpg")
        Rita = GalleryItem("{}".format(persistent.povname), 1, "galleryScene4", "Misc/Flashback/fb1.jpg", {"c2boy_sed":99, "exh":99})
        Rita = GalleryItem("{}".format(persistent.povname), 1, "galleryScene5", "Scenes/Chapter 2/c2 dream 1.jpg", {"boys_horny":99})
        Rita = GalleryItem("{}".format(persistent.povname), 1, "galleryScene6", "Scenes/Chapter 3/c3 intro 1.jpg", {"c2_end3":1})
        Rita = GalleryItem("{}".format(persistent.povname), 1, "c3wind", "Scenes/Chapter 3/c3 outside 4a.jpg", {"exh":99})
        Rita = GalleryItem("{}".format(persistent.povname), 1, "galleryScene7", "Scenes/Chapter 3/c3 outside 10a.jpg", {"exh":99})
        Rita = GalleryItem("{}".format(persistent.povname), 2, "galleryScene8", "Scenes/Chapter 3/c3 pizza 6.jpg", {"exh":99})
        Rita = GalleryItem("{}".format(persistent.povname), 2, "c3pool", "Scenes/Chapter 3/c3 pool 9.jpg", {"c2poolex":1})
        Rita = GalleryItem("{}".format(persistent.povname), 2, "c3end", "Scenes/Chapter 3/c3 end 7.jpg", {"c3pool":True, "c2_end2":1, "les":99})
        Rita = GalleryItem("{}".format(persistent.povname), 2, "c4bed", "Scenes/Chapter 4/c4 park 1.jpg", {"exh":99})
        Rita = GalleryItem("{}".format(persistent.povname), 2, "c4bed", "Scenes/Chapter 4/c4 park 9n.jpg", {"exh":99})
        Rita = GalleryItem("{}".format(persistent.povname), 2, "c4hroom", "Scenes/Chapter 4/c4 hotspring 10.jpg")
        Rita = GalleryItem("{}".format(persistent.povname), 2, "galleryScene15", "Scenes/Chapter 5/c5 photo 13.jpg", {"exh":99, "model_seduction":99}) # 5472
        Rita = GalleryItem("{}".format(persistent.povname), 2, "galleryScene14", "Scenes/Chapter 5/c5 locker 11.jpg") # 5969
        Rita = GalleryItem("{}".format(persistent.povname), 3, "galleryScene13", "Scenes/Chapter 5/c5 hj 3.jpg") # 6100
        Rita = GalleryItem("{}".format(persistent.povname), 3, "galleryScene12", "Scenes/Chapter 5/c5 end 6.jpg", {"c3boytease":True}) # 7420

        Violet = GalleryItem("{}".format(persistent.vioname), 1, "galleryScene2", "Scenes/Chapter 2/c2 outside 3-15.jpg")
        Rita = GalleryItem("{}".format(persistent.vioname), 1, "galleryScene9", "Scenes/Chapter 3/c3 viosex 4.jpg", {"vioc":1})
        Violet = GalleryItem("{}".format(persistent.vioname), 1, "galleryScene10", "Scenes/Chapter 4/c4 vtoi 2.jpg")
        Violet = GalleryItem("{}".format(persistent.vioname), 1, "galleryScene11", "Scenes/Chapter 5/c5 viosex 2.jpg")

        Other = GalleryItem("Other", 1, "galleryScene16", "Scenes/Chapter 5/c5 luna 2.jpg")

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
                idle "/modAdditions/images/button.png"
                hover Transform(im.MatrixColor("/modAdditions/images/button.png", im.matrix.brightness(0.2)))
            text "Back":
                style "modTextBody"
                xcenter 0.5
                ycenter 0.5

        imagebutton:
            action OpenURL("https://www.patreon.com/oscarsix/overview")
            idle Transform("/modAdditions/images/become_a_patron_button.png", zoom=0.7465437788)
            hover Transform(im.MatrixColor("/modAdditions/images/become_a_patron_button.png", im.matrix.brightness(0.2)), zoom=0.7465437788)
            xanchor 1.0

    vpgrid:
        cols 4
        xspacing 50
        yspacing 37
        pos (117, 360)

        for i in galleryMenu:
            vbox:
                imagebutton:
                    action [Show("sceneCharacterMenu", galleryCharacter=i[0]), Hide("sceneGalleryMenu")]
                    idle Transform(i[1], zoom=0.2)
                    hover Transform(im.MatrixColor(i[1], im.matrix.brightness(0.2)), zoom=0.2)
                text i[0]:
                    style "modTextBody"
                    xcenter 0.5

screen sceneCharacterMenu(galleryCharacter="All"):
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
                    action Show("sceneGalleryMenu"), Hide("sceneCharacterMenu")
                else:
                    action Function(galleryDecreasePageNumber)
                idle "/modAdditions/images/button.png"
                hover im.MatrixColor("/modAdditions/images/button.png", im.matrix.brightness(0.2))
            text "Back":
                style "modTextBody"
                xcenter 0.5
                ycenter 0.5

        fixed:
            xmaximum 186
            ymaximum 76
            xanchor 1.0

            if galleryPageNumber != max([galleryItem.pageNum for galleryItem in galleryItems if galleryItem.char == galleryCharacter]):
                imagebutton:
                    action Function(galleryIncreasePageNumber)
                    idle "/modAdditions/images/button.png"
                    hover im.MatrixColor("/modAdditions/images/button.png", im.matrix.brightness(0.2))
                text "Next":
                    style "modTextBody"
                    xcenter 0.5
                    ycenter 0.5

    vpgrid:
        cols 4
        xspacing 50
        yspacing 100
        pos (117, 360)

        for galleryItem in galleryItems:
            if galleryItem.char == galleryCharacter and galleryItem.pageNum == galleryPageNumber:
                imagebutton:
                    action Replay(galleryItem.label, scope=updateScope(galleryItem.scope), locked=False)
                    idle Transform(galleryItem.thumbnail, zoom=0.2)
                    hover Transform(im.MatrixColor(galleryItem.thumbnail, im.matrix.brightness(0.2)), zoom=0.2)

label beforeGalleryScene9:
    menu:
        mod "Path?"
        "Good":
            $ wheretoafterslayerbath = "good"
        "Neutral":
            $ wheretoafterslayerbath = "neutral"
        "Evil":
            $ wheretoafterslayerbath = "Evil"
    jump galleryScene9
