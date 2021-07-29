define config.developer = True

init python:
    galleryItems = []

    class GalleryItem:
        def __init__(self, char, label, thumbnail, scope=None):
            self.char = char
            self.pageNum = len(filter(lambda s: s.char == char, galleryItems)) // 8 + 1
            self.label = label

            if scope is None: self.scope = {}
            else: self.scope = scope

            self.thumbnail = os.path.join("/images/", thumbnail)
            galleryItems.append(self)

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

    $ scopeDict = {"povname":persistent.povname, "frname":persistent.frname, "vioname":persistent.vioname}

    return

screen sceneGalleryMenu():
    tag menu
    modal True
    add "/modAdditions/images/galleryBackground.png"

    python:
        resetGalleryItems()

        galleryMenu = [
            [persistent.povname, "/images/Scenes/Chapter 1/c1 photo 2-5.jpg"],
            [persistent.vioname, "/images/Scenes/Chapter 1/c1 outside 3-10.jpg"],
            ["Other", "/images/Scenes/Chapter 4/c4 cafe 1-13.jpg"],
        ]

        Rita = GalleryItem(persistent.povname, "galleryScene1", "Scenes/Chapter 1/c1 photo 2-5.jpg", {"model_seduction":99})
        Rita = GalleryItem(persistent.povname, "c2hottub", "Scenes/Chapter 2/c2 pool 8.jpg")
        Rita = GalleryItem(persistent.povname, "galleryScene3", "Scenes/Chapter 2/c2 laundry 7.jpg")
        Rita = GalleryItem(persistent.povname, "galleryScene4", "Misc/Flashback/fb1.jpg", {"c2boy_sed":99, "exh":99})
        Rita = GalleryItem(persistent.povname, "galleryScene5", "Scenes/Chapter 2/c2 dream 1.jpg", {"boys_horny":99})
        Rita = GalleryItem(persistent.povname, "galleryScene6", "Scenes/Chapter 3/c3 intro 1.jpg", {"c2_end3":1})
        Rita = GalleryItem(persistent.povname, "c3wind", "Scenes/Chapter 3/c3 outside 4a.jpg", {"exh":99})
        Rita = GalleryItem(persistent.povname, "galleryScene7", "Scenes/Chapter 3/c3 outside 10a.jpg", {"exh":99})
        Rita = GalleryItem(persistent.povname, "galleryScene8", "Scenes/Chapter 3/c3 pizza 6.jpg", {"exh":99})
        Rita = GalleryItem(persistent.povname, "c3pool", "Scenes/Chapter 3/c3 pool 9.jpg", {"c2poolex":1})
        Rita = GalleryItem(persistent.povname, "c3end", "Scenes/Chapter 3/c3 end 7.jpg", {"c3pool":True, "c2_end2":1, "les":99})
        Rita = GalleryItem(persistent.povname, "c4bed", "Scenes/Chapter 4/c4 park 1.jpg", {"exh":99})
        Rita = GalleryItem(persistent.povname, "c4bed", "Scenes/Chapter 4/c4 park 9n.jpg", {"exh":99})
        Rita = GalleryItem(persistent.povname, "c4hroom", "Scenes/Chapter 4/c4 hotspring 10.jpg")
        Rita = GalleryItem(persistent.povname, "galleryScene15", "Scenes/Chapter 5/c5 photo 13.jpg", {"exh":99, "model_seduction":99}) # 5472
        Rita = GalleryItem(persistent.povname, "galleryScene14", "Scenes/Chapter 5/c5 locker 11.jpg") # 5969
        Rita = GalleryItem(persistent.povname, "galleryScene13", "Scenes/Chapter 5/c5 hj 3.jpg") # 6100
        Rita = GalleryItem(persistent.povname, "galleryScene12", "Scenes/Chapter 5/c5 end 6.jpg", {"c3boytease":True}) # 7420
        Rita = GalleryItem(persistent.povname, "galleryScene17", "Scenes/Chapter 6/c6 boys 10.jpg")
        Rita = GalleryItem(persistent.povname, "galleryScene18", "Scenes/Chapter 6/c6 pool 17.jpg")
        Rita = GalleryItem(persistent.povname, "galleryScene19", "Scenes/Chapter 7/c7 home 23.jpg")
        Rita = GalleryItem(persistent.povname, "galleryScene20", "Scenes/Chapter 7/c7 locker 22.jpg")
        Rita = GalleryItem(persistent.povname, "galleryScene21", "Scenes/Chapter 7/c7 pool 12.jpg")
        Rita = GalleryItem(persistent.povname, "galleryScene22", "Scenes/Chapter 8/c8 josh bjclimax 2.jpg")
        Rita = GalleryItem(persistent.povname, "galleryScene23", "Scenes/Chapter 8/c8 pizzaboy 12.jpg")
        Rita_Violet = GalleryItem(persistent.povname, "c9vioscene", "Scenes/Chapter 9/c9 vio 30.jpg", {"c9lunasex":True, "c9hadsex":True})
        Rita_Luna = GalleryItem(persistent.povname, "c9lunascene", "Scenes/Chapter 9/c9 luna 32.jpg", {"c9lunasex":True, "c9hadsex":True})
        Rita = GalleryItem(persistent.povname, "c9cjscene", "Scenes/Chapter 9/c9 threesome 52-c.jpg", {"c9lunasex":True, "c9hadsex":True})

        Violet = GalleryItem(persistent.vioname, "galleryScene2", "Scenes/Chapter 2/c2 outside 3-15.jpg")
        Violet = GalleryItem(persistent.vioname, "galleryScene9", "Scenes/Chapter 3/c3 viosex 4.jpg", {"vioc":1})
        Violet = GalleryItem(persistent.vioname, "galleryScene10", "Scenes/Chapter 4/c4 vtoi 2.jpg")
        Violet = GalleryItem(persistent.vioname, "galleryScene11", "Scenes/Chapter 5/c5 viosex 2.jpg")
        Violet = GalleryItem(persistent.vioname, "galleryScene24", "Scenes/Chapter 7/c7 vio mmf 21.jpg")

        Luna = GalleryItem("Other", "galleryScene16", "Scenes/Chapter 5/c5 luna 2.jpg")
        Luna = GalleryItem("Other", "galleryScene25", "Scenes/Chapter 6/c6 lunahome 10.jpg")
        Luna = GalleryItem("Other", "galleryScene26", "Scenes/Chapter 8/c8 cafe 13.jpg")

    fixed:
        xysize (1536, 98)
        pos (85, 14)

        text "Scene Gallery":
            style "modTextHeader"
            align (0.5, 0.5)

    vbox:
        spacing 20
        pos (1666, 39)

        imagebutton:
            action Hide("sceneGalleryMenu"), ShowMenu("main_menu")
            idle "/modAdditions/images/backButton.png"
            hover Transform(im.MatrixColor("/modAdditions/images/backButton.png", im.matrix.brightness(0.2)))

    fixed:
        xysize (1875, 789)
        pos(19, 115)

        vpgrid:
            cols 4
            spacing 50
            align (0.5, 0.5)

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
    add "/modAdditions/images/galleryBackground.png"

    fixed:
        xysize (1536, 98)
        pos (85, 14)

        text "[galleryCharacter] Scenes - Page [galleryPageNumber]":
            style "modTextHeader"
            align (0.5, 0.5)

    vbox:
        spacing 20
        pos (1666, 39)

        imagebutton:
            if galleryPageNumber == 1:
                action Show("sceneGalleryMenu"), Hide("sceneCharacterMenu")
            else:
                action SetVariable("galleryPageNumber", galleryPageNumber - 1)
            idle "/modAdditions/images/backButton.png"
            hover im.MatrixColor("/modAdditions/images/backButton.png", im.matrix.brightness(0.2))

        if galleryPageNumber != max([galleryItem.pageNum for galleryItem in galleryItems if galleryItem.char == galleryCharacter]):
            imagebutton:
                action SetVariable("galleryPageNumber", galleryPageNumber + 1)
                idle "/modAdditions/images/nextButton.png"
                hover im.MatrixColor("/modAdditions/images/nextButton.png", im.matrix.brightness(0.2))

    fixed:
        xysize (1875, 789)
        pos(19, 115)

        vpgrid:
            cols 4
            spacing 50
            align (0.5, 0.5)

            for galleryItem in galleryItems:
                if galleryItem.char == galleryCharacter and galleryItem.pageNum == galleryPageNumber:
                    imagebutton:
                        action Replay(galleryItem.label, scope=updateScope(galleryItem.scope), locked=False)
                        idle Transform(galleryItem.thumbnail, zoom=0.2)
                        hover Transform(im.MatrixColor(galleryItem.thumbnail, im.matrix.brightness(0.2)), zoom=0.2)
                        insensitive Transform(im.Blur(galleryItem.thumbnail, 15), zoom=0.2)
