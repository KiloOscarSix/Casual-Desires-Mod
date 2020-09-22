############ MAIN MENU THEME ##############################################
define config.main_menu_music = "audio/sunny.mp3"
$renpy.music.set_volume(0.2, 0, 'music')

############ SPLASH SCREEN ################################################
label splashscreen:
scene black
show text "This game is only intended for access by adults {b}over the age of 18{/b}. The creator holds no responsibility for minors launching the program without parental approval. All characters portrayed are above the age of 18, and thus abides by Canada and US law." with dissolve
with Pause(6)
hide text with dissolve
return

############# DEFINITIONS #################################################
define moveinoutdissolve = ComposeTransition(dissolve, before=moveoutleft, after=moveinright)
define fadehold = Fade(0.5, 1.0, 1.0)
define fadeholdshort = Fade(0.5, 0.5, 0.5)
define fadeholdlong = Fade(0.5, 1.5, 1.5)
define fadein = Fade(0.5, 0.0, 0.0)
define fadeinlong = Fade(0.5, 0.5, 2.5)
define fadeinverylong = Fade(0.5, 0.5, 5.0)
define flash = Fade(0.1, 0.0, 0.5, color="#fff")
define dissolvesemilong = Dissolve(1.5)
define dissolvelong = Dissolve(2.0)
define dissolveverylong = Dissolve(5.0)

#VISIBLE STATS
default vir = "Yes"
default anvi = "Yes"
default perv = 0
default sexp = 0
default scount = 0
default bjcount = 0
default hjcount = 0
default sexe = 0
default fp = "None"
default chaptercount = "Prologue"

#INVISIBLE STATS
default exh = 0
default boys_horny = 0
default model_motive = 0
default model_seduction = 0
default c2boy_sed = 0
default c2poolex = 0
default c2see = 0
default c2_end1 = 0
default c2_end2 = 0
default c2_end3 = 0
default les = 0
default het = 0
default inn = 0
default vioc = 0
default viop = 0
default c3pizza = False
default c3boytease = False
default c3pool = False
default c3nopool = False
default c4viostranger = False
default c4viosharing = False
default c4kissenjoy = False

############# CURSOR ######################################################
define config.mouse = {"default":[ ("images/misc/cursor.png", 1, 1) ] }

############# CHARACTER DEFINITIONS #######################################
define m = Character("Narrator", color="F28E3F")
define ion = Character("ionDivvy", color="F28E3F")
define pov = Character("[povname]", color="C94AE2")
default povname = "Rita"
define vio = Character("[vioname]", color="#3F65F2")
default vioname = "Violet"
define fr = Character("[frname]", color="#479D2F")
default frname = "Haruka"
define luna = Character("Luna", color="#FF5C33")
define c = Character("Connor")
define j = Character("Josh")
define bo = Character("Boys")
define boy = Character("Boy")
define ev = Character("Everyone")
define ni = Character("Nick")
define ja = Character("Jason")
define luc = Character("Lucas")
define st = Character("Stranger")
define girl = Character("Girl")
define man = Character("Man")
define men = Character("Men")
define wom = Character("Woman")
define voi = Character("Voice")
define rdad = Character("[pov]'s Dad")
define rmom = Character("[pov]'s Mom")
define manl = Character("Man On Left")
define manr = Character("Man On Right")

############# STATS #####################################################
screen control():
    frame:
        xalign 0.98
        yalign 0.98
        textbutton "Stats" action If(renpy.get_screen("stat_box"), Hide("stat_box"), Show("stat_box"))

screen stat_box():
    frame:
        align (0.98,0.02)
        vbox:
            text "Chapter: [chaptercount]"
            text "Virgin: [vir]"
            if vir == "No":
                text "First partner(s): [fp]"
            text "Anal virgin: [anvi]"
            text "Sex partners: [sexp]"
            if vir == "No":
                text "Times penetrated: [scount]"
            if hjcount >= 1:
                text "Handjobs given: [hjcount]"
            if bjcount >= 1:
                text "Blowjobs given: [bjcount]"
            text "Sexual experiences: [sexe]"
            text "Perversion: [perv]/10"

######### GAME START #######################################################

label start:
    show screen control()
    scene intro bg 1
    with pixellate
    m "Welcome to the perverted world of {b}Casual Desires{/b}!"
    m "I, your benign and degenerate narrator, shall do my best to entertain you with our lovely heroine's gradual fall into depravity."
    show heroine portrait intro
    with dissolve
    m "......{p}My, what a seductive little minx."
    $ povname = renpy.input("What will you name the female protagonist? Default is {b}Rita{/b}.")
    $ povname = povname.strip()
    if povname == "":
        $ povname="Rita"
    m "Nice choice!"
    hide heroine portrait intro
    with dissolve
    show intro bg 2
    with dissolve
    m "And what about her friend?"
    show femalefriend portrait intro
    with dissolve
    $ frname = renpy.input("What will you name [pov]'s Japanese friend? Default is {b}Haruka{/b}.")
    $ frname = frname.strip()
    if frname == "":
        $ frname="Haruka"
    m "Cool!"
    hide femalefriend portrait intro
    with dissolve
    show intro bg 3
    with dissolve
    m "And finally..."
    show secondary portrait intro
    with dissolve
    $ vioname = renpy.input("What will you name the secondary heroine? Default is {b}Violet{/b}.")
    $ vioname = vioname.strip()
    if vioname == "":
        $ vioname="Violet"
    m "Gotcha!"
    hide secondary portrait intro
    with dissolve
    show intro bg 1
    with dissolve
    m "Thank you for showing interest in {b}Casual Desires{/b}. I hope you will enjoy it as much as I've enjoyed developing it!"
    if persistent.pskip:
        m "I notice you've completed the Prologue before. Would you like to skip straight to Chapter 1? \n {i}{size=-5}(Note: The first player choice will default to teasing the boys.){/size}{/i}"
        menu:
            "Yes.":
                $ perv +=1
                $ boys_horny +=1
                $ sexe +=1
                stop music fadeout 0.5
                jump chapter1
                with fadehold
            "No.":
                m "Then let's get started once more!"
    else:
        m "...... And now, without further ado, I shall say adieu and let our {i}[pov]{/i} take over......"

label prologue:
    stop music fadeout 1.0
    show prologue title
    with fadeholdlong
    play music "audio/cloudy.mp3" fadein 0.5 loop
    pov "Umm... well, hello there!"
    pov "My name is {i}[pov]{/i}. I graduated from high school last summer, which means I'm supposedly an adult now, or something!"
    pov "I'm 18 years old, but my 19th birthday is in a couple months."
    hide prologue title
    show intro room 1
    with dissolvelong
    pov "In others words, I'll finally be able to drink legally here in Canada."
    pov "Though it's not like my parents would ever let me drink..."
    pov "Speaking of my parents, they left a couple days ago for some sort of business opportunity in Japan."
    show intro parents
    with dissolve
    pov "My dad's from a German background."
    pov "He was born in Germany and moved to Canada as an adult. So, he ended up getting dual citizenships."
    pov "My mom, on the other hand, is Japanese, which explains why they go to Japan sometimes."
    pov "I've gone with them a few times, and even studied there for a year back in middle school."
    pov "But Canada has always felt more... freeing, I guess."
    pov "Unlike my parents, I'm a Canadian through and through, and never grew up elsewhere like they did."
    pov "...... But... yeah, we've never been short on money, especially with mom being a fairly well-known pianist."
    pov "Some might even call us rich."
    show intro room 1
    with dissolve
    pov "So I've always had to act well-mannered and such around them, and was forced to study like crazy in school."
    pov "As long as I worked hard, they gave me spending money as a reward, and more or less overlooked my hobbies."
    pov "...... Though, obviously, the things that were {i}really{/i} private, I would hide on my phone or computer."
    pov "God, would they ever kill me if they saw the kinds of things I have on my PC..."
    pov "......"
    show cityscape afternoon 2
    with fadeholdshort
    pov "We live in Vancouver— the third biggest city in Canada."
    pov "Or to be more specific, our house is in the Richmond area, where a lot of rich and Asian families settle down."
    pov "We've been here pretty much my whole life, aside from that one year when I studied in Japan on an exchange program."
    pov "Vancouver is a bit of an... anomaly, I guess you could say."
    pov "It's the only major city in North America with a roughly 50 percent Asian population."
    pov "It's basically a blend of Asian and European cultures, which works well for me due to my own half-Japanese, half-German background."
    pov "I've never felt out of place here. And I can connect with both the European and Asian sides of me."
    hide cityscape afternoon 2
    show intro room 2
    with dissolve
    pov "Anyway, since my parents are gone for now, that means I'm home alone taking care of the place until they're back."
    pov "How long will that be? I'm not really sure, but..."
    pov "They're supposedly training him as a translator, or something like that."
    show intro room 3
    with dissolve
    pov "I mean, it's not like I mind being by myself!"
    pov "At least now I can have the freedom to do whatever I want."
    pov "Plus, getting a knock on your door when you're looking at {i}certain{/i} things online is kind of annoying..."
    show intro boys 1
    with fadeholdshort
    pov "My best friends are my two former high school classmates, {i}Connor{/i} and {i}Josh{/i}."
    pov "I like to sometimes mix the two and call them {i}'CJ'{/i}."
    pov "Why? Well, to annoy them, of course."
    show intro boys 2
    with dissolve
    pov "They're really cool guys, and we share all sorts of geeky hobbies with each other."
    pov "Unlike with other girls, I can play video games with them, make perverted and insensitive jokes, and just be myself."
    pov "I do enjoy typical {i}girl things{/i} like fashion and make-up, too, but..."
    pov "Nothing beats the fun of a great game or anime."
    show intro boys 3
    with dissolve
    pov "That's why I've mostly been together with them, ever since we first met in our freshman homeroom class."
    pov "There were rumours at first, I mean... a girl hanging out with two guys after school all the time..."
    pov "But I was never on bad terms with my other classmates, so that got cleared up pretty quick. {size=-5}(Thank god for that...){/size}"
    pov "I just never really became too close with anyone else."
    pov "Not in high school, at least."
    show intro room 4
    with fadeholdshort
    pov "Heck, I've never even had a boyfriend yet, and kissing is as far as I've gone."
    pov "During prom night, there was some drinking involved and, well... me and a boy ended up kissing for a little bit."
    pov "But that's the extent of my experience."
    pov "I've never had sex or anything like that. And I've never touched a guy, or been touched before."
    pov "I guess that's a bit surprising considering I'm almost 19."
    pov "Most girls lose their virginity during high school, after all."
    pov "Personally, I just don't want to have sex simply because everyone else is doing it, or because I feel like I'll be judged if I don't."
    pov "I want to experience it when the time is right."
    pov "I don't want to regret anything."
    show intro room 5
    with dissolvelong
    pov "One day (hopefully some time soon) I'd like to get a boyfriend and experiment with him, but I'm not in any real rush."
    pov "Plus, I'm a bit worried I might weird them out, since I have a pretty high sexual drive (I think)."
    pov "It's a bit embarrassing to say, but I've been watching porn, well, pretty much every day for years now."
    pov "And being a girl my age, touching myself has just kind of gone with that."
    show intro room 6
    with dissolve
    pov "More importantly... and this is a big secret of mine... I have what you might call an {i}'exhibitionism'{/i} fetish."
    pov "Basically, an exhibitionist enjoys showing their body off, especially in public."
    pov "If they're on the extreme end, they might go naked in a public area, or flash random people."
    pov "Most girls with this kink probably stop at cosplaying, or uploading videos of themselves masturbating— stuff like that."
    show intro room 7
    with dissolve
    pov "Either way, it's pretty perverted, I guess..."
    pov "I mostly just get excited by the idea, and it's not like I've ever done it myself, but..."
    pov "Sometimes I wonder if maybe it wouldn't be so bad to just give someone a look here or there."
    pov "I mean, it's just looking, after all."
    pov "And imagining someone undressing me with their eyes, or even thinking of me at night, is kind of exciting."
    pov "I'm not sure why..."
    pov "I guess I'm a bit weird..."
    show intro room 8
    with dissolve
    pov "Very weird, probably..."
    pov "......"
    pov "Anyway, I'm not sure why I'm talking to myself!"
    pov "Maybe it means I'm lonely...? {size=-10}Wait, crap!{/size}"
    pov "...... Ah well."
    pov "Time to fire up the computer."
    stop music fadeout 1.0
    "..."
    "......"

    play music "audio/chill.mp3" fadein 2.0 loop
    window hide
    show intro room 9
    with dissolvelong
    with Pause(1)
    pov "(Ah!)"
    window show
    pov "(That's the spot!)"
    pov "(Yes!!)"
    with vpunch
    pov "(Ah!!)"
    with vpunch
    pov "(Ohhh——!!!!)"
    pov "(Hah... hah.... {i}*exhales*{/i})"
    pov "(Amazing...)"
    show intro room 10
    with fadeholdshort
    pov "This is my nightly routine, you could say."
    pov "Usually I'll just click on whatever video is popular at the moment, but tonight I found a really nice one."
    pov "Not that I'd ever do anything like that in real life, but..."
    pov "I came so hard that I don't even feel like moving anymore."
    pov "Maybe I overdid it a little..."
    pov "Those two are probably free tomorrow, so I'll text them in the morning and see if I can hang out!"
    stop music fadeout 0.5
    "..."
    "......"

    play music "<from 1.6>audio/absurd.mp3" fadein 0.5 loop
    show intro boys 4
    with irisout
    j "God damnit, man! Are you kidding me!?"
    j "That character is so fucking broken that it's not even fair!"
    c "Dude, it's not my fault that you suck at the game..."
    c "And, just sayin', but being salty like this all the time is why you can't get laid."
    j "Pfft... whatever. Go suck a dick, man."
    show intro boys 5
    with dissolve
    pov "Wait, Connor, did you suddenly have sex or something?"
    pov "I thought there were two boys in here who've never gotten a girl wet before..."
    c "S-shut up!"
    c "All girls are sluts, anyway, and I can't compete in {i}Smash{/i} if I'm giving all my time to some chick."
    show intro boys 6
    with dissolve
    pov "... Did you say something... ?"
    c "N-no... no! I mean other girls, obviously! You're nothing like the roasties that were at school."
    c "Unlike them you actually have a personality."
    c "And, hell, I mean, you're pretty enough that I don't know why you don't have a guy yet..."
    show intro boys 5
    with dissolve
    pov "Look, I know I'm cute and all, but don't get your hopes up, alright?"
    j "Haha! Get wrecked, dude."
    c "Hey now, that's not cool, [pov]! {i}*laughs*{/i}"
    pov "{i}*chuckles*{/i} But really, I just haven't met anyone I like yet."
    pov "Plus, I'm having enough fun just hanging out with you guys, anyway."
    j "Haha..."
    "..."
    show intro boys 7
    with dissolve
    pov "{i}(Wait, is he blushing?){/i}"
    pov "{i}(I know they aren't very confident with girls, but shouldn't they both be used to me after all this time?){/i}"
    pov "{i}(We've been hanging out for over four years now, after all.){/i}"
    pov "{i}(And it's not like I haven't made dirty jokes with them before.){/i}"
    pov "{i}(We're close enough that they almost feel like brothers to me sometimes...){/i}"
    pov "{i}(Hmm...){/i}"
    pov "{i}(You know what? I think I'll try teasing them a bit!){/i}"
    show intro boys 8
    with pixellate
    with Pause(0.5)
    pov "Hmm... I forgot what other games you guys have."
    pov "Let me take a look for a sec."
    pov "Mmm..."
    pov "..."
    show intro boys 10
    with dissolve
    bo ".....!"
    c "{i}(Woah...){/i}"
    j "{i}(Not bad, [pov]...){/i}"
    pov "{i}(Oh... I can definitely tell I've gotten their attention.){/i}"
    pov "{i}(Should I go a bit further?){/i}"
    menu:
        "Tease them more. [gr]\[BoysHorny +1\]":
            show intro boys 9
            with dissolve
            with Pause(0.5)
            pov "Are you guys liking what you see?"
            with hpunch
            pov "... Nice and big?"
            bo "W-what?!"
            pov "I mean, do you like the new {i}Smash{/i} stage you unlocked? You guys were excited a minute ago."
            j "Ohh... the game..."
            c "U-uhh... yeah... haha..."
            bo "..."
            bo "......"
            pov "{i}(Haha! They're completely silent.){/i}"
            pov "{i}(Too easy... way too easy.){/i}"
            $ boys_horny +=1
        "That's enough for now. [gr]\[Innocent +1\]":
            show intro boys 8
            with dissolve
            pov "{i}(Nah... I'd rather not push it too far and have them think I'm some kind of weirdo.){/i}"
            pov "{i}(Besides, it's not like this is my only chance to tease them...){/i}"
            pov "{i}(I see them pretty much every other day, after all.){/i}"
            pov "{i}(Just a little treat for their eyes will do for now!){/i}"
            $ inn +=1
    $ sexe +=1
    show intro boys 10
    with fadeholdshort
    pov "{i}(This is a little bit embarrassing, after all...){/i}"
    pov "{i}(I wonder if it's the first time they've ever seen a girl's butt this close?){/i}"
    pov "{i}(Or maybe they're surprised my body has matured a bit compared to before?){/i}"
    pov "{i}(I mean, I'm not the boobless nerd I was back in freshman year, after all.){/i}"
    pov "{i}(Either way...){/i}"
    show intro boys 5
    with dissolvelong
    pov "Well... there's some fun-looking ones here, but I think I'm still in the mood for watching you guys play {i}Smash{/i}, after all."
    j "A-All right."
    c "Suit yourself..."
    pov "{i}(Haha. They're usually swearing and trash-talking each other, but their reactions can be sort of cute!){/i}"
    show intro boys 11
    with dissolve
    pov "{i}(Maybe it'd be fun to tease them a bit more often?){/i}"
    pov "{i}(For example... next time I could try teasing them in my underwear.){/i}"
    pov "{i}(I mean, we're best friends, so I trust them and know that they won't do anything bad.){/i}"
    pov "{i}(And it's just looking...){/i}"
    pov "{i}(Hmm...){/i}"
    pov "{i}(It's still early, so I guess I'll keep playing games for a bit.){/i}"
    "......"
    show intro boys 12
    with fadeholdlong
    pov "{size=-4}{i}*stretches*{/i}{/size}"
    pov "{i}(Time sure flies when playing games. It's already past my dinner time!){/i}"
    pov "{i}(I guess I should just head back home, instead of stopping somewhere on the way.){/i}"
    pov "{i}(I mean, who knows what kind of perverts are outside once it gets dark.){/i}"
    pov "{i}(Perverts, huh...){/i}"
    pov "{i}{size=-6}*giggles*{/size}{/i}"
    stop music fadeout 2.0
    show intro bg 1
    with wiperight
    "......"
    $ perv +=1

    m "{size=-3}Congratulations! [pov] has reached: {b}Perversion, Rank 1{/b}.{/size}"
    m "{size=-3}She is now capable of:{/size}"
    m "{size=-3}— Light exhibitionism (underwear){p}— Teasing{/size}"
    m "{size=-3}Nothing wrong with enjoying a bit of attention, {i}right{/i}?{/size}"
    "......"
    "{b}Prologue: Complete{/b}"

    ####################### END OF PROLOGUE ####################################

    ####################### CHAPTER 1 ##########################################
    $ persistent.pskip = True

label chapter1:
    $ chaptercount = 1
    play music "audio/feelgood.mp3" fadein 4.0 loop
    show c1 title
    with fadehold
    with Pause(1)
    pov "{size=-7}{i}*sighs*{/i}{/size}"
    pov "Now that my parents are away and I'm done with school, there just hasn't been a whole lot to do..."
    pov "Playing games with the guys is fun and all, and I've had plenty of time to relax and catch up on my other hobbies, but..."
    pov "There's only so much gaming and anime you can do until it gets boring."
    pov "...... maybe it's time to try something else."
    show c1 basement 1
    with dissolve
    pov "I mean, I'm an adult now, after all, and can't just be sitting at home all the time with no school or job."
    pov "Just because my parents have lots of money, doesn't mean I should mooch off them forever like a bum."
    pov "Plus, I'm feeling a lot more bored lately without anybody home."
    pov "I still hang out with Connor and Josh every couple days or so, but it's not the same as having family you can talk to every day at home."
    pov "I guess I should consider finding a roommate and a place of my own eventually, but for now..."
    pov "...... I wonder if there's something I could try part-time?"
    show c1 basement 2
    with dissolve
    pov "Hmm..."
    pov "Well..."
    pov "There's a few that seem pretty easy, but they all look so boring..."
    pov "A cashier? No thank you!"
    pov "Ew... I'm definitely not stocking things in a supermarket..."
    pov "Wait, what about this?"
    "{i}{size=-4}Recruiting: Female models for fashion website. Must be 18 or older.{/size}{/i}"
    menu:
        "Hmm... should I?"
        "Absolutely! [gr]\[ModelMotived +1\]":
            show c1 basement 3
            with dissolve
            pov "{i}!!{/i}"
            pov "This seems interesting!"
            pov "I've always admired models and how pretty they are."
            pov "Plus, the amount of attention they get from guys always made me feel kind of jealous..."
            pov "I mean, if it's possible, I'd at least like to give modelling a try!"
            $model_motive+=1
        "I'm not sure...":
            show c1 basement 3
            with dissolve
            pov "I mean, I like having pictures of me taken, but..."
            pov "Having to make all sorts of forced poses and what not seems like it could get exhausting."
            pov "Then again, compared to managing a cash register or stocking things in some dump?{p}I'll {i}gladly{/i} be some old man's picture monkey instead!!"

    pov "Though I'm not sure what this '{i}18 or older{/i}' part is about..."
    pov "Maybe there's some sort of law that makes using pictures of minors illegal? I don't know much about politics..."
    m "{size=-7}([pov], is the ToS a joke to you?!){/size}"
    pov "...... Did someone just say something to me?"
    if model_motive >= 1:
        pov "...... Anyway, modelling seems like a lot of fun, and the pay is pretty high compared to most of these other listings!"
    else:
        pov "...... Anyway, modelling doesn't sound too bad, and the pay is pretty high compared to most of these other listings."
    pov "No experience is even required!"
    show c1 basement 4
    with dissolve
    pov "They're apparently having open door interviews for the next couple of days."
    pov "That's a bit unconventional, but..."
    pov "I guess a model's looks are most important, and you can't tell unless you see them in person?"
    pov "I mean, I {i}do{/i} have confidence in my looks..."
    pov "...... especially my body."
    pov "I've been around two perverted boys long enough to know what people are looking for, after all."
    if boys_horny >=1:
        pov "Or maybe I'm the perverted one... ?"
    pov "{i}{size=-7}*giggles*{/size}{/i}"
    show c1 basement 5
    with dissolve
    pov "Anyway, guess I can get ready in a bit and take the train there this afternoon."
    pov "It's still only 10 in the morning. And it's not like I have anything better to do today."
    pov "I feel more comfortable having an interview face-to-face, rather than over the phone, so I guess it's not that scary."
    stop music fadeout 2.0
    pov "There's no real harm in showing up and seeing how it goes."
    pov "Time to shower!"
    "......"

    play music "audio/swing.mp3" fadein 2.0 loop
    show c1 outside 1-1
    with fadehold
    "......"
    pov "Hmm... is this the place? My Google Maps is pointing here."
    pov "It's on the 8th floor, so... it's probably in this big office building here."
    pov "I'm pretty nervous since this is my first job interview."
    pov "What do they even ask models, anyway... ?"
    pov "Jeez, talk about being unprepared!"
    show c1 outside 1-2
    with dissolve
    pov "Well, whatever... there's no point in backing out now that I've come all this way."
    pov "The worst that can happen is that I'm just sent back home."
    pov "And I can always make up for my lack of preparation with enthusiasm."
    if model_motive >= 1:
        pov "I've always wanted to be a model, anyway, so as long as I communicate that I should be good!"
    else:
        pov "I don't really like pretending, but... smiling is the most important part of an interview, I hear. And I've always been a good actress!"
    pov "Guess I'll just do my best and see how it goes!"
    show c1 elevator 1
    with fadehold
    pov "I hope I'm headed to the right place..."
    pov "It'd be pretty embarrassing if I was in the wrong building, and got lost in some random office."
    pov "I usually don't go to these sorts of places, after all, so it's a bit confusing..."
    pov "Especially for a teenaged girl."
    pov "Most of the time when I go out it's just to the mall, or a restaurant or something like that."
    pov "Well, whatever the case..."
    pov "We should be at the 8th floor any second."

    show c1 interview 1
    with fadehold
    pov "{i}(So this is the office, huh.){/i}"
    pov "{i}(A lot fancier than I was expecting.){/i}"
    pov "{i}(There was a security guy outside who asked me a couple questions before letting me in.){/i}"
    pov "{i}(And then the receptionist lady at the front desk told me to come to this room.){/i}"
    pov "{i}(She said to wait about 15 minutes or so?){/i}"
    pov "{i}(Well, I guess that's what I'll be doing... waiting... nervously...){/i}"
    "......"
    show c1 interview 2
    with fadehold
    man "Sorry for the wait."
    man "You can take a seat here if you don't mind."
    pov "Thank you!"
    man "No problem."
    show c1 interview 3
    with dissolve
    man "I'll be the one conducting your interview today."
    man "You can call me Jason— no need for any formalities."
    pov "{size=-3}{i}*nods*{/i}{/size}"
    ja "Alright, so, first off, please introduce yourself and tell me about your reason for coming here today."
    pov "Sure!"
    show c1 interview 4
    with dissolve
    pov "My name is [pov]! I'm 18 years old and from a half-Japanese, half-German background."
    pov "I'm not attending university at the moment, so I'm looking to work part-time while I decide my future plans."
    if model_motive >= 1:
        pov "I've always had a lot of respect for the fashion industry, and I've aspired to try modelling ever since I was a kid."
        pov "So, I thought this would be a great opportunity for me."
        pov "As soon as I saw the listing on my phone, I knew I couldn't pass this chance up!"
        ja "{i}*chuckles*{/i} Well, I'm happy to hear you're so excited."
    else:
        pov "I thought it would be best to try something new, and learn and grow from those experiences."
        pov "And with something like modelling, I'd not only grow personally, but be able to use my social skills to my advantage."
        pov "I've always been a people-person, you could say. {i}*giggles*{/i}"
        ja "Haha. You do seem energetic, that's for sure."
    show c1 interview 5
    with dissolve
    ja "Anyway, I'm not going to bore you with the typical interview questions."
    ja "Modelling is all about charm and appearances, see."
    ja "And you do look, to put it mildly... gorgeous."
    ja "It's not often I come across a pretty young lady with as much potential as yourself."
    ja "{i}(She also looks quite naive, and with a bit of time, manipulable...){/i}"
    show c1 interview 4
    with dissolve
    pov "{i}*giggles*{/i} Thank you! I'm flattered to hear that."
    pov "{i}(That look in his eyes... I can tell when a guy is having naughty thoughts.){/i}"
    pov "{i}(Men can be so simple sometimes...)"
    show c1 interview 3
    with dissolve
    ja "So, how about we do a quick mock shoot?"
    ja "I'm technically the owner here, but really my duties are more... {i}hands-on{/i}, you could say."
    ja "If all goes fine I'll give you the job right away."
    pov "Wait, really? Yes! I'll gladly participate."
    ja "Great!"
    "......"
    show c1 changing 1
    with fadehold
    pov "So this is the 6th floor changing room, huh."
    pov "I know there's a lot of other companies that work here, but this is still much bigger than I expected."
    pov "At least this is the girls room... I think... so I won't get peeped on."
    pov "Right......?"
    show c1 changing 2
    with dissolve
    pov "Hmm..."
    pov "You know, thinking about it..."
    pov "This test shoot is pretty sudden, after all."
    pov "I guess you can't always decide whether or not to hire, just by talking to someone."
    pov "... speaking of which, I should probably hurry up and change now."
    pov "Shouldn't keep him waiting too long!"
    pov "There's a few different sizes here, so one of these outfits should hopefully fit."
    show c1 photo 1-1
    with fadehold
    play sound "audio/effects/camera1.mp3"
    "*click*"
    play sound "audio/effects/camera2.mp3"
    "*snap*"
    pov "Like this?"
    pov "{i}(This is my first time wearing something so mature.){/i}"
    if model_motive >=1:
        pov "{i}(Having the camera on me like this... it's kind of exciting.){/i}"
        if boys_horny >=1:
            pov "{i}(Reminds me of those two, a few days ago.){/i}"
    else:
        pov "{i}(And especially in front of a camera... it makes me a bit nervous.){/i}"
    ja "Good, good! Yes! That outfit fits you perfectly."
    ja "My, if you aren't one of the most beautiful girls I've laid eyes on."
    show c1 photo 1-2
    with dissolve
    pov "{size=-7}{i}*giggles*{/i}{/size} Thank you!"
    ja "Alright, give me one last pose."
    ja "Let's see... how about something a bit more... sexy?"
    ja "Or if you'd prefer, you could just do something... hmm... 'cute' instead."
    pov "OK... got it!"
    pov "{i}(Hmm...){/i}"
    menu:
        "Which should I choose?"
        "Sexy pose. [gr]\[ModelSeduction +1\]":
            show c1 photo 1-3
            with dissolve
            pov "{i}(Hehe... I'll give him a bit of a treat. That's what he wants, after all.){/i}"
            pov "How's this?"
            ja "W-woah... !"
            ja "Yes, that'll do just fine! Perfect!"
            play sound "audio/effects/camera1.mp3"
            "*snap*"
            ja "Amazing!"
            play sound "audio/effects/camera3.mp3"
            "*click*"
            ja "Jeez, you sure know how to impress..."
            ja "... Alright, I think that about does it."
            $ model_seduction +=1
        "Cute pose. [gr]\[Innocent +1\]":
            show c1 photo 1-4
            with dissolve
            pov "{i}(Nah... I'd rather stick with what I know best, for now.){/i}"
            pov "How's this?"
            ja "Yes! That's what I like to see."
            ja "You sure know how to look good before a camera."
            play sound "audio/effects/camera1.mp3"
            "*snap*"
            ja "Nice!"
            play sound "audio/effects/camera2.mp3"
            "*click*"
            ja "Alright, I think that about does it."
            $ inn +=1
    show c1 photo 1-5
    with dissolve
    ja "So, regarding your results..."
    ja "Although it's clear you are a still a beginner, I am pleasantly surprised by the amount of potential you have shown today."
    ja "Your smile is natural, and I could sense your energy and passion."
    ja "...... [pov], you have the talent for modelling - there's no doubt in my mind."
    ja "You're hired."
    pov "Wait, really?! Yes!! Thank you so much!!"
    pov "{i}(I'm hired that easily?!){/i}"
    ja "I'll email you a work schedule in a couple days or so, after I finalize some things."
    ja "Thanks for showing up here today. I'm looking forward to our next meeting, [pov]. "
    ja "{i}(...... Oh, am I ever looking forward to it.){/i}"
    pov "Not a problem at all! And thank you so much for giving me this opportunity."
    pov "I won't let you down! {i}*winks*{/i}"

    show c1 subway 1
    with fadehold
    pov "Finally done..."
    pov ".... So I've gone from being a lazy NEET, to actually having a job, just like that."
    if model_motive >= 1:
        pov "Plus, it's my dream job, modelling!"
    pov "Not bad. Not bad at all!"
    show c1 subway 2
    with dissolve
    pov "I was so nervous at first that I thought my heart would explode, but I'm in a pretty good mood now!"
    pov "Never expected I'd get a job on my first try."
    pov "I should celebrate my victory somehow..."
    stop music fadeout 2.0
    pov "Hmm..."
    pov "Maybe I'll treat myself to a bit of shopping on the way home!"

    play music "<from 5.0>audio/obento.mp3" fadein 2.0 loop
    show c1 home 1-1
    with fadeholdlong
    pov "It's been a few days since my interview."
    pov "Since then, I've mostly just been waiting, and playing more games and stuff to pass the time."
    pov "This morning I finally got an email."
    pov "It said to come in the day after tomorrow, for my first shift."
    pov "Sadly, due to the way modelling works, I won't exactly be able to work every day..."
    pov "Once or twice a week seems to be the pace for now, according to my boss."
    show c1 home 1-2
    with dissolve
    pov "But the pay is good! And one day of work is still better than zero!"
    pov "Plus, it leaves plenty of time open in case I decide to find a second job later on."
    pov "Anyway, I still have a couple days until my first shift... so I might as well do something!"
    pov "Maybe the guys are free today?"
    pov "I'll try inviting them here this time."

    show c1 boys 1
    with fadehold
    c "Yes! That's what he gets."
    j "Haha! Thank god. I couldn't stand seeing this dickhead any longer."
    j "...... Man, this episode is intense."
    j "What do you think about it, [pov]?"
    pov "It's pretty good, I guess!"
    show c1 boys 2
    with dissolve
    pov "{i}(...... they're busy as usual.){/i}"
    pov "{i}(I'm not really in the mood for tons of anime today, though.){/i}"
    pov "{i}(We've already been watching for a couple hours now.){/i}"
    pov "{i}(And I prefer romance shows over action, anyway...){/i}"
    pov "{i}(Hmm...){/i}"
    pov "{i}(...... I have just the right idea!){/i}"
    show c1 boys 3
    with dissolve
    pov "Hey, do you mind if I take a shower quick?"
    pov "It's almost summer and you know I get really self-conscious about sweating."
    c "That's bulls— oh, yeah, sure, go ahead."
    c "It's your own house, after all."
    c "No need to ask us."
    pov "Thanks!"
    pov "{i}(I'll gladly do just that!){/i}"
    pov "{i}(Time for a round two...){/i}"
    "......"
    show c1 boys 4
    with fadehold
    pov "Umm... I accidentally got water on my clothes."
    pov "So I noticed you left one of your shirts here, and put that on, if it's OK?"
    bo "!!"
    c "U-Uhh... yeah, I don't mind."
    j "......"
    pov "Alright, thanks!"
    show c1 boys 5
    with dissolve
    pov "{i}(Looks like I caught them by surprise again!){/i}"
    pov "{i}(They're looking at me everywhere except my face.){/i}"
    pov "{i}(Boys can be so predictable...){/i}"
    pov "{i}(Hmm...){/i}"
    menu:
        "Tease them a bit?"
        "Why not? [gr]\[BoysHorny +1\] \[Sexe +1\]":
            pov "{i}(I'll ramp it up a little bit. It's not like they aren't used to seeing my underwear lying around.){/i}"
            window hide
            show c1 boys 6
            with pixellate
            with Pause (2.5)
            pov "By the way, I was wondering if I should get some new lingerie."
            pov "Maybe I should wear something a bit more mature, y'know?"
            pov "What do you guys think?"
            pov "Sometimes these panties are a bit tight around my butt..."
            show c1 boys 7
            with dissolve
            with Pause (2.0)
            pov "...... squeezes around all sorts of places..."
            c "Umm.... uhh, I think it looks just fine..."
            j "... Yeah. I guess it's hot enou—— wait, crap!"
            j "I mean, it fits you nicely!"
            pov "{i}*giggles*{/i}"
            pov "Really?"
            pov "{i}(I didn't expect they'd be able to come up with a proper answer.){/i}"
            pov "{i}(At least not with the scene before their eyes.){/i}"
            pov "Alright, good to know!"
            $ boys_horny +=1
            $ sexe +=1
        "Nah. I'm not in the mood. [gr]\[Innocent +1\]":
            pov "{i}(I mean, I'm already standing in front of them in my underwear!){/i}"
            pov "{i}(Nah... no need to get carried away.){/i}"
            pov "{i}(Everything in moderation, or whatever my dad says...){/i}"
            pov "{i}(There'll be plenty more chances to tease them, anyway!){/i}"
            pov "Hmm... maybe I should go clothes shopping soon."
            $ inn +=1
    show c1 boys 8
    with dissolve
    pov "I guess it's kinda pointless asking you guys for advice. {size=-10}{i}*laughs*{/i}{/size}"
    pov "You've both never had a girlfriend, after all..."
    j "H-hey! If you knew we don't know anything then why comment?!"
    c "Yeah, dude, no need to shit on us."
    c "I know when something looks good but I'm no expert on girl crap..."
    c "You're asking for underwear advice from a couple of dudes..."
    pov "That's true. Maybe I just like annoying you guys."
    c "Not 'maybe'... you {i}definitely{/i} do."
    ev "{size=-10}{i}*laughs*{/i}{/size}"
    show c1 boys 9
    with dissolve
    if boys_horny >=2:
        pov "Okay. Let's play a couple games before I fall asleep."
        pov "Who knows what kind of things you perverts might do to me if I pass out..."
        c "What the hell?! Why would I want to touch you..."
        pov "{i}(He's blushing again... clearly he's not being honest with himself.){/i}"
        pov "{i}(But that's what makes it so fun to tease them.){/i}"
        pov "Yeah, yeah. You'd be all over any girl that so much as glances at you."
    else:
        pov "All in good fun, though."
        pov "You're my best friends, so obviously I don't mean to hurt your feelings or anything..."
        pov "Well, maybe just a {i}little{/i}..."
    c "Pfft... whatever. Instead of shit-talking, why don't you try and beat me at this game?"
    c "I can't even remember the last time you were able to win against me."
    c "Let's see how tough you really are?"
    stop music fadeout 1.2
    pov "OK. You're on!"
    pov "I've just been holding back until now!"
    "......"

    play sound "audio/effects/cityambient.mp3" fadein 1.0
    show cityscape afternoon 2
    with fadeholdlong
    pause (2.0)
    hide cityscape afternoon 2
    stop sound fadeout 0.5
    play music "audio/swing.mp3" fadein 5.0 loop
    show c1 outside 2-1
    with fadeholdlong
    "Two days later."
    pov "It's almost the end of May now, so it's gotten a lot hotter outside."
    pov "Most of my time lately is spent indoors, but..."
    pov "Now it's finally time for my first real day of modelling."
    pov "I'm still a little nervous since it's only the second time around, but I kind of know what to expect... I think."
    if model_seduction >=1:
        pov "It's so easy to give men what they're looking for, after all..."
    pov "Anyway, no point in hanging around out here!"
    pov "Let's go!"

    show c1 office 1
    with fadehold
    ja "Hello, [pov]! Glad to see you again."
    ja "I've been looking forward to you joining our team."
    pov "I'm glad to see you, too! And I'm thankful for the opportunity."
    ja "Likewise."
    ja "Perhaps it was a fateful encounter. {size=-5}{i}*laughs*{/i}{/size}"
    show c1 office 2
    with dissolve
    ja "So, today we're not going to be doing typical fashion modelling like last time."
    ja "One of our other models recently finished this month's commissions."
    ja "Instead, we'll have you trying out a new set of lingerie for a women's magazine."
    ja "It's slightly more bold than what you wore last time, but..."
    ja "I trust you're OK with that?"
    pov "{i}(So... basically that means I'm wearing just underwear this time?{/i})"
    pov "Hmm..."
    show c1 office 3
    with dissolve
    if model_seduction >= 1:
        pov "{i}(I can't say I'm all that experienced with random people seeing me half-naked.){/i}"
        pov "{i}(But I already gave him some eye-candy last time, so this is pretty similar...){/i}"
        pov "{i}(And wearing only underwear is no different from being in a bikini, for example.){/i}"
        pov "{i}(No big deal!){/i}"
    else:
        pov "{i}(It's one thing to tease my friends, but to be half-dressed in front of someone I don't really know...){/i}"
        pov "{i}(It's a little bit embarrassing, after all.){/i}"
        pov "{i}(But... that's what models have to do. I'm not going to get anywhere if I don't break out of my comfort zone.){/i}"
    pov "Yup. That's fine with me!"
    show c1 office 4
    with dissolve
    ja "Great. My secretary will get you started."
    ja "She'll show you to the dressing room, where she'll help you get ready for the shoot."
    ja "We'll get going once that's all taken care of."
    pov "OK! Got it."
    "......"
label galleryScene1:
    show c1 photo 2-1
    with fadehold
    pov "{i}(Well, here I am...){/i}"
    pov "{i}(This is definitely a first for me.){/i}"
    pov "...... Does it fit me fine?"
    pov "{i}(I gave my measurements a few days ago, but it's hard not to feel a bit self-conscious.){/i}"
    pov "{i}(It's not like it's an everyday thing, having pictures taken of me half-naked...){/i}"
    show c1 photo 2-2
    with dissolve
    ja "Not a problem at all. It fits you like a glove."
    ja "I have to say, though, you're a bit more... err, voluptuous, than I had originally imagined."
    ja "Since swimwear modelling emphasizes the body, larger breasts will be a valuable asset."
    ja "Hmm... I'm impressed... you'll make a wonderful model, indeed."
    ja "No doubt you're popular with the boys?"
    pov "......"
    menu:
        "Tell him the truth. [gr]\[ModelSeduction +1\]":
            show c1 photo 2-3
            with dissolve
            pov "Well... I have had a lot of boys tell me I'm cute and hot and stuff."
            pov "Not so much when I was younger, but then I had a growth spurt and things changed a bit, I guess."
            pov "Lately, I feel like guys have been staring at, umm... my {i}breasts{/i} a lot."
            pov "I'm never sure if I should be flattered or annoyed..."
            ja "Haha. It's a natural instinct, so I wouldn't take it too personally."
            ja "And being a healthy young lady is never a bad thing."
            pov "{i}{size=-7}*giggles*{/size}{/i} I guess you might be right."
            $ model_seduction +=1
        "Brush off his comment. [gr]\[Innocent +1\]":
            show c1 photo 2-4
            with dissolve
            pov "Haha. I'm not too sure, but I guess I have gotten some compliments before."
            pov "I don't know if I'm that popular."
            ja "Well, either way, you'll be getting a lot more popular now."
            ja "... and I don't just mean popular with me. Haha!"
            $ inn +=1
    ja "Anyway, I'll just have you take a few poses over there."
    ja "I finished preparing the camera's settings while you were dressing, so we can get shooting right away."
    pov "Got it!"
    "......"
    show c1 photo 2-5
    with fadehold
    "15 minutes later."
    play sound "audio/effects/camera1.mp3"
    ja "{i}*click*{/i}"
    ja "Perfect! You really do have a talent for this."
    pov "Thank you!"
    ja "Next, can you, err... emphasize your breasts a bit?"
    show c1 photo 2-6
    with dissolve
    pov "Sure."
    ja "Good! Good! Yes, that's what I'm looking for."
    play sound "audio/effects/camera2.mp3"
    ja "{i}*click*{/i}"
    ja "Beautiful."
    ja "...... Alright, let's have you turn around. We'll finish up with a few shots from behind."
    show c1 photo 2-7
    with dissolve
    ja "Wow...!"
    ja "Now this is quite something."
    play sound "audio/effects/camera3.mp3"
    ja "{i}*snap*{/i}"
    ja "I can tell why the boys are so starstruck by you."
    if model_seduction >=2:
        ja "They must just want to sweep you off your feet."
        ja "If I was them, I wouldn't just let you be, either."
    else:
        ja "You were meant for modelling, after all."
    pov "{i}*giggles*{/i} Really?"
    "......"
    show c1 photo 2-8
    with dissolve
    ja "Okay, that about does it for today. Good work!"
    ja "You performed far better than I'd expect from a first-timer."
    pov "Thank you!"
    ja "We'll continue where we left off during your next shift."
    ja "As for your pay, it'll be automatically deposited into your bank account on the 15th and 30th of each month."
    ja "If you ever have any issues with payment, feel free to call me or the office staff."
    pov "OK! No problem."
    stop music fadeout 3.0
    show c1 photo 2-9
    with dissolve
    ja "{i}(God, I can't wait for the chance to get a taste of her...){/i}"
    ja "{i}(I wonder if she's already taken?){/i}"
    ja "{i}(A beauty like that, surely...){/i}"
    "......"
    $ renpy.end_replay()
    play sound "audio/effects/cityambient.mp3" fadein 1.0
    show cityscape dusk
    with fadeholdlong
    pause (2.0)
    hide cityscape dusk
    stop sound fadeout 1.0
    play music "audio/blues.ogg" fadein 4.0 loop
    show c1 outside 3-1
    with fadeholdlong
    pov "Hmm... that was definitely more exhausting than I pictured."
    pov "The real thing is different from a little mock-shoot, after all."
    pov "Having to make all these smiles and expressions, redoing the same poses over and over..."
    pov "Plus, the light blinding my eyes..."
    show c1 outside 3-2
    with dissolve
    if model_motive >=1:
        pov "But, still, I enjoyed it quite a lot!"
        pov "It just makes me even more impressed by all the famous models out there, and the stamina they have."
        if model_seduction >=1:
            pov "And hearing compliments non-stop, beautiful {i}this{/i}, perfect {i}that{/i}..."
            pov "...... it might have excited me a bit."
            pov "Hehe."
    else:
        pov "But it's not like all jobs are supposed to be easy."
        pov "And I still only just started, so I need to keep trying and doing better."
        pov "You can do it, [pov]!!"
    show c1 outside 3-3
    with dissolve
    pov "Hmmm......"
    pov "I'm tired, but I don't really feel like going home right away."
    pov "Maybe I'll walk around downtown a bit to clear my head."
    pov "I am getting pretty hungry, too, since it's already evening now."
    pov "It's not like there's a shortage of places to eat here in downtown Vancouver— especially if it's Asian food."
    pov "I love Japanese food, obviously, but I think I'm more in the mood for some sweets right now."
    stop music fadeout 2.0
    pov "That cafe on Dowing Street looked kind of neat, actually."
    pov "Maybe I'll g——"
    play music "<from 1.8>audio/garden.mp3" loop
    show c1 outside 3-4
    with pixellate
    pov "{i}(W-what?!){/i}"
    pov "{i}(Is someone touching my butt?!){/i}"
    pov "{i}(You're kidding me!){/i}"
    st "{i}*squeeze*{/i}"
    show c1 outside 3-5
    with dissolve
    st "Hey, girl, you wanna come for a drink with me?"
    pov "Uh... no... I'm good."
    pov "({i}I've had guys hitting on me before, but this is seriously crossing the line...!){/i}"
    st "No need to worry. C'mon, it'll be fun."
    show c1 outside 3-6
    with dissolve
    pov "No... really, I need to go. Sorry."
    st "Haha. You can go later on, can't you?"
    st "I know just the right place."
    st "I'll show you a good tim——"
    stop music fadeout 2.0
    show white
    with flash
    play sound "audio/effects/jab.wav"
    "{size=+15}{i}*KAPOW*{/i}{/size}"
    st "Gah!"
    girl "Are you okay?!"
    $ sexe +=1
    play music "audio/blues.ogg" fadein 2.0 loop
    hide white
    show c1 outside 3-7
    with fadehold
    pov "...... H-huh?"
    pov "{i}(He's laying on the floor?){/i}"
    pov "{i}(...... wait, did she just knock him down?!){/i}"
    show c1 outside 3-8
    with fadeholdshort
    girl "He ran away..."
    girl "Fucking perverts..."
    girl "He didn't do anything else to you, did he?"
    pov "N-no... he just grabbed me and tried to make me go somewhere with him."
    show c1 outside 3-9
    with dissolve
    girl "A textbook scumbag, huh."
    girl "I'm glad I noticed in time before things got any worse."
    girl "The place I work at is just at the end of this street."
    girl "I was about to get ready for my evening shift, and then I looked out the window and saw this douchebag touching you."
    pov "I-I see..."
    show c1 outside 3-10
    with dissolve
    girl "Anyway, this area is usually pretty safe, but creeps will take a chance if they see an opportunity."
    girl "Best to be careful."
    girl "My name is [vio], by the way."
    pov "Uh... umm... thank you. I'm [pov]."
    show c1 outside 3-11
    with dissolve
    vio "OK. I wish it was under better circumstances that we could introduce ourselves, but anyway..."
    vio "I take it you're not too used to this sort of thing."
    pov "No... I mean, I've had people hit on me before, but this was a first."
    vio "I figured as much."
    show c1 outside 3-12
    with dissolve
    vio "Anyway, how about this?"
    vio "I'll give you my number, and if any creep starts causing you trouble, I'll try my best to come help."
    vio "My apartment is right around here, so it's no big deal at all."
    vio "I fucking hate scumbags like this, so I'll {i}gladly{/i} kick their ass for you."
    show c1 outside 3-13
    with dissolve
    pov "Sure... and thank you! I really don't know how I let myself get into this situation..."
    pov "I'll be more careful from now on..."
    vio "No worries. It can happen to anyone."
    stop music fadeout 2.0
    vio "OK, so here's my number..."
    "......"

    play music "audio/city.mp3" fadein 2.0 loop
    show c1 home 2-1
    with fadeholdlong
    pov "{i}*sighs*{/i}"
    pov "Today definitely could have been better."
    if model_motive >=1:
        pov "I did enjoy modelling a lot, so it wasn't completely terrible, I guess."
        pov "I'm really looking forward to my next shift, too."
    else:
        pov "I was already pretty tired after modelling all afternoon, and then {i}that{/i} happened..."
    pov "I did get [vio]'s number, so that eases my mind a bit."
    pov "If anything ever happens again I'll try calling or texting her first."
    pov "I really don't want to get the police involved if I can help it."
    show c1 home 2-2
    with dissolve
    pov "There really are some strong girls out there, though, huh..."
    pov "It looked like she had some sort of martial arts training."
    pov "If only I had that kind of power..."
    pov "......"
    show c1 home 2-3
    with dissolve
    pov "Anyway, putting that little incident aside..."
    pov "I've been having a lot more fun lately."
    pov "Being active and working, rather than just sitting at home all the time, really does make me feel happier, after all."
    pov "And I've been feeling more confident in myself, too."
    show c1 home 2-4
    with dissolve
    if model_seduction >=2:
        pov "Jason— that was my boss' name, right? It's pretty obvious he's attracted to me."
        pov "I mean, is there ever a moment he's {i}not{/i} flattering me?"
    else:
        pov "Jason— that was my boss' name, right? He sure compliments me a lot at work."
    if boys_horny >=2:
        pov "Plus, Connor and Josh are constantly eyeing me up now."
        pov "Not too surprising with all my teasing lately..."
    else:
        pov "And Connor and Josh are looking at me more as a woman lately, it feels like."
    pov "I'm not entirely sure... but I have a hunch they might be interested in me as more than just friends."
    pov "Maybe I'll test that theory out at some point?"
    pov "Hmm..."
    show c1 home 2-5
    with dissolve
    pov "I have to say... having guys look at me so much recently has gotten me feeling a bit excited."
    pov "It might be time to try something a bit different."
    pov "For example, rather than just underwear, I could let them see me topless."
    pov "Or maybe even a little bit of touching wouldn't be so bad."
    pov "I've never had my boobs touched by anyone before, after all."
    pov "I wonder how it would feel?"
    show c1 home 2-3
    with dissolve
    pov "......."
    pov "...... well, it's just an idea."
    pov "Just an idea..."
    stop music fadeout 2.0
    "......."
    hide c1 room 2-3
    show black
    with fadehold
    pov "Ahhh!!"
    pov "Yes—!!!"
    pov "{i}(And so, my nightly routine began once again.){/i}"
    pov "{i}(But some part of me felt like it had changed.){/i}"
    pov "{i}(Like a switch had just been flipped on.){/i}"
    "......"
    $ perv +=1

    hide black
    show intro bg 1
    with wiperight
    m "{size=-3}Congratulations! [pov] has reached: {b}Perversion, Level 2{/b}.{/size}"
    m "{size=-3}She is now capable of:{/size}"
    m "{size=-3}— Moderate exhibitionism (topless nudity){p}— Touching{/size}"
    "......"
    "{b}Chapter 1: Complete{/b}"

    ####################### END OF CHAPTER 1####################################

    ####################### CHAPTER 2 ##########################################

label chapter2:
    $ chaptercount +=1
    play music "<from 10.8>audio/sparkle.mp3" fadein 2.0 loop
    show c2 title
    with fadeholdlong
    "......"
    pov "It's been a couple weeks or so since that incident."
    pov "Now that it's June, spring is finally over, and summer is here."
    pov "My favourite time of the year!"
    show c2 outside 1-1
    with dissolve
    pov "I love the sunny weather, and nothing beats summer fashion or being able to relax on the beach."
    pov "Girls always look their cutest during the summer."
    pov "Most people are also off school, or starting to take vacations from work."
    pov "It's a pretty happy time of year all around."
    pov "Speaking of which..."
    show c2 jpflashback 1
    with pixellate
    pov "My friend from when I was on exchange in Japan, is on summer break now."
    pov "Since we used to talk about Canada a lot, [fr] always mentioned how she wanted to come here."
    pov "And then last fall, I found out she decided to study at a university here in Vancouver."
    pov "She was always really good at English, so it didn't surprise me too much when I found out."
    show c2 jpflashback 2
    with dissolve
    pov "We've met a few times since, but haven't had too many opportunities lately."
    pov "She's been busy constantly with all her classes and extracurriculars."
    pov "[fr] was never one to slack on schoolwork, after all."
    pov "I was always kinda jealous of her grades whenever I saw them..."
    show c2 jpflashback 3
    with dissolve
    pov "Due to being in a foreign country, it was hard for me to get used to the language at first."
    pov "I can speak Japanese now, but at the time I was still pretty bad."
    pov "[fr] helped me out a lot with learning."
    pov "And it was thanks to her that I got used to the culture."
    pov "I was only 13 or 14 back then, so it was kind of difficult living abroad."
    pov "I mean, it takes time for {i}anyone{/i} to adapt to a new country, but especially for a kid it can be a bit scary."
    pov "So whenever I was feeling down, [fr] would take me somewhere in Shibuya to have fun."
    pov "Karaoke, shopping, purikura— you name it."
    pov "Good times!"
    pov "Anyway, back to the present..."
    show c2 outside 1-2
    with pixellate
    pov "Now that she's free, today we decided to have lunch together and catch up."
    pov "I'm pretty excited, since she's probably my closest female friend."
    pov "I mean, she's much more... how should I put it... 'straight-laced', or serious than I am, but..."
    pov "Maybe because of our differences, we managed to get along really well."
    pov "I could always talk to her about my problems, and she never judged me for my hobbies."
    show c2 outside 1-3
    with dissolve
    pov "And of course, when she was struggling with something, or needed help with English, I would be there for her, too!"
    pov "I was actually the one who helped her move in to her dorm a few months back."
    pov "That reminds me... those rooms sure are tiny, huh..."
    pov "And with a roommate, you don't even have the privacy to do anything..."
    pov "Makes me thankful for my parents and the house we have..."
    show c2 outside 1-4
    with dissolve
    pov "...... Hmm."
    pov "Well, anyway, I should be at the station any second now."
    pov "Knowing her, she probably arrived early like usual."
    pov "Guess I should hurry up, too!"
    "......"

    show c2 library 1
    with fadeholdlong
    fr "Hey! Long time no see."
    fr "Hope it wasn't too much of a bother coming all the way to the campus."
    pov "Yo! No problem!"
    pov "It's been a couple months now, hey?"
    show c2 library 2
    with dissolve
    fr "Sorry about that..."
    fr "You know how it is, midterms and finals and everything..."
    fr "But now I finally have some time to myself again."
    fr "I'm taking a couple summer electives so I can graduate early. But that's about all that's left."
    fr "Student loans are still taking care of everything, so I thought it'd be best to focus on gaining credits rather than working part-time."
    show c2 library 3
    with dissolve
    pov "Wow... you sure don't know when to stop, do you? {i}*laughs*{/i}"
    pov "Back in middle school, you were always super serious about your schoolwork, too."
    pov "Nothin' compared to the workload you have now, though."
    pov "But yeah, no worries! I've been pretty busy myself lately, too."
    pov "I actually started working part-time!"
    show c2 library 4
    with dissolve
    fr "Wait, really?! Congratulations!"
    fr "What did you decide to do for work?"
    pov "Hmmm... can you guess? {i}*giggles*{/i}"
    fr "...... Well, I can't really picture you working in fast-food or retail..."
    fr "Maybe something to do with fashion?"
    show c2 library 5
    with dissolve
    pov "Bingo!"
    pov "I actually started doing some modelling."
    pov "Well, it's only one or two days a week, but still."
    if model_motive >=1:
        pov "It's been pretty fun so far!"
        pov "And it's awesome being able to try out new clothes all the time."
    else:
        pov "It can be tiring sometimes, but it's nice to be active!"
    show c2 library 4
    with dissolve
    fr "Wow! I guess I'm not surprised. You always loved fashion, after all."
    fr "I remember you'd sneak magazines in to class all the time."
    fr "And then the teacher would catch you and yell at you... {i}*laughs*{/i}"
    show c2 library 6
    with dissolve
    pov "Haha!! Those were the days. Mr. Suzuki definitely didn't like me much after that..."
    pov "But yeah, it's been going pretty well!"
    pov "I'm still not sure what I want to do as a career or anything..."
    pov "I mean, I've considered going to university like you, but I'm not decided yet."
    pov "It's a big commitment, after all."
    show c2 library 4
    with dissolve
    fr "Hey, no pressure! We're still young."
    fr "Just keep it up for now and you'll figure out soon enough."
    fr "Anyone who thinks you need to have everything in your life figured out is silly, anyway."
    fr "We all do things at our own pace. No need to rush anything and make mistakes."
    pov "I guess you're right about that!"
    pov "Most people who pressure others are just boomers stuck in the 80s, anyway."
    pov "But yeah, thanks for supporting me."
    show c2 library 7
    with dissolve
    fr "No problem. Any time."
    fr "By the way, how's your Japanese doing these days?"
    fr "You haven't forgotten how to speak it, right...?"
    pov "Hey, rude!! I can still understand it just fine!"
    pov "I mean, I haven't been speaking it daily or anything..."
    pov "But you don't forget your second language that easily!"
    pov "And I still play Japanese games and stuff like that pretty often."
    fr "{i}*laughs*{/i} Well, I'm glad to hear that."
    fr "I'm just teasing you. You did have a knack for learning languages, after all."
    fr "You went from zero to almost being fluent in just a year or so."
    fr "Anyway... so, lately..."
    "......"
    show c2 library 8
    with fadehold
    "2 hours later."
    pov "Well, I guess we should wrap it up for now."
    pov "Since you're on summer break, we can meet up again soon, after all."
    fr "Yup! Maybe some time next week we can go see a movie, or do some shopping together?"
    fr "Or if there's something else you're interested in, we could do that instead."
    pov "Sounds like a plan!"
    show c2 library 9
    with dissolve
    fr "Alright, I'll message you about it later on then!"
    fr "I still have an essay I need to finish up this evening, so I'm sorry we couldn't chat for too long or go anywhere together."
    fr "It was really nice seeing you again, [pov]."
    fr "And I'm happy to hear you've been doing so well lately."
    stop music fadeout 2.0
    pov "Same here!"
    pov "See you again soon!"
    "......"

    play music "audio/low.mp3" fadein 2.0 loop
    show c2 outside 2-1
    with fadeholdlong
    pov "......."
    pov "Well, that's that..."
    pov "It was nice talking to [fr] for the first time in so long."
    pov "And we both got to vent a little bit, too, so that takes a load of stress off my shoulders."
    pov "It's always important to have friends you can talk to about serious stuff."
    show c2 outside 2-2
    with dissolve
    pov "Of course, I can talk to those two as well, but..."
    pov "There's just some things you can only talk about with a fellow girl, after all."
    pov "And now that we've caught up, me and [fr] can just chill and do something together next time."
    pov "It'll be fun to just let loose with her again after all these years."
    pov "Speaking of which..."
    show c2 outside 2-3
    with dissolve
    pov "That boy over there is looking pretty lonely."
    pov "Something must have happened to him."
    pov "Maybe he got rejected by someone he likes? Or his crush found a boyfriend or something?"
    pov "I'm kinda curious..."
    pov "It's hard to know what happened just by looking at him."
    show c2 outside 2-4
    with dissolve
    pov "Though... hmm... I really haven't done much lately."
    pov "I guess I could try raising his spirits a bit."
    menu:
        pov "Should I talk to him?"
        "Yes. {i}[gr]\[BoySeduction\]":
            pov "After all that serious talk... I need a little bit of fun!"
            pov "It's not as though he looks dangerous or anything, either."
            pov "And if I take the initiative, guys are pretty easy to control, anyway..."
            pov "The only real outcome I can imagine is that I'd brighten his day."
            show c2 outside 2-5
            with dissolve
            pov "Hey, are you OK?"
            boy "H-Huh? U-Uh... yeah."
            pov "Alright, just checking!"
            pov "I just saw you passing by, and was worried that something happened."
            pov "I thought it'd be a shame if a cute boy like you was feeling down, y'know?"
            pov "{size=-7}{i}*chuckles*{/i}{/size}"
            boy "T-Thanks..."
            show c2 outside 2-6
            with dissolve
            pov "{i}(He's blushing...){/i}"
            pov "{i}(Should I take this a step further?){/i}"
            menu:
                "I want more. [gr]\[Sexe +1\] \[BoySeduction +2\]":
                    pov "{i}(All I've been doing is teasing people lately.){/i}"
                    pov "{i}(Flirting and being provocative is fun, but...){/i}"
                    pov "{i}(I want to try something new now.){/i}"
                    pov "{i}(What's the worst that could happen...?){i}"
                    show c2 outside 2-7
                    with dissolve
                    pov "{i}*grabs hand*{/i}"
                    pov "Hey, trust me!"
                    pov "A boy like you should have no trouble finding someone."
                    "{i}*rubs*{/i}"
                    pov "Just be direct and physical with them!"
                    pov "OK?"
                    boy "U-Uhh... yeah... t-thanks."
                    pov "Alright, good——"
                    with Pause(1.0)
                    show c2 outside 2-8
                    with dissolve
                    pov "——Ahhh..."
                    pov "{i}(...... wait, did I just moan out loud?!){/i}"
                    pov "{i}(You're kidding me...){/i}"
                    pov "{i}(Oh my god... time to stop!){/i}"
                    pov "{i}(Abandon ship!){/i}"
                    show c2 outside 2-9
                    with dissolve
                    pov "Umm... anyway, I need to get going now!"
                    pov "See ya!"
                    boy "......"
                    boy "S-sure..."
                    boy "???"
                    show c2 outside 2-10
                    with fadehold
                    pov "{i}(Yikes...){/i}"
                    pov "{i}(That was embarrassing.){/i}"
                    pov "{i}(I escaped as soon as I could.){/i}"
                    pov "{i}(What happened is definitely not what I had in mind.){/i}"
                    pov "{i}(I mean, I was planning to fool around a bit, but I didn't think my body would react like that.){/i}"
                    pov "{i}(And especially not that quickly.){/i}"
                    pov "{i}(Come to think of it...){/i}"
                    show c2 outside 2-11
                    with dissolve
                    pov "{i}(That was my first time having a boy touch me there, huh...){/i}"
                    pov "{i}(I wish it could have lasted a bit longer.){/i}"
                    pov "{i}(A few seconds is just too short...){/i}"
                    pov "{i}(......){/i}"
                    stop music fadeout 2.0
                    pov "{i}(Ummm... anyway...){/i}"
                    pov "{i}(I'm getting a bit hungry now...){/i}"
                    pov "{i}(Maybe I'll get some ice cream before I go home?){/i}"
                    $ sexe +=1
                    $ c2boy_sed +=2
                    jump c2ice
                "No, that's enough. [gr]\[BoySeduction +1\]":
                    pov "{i}(Nah... I'm already flirting with a random boy on the streets.){/i}"
                    pov "{i}(No need to get carried away.){/i}"
                    pov "{i}(The whole point was to lift his spirits, after all— not to make him think I'm some slut.){/i}"
                    pov "{i}(Plus, it might just encourage him to keep going.){/i}"
                    pov "{i}(And then it could end up like last time...){/i}"
                    show c2 outside 2-5
                    with dissolve
                    pov "Haha. Well, anyway, I have to get going now."
                    pov "Just know that there's people out there who care. And remember to focus on tomorrow, not on the past!"
                    pov "See ya!"
                    boy "Umm... thanks. Y-You too!"
                    show c2 outside 2-11
                    with dissolve
                    pov "{i}(Alright. What should I do now...){/i}"
                    pov "{i}(I'm a bit hungry, so I guess I'll get a bite to eat.){/i}"
                    pov "{i}(It's already past 6 PM, but I'm not that hungry since I had a big lunch earlier.){/i}"
                    stop music fadeout 2.0
                    pov "{i}(A snack sounds about right.){/i}"
                    pov "{i}(It's still hot out, so maybe some ice cream?){/i}"
                    $ c2boy_sed +=1
                    jump c2ice
        "No. [gr]\[Innocent +1\]":
            pov "Nah... I feel bad for him, but..."
            pov "I just don't think I should push my luck with strangers."
            stop music fadeout 2.0
            pov "Especially not after what happened last time..."
            pov "Anyway, I'm pretty hungry now, so I guess I'll get a bite to eat."
            pov "Maybe some ice cream?"
            $ inn +=1
            jump c2ice

label c2ice:
    play music "audio/city.mp3" fadein 2.0 loop
    show c2 ice 1
    with fadehold
    pov "It's my first time coming to this store..."
    pov "It seems pretty cute."
    pov "Says they recently opened, so I guess not too many people know about it yet."
    pov "And there's a window outside offering take-out, so most people probably do that instead of sitting inside."
    pov "I'm the only customer in here right now, it seems."
    pov "I wonder what I should get..."
    pov "Hmm..."
    show c2 ice 2
    with dissolve
    pov "Hey, could I please get a double of blueberry and bubblegum?"
    pov "And a small iced tea with that, too."
    wom "Sure. That'll be $3.50."
    wom "Cash or debit?"
    pov "Debit. One second..."
    "......"
    show c2 ice 3
    with fadehold
    pov "Ahh... I'm already stuffed."
    pov "It's my first time coming here, but the ice cream was pretty tasty."
    pov "Not that it's healthy to have lots of sweets and junk food, but..."
    pov "It's been a week or two since I've treated myself to anything."
    show c2 ice 4
    with dissolve
    pov "Since I'm doing modelling now, I've been forcing myself to have only one meal a day, which is usually dinner."
    pov "Gaining weight is basically a death sentence for a model, after all."
    pov "Though it's not like I've ever been able to put on much weight..."
    pov "Ever since high school, I've always been around 105 lbs {size=-12}(48kg){/size} or so."
    pov "But I'm only about 5'3 {size=-12}(160cm){/size}, so my doctor said it was healthy."
    pov "My mom's pretty thin, too, now that I think of it."
    pov "I guess that's our Asian genetics? {i}*chuckles*{/i}"
    show c2 ice 5
    with dissolve
    pov "Anyway......"
    pov "I've been noticing it for a while now, but I've been feeling a bit strange..."
    if c2boy_sed >=1:
        pov "Ever since I started flirting with that boy, I've been feeling sort of flushed."
    else:
        pov "Probably when I saw that boy outside, is when I started noticing."
        pov "Wait... surely not..."
    pov "I think I might have gotten horny...?"
    pov "And it'll take over an hour to get home from here..."
    pov "No way..."
    pov "......"
    show c2 toilet 1
    with fadehold
    pov "Ahhh!"
    pov "Oh my god!"
    if c2boy_sed <=0:
        pov "{i}(I must have a lot of sexual tension built up.){/i}"
        pov "{i}(I've been holding back a lot lately, after all.){/i}"
        pov "{i}(But my body needs release from time to time...){/i}"
        pov "{i}(I just can't seem to stop my perverted thoughts, after all...){/i}"
        stop music fadeout 2.0
        show c2 toilet 2
        with dissolve
        pov "Ohh--!"
        pov "I'm cumming!"
        "......"
        jump c2hottub
    if c2boy_sed <=1:
        pov "{i}(Flirting with that boy must have been what got me so excited.){/i}"
        pov "{i}(The thrill of hitting on a stranger like that...){/i}"
        pov "{i}(It's not often I've done that.){/i}"
        pov "{i}(I want more...{/i})"
    if c2boy_sed >=2:
        pov "{i}(I can't get that boy out of my head...){/i}"
        pov "{i}(That feeling when he touched my boob...){/i}"
        pov "{i}(It was my first time being touched there, but my body reacted immediately.){/i}"
        pov "{i}(I want to have my boobs touched again...){/i}"
    stop music fadeout 2.0
    show c2 toilet 2
    with dissolve
    pov "Ohh--!"
    pov "I'm cumming!"
    "......"

label c2hottub:
    play music "<from 1.7>audio/absurd.mp3" fadein 0.5 loop
    show c2 pool 1
    with fadeholdlong
    "A few days later."
    pov "Ahh..."
    pov "Soaking in the pool might just be my favorite thing about summer..."
    pov "Or at least one of them, anyway."
    pov "It really helps to take your mind off things."
    pov "And it feels so nice..."
    show c2 pool 2
    with dissolve
    pov "Y'know, maybe me and [fr] can chill here the next time we hang out."
    pov "Or maybe I can even invite {i}those{/i} two?"
    pov "Hmm..."
    pov "Of course, I like going to the beach with friends, too, but..."
    pov "Nothing beats the privacy of being in your own backyard."
    show c2 pool 3
    with dissolve
    pov "Privacy, huh..."
    pov "......"
    pov "A peeper?!"
    pov "More importantly, did he seriously think I wouldn't notice him there?!"
    pov "He's not even making an effort to hide himself..."
    show c2 pool 4
    with dissolve
    pov "{i}*sigh*{/i} Perverts never change, huh..."
    pov "They always think with their {i}thing{/i} rather than their brain."
    pov "I mean, he looks like his pants are about to explode."
    pov "Poor guy..."
    pov "Maybe his wife isn't satisfying him enough?"
    show c2 pool 5
    with dissolve
    pov "Whatever the case..."
    pov "He's not filming or anything, so it's not like him looking is harming me."
    pov "I'm just in my swimsuit, anyway."
    pov "No different from anything guys would see at the beach."
    pov "Hmm..."
    pov "I've already gotten used to guys seeing me like this."
    menu:
        pov "Should I give him something more to look at?"
        "Take my top off. [gr]\[Sexe +1\] \[PoolExhibition +1\] \[Exhibition +1\]":
            show c2 pool 6
            with dissolve
            pov "To be honest, this isn't enough for me anymore..."
            pov "It's fun watching guys' reactions, but it's just too tame for me to get excited from it."
            pov "Guys have seen me in my swimsuit, and even my underwear quite a few times already."
            pov "And I've always fantasized about guys seeing me naked and stuff..."
            pov "I just never really had an opportunity to try anything."
            show c2 pool 7
            with dissolve
            pov "But now, there's actually a chance to have some fun."
            pov "I'm at home, too, so I have the freedom to do things I wouldn't be able to in public."
            pov "Plus, it'd be a nice little surprise for him."
            pov "Both of us get to enjoy something, so it's a win-win."
            pov "Hehe..."
            show c2 pool 8
            with fadehold
            pov "Hmm..."
            pov "There we go."
            pov "I wonder how he'll react?"
            pov "I'm sure he wasn't expecting to see something like this."
            pov "{i}*giggles*{/i}"
            show c2 pool 9
            with dissolve
            pov "Wow..."
            pov "Seems he liked that."
            pov "I guess I shouldn't be too surprised, seeing as he's a pervert..."
            pov "Maybe I should give him a better look."
            show c2 pool 10
            with dissolve
            pov "Hehe..."
            pov "This should do it."
            pov "...... Hmm."
            pov "You know, I've thought about it lately, but..."
            pov "I wonder how big my boobs are compared to most girls?"
            pov "I'm a C cup, so I feel like they're at least average, but..."
            pov "It's not as though I ever really paid much attention to other girls."
            show c2 pool 11
            with dissolve
            pov "Well, whatever the case..."
            pov "He must be enjoying himself."
            pov "It's hard to see from here, but it kinda looked like he had a bit of a tent in his pants..."
            pov "I mean, if I was a guy, I'd probably get a boner, too..."
            show c2 pool 12
            with dissolve
            pov "I do have a nice body, after all. {i}*giggles*{/i}"
            pov "That's one area I definitely have confidence in."
            pov "This reminds me..."
            pov "I've never actually had anyone see me topless before."
            pov "This is my first time having my boobs seen, huh..."
            pov "It's kind of exciting..."
            pov "I can't really tell since I'm in the pool, but I wonder if I would have gotten wet?"
            pov "I am feeling pretty horny, after all..."
            show c2 pool 13
            with dissolve
            pov "Alright..."
            pov "It's probably time to wrap it up here and finish up in my bedroom."
            pov "...... I feel like I'll go crazy if I don't touch myself soon."
            pov "I've never been good at controlling myself in that regard."
            stop music fadeout 2.5
            pov "And this guy might let it get to his head and try something funny if I tease him for too long."
            pov "Sorry, random peeper dude..."
            pov "......"
            $ sexe +=1
            $ c2poolex +=1
            $ exh +=1
        "It's too risky. [gr]\[Innocent +1\]":
            show c2 pool 6 -
            with dissolve
            pov "Nah..."
            pov "If he's peeping on random girls, he's probably not a very nice person."
            pov "And, I mean, if I took it further, he might take it as a sign that I'm inviting him..."
            pov "...... who knows what he would do if that happened?"
            pov "Way too risky..."
            pov "I'll think about it and maybe try teasing him next time if it happens again, but..."
            stop music fadeout 2.0
            pov "For now, I'll just relax and ignore him."
            pov "......"
            $ inn +=1
    $ renpy.end_replay()
    play music "audio/friends.ogg" fadein 3.0 loop
    show c2 boys 1
    with fadeholdlong
    pov "Wait... seriously?"
    pov "Your brother is moving to the UK this fall?"
    j "Yeah. He's studying abroad for a couple semesters, I guess."
    j "He decided on his own and is paying with his own savings, it seems."
    pov "Wow. Well, congratulations to him then!"
    pov "What about you? Are you planning to go to uni or anything?"
    show c2 boys 2
    with dissolve
    j "Hmm..."
    j "Well, I'm not really sure yet, but..."
    j "For now, I'm just going to keep helping my dad with his business."
    j "He pays me decently enough, and maybe one day I can take over the business for him."
    j "Or if not, I can just use the money to pay for tuition."
    j "Kind of like what my brother did."
    pov "Good to hear! Nothing wrong with saving up a bit first."
    c "Yeah... not everyone is rich like you and your folks, [pov]."
    show c2 boys 3
    with dissolve
    pov "Hey! That's uncalled for! {size=-8}{i}*laughs*{/i}{/size}"
    pov "So, Connor, I guess you're finished your final exams now, hey?"
    pov "My friend, [fr], goes to the same uni as you, I think."
    pov "I wonder if you shared some of the same classes."
    pov "Speaking of which... you sure you aren't lonely at uni without your {i}pal{/i}?"
    show c2 boys 4
    with dissolve
    c "Nah. I already have enough fun wrecking Josh in Smash."
    j "Dude, maybe if you actually studied instead of no-lifing the game constantly..."
    j "How many times did you skip class because you were up until 4 or 5 AM?"
    j "Probably jerking it to anime girls or something, too."
    c "Pfft... first year in uni is so damn easy that it wouldn't have made a difference either way."
    c "And you aren't one to talk, dude..."
    c "You should really consider it, though. Both of you. Coming to university, that is."
    show c2 boys 5
    with dissolve
    pov "Hmmm..."
    pov "I've thought about it, but..."
    pov "Nothing I want to do right now really requires a university degree."
    pov "Plus, I'm only turning 19 next month, so there's no real rush or anything."
    pov "If I do go, maybe I'll try for the winter semester, or, more likely, next September."
    pov "Long ways away, either way..."
    show c2 boys 6
    with dissolve
    c "True. Nothing wrong with just chilling for another year or so."
    c "Working part-time gives you something to do, anyway."
    c "You said you were doing modelling now, right?"
    j "Oh yeah. How's that been going?"
    j "I always imagined you'd be into something like that."
    show c2 boys 7
    with dissolve
    if model_motive >=1:
        pov "It's been great so far!"
        pov "I get to wear cute and sexy clothes all the time, {i}and{/i} I get paid for it."
        pov "Honestly, I couldn't have asked for a better job. {i}*giggles*{/i}"
    else:
        pov "It's been alright so far!"
        pov "I mean, it can get tiring sometimes, but it's not too bad."
        pov "I wasn't sure what to expect at first, but I've been enjoying it a lot more lately."
    pov "Imagine working at fast food or a call center or something instead... yikes."
    pov "I guess I have it pretty easy in comparison."
    show c2 boys 6
    with dissolve
    c "Haha, haven't you always had it easy?"
    c "Your parents always took care of everything for you."
    c "Unlike us two who have to pay for everything on our own..."
    c "But yeah, good to hear that it's all working out for you."
    j "Yeah. If you're happy with it, all's good."
    show c2 boys 8
    with dissolve
    pov "Thanks!"
    pov "I mean, I might do something else this year, too, but it's a start."
    pov "Anyway, so, what have you guys been up to lately?"
    pov "This morning, I..."
    "......"
    show c2 boys 9
    with fadehold
    "1 hour later."
    pov "Alright... I'm pretty full now."
    pov "A girl can only have so much pasta, after all..."
    pov "You guys might want to get desert or something, but I'm good."
    pov "I guess it's about time to head back?"
    bo "Sure."
    show c2 boys 10
    with dissolve
    pov "What are you guys planning to do tonight?"
    c "Me and Josh are gonna play games at my place for a bit."
    j "Yeah. I've got work in the morning, so I'll probably just stay at his for the night."
    pov "Try not to do anything funny, you two..."
    c "Gross."
    ev "{i}*laughs*{/i}"
    show c2 boys 11
    with dissolve
    pov "Well, time to—"
    show c2 boys 12
    with pixellate
    pov "...... head out now."
    pov "{i}(?!){/i}"
    pov "{i}(Uh-oh...){/i}"
    pov "{i}(I'm guessing that wasn't on purpose.){/i}"
    show c2 boys 11
    with dissolve
    pov "{i}(You two sure can be clumsy sometimes, huh...){/i}"
    pov "{i}(It's a good thing that it's me, since any other girl would probably misunderstand and be creeped out...){/i}"
    pov "{i}(...... it's not like they actually have the guts to feel up a girl, though.){/i}"
    pov "{i}(......){/i}"
    show c2 boys 13
    with dissolve
    if boys_horny >=2:
        pov "{i}(But, I guess after all I've done around them lately...){/i}"
        pov "{i}(Maybe it wouldn't be too surprising if they tried something.){/i}"
        pov "{i}(And I guess I wouldn't really be upset if they did...){/i}"
        pov "{i}(I wonder how it would feel, if one of them squeezed my butt on purpose?){/i}"
        if c2boy_sed >=2:
            pov "{i}(Or maybe my boobs, like what happened with that boy from before.){/i}"
        pov "{i}(......){/i}"
        pov "{i}(Well, anyway...){/i}"
        stop music fadeout 2.0
        pov "{i}(I should keep my thoughts locked up... at least until I get home.){/i}"
        "......"
    else:
        pov "{i}(If they wanted to experiment with a girl and touch me, though...){/i}"
        pov "{i}(I guess I wouldn't be too opposed to it.){/i}"
        pov "{i}(Of course, I'd get mad if they went too far, but...){/i}"
        pov "{i}(If it was just a little bit of touching, I wonder how it would feel?){/i}"
        stop music fadeout 2.0
        pov "{i}(Well, I doubt it will ever happen, but...){/i}"
        pov "{i}(I'll think about it if the time ever comes.){/i}"
        "......"

    play music "<from 3.5>audio/isolation.mp3" fadein 0.5 loop
    show c2 outside 3-1
    with fadeholdlong
    pov "That had to be some of the best pasta in the universe..."
    pov "Connor and Josh aren't big fans of cooking, so we usually go downtown whenever we're hungry."
    pov "We've gone maybe twenty times now? {i}Fifty{/i}? I've lost track..."
    pov "Connor's place is nearby since he lives on campus."
    pov "Meanwhile, my home is all the way on the other side of Vancouver..."
    pov "So it's only natural that we'd go our separate ways for now."
    show c2 outside 3-2
    with dissolve
    pov "......?"
    pov "That person walking below me seems kind of familiar."
    pov "Wait... is that the girl from before?"
    pov "[vio], I think her name was?"
    pov "I should thank her again for her help last time."
    show c2 outside 3-3
    with fadehold
    pov "Hi! Umm... sorry if I'm disturbing you."
    pov "I'm [pov]. We met a few weeks back."
    pov "I'm not sure if you remember, but you saved me from a weirdo back then."
    pov "I was pretty flustered at the time, so I couldn't really express myself too well, but..."
    pov "Just saw you walking by, and wanted to say thanks once more!"
    show c2 outside 3-4
    with dissolve
    vio "Oh, hey there. No problem!"
    vio "Of course I remember you."
    vio "It's hard to forget that idiot's face when he was running away."
    vio "Hmm... funny running into each other again, though."
    vio "I guess this city is a lot smaller than it seems, huh."
    vio "Actually..."
    vio "This might be a good opportunity."
    show c2 outside 3-5
    with dissolve
    pov "Hmm?"
    vio "Well, one of the girls at the cafe I work at quit recently."
    vio "There's a shortage in staff because of that, and we've been having troubles finding someone."
    vio "So, I guess why not try asking you?"
    vio "If you're ever interested in a part-time job, feel free to let me know."
    show c2 outside 3-6
    with dissolve
    pov "Oh... thanks for telling me!"
    pov "Hmm..."
    pov "Actually, I might have enough time for another part-time job."
    pov "I'd have to think about it some more, but..."
    pov "I'll definitely consider the offer."
    show c2 outside 3-7
    with dissolve
    vio "Cool, cool. Well, no pressure."
    vio "Whenever you're interested, you can just drop me a text and I'll fill you in on the details."
    vio "My numbe— oh, that's right. I already gave you my number."
    ev "{i}*laughs*{/i}"
    show c2 outside 3-8
    with dissolve
    vio "Well, anyway, I should probably get going. I'm supposed to be meeting someone soon."
    vio "I'd stay and tell you more about the job, but I'm already late as is."
    vio "Just send me a message whenever you feel like."
    pov "Sure, no problem! Glad we could see each other again."
    vio "Yup. See ya later!"
    vio "And remember to be careful!!"
    "......"
    show c2 outside 3-9
    with fadehold
    pov "Looks like those two made it back already."
    pov "And [fr] is free next weekend, she says."
    pov "...... Oh?"
    pov "There's a movie she's interested in."
    pov "Guess we can go see that, and maybe catch a bite to eat and shop afterwards?"
    show c2 outside 3-10
    with dissolve
    voi "You're ready, right?"
    voi "I guess..."
    voi "How about the usual spot, then?"
    voi "Alright..."
    voi "But I'm stopping if I don't feel like it. OK?"
    voi "Yeah, yeah. C'mon."
    show c2 outside 3-11
    with dissolve
    pov "...... Hmm?"
    pov "It might just be my imagination, but I thought I saw [vio] again a second ago."
    pov "I guess whoever she was meeting showed up already?"
    pov "She {i}was{/i} in a rush, after all. And she did say she was late."
    pov "Well, whoever it was, it looked like a guy..."
    pov "Maybe it was her boyfriend?"
    pov "I'm kind of curious now..."
    menu galleryScene2:
        pov "Should I check what they're doing?"
        "I need to know. [gr]\[Peak\]":
            show c2 outside 3-12
            with dissolve
            pov "... Surely it can't hurt to take a quick peek for a second, right?"
            pov "She sounded kind of nervous, for some reason."
            pov "What if she was pressured into something?"
            stop music fadeout 2.0
            pov "Well... guess I could try following them to make sure she's not getting in any trouble."
            "......"
            show c2 outside 3-13
            with fadehold
            play music "audio/blues.ogg" fadein 2.0 loop
            pov "Hmm..."
            pov "I don't hear them anymore."
            pov "Maybe they went in this alleyway over here?"
            pov "I can't think of anywhere else they could disappear to."
            pov "... Though I'm not sure why they would go here."
            pov "...... Seems kind of suspicious."
            show c2 outside 3-14
            with pixellate
            vio "Really? Right here?"
            vio "I sure hope nobody will see us this time..."
            vio "I don't want to deal with another homeless guy walking past here."
            man "Haha. If it ain't a cop or something, who cares, really."
            man "A little gallery just makes it more exciting."
            man "Anyway, help get me ready."
            show c2 outside 3-15
            with dissolve
            vio "Mmmm..."
            man "Oh fuck... yes."
            man "Just like that."
            pov "{i}(?!){/i}"
            pov "{i}(No way...){/i}"
            pov "{i}(She's giving a blowjob in public?!){/i}"
            pov "{i}(What if she gets caught?!){/i}"
            pov "{i}(Heck, she already has been if you count me finding her...){/i}"
            pov "{i}(This can't be normal...){/i}"
            pov "{i}(Maybe this is her kink or something?){/i}"
            pov "{i}(Still...){/i}"
            man "Holy shit..."
            show c2 outside 3-16
            with dissolve
            man "Hey, [vio], I can't hold back anymore."
            vio "Ah... you want to do it, right?"
            vio "Alright. Mmm... fine... I'll turn around for you."
            vio "But— ahh— try to keep it quiet!"
            man "I'm not the one who needs to keep quiet here..."
            show c2 outside 3-17
            with dissolve
            vio "Ahh——?!"
            man "{i}You{/i} are!"
            vio "Aaaahh!"
            man "You little slut."
            man "You wanted this, didn't you?"
            vio "Ahhh... y-yes... yes, I want it!"
            vio "Ohh—!"
            show c2 outside 3-18
            with dissolve
            pov "{i}(......){/i}"
            pov "{i}(I can't believe what I'm seeing.){/i}"
            pov "{i}(I mean, I've seen lots of porn and all, so it's not as though I don't know what a dick looks like.){/i}"
            pov "{i}(But...){/i}"
            pov "{i}(This is the first time I've seen one in real life.)"
            pov "{i}(Or people having sex, for that matter.){/i}"
            pov "{i}(Like... it would be one thing if I just accidentally opened someone's bedroom door or something, but...){/i}"
            show c2 outside 3-19
            with dissolve
            pov "{i}(In public like this?!){/i}"
            pov "{i}(It's like we're in a porn movie, or an erotic game or something...){/i}"
            pov "{i}(...... I mean, yeah, it's hot and all when I see people in porn doing it outside, but...){/i}"
            pov "{i}(To {i}actually{/i} be doing it...){/i}"
            pov "{i}(I can't imagine me ever doing something like this...){/i}"
            show c2 outside 3-20
            with dissolve
            vio "I'm about to cum!"
            vio "Nick... please... cum inside me."
            ni "Damn rights I will!"
            pov "{i}(......){/i}"
            pov "{i}(They know each other's name, so...){/i}"
            pov "{i}(I guess that's her boyfriend, then?){/i}"
            show c2 outside 3-19
            with dissolve
            pov "{i}(Anyway...!!){/i}"
            pov "{i}(I shouldn't stay here any longer!){/i}"
            pov "{i}(If she catches me, I'll be in big, big trouble.){/i}"
            pov "{i}(And if a stranger walking by sees me peeping, that'll end up being twice as awkward.){/i}"
            pov "{i}(Best to just let couples do their own weird thing...){/i}"
            pov "{i}(......){/i}"
            show c2 outside 3-21
            with fadehold
            pov "{i}(Wow...){/i}"
            pov "{i}(Time to take a deep breath and calm down.){/i}"
            pov "{i}(I'll just try to pretend I never saw that.){/i}"
            pov "{i}(And I should probably be thankful that she didn't see me...){/i}"
            pov "{i}(Hmm... I wonder, though...){/i}"
            pov "{i}(One day will I get to do things like that, with a boyfriend of my own?){/i}"
            pov "{i}(I still have no idea what sex would feel like.){/i}"
            pov "{i}(Obviously, it's probably a lot different than my fingers.){/i}"
            pov "{i}(Either way, whenever I {i}do{/i} get a boyfriend, we definitely wouldn't be doing it in public like that...){/i}"
            stop music fadeout 2.0
            pov "{i}(Probably... no, surely not...){/i}"
            pov "{i}(......){/i}"
            $ c2see +=1
        "Nah... that's her own business.":
            show c2 outside 3-12
            with dissolve
            pov "I'm interested in what she's up to, but..."
            pov "It's best to respect people's privacy."
            pov "Plus, she saved my butt only a few weeks ago."
            pov "So, I don't think it'd be a good way to show thanks, doing things behind her back like this."
            pov "I wouldn't want someone following me around, either."
            pov "Plus, I could always just ask her directly what she was doing, the next time we meet."
            stop music fadeout 2.0
            pov "Nah... I'll leave them be."
            "......"
    $ renpy.end_replay()
    show c2 laundry 1
    with fadeholdlong
    play music "audio/city.mp3" fadein 2.0 loop
    "A couple days later."
    pov "Man, these guys really need to learn how to take of themselves..."
    pov "Sometimes it's almost like I'm their mother or something."
    pov "I mean, I'm not even some sort of clean freak."
    pov "And usually I don't say anything since it's their problem and all..."
    show c2 laundry 2
    with dissolve
    pov "But... their laundry has been laying there for, what, {i}weeks{/i} now?"
    pov "It gets hard not to notice when I'm there every other day..."
    pov "Plus, boys being boys, there's usually some sort of strange odor."
    pov "More so than usual, lately..."
    if boys_horny >=1:
        pov "I wonder if I had something to do with that?"
        pov "......"
        pov "Well, it wouldn't surprise me..."
        if boys_horny>=2:
            pov "I have given them a lot of material to think about, after all..."
    show c2 laundry 3
    with dissolve
    pov "...... Anyway, that's pretty much why I decided to clean it for them."
    pov "Connor lives on campus, so there's no washing machine except here in the commons area."
    pov "It's a bit annoying having to do their dirty work for them, but it's easier to just get it over with rather than bug them about it constantly."
    pov "They barely listen to me about stuff like this, anyway."
    pov "Well, on the bright side, at least it's not too busy here tonight."
    show c2 laundry 4
    with dissolve
    pov "Just me and this guy here right now."
    "......."
    menu galleryScene3:
        "Should I release some stress?"
        "I don't see why not. [gr]\[Sexe +1\] \[Exhibition +1\]":
            pov "You know what..."
            pov "Since Josh and Connor have been annoying today..."
            pov "Maybe I'll surprise someone who's {i}actually{/i} being a good boy."
            pov "And I deserve some sort of reward for doing those two a favour!"
            show c2 laundry 5
            with dissolve
            pov "Hmm..."
            pov "If I'm doing laundry... might as well put in something of my own."
            pov "Not {i}everything{/i}, of course... I need to go back to their room until the laundry is done, after all."
            pov "But I can live without underwear for an hour or so."
            pov "{i}*giggles*{/i}"
            show c2 laundry 6
            with fadeholdshort
            pov "There's my bra..."
            pov "I undressed as noisily as possible, so he must have noticed by now."
            pov "He probably wishes I was facing the opposite way right now, huh."
            pov "That way he'd get a good look at these fine boobs."
            pov "Well, he has something else to look forward to in a second."
            pov "Next..."
            pov "......"
            show c2 laundry 7
            with dissolve
            pov "That's all of it."
            pov "......"
            pov "Wow... I'm actually naked in front of someone else, huh."
            pov "Well, they can only see me from behind, but still..."
            pov "...... this is definitely getting into pervert territory."
            pov "Well, from my perspective, at least..."
            pov "Anyone else who saw me doing this would 100 percent consider me one."
            show c2 laundry 8
            with dissolve
            pov "That said..."
            pov "I do still have some limits, I guess."
            pov "I don't really feel comfortable going all the way and being seen {i}there{/i} by a stranger."
            pov "At least not right now..."
            pov "So I'll have to avoid turning around."
            pov "I might lose my courage if they see my face, too."
            pov "And they do live in the same dorm as Connor, so it might be bad if they recognize me later on..."
            show c2 laundry 9
            with dissolve
            pov "Hmm..."
            pov "I wonder what they're thinking right now?"
            pov "Must not have expected a perverted girl like this to be down here with them..."
            pov "That reminds me..."
            pov "I'm in a public area right now."
            pov "...... Uh-oh!"
            show c2 laundry 10
            with dissolve
            pov "Abort! Abort!"
            pov "I should put my clothes on before I get in trouble!"
            pov "I'll be without my underwear for an hour or so, but..."
            pov "Obviously, there's no way I'd be able to walk back to their room completely naked."
            stop music fadeout 2.0
            pov "Hopefully those two don't notice that I'm not wearing any underwear..."
            pov "......"
            $ exh +=1
            $ sexe +=1
        "Maybe some other time. [gr]\[Innocent +1\]":
            show c2 laundry 11
            with dissolve
            pov "Hmm..."
            pov "I don't know if I'm in the mood to do anything perverted right now."
            pov "Plus, I'm in a public area, and they're a complete stranger."
            pov "What if they recognized me?"
            pov "That could get Connor into some trouble, too..."
            pov "I'm almost 100 percent sure he's a student here."
            show c2 laundry 3
            with dissolve
            pov "It's definitely risky..."
            pov "I mean, there's always a time and a place for having fun, but..."
            pov "Now is not one of those times, I think..."
            pov "Well, anyway..."
            stop music fadeout 2.0
            pov "Guess I should hurry up here and come back down when it's time."
            pov "......"
            $ inn +=1
    $ renpy.end_replay()
    play music "audio/cloudy.mp3" fadein 0.5 loop
    show c2 home 1
    with fadeholdlong
    pov "{size=-5}{i}*yawns*{/i}{/size}"
    pov "Back home just before the last train."
    pov "I suppose I could have just stayed the night at their place..."
    pov "It's not like my parents are home, so they wouldn't get mad at me or have funny thoughts if I came back in the morning."
    pov "For the most part, I have the freedom to do whatever I want."
    show c2 home 2
    with dissolve
    pov "Maybe next time I'll stay at theirs instead of going home?"
    pov "Not that staying at a guy's place is something I would normally do, but..."
    pov "We're best friends, so I can trust them."
    pov "And they know I can be feisty when they annoy me."
    if boys_horny>=1:
        pov "Though, to be fair, I know they'll at least have some thoughts, due to how much I've been teasing them lately."
        pov "Who knows, maybe they even had a wet dream or two..."
    show c2 home 3
    with dissolve
    pov "Anyway..."
    pov "It's kind of surprising how much more open I've become in just a month or so."
    pov "I've more or less gotten used to modelling already, and people looking at me no longer makes me nervous like before."
    pov "Getting attention from guys has been kind of flattering, too."
    pov "Sometimes you just have to break out of your comfort zone."
    show c2 home 4
    with dissolve
label galleryScene4:
    if c2boy_sed >=2:
        pov "Well, some things lately have been a bit more than that..."
        show fb1
        with pixellate
        pov "Having that boy touch my boobs, for example..."
        if exh >=2:
            show fb2
            with pixellate
            pov "And having my naked body seen..."
            show fb3
            with pixellate
            pov "I've been pretty bold lately, I guess."
        hide fb1
        hide fb2
        hide fb3
        with dissolve
        pov "It's definitely a big change from before."
        pov "I don't want to become a slut or anything, but small events like this have been pretty fun."
    else:
        pov "There's still some lines I didn't feel ready to cross yet, but..."
        pov "I'm not against trying new things."
        pov "Maybe instead of just being seen... I could try touching, or being touched a little bit."
        pov "Kind of like Josh's little accident a few days ago..."
    $ renpy.end_replay()
    pov "......"
    show c2 home 5
    with dissolve
    pov "That aside..."
    pov "[vio] asked me about that job, didn't she?"
    pov "I suppose a second part-time job couldn't hurt."
    pov "Modelling only takes up one or two days a week, after all."
    pov "Plus, working at a cafe doesn't sound too bad compared to most other jobs out there."
    pov "I guess I'll text her in a day or two after I've decided."
    if c2see >=1:
        show c2 home 6
        with dissolve
        pov "It feels a bit weird talking to her after seeing all that, though..."
        show fb4
        with pixellate
        pov "She definitely didn't seem the type to be into things like that."
        hide fb4
        with dissolve
        pov "Well, we all have our secrets, I guess."
        pov "And I'm no exception..."
        if exh >1:
            pov "If she knew I was showing my body off to random guys, I guess she'd be pretty surprised, too."
            pov "She didn't seem to enjoy the risk of being seen, after all."
            pov "I, on the other hand, kinda enjoy that part..."
        else:
            pov "If she knew the kind of porn I was looking at, she'd be pretty surprised, too."
            pov "Thankfully I've been able to keep it a secret from everybody..."
        pov "......"
    show c2 home 7
    with dissolve
    pov "Well, time to head to sleep, I think."
    pov "It's almost midnight now."
    pov "Can't risk messing up my schedule now that I'm working!"
    pov "Girls need their beauty sleep... or whatever they say."
    pov "......"

    show white
    with dissolvelong
    "Due to recent events, [pov]'s mind races with thoughts and fantasies."
    "2 hours after she heads to bed, [pov] dreams that she..."
    menu galleryScene5:
        "... spends a loving night with her future boyfriend. [gr]\[C2End1\]":
            hide white
            show c2 dream 1
            with dissolveverylong
            pov "......?"
            pov "...... Huh?"
            pov "What was I doing here with this guy?"
            pov "And why are we naked?"
            pov "...... Ah, that's right. We're a couple."
            pov "We were going to make love tonight, weren't we?"
            pov "I want it in me..."
            pov "......"
            show c2 dream 2
            with dissolvelong
            pov "Ah..."
            pov "Baby, I love you."
            pov "It feels so good..."
            pov "I can't stop thinking about you."
            pov "Please, give it to me more."
            pov "Fill me up..."
            pov "If it's with you, I don't care if I get pregnant."
            "..."
            "......"
            "And so, [pov]'s romantic dream continued throughout the night."
            "Only for her to wake up and realize it was but a dream, much to her dismay..."
            $c2_end1+=1
            hide c2 dream 2
            with wiperight
            show intro bg 1
        "... experiments with another girl. [gr]\[C2End2\] \[Lesbian +1\]":
            hide white
            show c2 dream 3
            with dissolveverylong
            pov "......?"
            pov "...... Huh?"
            pov "What's going on?"
            pov "... Why am I being licked there?"
            pov "And why is a girl doing it?"
            pov "I don't even like girls that way..."
            pov "...... Ah, that's right."
            pov "We wanted to try it once, to make sure we weren't missing anything."
            pov "It feels kind of funny..."
            pov "I guess it's not too bad being licked there, even if it's a girl."
            pov "As long as it's only a one time thing..."
            pov "Ah..."
            "..."
            "......"
            "And so, [pov]'s strange dream continued throughout the night."
            "Much to her relief, she would eventually awake and realize it was but a dream..."
            $c2_end2+=1
            $les+=1
            hide c2 dream 3
            with wiperight
            show intro bg 1
        "... seduces two boys for fun. [gr]\[C2End3\]":
            hide white
            show c2 dream 4
            with dissolveverylong
            pov "......?"
            pov "...... Huh?"
            pov "Why am I surrounded by two guys?"
            pov "And why are we naked?"
            pov "Their things are right in front of me..."
            pov "I'm kind of turned on..."
            pov "...... Ah, that's right. We were going to have sex, weren't we?"
            pov "I have to make sure to get them ready before we start."
            "......"
            show c2 dream 5
            with dissolvelong
            pov "Ahh!"
            pov "It feels so good!"
            if boys_horny >=2:
                pov "That's you two, right? Connor and Josh?"
            else:
                pov "I can't remember who you two are, but it doesn't matter anymore!"
            pov "Two at the same time is amazing."
            pov "I've always wanted something like this."
            pov "Please, don't stop!"
            pov "I want you to fill me up."
            "..."
            "......"
            "And so, [pov]'s perverted dream continued throughout the night."
            "Only for her to wake up and realize it was but a dream, much to her dismay..."
            $c2_end3+=1
            hide c2 dream 5
            with wiperight
            show intro bg 1
    $ renpy.end_replay()
    stop music fadeout 2.0
    m "{size=-3}Congratulations! [pov] has reached: {b}Perversion, Level 3{/b}.{/size}"
    m "{size=-3}She is now capable of:{/size}"
    m "{size=-3}— Heavy exhibitionism (full nudity){p}— Light foreplay{/size}"
    "......"
    "{b}Chapter 2: Complete{/b}"
    $ perv +=1

    ####################### END OF CHAPTER 2 ###################################

    ####################### CHAPTER 3 ##########################################
    $ chaptercount +=1

    play music "audio/city.mp3" fadein 2.0 loop
    show c3 title
    with fadeholdlong
    "1 year earlier, in [pov]'s old home..."
    rdad "So, [pov], your graduation ceremony is coming up."
    rdad "Next Friday, wasn't it?"
    pov "Yeah. We just finished all our coursework a week or two ago."
    show c3 parents 1
    with dissolve
    rmom "I hope your hard work and studying has paid off."
    rmom "Since your father's company has been pressuring him to work overseas, there may come a time soon when you have to take care of yourself for a while."
    rmom "And you can't do that if you are required to repeat the school year..."
    rmom "...... I highly doubt that could ever be the case, but we still haven't seen your final grades."
    rmom "I hope you weren't slacking just because it's the end of your time in high school?"
    pov "What?! Of course not. Duh!"
    pov "I got mostly straight A's."
    pov "Well, I think I only got a B minus in Math..."
    show c3 parents 2
    with dissolve
    rmom "B minus?!"
    rmom "How on Earth did you get such a middling grade?"
    rmom "I don't recall your grades dropping this much last term."
    rmom "You know we condone your hobbies. Every girl needs time to unwind and enjoy themselves..."
    rmom "But you have to remember studying comes before that."
    rdad "Hey, cut the kid some slack. She was probably busy preparing for graduation with her friends."
    rdad "We don't need to be strict on her during times of celebration."
    show c3 parents 3
    with dissolve
    pov "Exactly! Plus, you know I've always been bad at math."
    pov "Not everyone is perfect at everything like you are, mom..."
    pov "Can't I have just one subject I'm not amazing at?"
    show c3 parents 2
    with dissolve
    rmom "Fine... but I sure hope it wasn't because you were busy playing with those two boys again."
    rmom "I don't know what I'll do if I hear any funny rumours about you three."
    rmom "You aren't a child anymore, after all."
    show c3 parents 3
    with dissolve
    pov "Oh my god... here we go again."
    rmom "But you mustn't forget how important your GPA is for university applications."
    rmom "I know you aren't planning on going this fall, but what about a year or two from now when you {i}do{/i} start applying?"
    rmom "A local university may accept you, but the more elite the university, the more competitive it becomes."
    rmom "We're just asking you to do what's best for your future."
    pov "......"
    pov "Yeah, yeah..."
    pov "I get it. You don't need to keep lecturing me about it."
    pov "I'm taking it seriously."
    rmom "......"
    show c3 parents 4
    with dissolve
    rdad "...... Uh, anyway, just go have fun with graduation and prom night for now."
    rdad "You only get to experience it once in your life, after all."
    rdad "After that you'll eventually become an old fart like me."
    pov "Hey, you aren't that old yet!"
    pov "I'll wait until you start going grey before we ship you away to an old folks home."
    rdad "Haha. Well, assuming this crazy woman doesn't kick me to the curb before then."
    pov "Yeah, you {i}did{/i} marry a pretty scary person."
    pov "Poor dad..."
    show white
    with dissolve
    rmom "...... Okay, time to stop acting silly now, you two."
    rmom "Or I might actually consider it..."
    rdad "Wait... you're joking, right? ... {i}Right?{/i}"
    ev "{i}*laughs*{/i}"
    "......"

    label galleryScene6:
    hide white
    show c3 intro 1
    with fadeholdlong
    pov "{i}*yawns*{/i}"
    pov "9 AM, huh..."
    pov "I'm surprised I woke up before my alarm went off, since I'm usually too lazy to get out of bed before then."
    pov "...... I feel like I had a weird dream last night..."
    pov "What was it, again?"
    pov "Hmm..."
    if c2_end1>=1:
        show c3 intro 2
        with dissolve
        pov "Oh, right..."
        pov "I dreamt I was with a boyfriend or something."
        pov "We were watching a movie together and there was a romantic scene, so we suddenly started kissing, I think?"
        pov "And then things escalated to sex, huh..."
        pov "......"
        show c3 intro 3
        with dissolve
        pov "Well, I can't deny I'd like for something like that to happen one day..."
        pov "But I don't really feel ready for sex... yet."
        pov "Plus, I haven't found anyone that I have feelings for in that way."
        pov "And I guess I'm still worried guys would find me weird if they knew about all the perverted stuff I'm into."
        pov "I'm sure there's someone out there, though."
    if c2_end2>=1:
        show c3 intro 2
        with dissolve
        pov "Oh my god..."
        pov "That's right..."
        pov "I dreamt I was doing something with another girl."
        pov "......"
        pov "I've never thought about girls like that before, so I'm not sure why I would dream about it."
        show c3 intro 3
        with dissolve
        pov "I mean, I {i}have{/i} seen porn of two girls playing with each other before."
        pov "But I only watched those videos out of... curiosity."
        pov "It's not like I'd want to try it myself or anything... right?"
        pov "......"
        pov "Yikes... this is kind of embarrassing..."
        pov "Well..."
    if c2_end3>=1:
        show c3 intro 2
        with dissolve
        pov "Holy..."
        pov "I just remembered now."
        pov "I was flirting with two guys in my dream, and for some reason we went somewhere together, I think?"
        pov "And then it escalated all the way, into us having a threesome..."
        pov "Jeez..."
        pov "This is way more extreme than anything I've dreamt about before."
        pov "I mean, it is pretty hot... in porn, I mean. Several guys and all that."
        show c3 intro 3
        with dissolve
        pov "But there's no way I'd be comfortable doing something like that..."
        pov "I haven't even had sex yet in the first place!"
        pov "And I'd like to give my first time to someone I'm in a serious relationship with, before I'd even consider anything more extreme."
        pov "I guess I {i}have{/i} been having a lot of perverted thoughts lately, though..."
        pov "So maybe it isn't surprising that I'd have a weird dream like this."
        pov "......"
    show c3 intro 4
    with dissolve
    pov "Either way..."
    pov "Me and [fr] were going to meet up today, like we had planned before."
    stop music fadeout 2.0
    pov "So I should probably stop thinking about some dream I had, and focus on reality."
    pov "I need to start getting ready."
    pov "She really hates tardiness, after all."
    "......"

    play music "<from 10.8>audio/sparkle.mp3" fadein 2.0 loop
    show c3 friend 1
    with fadeholdlong
    fr "What do you think of this phone?"
    fr "People seem to be giving it good reviews, but it's a bit too expensive for me..."
    pov "Wait... a thousand dollars?!"
    pov "Even if I {i}did{/i} have the money, no way..."
    pov "Phones cost way too much these days."
    show c3 friend 2
    with dissolve
    fr "Exactly. They're basically the same price as computers now."
    fr "Actually... it's almost half a semester's tuition for me, now that I think of it..."
    fr "But I guess considering how much we use our phones, it's not {i}that{/i} bad of an investment."
    pov "That's true..."
    pov "I just don't want to use my parents' money anymore if I can help it."
    pov "I'd rather use the money I've earned instead, through working and what not."
    show c3 friend 3
    with dissolve
    fr "Wow... you've grown up, huh? {i}*laughs*{/i}"
    fr "That's a big difference from how you used to be in middle school."
    fr "Mom, buy me this... dad, give me money for that..."
    pov "Hey! We were all dumb when we were younger."
    pov "You also got into fights with your brother all the time, didn't you?"
    show c3 friend 4
    with dissolve
    fr "Yeah. Thankfully we're in different countries now, so I don't have to deal with him..."
    fr "He hasn't grown up that much yet."
    fr "I mean, I'll already be turning 20 this fall, but he's four years younger than me."
    fr "High school boys can be pretty annoying."
    fr "It's always some fart joke, or something perverted or sexist..."
    show c3 friend 2
    with dissolve
    pov "Yeah... I can't say I miss dealing with that in school."
    pov "I guess it's also a good thing I'm an only child."
    fr "Yup."
    fr "The less sibling drama you have to deal with, the better."
    fr "But anyway, that all aside..."
    show c3 friend 5
    with dissolve
    fr "I guess there isn't anything else I really need to buy right now."
    fr "What do you say we go take a break, and get a cup of coffee?"
    pov "Sure."
    pov "We've been standing for quite a while now, so I could use the rest."
    "......"
    show c3 friend 6
    with fadeholdlong
    pov "Hey, could I get a medium white mocha, please?"
    wom "Sure."
    fr "And I'll have a medium hot chocolate."
    fr "That's all for us, I think."
    wom "Okay. That'll be $7.83 in total— tax included."
    show c3 friend 7
    with dissolve
    pov "I'll pay with debit."
    pov "And don't worry, it's on me, [fr]."
    pov "I'm the one introducing you to this place, after all."
    fr "Thanks! I'll pay you back some other time."
    show c3 friend 8
    with fadeholdlong
    fr "This store seems pretty good."
    fr "I don't think I've ever heard the company's name before, so it must be a local Vancouver thing."
    fr "It's a cozy little place, huh."
    pov "Yup. I come here every now and then."
    pov "Well, more so lately since it's on my way home from our model agency."
    pov "I'm usually so tired after work that I need caffeine to keep staying awake..."
    fr "That makes sense."
    show c3 friend 9
    with dissolve
    fr "...... So, if you don't mind me asking..."
    pov "Uh-oh. Here it comes..."
    fr "Did you manage to find a boyfriend yet, or someone you like?"
    pov "......"
    menu:
        "{i}(How should I respond?){/i}"
        "Not yet, but I'm looking.":
            show c3 friend 10
            with dissolve
            pov "Nah... not yet."
            pov "I'm interested in finding a boyfriend, of course."
            pov "But there hasn't been a guy I've had feelings for or anything."
            pov "Josh and Connor are pretty close friends of mine, but I'm not sure if they're relationship material."
            pov "Well... {i}maybe{/i}."
            pov "I do feel comfortable around them. And I don't think they're bad looking or anything."
            pov "But if I did go out with one of them, what would happen with the other person?"
            pov "There's no way we'd still be able to hang out as a group of three."
            pov "It'd ruin our friendship... I don't want that."
            show c3 friend 11
            with dissolve
            fr "Hmm..."
            fr "That's true..."
            fr "It's a pretty complicated situation to be in."
            fr "...... Oh, here's an idea!"
            fr "What if you just went out with both of them at the same time? {size=-7}{i}*laughs*{/i}{/size}"
            show c3 friend 12
            with dissolve
            pov "?!"
            pov "{i}*chokes*{/i}"
            pov "W-what?!"
            fr "Woah, are you okay?!"
            fr "I'm just teasing you!"
            show c3 friend 14
            with dissolve
            pov "You sure surprised me..."
            pov "Sometimes you just come up with the craziest comments..."
            if boys_horny >=2:
                pov "{i}(Hmm... two boyfriends, huh...){/i}"
                pov "{i}(I've never even thought of that before.){/i}"
                pov "{i}(I guess I wouldn't be 100 percent opposed to the idea...){/i}"
                pov "{i}(But there would be jealousy between the other two, so I highly doubt there's anyone out there who would be okay with something like that.){/i}"
                pov "{i}(Not like it would ever happen, though...){/i}"
            else:
                pov "{i}([fr] is usually so serious and mature, so it takes me by surprise when she says things like this...){/i}"
                pov "{i}(I wonder if that's just the Japanese style of humour?){/i}"
        "I'm not interested in anything like that right now. [gr]\[Innocent +1\]":
            show c3 friend 10
            with dissolve
            pov "Nah... I haven't really thought about it."
            pov "It's not like I'm against finding a boyfriend or anything, but..."
            pov "Right now, I've just been focusing on modelling and things like that."
            pov "Plus, if I do end up going to university like you, that might strain the relationship and change things a bit."
            pov "So maybe it'd be best to wait until I enroll first, or until I have a more serious and stable job."
            show c3 friend 11
            with dissolve
            fr "Hmm... that's a smart way of thinking about it."
            fr "We're still teenagers for a little while, anyway, so no need to rush anything."
            fr "I was just curious! Sorry if it felt like I was pressuring you."
            pov "No, no! It's all good!"
            $inn +=1
    pov "Anyway..."
    pov "Now that you've asked me the dreaded question, what about {i}you{i}?"
    pov "I don't see any guys tagging along on your social media posts..."
    show c3 friend 13
    with dissolve
    fr "Crap... my turn, huh."
    fr "Well, I'm in the same boat as you, pretty much."
    fr "I just haven't had the time to consider a boyfriend, what with how busy I've been."
    fr "They'd want to meet up every day or two, and that just wouldn't work..."
    fr "Well, it {i}could{/i}, but then my GPA would seriously suffer."
    fr "I tried so hard just to get into a Canadian university in the first place, so I don't want to risk losing my scholarships."
    fr "Exchange students have to pay, like, three times the amount a Canadian student does."
    fr "It's a lot of money, and I wouldn't be able to pay for it without the scholarships."
    show c3 friend 14
    with dissolve
    pov "Yeah, that makes sense."
    pov "Doing well in school obviously comes first for someone in your situation."
    pov "I mean, I couldn't really picture you having a guy in your life right now, anyway, with how busy you always are."
    pov "You've barely even been able to hang out with your friend [pov], after all. {size=-5}{i}*giggles*{/i}{/size}"
    pov "But I mean, who knows, maybe you'll find someone at school who's also serious about their grades, like you are?"
    pov "That way you could spend time together through studying."
    pov "Sounds kind of romantic in its own way, actually."
    show c3 friend 13
    with dissolve
    fr "Hmm... now that you mention it, that wouldn't be so bad."
    fr "It would definitely be easy to meet up."
    fr "And I wouldn't have to worry about my grades dropping too much."
    fr "{i}{size=-7}(Not that I really want a boyfriend, though...){/size}{/i}"
    pov "Actually, didn't you have a boyfriend like that for a few weeks, back in high school?"
    pov "I forgot about that until now."
    show c3 friend 15
    with dissolve
    fr "Oh, right... {i}him{/i}."
    fr "Well, we did study together sometimes, but the issue is he cheated on me... remember?"
    pov "Oh, crap!"
    pov "Sorry for being insensitive! I should have thought about that before I brought it up."
    fr "No worries. I moved on from him a long time ago."
    fr "Plus, we weren't in that serious of a relationship to begin with."
    fr "We just had mutual feelings for each other, and held hands - that sort of thing."
    fr "We kissed maybe once or twice for a couple seconds each, and then he never had the courage to do anything again."
    fr "It still hurt when he cheated on me, but we were just kids at the time."
    show c3 friend 16
    with dissolve
    pov "Gotcha."
    pov "Well, I'm glad that's all in the past now."
    pov "Anyway, we should probably end this depressing topic and head out again."
    pov "It's almost time for the movie, isn't it?"
    stop music fadeout 2.0
    fr "Oh right. We should probably get going!"
    fr "I need to go to the bathroom first, and I'd like to get some popcorn once we're there."
    "......"

    play music "<from 3.5>audio/isolation.mp3" fadein 0.5 loop
    show c3 outside 1
    with fadeholdlong
    "The next day."
    pov "I wonder what kind of fashion we'll be shooting today?"
    pov "My boss wasn't decided on which sets he'd be assigning to who."
    pov "Lately I've been getting picked for the swimwear ones quite a bit, though."
    pov "Makes me wonder if it's just a coincidence, or if there's some sort of reason for it..."
    show c3 outside 2
    with dissolve
    if model_seduction >=2:
        pov "He might just be using it as an excuse to stare at my body again, or something like that..."
        pov "He's a man, after all."
    else:
        pov "I guess it's probably just coincidence, since I do still get assigned to regular shoots every now and then."
    pov "Well, whatever..."
    pov "I managed to finish getting ready earlier than usual today, so there's a few minutes to spare."
    if inn >=2:
        show c3 outside 3
        with dissolve
        pov "But I should probably just arrive at the office a few minutes early."
        label c3wind:
        pov "It makes me look more serious about the job."
        pov "If I'm ever planning to get a promotion or a raise or something, having a good image and reputation helps a lot."
        pov "Well, I already do get along well enough with the other models."
        pov "Calling them 'friends' would be a bit of a stretch, though, since we {i}are{/i} each other's competition."
        pov "But nobody hates each other, and there's no drama as far as I can tell."
        pov "I guess that's what happens when everyone is an adult."
        pov "And th——"
        if exh >=2:
            show c3 outside 4a
            with pixellate
            pov "?!"
            pov "......"
            pov "No way..."
            pov "This is embarrassing."
        else:
            show c3 outside 4b
            with pixellate
            pov "?!"
            pov "......"
            pov "No way..."
            pov "This is embarrassing."
        pov "...... Oh my god."
        pov "That woman standing there just saw me, too..."
        show c3 outside 5
        with dissolve
        if exh >=2:
            pov "Not only that, but she saw that I wasn't wearing any panties..."
            pov "I went outside today without any, since I thought the thrill of it would be fun."
            pov "But..."
            pov "I didn't think anyone would {i}actually{/i} end up seeing anything."
            pov "She probably thinks I'm a complete pervert..."
        pov "I guess that's my own fault for wearing a light skirt when it's windy outside."
        pov "Still... talk about embarrassing..."
        pov "At least it was a woman instead of a guy who saw me."
        pov "......"
        menu:
            "It was kind of exciting being seen by a girl. [gr]\[Lesbian +1\] \[Sexe +1\]":
                show c3 outside 6
                with dissolve
                pov "You know..."
                pov "I'm only really interested in guys, but..."
                pov "If it's just {i}looking{/i}, I guess some attention from other women isn't necessarily a bad thing."
                pov "It actually kind of excited me a bit when she saw me."
                pov "I mean, it might just be that {i}any{/i} attention is exciting, rather than it being because of her sex or whatever."
                pov "I'm not sure..."
                pov "It's not like I've spent a lot of time considering things like this."
                pov "Well, whatever..."
                pov "I've wasted enough time already. I should hurry up before being 'early' turns into being 'late'."
                $les+=1
                $sexe+=1
                $ renpy.end_replay()
                jump c3office
            "I don't feel any different. [gr]\[Sexe +1\]":
                show c3 outside 7
                with dissolve
                pov "It doesn't come as a surprise or anything, but..."
                pov "Unlike when guys are looking at or flirting with me, I didn't really feel anything from her seeing me."
                pov "The feeling isn't much different from when I'm in a changing room with other girls, for example."
                pov "Why would you be interested in something you already have, after all?"
                pov "Really, I'm just embarrassed more than anything."
                stop music fadeout 2.0
                pov "......"
                pov "Alright. I should hurry up before being 'early' turns into being 'late'."
                $sexe+=1
                $ renpy.end_replay()
                jump c3office
    else:
        menu:
            pov "Maybe I should have a little bit of fun...?"
            "Flash someone outside. [gr]\[Sexe +1\] \[Exhibition\]":
                label galleryScene7:
                show c3 outside 8
                with dissolve
                pov "Well, if I only have a few minutes..."
                pov "Rather than talking to someone, I could try giving them a little... 'glimpse', along the way."
                pov "That way I don't waste any time getting to work, {i}and{/i} I can have a few seconds of harmless fun."
                show c3 outside 9
                with dissolve
                pov "Hmm..."
                pov "This guy is walking close enough to see."
                pov "And he doesn't look too scary."
                pov "....... Alright, I've picked the lucky victim for today."
                if exh >=2:
                    show c3 outside 10a
                    with pixellate
                    pov "......"
                    pov "I'll just lift up my skirt a little bit, just like this..."
                    pov "This should give him enough to see."
                    pov "Especially since I'm not wearing any panties today..."
                    pov "I thought I'd try something a bit different, for the thrill of it."
                    man "......?!"
                    man "{i}(Huh?){/i}"
                    show c3 outside 11
                    with dissolve
                    man "{i}(What the...){/i}"
                    man "{i}(There's no way this isn't on purpose...){/i}"
                    man "{i}(Is she trying to seduce me?){/i}"
                    man "{i}(She's not even wearing any underwear...){/i}"
                    man "{i}(Some girls these days really do have strange hobbies.){/i}"
                    man "{i}(I mean, if that's what she wants to do, I'm certainly not going to complain about the view she's giving me...){/i}"
                    man "{i}(She is quite hot, after all.){/i}"
                    "......"
                    $ renpy.end_replay()
                    jump c3outb
                else:
                    show c3 outside 10b
                    with pixellate
                    pov "......"
                    pov "I'll just lift my skirt up a little bit, like this..."
                    pov "This should give him enough to see."
                    pov "It's just my panties, but there's no way I'm undressing in the middle of the streets, in broad daylight..."
                    pov "This is already plenty."
                    man "......?!"
                    show c3 outside 11
                    with dissolve
                    man "{i}(Huh?){/i}"
                    man "{i}(What the...){/i}"
                    man "{i}(There's no way this isn't on purpose...){/i}"
                    man "{i}(Is she trying to seduce me?){/i}"
                    man "{i}(You don't just show a stranger your panties by accident.){/i}"
                    man "{i}(Especially not out in public like this...){/i}"
                    man "{i}(I mean, whatever her reason is, I'm not complaining about the sight she's giving me...){/i}"
                    man "{i}(She is quite cute, after all.){/i}"
                    "......"
                    jump c3outb
                label c3outb:
                show c3 outside 12
                with dissolve
                pov "Wow..."
                pov "I can't tell if he was more surprised or excited?"
                pov "Probably a bit of both, huh..."
                pov "A cute girl giving you a surprise like this as you're walking along, minding your own business..."
                pov "It's certainly not what you'd expect to have happen."
                pov "...... I wonder if he's still looking this way?"
                stop music fadeout 2.0
                pov "Well, unfortunately for him, I have to get to work."
                pov "He can entertain himself with the memory whenever he gets back home."
                "......"
                $sexe+=1
                $exh+=1
                jump c3office
            "Now's not the time.":
                pov "Nah..."
                pov "I'd rather not get carried away with anything before work."
                show c3 outside 3
                with dissolve
                pov "And I should probably just arrive a few minutes early, anyway."
                jump c3wind

    label c3office:
    play music "audio/cloudy.mp3" fadein 0.5 loop
    show c3 office 1
    with fadeholdlong
    ja "Good afternoon, [pov]."
    ja "I've been looking forward to seeing you again today."
    ja "You're a bit earlier than usual, no?"
    pov "Good afternoon! Same to you."
    pov "I wanted to get here a bit earlier today, if I could."
    pov "No special reason for it, but I just felt like working extra hard today."
    ja "Haha. Well, I'm happy that you're so motivated lately."
    show c3 office 2
    with dissolve
    ja "Hmm..."
    ja "There's still a little bit of time before we need to start shooting."
    ja "Would you like to join me for a quick chat?"
    ja "This is still my lunch hour, so no need to be reserved."
    pov "Sure! I'd be glad to join you."
    ja "Great. Let's head to this table over here, then."
    "......"
    show c3 office 3
    with fadeholdlong
    ja "So, what do you think of everything so far?"
    ja "...... Oh, no need to sweat it and think about the question too seriously."
    ja "We've already finished the interview process, after all. {i}*laughs*{/i}"
    ja "I'm just checking up on you, is all."
    show c3 office 4
    with dissolve
    pov "Haha. Well, I've been enjoying it a lot so far."
    pov "All the other models have been kind to me, and I haven't had any problems or anything like that."
    pov "Plus, you've also been extremely helpful."
    pov "I'm able to work without being stressed about anything, since you always give me tips and encourage me when I'm lost."
    show c3 office 5
    with dissolve
    ja "That's good to hear."
    ja "I always give our new models as much encouragement as I can offer."
    ja "In your case, though, I've given even more attention than usual, since I feel there's a great amount of potential in you."
    ja "A lot of girls do modelling as a bit of side income, or for fun, but..."
    ja "I can picture this becoming a long-term vocation for you."
    show c3 office 4
    with dissolve
    pov "Wait, really? I'm happy to hear that."
    pov "I'll keep doing my best. I hope I can do even better from here on."
    ja "I have no doubts you will."
    show c3 office 6
    with dissolve
    ja "...... Hmm, this is a bit personal, but..."
    ja "I went through a divorce not too long back, see..."
    ja "It's no secret around here since the girls enjoy their gossip."
    ja "You'd have found out sooner or later, I'm sure."
    ja "If you ask one of them, they'll probably tell you the story behind the divorce, which is that my ex-wife was unfaithful to me."
    show c3 office 7
    with dissolve
    ja "And that's unfortunately the truth..."
    ja "So there are times when I feel a bit on the lonely side, and can be a bit flirty or touchy-feely."
    ja "If there's ever any moment where you feel uncomfortable, please don't be afraid to let me know."
    ja "You being comfortable at this company is the only thing I'm asking for, after all."
    show c3 office 8
    with dissolve
    pov "......"
    pov "I'm sorry to hear about what happened..."
    pov "But, please, don't worry. You haven't made me feel uncomfortable or anything like that."
    pov "If anything, I've felt happy about how much you've been praising me."
    pov "You're more than welcome to keep treating me as you always have."
    pov "And if it makes you feel better, even more reason to do so."
    pov "Of course, that's also not to say {i}anything{/i} goes... but there's nothing wrong with how you've been so far."
    show c3 office 9
    with dissolve
    ja "Okay, good to know."
    ja "Thanks for the concern."
    ja "Just making sure, since that's been something I've thought about as of late."
    ja "You're a kind girl, [pov]."
    pov "Thank you."
    show c3 office 10
    with dissolve
    ja "Well, anyway..."
    ja "I'd like to chat some more with you, but we should probably start getting ready soon."
    ja "What do you say we continue the conversation some other time?"
    pov "Sure, I'd be glad to."
    stop music fadeout 2.0
    ja "Great."
    ja "Well then..."
    ja "I'll meet you in a little bit after you finish getting ready."
    play music "audio/swing.mp3" fadein 2.0 loop
    if model_seduction >=2:
        show c3 photo 1a
        with fadeholdlong
        pov "{i}(Alright... just waiting for him to finish getting the camera set up.){/i}"
        pov "{i}(This bikini I'm wearing today, though...){/i}"
        pov "{i}(It's a bit more revealing than the other outfits we've shot with.){/i}"
        pov "{i}(I mean, I wouldn't be opposed to wearing it in my own time...){/i}"
        pov "{i}(In fact, I already have a string bikini that I bought not too long ago. I was thinking of giving it a go and wearing it for the first time, some time soon.){/i}"
        show c3 photo 2a
        with dissolve
        pov "{i}(But... I didn't think we'd be shooting with one, since there's other models here with better proportions than me.){/i}"
        pov "{i}(I {i}do{/i} have a nice body, but there's definitely better than me at this agency.){/i}"
        pov "{i}(Whatever the reason he chose me, though, I'm not gonna complain.){/i}"
        ja "Alright, we should be good to go now."
        ja "I'll just have you step into position, and then we can start shooting."
        show c3 photo 3a
        with dissolvelong
        ja "Great job. Keep emphasizing your body like that."
        play sound "audio/effects/camera1.mp3"
        "*snap*"
        ja "We'll edit in the effects later on to make it look like you're on the beach."
        ja "Let's get another pose... something similar."
        show c3 photo 4a
        with dissolve
        ja "Yes, just like that!"
        play sound "audio/effects/camera1.mp3"
        "*click*"
        ja "Pretend you're enjoying the scenery around you."
        play sound "audio/effects/camera2.mp3"
        "*click*"
        ja "Next, I want you to lay back a bit and act like you're relaxing in the sun."
        show c3 photo 5a
        with dissolve
        ja "Perfect!"
        ja "Anyone seeing these photos in the magazine will be quite enamored, I'm sure."
        play sound "audio/effects/camera1.mp3"
        "*snap*"
        ja "Wow..."
        ja "Can you go on your knees and give the camera... uh, a good view of your cleavage?"
        show c3 photo 6
        with dissolve
        pov "Like this?"
        ja "Yes, that's exactly what I was looking for."
        play sound "audio/effects/camera2.mp3"
        "*snap*"
        ja "Beautiful..."
        ja "Now, lastly..."
        ja "Assuming you're OK with it, can you stand up and show your... rear to the camera?"
        show c3 photo 7
        with dissolve
        pov "Is this what you mean?"
        ja "Woah... yes. Just what I meant."
        play sound "audio/effects/camera3.mp3"
        "*snap*"
        ja "I'm impressed..."
        ja "Hmm..."
        ja "This should do for the current scene. We'll move on to the next scene now."
        show c3 photo 8a
        with fadeholdlong
        "A little while later."
        ja "Splendid work as usual, [pov]."
        ja "Maybe we should have you wear mature swimwear like this more often? Haha..."
        show c3 photo 9
        with dissolve
        ja "Well, it'll depend on our sponsors, of course, but I'd like to try and schedule you for more scenes like this."
        ja "That is, of course, assuming you're OK with that?"
        show c3 photo 8a
        with dissolve
        pov "Of course. That's no problem at all."
        pov "I enjoyed it quite a bit."
        ja "Good to know. Thanks for being so cooperative."
        "......"
        show c3 photo 10a
        with dissolve
        pov "{i}(Hmm... you know...){/i}"
        pov "{i}(I feel kind of bad for him after what he told me earlier.){/i}"
        pov "{i}(I should give him a bit of a reward, since he said he's been feeling depressed for a while.){/i}"
        pov "{i}(Nothing perverted, though. I'm a bit too tired for that after all this shooting.){/i}"
        pov "{i}(Hmm... this should be fine.){/i}"
        show c3 photo 11
        with dissolve
        "{i}*kiss*{/i}"
        pov "A reward for confiding in me earlier."
        pov "And for being such a nice person to me."
        pov "Just a hug and a kiss on the cheek..."
        pov "You weren't expecting me to kiss you on the lips, were you...?"
        ja "Haha... no, of course not."
        pov "Okay, because I'd only do that for someone I'm going out with."
        show c3 photo 12
        with dissolve
        ja "No worries. That's only natural."
        ja "Hmmm..."
        ja "That makes me wonder..."
        ja "Is there a boy you're dating right now, if you don't mind me asking?"
        pov "{i}(He's holding me with his hand on my butt...){/i}"
        pov "{i}(I guess I don't really mind, since it's probably not on purpose.){/i}"
        pov "{i}(Even if it was... well, whatever.){/i}"
        pov "{i}(A guy touching my butt isn't something that bothers me.){/i}"
        pov "{i}(Especially after what he told me, I can't really get mad at him.){/i}"
        show c3 photo 13
        with dissolve
        pov "No, not right now."
        pov "Maybe some time soon I will, but I'm just focused on working right now."
        ja "I see..."
        ja "Well, if you ever did find someone, our models are free to do whatever they like in their personal lives."
        ja "Although, since you're free, I suppose that means I have a chance, huh?"
        pov "I guess so..."
        ev "{i}*laughs*{/i}"
        ja "Alright, I should probably stop teasing and let you go now."
        stop music fadeout 2.0
        ja "I have another shoot coming up later this afternoon."
        pov "Sure. I'll let you get to that, then."
        "......"
        jump c3boys
    else:
        show c3 photo 1b
        with fadeholdlong
        pov "{i}(Alright... just waiting for him to finish getting the camera set up.){/i}"
        pov "{i}(There were a couple different choices today, for what bikini I'd wear.){/i}"
        pov "{i}(There was this one, and then another more revealing one...){/i}"
        pov "{i}(I guess, naturally, I was just kinda drawn to this one since it's similar to what I'm usually wearing in these shoots.){/i}"
        pov "{i}(Plus... while I'm fine wearing it in my own time...){/i}"
        pov "{i}(I don't know if I'm ready to wear something as revealing as a string bikini in front of a camera, for thousands of people to see.){/i}"
        show c3 photo 2b
        with dissolve
        pov "{i}(I do have a pair of my own at home, and I've been thinking of wearing it soon, but...){/i}"
        pov "{i}(There's other girls here much more equipped to handle a photoshoot like that.){/i}"
        pov "{i}(I definitely don't have the biggest breasts here... not by a long shot.){/i}"
        pov "{i}(So, I decided to let someone else take care of wearing the string bikini.){/i}"
        ja "Alright, we should be good to go now."
        ja "I'll just have you step into position, and then we can start shooting."
        show c3 photo 3b
        with dissolvelong
        ja "Great job. Keep emphasizing your body like that."
        play sound "audio/effects/camera1.mp3"
        "*snap*"
        ja "We'll edit in effects later on to make it look like you're on the beach."
        ja "Let's get another pose... something similar."
        show c3 photo 4b
        with dissolve
        ja "Yes, just like that!"
        play sound "audio/effects/camera1.mp3"
        "*click*"
        ja "Pretend you're enjoying the scenery around you."
        play sound "audio/effects/camera2.mp3"
        "*click*"
        ja "Next, I want you to lay back a bit and act like you're relaxing in the sun."
        show c3 photo 5b
        with dissolve
        ja "Perfect!"
        ja "Anyone seeing these photos in the magazine will be quite enamored, I'm sure."
        play sound "audio/effects/camera3.mp3"
        "*snap*"
        ja "Wow..."
        ja "Hmm..."
        ja "This should do for now. We'll move on to the next scene now."
        "......"
        show c3 photo 8b
        with dissolve
        "A little while later."
        ja "Splendid work as usual, [pov]."
        ja "You do well with the fashion shoots, but these bikini ones might just be your true calling. {i}*laughs*{/i}"
        pov "Maybe so. {i}*giggles*{/i}"
        ja "Well, anyway, that should be all for today."
        ja "I should let you get going, since there's another shoot I have to prepare for soon."
        ja "I'm really looking forward to seeing you next week."
        ja "You're my favourite for a reason. {i}*laughs*{/i}"
        stop music fadeout 2.0
        pov "Wow, I'm flattered to hear that..."
        pov "Alright. Thanks for leading me again today."
        pov "See you next week!"
        "......"
        jump c3boys

    label c3boys:
    play music "<from 1.6>audio/absurd.mp3" fadein 0.5 loop
    show c3 boys 1
    with fadeholdlong
    pov "So what was Connor doing today, again?"
    j "He had a haircut scheduled, I think?"
    j "I texted him when I was on the way, and he said he'll be here whenever he's done."
    pov "Ah, gotcha."
    pov "A haircut, though... I wonder if there's a special reason for it?"
    pov "Surely he hasn't found a girl he likes... {i}right{/i}?"
    show c3 boys 2
    with dissolve
    j "Haha, nah, not him."
    j "He's always been shy around girls and what not."
    j "There was actually a girl back in junior year who told me she liked him, but he was too nervous to actually ask her out."
    j "Which is a shame, since I don't think he's gotten another opportunity since."
    show c3 boys 1
    with dissolve
    pov "Aww... sounds like Connor, alright."
    pov "I guess it's a bit different in your case, though, huh?"
    pov "Rather than being shy, you've just never shown much of an interest in dating as far as I can tell."
    pov "You were pretty popular back in school, too..."
    show c3 boys 2
    with dissolve
    j "Well, I figured high school relationships wouldn't last beyond graduation."
    j "And I wanted to get a career sorted out before thinking about a girlfriend."
    show c3 boys 3
    with dissolve
    j "I guess I could probably manage a relationship now, since I've mostly figured things out with my dad's company."
    j "But I don't really care enough to actively search for one, either."
    j "I'm not in school anymore, so my options are limited to Tinder and things like that."
    j "I mean, shit, I won't lie... I've tried looking on there a few times, but none of the girls there were my type."
    j "I could only ever last maybe ten minutes before I gave up and uninstalled that garbage."
    show c3 boys 4
    with dissolve
    pov "True... I can't imagine the average Tinder girl looking for a one-night-stand is what you're interested in."
    pov "You've always been into girls with a more serious personality, and cute looks, from what I can tell."
    pov "It's obvious by looking at your face whenever we watch anime..."
    show c3 boys 3
    with dissolve
    j "Haha. Yeah, anime girls sure are something."
    j "...... Well, whatever. I'll find someone one day. I'm not really worried."
    j "It's the same thing for you, isn't it?"
    show c3 boys 4
    with dissolve
    pov "I guess you could say that..."
    pov "I'm keeping an eye open, but I'm not on a quest to find someone, either."
    pov "Forcing yourself to find someone is just destined to end in disaster."
    pov "Plus, there's no telling what kind of weirdos you might find through dating apps and what not."
    pov "I guess the two of us can just be lonely together, huh?"
    j "{i}*laughs*{/i}"
    j "Yeah, maybe."
    show c3 boys 5
    with dissolve
    pov "{i}(.......){/i}"
    pov "{i}(You know...){/i}"
    pov "{i}(Sometimes I wonder if the real reason he hasn't looked for someone, is because there's a girl he's already interested in.){/i}"
    pov "{i}(And I wonder if it's a certain girl who's around him all the time...){/i}"
    pov "{i}(Well, no way to know for sure...){/i}"
    pov "{i}(And I don't want to risk the friendship between us three by asking something weird.){/i}"
    pov "{i}(Even if Josh was interested in me, I care about Connor just as much, too...){/i}"
    pov "{i}(Ahh... forget it!!){/i}"
    show c3 boys 2
    with dissolve
    pov "Alright, enough of all this serious talk..."
    pov "Let's watch an episode or two on Netflix before Connor gets here."
    j "Sure. What do you wanna watch?"
    "......"
    show c3 boys 6
    with fadeholdlong
    c "Yo..."
    c "If you make fun of me, I'll kick your ass, man."
    c "You too, [pov]...... not literally, but figuratively."
    c "You get a pass since you're a girl."
    show c3 boys 7
    with dissolve
    pov "Aww, what a gentleman you are."
    pov "Hmm..."
    pov "It looks nice, though. I wouldn't be shy about it if I were you!"
    j "Yeah, seems fine to me."
    c "Alright... good."
    c "What have you two been up to, anyway?"
    j "We were just watching some anime on Netflix until you got here."
    c "Oh, cool. I'm down to watch for a little bit, too."
    c "I'm getting pretty hungry, though."
    c "Are you guys interested in getting something for dinner?"
    j "Sure... uhh, maybe pizza or something?"
    pov "Yeah, pizza sounds good to me!"
    pov "Take a look at the online menu quick and tell me what you guys want. I'll order it in a few minutes."
    "......"
    show c3 boys 8
    with fadeholdlong
    play sound "audio/effects/doorbell1.mp3"
    "{i}*ding dong*{/i}"
    pov "Oh, they're here already?"
    pov "I guess the store is pretty close, after all."
    pov "I'll go upstairs and pay quick. Just give me a couple bucks afterwards, and we're good."
    c "Oh, sweet. Thanks for the deal."
    j "Yeah. Thanks."
    "......"
    label galleryScene8:
    show white
    with dissolve
    "Noticing on her phone that their delivery driver's name is that of a male, [pov] decides to..."
    menu:
        "Tease the delivery boy for a minute. [gr]\[Sexe +1\] \[Exhibition +1\]":
            pov "{i}(Hmm...){/i}"
            pov "{i}(I don't have the time to go all the way to my bedroom and find something sexy.){/i}"
            pov "{i}(He's at the door and will probably leave if I don't answer quickly.){/i}"
            pov "{i}(I guess that leaves... this, then.){/i}"
            pov "One second!"
            "......"
            hide white
            show c3 pizza 1
            with fadeholdlong
            pov "Umm... hi."
            pov "Sorry... I was just in the bath and wanted to answer the door in time."
            pov "{size=-5}{i}(That's a lie. I just took my gown off quickly in the bathroom.){/i}{/size}"
            pov "Hope you don't mind?"
            boy "?!"
            boy "Uh... uhh..."
            boy "No, it's alright..."
            show c3 pizza 2
            with dissolve
            boy "A l-large 'meat lovers', and a m-medium 'creamy cheese'..."
            boy "...... Is this right?"
            pov "Oh, yes! That's me."
            pov "Can I have a look quick?"
            boy "O-Okay... I left it by the door. One second..."
            pov "{i}{size=-5}(He probably would have dropped the boxes in surprise, if he didn't put them on the bench first...){/size}{/i}"
            show c3 pizza 3
            with dissolvelong
            pov "Oh, this looks delicious!"
            pov "I can't wait to eat it."
            boy "..... Err, well, feel free to pay whenever you're ready."
            pov "Okay. One second."
            pov "Wait, I think I dropped my card here earlier..."
            show c3 pizza 4
            with pixellate
            with Pause (2.0)
            "......"
            boy "?!"
            boy "{i}(What the...){/i}"
            boy "{i}(I mean, I'm not complaining, but...){/i}"
            boy "{i}(...... Man, she sure has quite the body.){/i}"
            pov "{size=-5}{i}(Truth be told, I didn't actually drop anything here...){/i}{/size}"
            show c3 pizza 5
            with pixellate
            with Pause (2.0)
            boy "{i}(I wonder how old she is?){/i}"
            boy "{i}(Maybe 18 or 19?){/i}"
            boy "{i}(Probably around the same age as me.){/i}"
            boy "{i}(Shit... I almost wish my girlfriend was this hot...){/i}"
            pov "{size=-5}{i}(Not only did I not drop it, but I've known where it was all along... on my bedroom desk.){/i}{/size}"
            show c3 pizza 6
            with dissolvelong
            pov "Okay, I think I left my debit card somewhere else..."
            pov "So I'll just pay you in cash instead, since I have some laying around."
            pov "Sorry about that!"
            boy "Uh, no problem..."
            pov "{i}(He seems pretty young, so I'm sure he enjoyed that little show.){/i}"
            pov "{i}(Hmm...){/i}"
            pov "{i}(Since I'm in an extra good mood today, I guess I'll give him a nice big tip.){/i}"
            pov "{i}(Maybe that'll convince him to volunteer taking my order from now on?){/i}"
            pov "{i}(If I ordered on the same time and day of the week, the chances of him working again are relatively high...){/i}"
            pov "{i}(......){/i}"
            $c3pizza = True
            $exh+=1
            $sexe+=1
        "Pay for the food, and not waste any time. [gr]\[Innocent +1\]":
            pov "{i}(Hmm...){/i}"
            pov "{i}(Even if I wanted to, I just don't have the time for that right now.){/i}"
            pov "{i}(He's at the door, and will probably leave if I don't go up there and answer right away.){/i}"
            pov "{i}(Maybe some other time.){/i}"
            pov "One second!"
            "......"
            hide white
            show c3 pizza 7
            with fadehold
            pov "Hi! Thanks for coming here."
            boy "No problem. One large 'meat lovers', and a medium 'creamy cheese'... is this right?"
            pov "Yup, that's us."
            pov "Do you mind if I take a look quick?"
            boy "No problem. I put it down just outside the door, so let me get it for you quickly."
            show c3 pizza 8
            with dissolve
            pov "Oh, this looks delicious!"
            pov "I can't wait to eat it."
            boy "Great. The total comes to $21.99. Please enter your card whenever you're ready."
            pov "Okay."
            pov "{i}(I feel kind of bad for him since I'm in such a rush...){/i}"
            if exh >=2:
                pov "{i}(And I didn't give him any sort of 'service' of my own, so to speak...){/i}"
                pov "{i}(There's always a next time for teasing, though.){/i}"
            pov "{i}(I guess I'll give him a nice, big tip to make up for it.){/i}"
            $inn+=1
    $ renpy.end_replay()
    show c3 boys 9
    with fadeholdlong
    pov "Alright, that's all the pizza, paid for and everything."
    if c3pizza:
        c "Oh. What took you so long?"
        j "Yeah, we were wondering if there was a problem or something."
        pov "Oh, nothing! It just wouldn't accept my card for some reason, so I had to go get cash instead."
    else:
        c "Oh, nice. That was pretty fast."
        j "Yeah. The hotter the pizza, the better, huh."
        pov "Yup. Didn't waste any time chatting with the delivery person, since I wanted to hurry and eat with you guys."
    pov "Anyway, let's dig in and keep watching!"
    stop music fadeout 2.0
    pov "I want to play some games once we're done eating, if that's cool?"
    j "Sure. I'm about ready to call it with the anime, too."
    "......"
    if boys_horny >=2:
        play music "audio/low.mp3" fadein 2.0 loop
        show c3 boys 10
        with fadeholdlong
        pov "{i}(So it's been a couple hours of playing games now.){/i}"
        pov "{i}(We've watched a lot of Netflix, chat, ate, played games... so, it's about the time we usually wrap things things up for the night.){/i}"
        pov "{i}(But...){/i}"
        pov "{i}(I feel like something is missing.){/i}"
        pov "{i}(I mean, I've had lots of fun, but... especially after all the talk with Josh earlier about girls and such...){/i}"
        pov "{i}(There's this weird feeling inside that I want to release somehow.){/i}"
        pov "{i}(And there's only one way to solve that right now, that I can think of...){/i}"
        show c3 boys 11
        with dissolve
        "......"
        pov "Hey, umm..."
        pov "This is a bit sudden, and you guys might be a bit surprised and all..."
        pov "But we're close friends, so I know you won't be all weird about it afterwards."
        c "Huh?"
        j "What are you acting all secretive about suddenly?"
        pov "Well, I've been wondering lately..."
        pov "I've seen a lot of girls at work, especially when we're in the changing room, who have bigger boobs than me."
        pov "And..."
        show c3 boys 12
        with pixellate
        pov "I was wondering if mine are big enough?"
        c "W-what?!"
        j "?!"
        pov "Even if I ask the other girls there, they're girls, after all, so it's hard to trust their opinion..."
        pov "I want to hear it from a male's perspective instead."
        pov "And I thought that maybe you two can give me your opinions, since I know you guys are honest with me."
        show c3 boys 13
        with dissolve
        pov "...... What do you think?"
        bo "?!"
        bo "......"
        pov "{i}(I've teased them quite a bit already, but this is the first time they're getting a direct look.){/i}"
        pov "{i}(I hope this isn't going too far...){/i}"
        show c3 boys 14
        with dissolve
        c "Uhh..."
        c "W-well, they're pretty big, I-I would say."
        j "Yeah... uh, I mean, they're not the biggest in the world or anything, but..."
        j "It's not like they're lacking at all."
        j "......."
        j "Most guys would be pretty satisfied, I guess..."
        c "Y-Yeah... there's nothing to worry about there."
        c "They look fine to me..."
        show c3 boys 15
        with dissolve
        pov "{i}(Alright, I probably shouldn't put them on the spot much longer...){/i}"
        pov "{i}(And the longer this goes on, the more embarrassed I'll feel.){/i}"
        pov "Thanks."
        pov "That makes me feel a lot more comfortable about it."
        pov "I've never asked a guy what they think before, after all..."
        pov "Well..."
        show c3 boys 17
        with dissolve
        pov "That's about all I wanted to ask."
        pov "Sorry for asking you a question like that and undressing all of a sudden."
        pov "...... You don't think I'm a pervert or anything now, {i}right{/i}?"
        bo "N-no!"
        show c3 boys 16
        with dissolve
        j "It's fine... I mean, I was surprised, don't get me wrong..."
        j "But I guess since we're friends it's not that weird."
        c "Yeah. I wouldn't want you asking a random guy for their opinion instead..."
        c "They might try to take advantage of you or something..."
        show c3 boys 17
        with dissolve
        pov "That's true. I guess I made the right decision after all."
        pov "I suppose it was the first time you two have seen boobs this close, huh?"
        pov "Must be different from all that porn you guys watch? {i}*laughs*{/i}"
        c "S-shut up!"
        j "Yeah, porn is irrelevant..."
        j "And it's not like we're looking at you that way or anything..."
        show c3 boys 18
        with dissolve
        pov "{i}(Somehow I doubt that...){/i}"
        pov "{i}(Well, at any rate...){/i}"
        pov "{i}(That was pretty fun.){/i}"
        pov "{i}(I'll admit I'm a bit worried that things will be awkward now, though...){/i}"
        stop music fadeout 2.0
        pov "{i}(I guess an easy way to fix that would be to hang out a bit longer, and try to change the atmosphere.){/i}"
        pov "{i}(At least then we can kinda move on from what just occured.){/i}"
        pov "{i}(Guess we can play a different game for now.){/i}"
        "......"
        $sexe +=1
        $c3boytease = True
        jump c3pool
    else:
        jump c3boysafter

    label c3boysafter:
    play music "audio/friends.ogg" fadein 3.0 loop
    show c3 boys 19
    with fadeholdlong
    pov "Alright, I'm getting kind of bored of games now..."
    pov "And it's already been a few hours since we ate, so I'm kinda in the mood for a quick snack..."
    pov "Do you want to head upstairs and grab something eat?"
    pov "I'm not sure if there's much here that you guys might like, but there's probably something you'll at least find edible."
    show c3 boys 20
    with dissolve
    c "Sure, that's fine with me."
    j "Yeah. I guess we still have an hour or so before we need to start worrying about the last train."
    j "I was thinking of picking something up on the way home, so that works for me."
    c "Same here."
    pov "Alright, cool!"
    "......."
    show c3 boys 21
    with fadehold
    pov "Hmm... I guess it cost about $3000 overall, maybe?"
    pov "I saved up for it and all the monitors and everything, with the allowance I got each month."
    j "Holy..."
    j "Talk about being rich."
    j "I wish I had the money for an expensive gaming PC like you have, [pov]..."
    c "Yeah. I'm already up to my neck with paying for tuition."
    c "If I can even get {i}one{/i} new game every couple months or so, I'm a happy man."
    show c3 boys 22
    with dissolve
    pov "Well, it's not like money is the only important thing in the world..."
    pov "For example, if I ever found a boyfriend or something, I wouldn't care all that much about money."
    pov "As long as we can pay the bills, and we love each other, that'd be enough for me."
    c "Easy to say when you've never been poor before..."
    c "Well, whatever..."
    c "Now that you got me thinking of tuition, I remember you said your friend was going to the same uni as me?"
    c "[fr], was it?"
    show c3 boys 23
    with dissolve
    pov "Yeah. You should be in the same year this fall, since you both started at the same time."
    pov "I doubt you're in the same classes, though, since she's training for nursing and you're doing your own thing."
    pov "But I'm sure you've walked past each other a few times without knowing it."
    c "Haha, maybe."
    pov "One day I guess I could try inviting her, and all four of us could hang out together."
    pov "I'm a bit worried you guys will weird her out, though, since you make perverted jokes and talk about nerdy stuff all the time..."
    show c3 boys 24
    with dissolve
    j "Hey, we're not that weird..."
    j "And you're probably the most perverted out of all of us."
    c "Yeah. [pov]'s the one with the porn game hobby."
    show c3 boys 22
    with dissolve
    pov "Well, I can't deny the hobby part..."
    pov "But you two are also watching hentai and all sorts of other stuff, so it's not like you're any less weird than I am."
    pov "Every time I disappear for a second, I come back and hear you two talking about some girl or video."
    pov "Or you're showing each other perverted pictures on your phone..."
    pov "And then you put it away and act all flustered the instant you notice me."
    show c3 boys 24
    with dissolve
    c "Maybe it's just your imagination?"
    j "Yup. Can't say I've ever done anything like that."
    pov "You two..."
    show c3 boys 25
    with dissolve
    j "Haha. Just playing the trick you always do, [pov]."
    j "Anyway, we should probably start heading out soon."
    c "Oh yeah. If I don't leave in the next fifteen minutes or so, I'm kinda screwed."
    pov "Crap, it's that late already?"
    pov "That's scary. I completely lost track of time..."
    stop music fadeout 2.0
    pov "I don't want you guys to miss the train and have to stay here overnight, so I should let you two get going."
    pov "I guess we'll continue watching that show in a couple days or so?"
    j "Sure."
    c "Yup. I'm down for that."
    "......"
    $c3nopool = True
    jump c3end

    label c3pool:
    play music "audio/blues.ogg" fadein 4.0 loop
    show c3 pool 1
    with fadeholdlong
    pov "Well, home alone again..."
    pov "I'm getting a bit tired now."
    pov "They went back home since it's almost 11 PM, and the last train is coming up."
    pov "Worst case scenario, if they missed the train they could always just stay here for the night."
    pov "But that would inconvenience them since I don't have spare clothes and toothbrushes and such."
    pov "And we've already spent the entire day together now."
    show c3 pool 2
    with dissolve
    pov "Hmm... eight hours, I guess? Josh came by in the afternoon, and Connor a bit later."
    pov "That's about my limit before I start needing some time to myself."
    pov "But I'm not quite ready to hit the sack just yet."
    pov "And what I did earlier with those two, is still stuck in my head..."
    "......"
    show c3 pool 3
    with fadehold
    pov "Alright..."
    pov "Time to relax and have a breather first before I go to bed."
    pov "There's no work tomorrow, so it's not a big deal if I stay up a bit late tonight."
    pov "Usually I go to bed around 11 PM, but on free days I might go as late as 1 or 2 AM. Sometimes even later if there's a game or drama that I can't put down."
    pov "......."
    show c3 pool 4
    with dissolve
    pov "Ah, that feels nice..."
    pov "I was thinking of trying something a little different this time, in the pool..."
    pov "Rather than finding my swimsuit, I wanted to try going in nude one time."
    pov "It's on our private property, and I doubt anyone else is around this late at night, so it's not that big of a deal."
    pov "The chances of {i}him{/i} peeping again are pretty low."
    pov "That is, unless he is actively waiting for me..."
    pov "Which would be kind of creepy..."
    "......"
    show c3 pool 5
    with dissolvelong
    "15 minutes later."
    pov "Is he not coming, after all?"
    pov "Jeez, I got worried for nothing..."
    pov "Hmm..."
    pov "It feels nice being nude like this, but without anybody around... something feels lacking."
    pov "It doesn't feel any different from when I shower, for example."
    pov "...... This is a bit desperate... but..."
    pov "I guess I could try making a bit of noise to see if he shows up at all."
    pov "If he doesn't, I'm just gonna give up and go watch something before bed."
    "......"
    show c3 pool 6
    with dissolve
    pov "{size=+5}Ahh, this feels so nice!{/size}"
    pov "{size=+5}And there's nobody around to see me naked like this.{/size}"
    pov "{size=+5}The breeze on my nipples kind of tingles...{/size}"
    pov "{size=+5}I sure hope nobody outside sees me...{/size}"
    "......"
    show c3 pool 7
    with dissolvelong
    "5 minutes later."
    pov "He's here!!"
    pov "He must have heard me from somewhere in his house."
    pov "Which means... he's one of our neighbours, after all."
    pov "I thought that was the case, but didn't know for sure since we moved to this house recently."
    pov "Plus, we've never been the type to talk a ton to our neighbours and get all friendly with them."
    show c3 pool 8
    with dissolve
    pov "Well... I guess this means we've introduced ourselves... sorta?"
    pov "I don't think that's how it works..."
    pov "Well, whatever..."
    if c2poolex >=1:
        pov "He's lucky this time since he has something else to look at."
        pov "Instead of just my boobs, he gets the whole picture."
    else:
        pov "I feel kinda bad about not showing him last time, so this should make up for it."
        pov "I'm letting him see every part of me."
    pov "This is kind of exciting..."
    pov "Though I'm starting to get worried about my skin getting wrinkly, since it's been about a half hour now..."
    pov "I'll stand up and give him one good look before I head back indoors."
    show c3 pool 9
    with dissolve
    pov "Alright..."
    pov "He should be able to see everything with this."
    pov "Including {i}there{/i}..."
    pov "Well, I guess it might be a bit hard to see super well when I'm standing up or sitting down."
    pov "But I'm not exactly going to start spreading my legs or anything like that..."
    pov "Nah... for this perverted neighbour of mine, I've already given plenty of eye-candy for now."
    show c3 pool 10
    with dissolve
    pov "I should probably head back inside now and dry myself off."
    stop music fadeout 2.0
    pov "Maybe I'll study some Japanese before going to bed?"
    pov "...... Nah."
    pov "I know what I should do instead..."
    "......"
    $c3pool = True
    $ renpy.end_replay()
    jump c3end

    label c3end:
    play music "audio/cloudy.mp3" fadein 0.5 loop
    show c3 end 1
    with fadeholdlong
    "A couple days later."
    pov "It's been a while since I've been to a public swimming pool."
    if c3pool:
        pov "Usually I just hang out in our own pool, like I did the day before yesterday."
    else:
        pov "Usually I just hang out in our own pool, since it's right outside, and I don't have to worry about anyone else."
    pov "I'm kind of lazy like that, and don't like going out much more than I need to..."
    show c3 end 2
    with dissolve
    pov "But it gets boring after a while, being at home and doing the same old things."
    pov "Plus, there isn't nearly as much room to swim and exercise compared to a place like this."
    if c3pool:
        pov "And with nobody else there, it can get a bit lonely..."
        pov "Well, aside from that new 'friend' of mine..."
        pov "......"
    pov "That's why I thought it was about time to try going out somewhere like this instead."
    pov "It's a good way to pass a couple hours or so by myself."
    pov "And it gives me a good opportunity to wear something lewd like this..."
    show c3 end 3
    with dissolve
    pov "A string bikini might be a bit much for a swimming pool, but it's not like I'll get in any trouble for it, either."
    pov "I'll probably just get a couple raised eyebrows at most."
    pov "...... Well, if I {i}was{/i} wearing anything less, I'd for sure get kicked out..."
    pov "This is already just barely safe."
    show c3 end 4
    with dissolve
    pov "Anyway..."
    pov "Though nothing too unusual has really happened recently, I've been having a lot of fun, and I'm really glad I got to hang out with [fr] finally."
    pov "We get along even better than I thought, the two of us..."
    pov "I thought I'd only really be able to open up and be myself around guy friends, but I was just as open with [fr] as I am with those two."
    pov "I guess that's natural since we're both girls."
    pov "It could also be us maturing and getting older, too, since she was a little bit more shy back in middle school."
    pov "And she {i}has{/i} gotten more used to western culture, since she's been living here for the past year."
    show c3 end 5
    with dissolve
    pov "Well..."
    pov "I'm glad she lives here now. And I want to hang out with her more often."
    pov "Rather than once every few months, once a week or so would be nice."
    pov "And I could maybe invite her and the boys, and hang out as a group some time."
    pov "If not, just the two of us is plenty fun, too."
    pov "Anyway..."
    pov "I think I've had my fill of pools for a while. I should probably start getting dressed."
    "......"
    show c3 end 6
    with fadeholdlong
    pov "Hmm..."
    pov "You know, thinking about it..."
    pov "Maybe I should really take [vio] up on that offer of hers."
    pov "I didn't think too much about it at first since I was still getting used to modelling, but..."
    pov "Lately, I've had a lot of free time... too much, probably."
    pov "It's still hard to find things to fill my time with."
    show c3 end 7
    with dissolve
    pov "A lot of the time I'm still at home, playing games and looking at perverted things or whatever..."
    pov "So, a second job is probably something I should seriously think about doing."
    pov "I wonder if that position is still available?"
    pov "It's been a week or two since we last met and she told me about the job, so it could go either way."
    pov "But if they're that desperate for new workers, I think it's quite unlikely that they'd already be full after such a short period of time."
    show c3 end 8
    with dissolve
    pov "On the flip side, of course, the longer I wait, the more real the possibility that they {i}are{/i} full becomes..."
    pov "I should ask her about it, after all."
    pov "Maybe I'll be able to start working in the next couple weeks or so, if it's still available?"
    pov "Let's drop a quick message after I finish getting dressed..."
    pov "......"
    show c3 end 9
    with dissolve
    pov "Hmm..."
    pov "I might just be overthinking it, but I feel like that woman over there is staring at me..."
    pov "Maybe she's just zoning out like I was?"
    pov "Or maybe she just likes to compare herself to other women... or something like that."
    pov "......"
    show c3 end 10
    with dissolve
    pov "She's definitely focused on me now..."
    pov "We're the only ones in this part of the locker room, so I don't think she would stare without reason."
    pov "Clearly she must understand what that implies..."
    show c3 end 11
    with dissolve
    pov "So, it {i}could{/i} be that she's interested in me, and she's trying to communicate that..."
    pov "I mean, it's not like every girl is completely straight."
    if c2_end2>=1:
        pov "I had that weird dream a few days ago, too."
    if les>=1:
        pov "I like guys, of course, but it's not like I haven't ever thought about a girl before."
    pov "Well, either way..."
    pov "I need to message [vio], so I should hurry up and get dressed."
    $ renpy.end_replay()
    show white
    with dissolve
    "[pov]..."
    menu:
        "...... enjoyed the female attention. [gr]\[Lesbian +1\]":
            "Although [pov] had never much concerned herself with the gazes of other women, she felt a strange, exciting sensation— one that was fresh and new to her."
            "......"
            $les+=1
        "...... didn't really enjoy being stared at.":
            "While [pov] thought it flattering that another woman may be flirting with her, it did not appeal to her at the moment, for her mind was preoccupied with other matters."
            "......"
            $het+=1

    hide white
    show c3 viodate 1
    with fadeholdlong
    "Meanwhile..."
    play sound "audio/effects/phone1.wav"
    "{i}*beep*{/i}"
    ni "Hmm?"
    vio "Oh, it's just a text. No big deal. I'll look at it later."
    show c3 viodate 2
    with dissolve
    vio "So, anyway, your university convocation... how did that go?"
    vio "Sorry I didn't make it. But I was busy with work, and, well, you know I don't enjoy events like that too much..."
    ni "Haha, no worries. I never expected you'd come."
    show c3 viodate 4
    with dissolve
    ni "It went... fine? I mean, it was just a bunch of parents and old people watching us pick up our diplomas."
    ni "It did feel nice to finally have all my schooling done, though."
    ni "I enjoyed all the parties and everything, but uni seriously started to wear on me after the first two years."
    ni "Business and economics classes are anything but fun."
    ni "I almost regret not doing some sort of liberal arts major and slacking the whole way through."
    show c3 viodate 2
    with dissolve
    vio "What are you talking about? You {i}did{/i} slack through most of it..."
    vio "Hell, you even took an extra year to graduate when most of your friends only took 4 years."
    show c3 viodate 4
    with dissolve
    ni "Haha. True, true."
    ni "There was no way I was going to survive that shit without cutting back on my credits."
    show c3 viodate 3
    with dissolve
    vio "Well, either way, at least now you're finally done, and can focus on your new job this summer."
    vio "A bank accountant, was it?"
    vio "Can't imagine you'll have much money trouble with a job like that."
    show c3 viodate 2
    with dissolve
    ni "Yeah. Well, I wouldn't have gotten the job if it wasn't for my uncle recommending me."
    ni "I'm good, but not {i}that{/i} good."
    vio "I see..."
    vio "But, I suppose this means tonight's bill will be on {i}you{/i}, then?"
    ni "Woah... straight for the jugular, huh."
    ni "No worries. A restaurant tab is no big deal for me. {i}*laughs*{/i}"
    ni "...... Now that I think of it, people working at restaurants don't make a whole lot, huh..."
    show c3 viodate 3
    with dissolve
    vio "Hey! First of all, it's a cafe that I work at, not a restaurant..."
    vio "And we can get pretty hefty tips, y'know."
    vio "I wouldn't understate how much I'm making if I were you."
    vio "Unless you want to make up for my allegedly 'petty' income, by paying for all our rent from now on, {i}too{/i}?"
    ni "Woah, woah. No, I'm good there."
    ni "Sorry. Please don't kill me."
    ev "{i}*laughs*{/i}"
    show c3 viodate 5
    with dissolve
    vio "...... Anyway, this is a bit of a topic change..."
    ni "Oh?"
    vio "I'm not sure we should continue fooling around outside, like those last two times."
    vio "I get that you have your kinks, and I've tried my best to live up to them since I want to be a good girlfriend."
    vio "But I'm just not {i}that{/i} kind of girl."
    ni "So, you're not a slut, is what you mean?"
    vio "Well, yeah... if you want to phrase it in a crass way like that."
    ni "I'm just joking. But you did seem pretty into it the last time we did it, no?"
    show c3 viodate 7
    with dissolve
    vio "Oh my god..."
    vio "You know, a girl is obviously going to get aroused when they're in the middle of having sex."
    vio "We're dating, so it's not like you were forcing yourself on me or anything."
    vio "But it was pretty damn obvious that I wasn't too keen on the idea."
    vio "And I'm pretty sure you remember me being in a bad mood after we finished up."
    ni "Yeah... you didn't say a whole lot on the way back."
    show c3 viodate 6
    with dissolve
    vio "Plus, I'm a bit frustrated with myself, too, since I let myself get carried away at the end."
    vio "Ever since I started taking the pill, I've stopped caring about risks as much."
    vio "Even if there's only a 1 percent chance, I don't want to risk getting pregnant, after all. We haven't been going out {i}that{/i} long yet."
    show c3 viodate 8
    with dissolve
    ni "That's true."
    ni "...... I probably should have thought things through a bit more."
    ni "I mean, it was fun in the moment, but I shouldn't have focused only on what I wanted."
    ni "Sorry about that."
    show c3 viodate 6
    with dissolve
    vio "No, it's fine... I mean, I {i}did{/i} enjoy it."
    vio "But we should keep it to the bedroom for the time being."
    vio "If I'm in a good mood and feel like giving you a treat, I'll listen to your kinks and demands again."
    vio "A sort of present, let's say?"
    show c3 viodate 8
    with dissolve
    ni "Gotcha."
    ni "....... Hmm."
    ni "About that..."
    ni "Are there any sort of limits to these requests?"
    ni "Y'know, things that are too extreme for you, or that you just wouldn't feel comfortable doing?"
    vio "......"

    menu:
        "'I guess I'm pretty open-minded.' [gr]\[Vioc\]":
            show c3 viodate 5
            with dissolve
            vio "Well... I can't say I'd be willing to do {i}absolutely{/i} anything."
            vio "But I'm open-minded."
            vio "As long as it's not harming anyone, and it's not {i}completely{/i} out there, I can at least consider it."
            vio "And since we're a couple, I think it's important to compromise and to try and make your partner happy."
            ni "I see. I'm happy you feel that way."
            $vioc +=1
        "'I don't want to do anything out of the norm.' [gr]\[Viop\]":
            show c3 viodate 5
            with dissolve
            vio "Well... I'm not really interested in doing anything too weird or unusual."
            vio "I don't have any sort of kinks like that myself."
            vio "I just enjoy things the normal way, for the most part."
            vio "Sorry if that's disappointing... but I don't really want to force myself to do something I don't like."
            ni "No, no worries. I understand."
            $viop =+1
    show c3 viodate 1
    with dissolve
    ni "Well, anyway..."
    ni "That's probably enough sex talk for now."
    ni "It's been about 10 or 15 minutes now, so the food should be here any second."
    ni "After we finish eating, what d'ya say we head back home and watch a movie or something together?"
    show c3 viodate 2
    with dissolve
    vio "Sure. It's been a while since we've done that."
    stop music fadeout 2.0
    ni "How about an action flick, then? That's your favourite genre, isn't it?"
    vio "OK. Sounds like a date to me, then."
    "......"
    label galleryScene9:
    play music "audio/blues.ogg" fadein 4.0 loop
    show c3 viosex 1
    with fadeholdlong
    "And so, [vio]'s and Nick's promise of keeping it to the bedroom was fulfilled that night..."
    "......"
    vio "Ah..."
    vio "It's so much better like this, Nick..."
    vio "Nobody except us is looking..."
    vio "Ah—!"
    show c3 viosex 2
    with dissolvelong
    ni "Whatever you want, babe..."
    ni "We can go all-out here, at home."
    ni "No need to worry about noise."
    vio "Oh—!"
    vio "It's so deep..."
    show c3 viosex 3
    with dissolvelong
    vio "You're so big, Nick."
    ni "You like big cocks, don't you?"
    vio "Yes... yes, I do."
    vio "Your size is perfect..."
    show c3 viosex 4
    with dissolvelong
    ni "And your pussy is perfect."
    ni "Much tighter than anyone else I've been with."
    ni "We make a good match, huh."
    ni "......"
    ni "...... I can't hold back much longer, [vio]."
    ni "You feel too good for me to stop..."
    ni "Where do you want it...?"
    vio "Ahh! On my body, please... cover me."
    vio "Please..."
    show c3 viosex 5
    with dissolvelong
    with vpunch
    ni "Shit... I'm cumming."
    vio "Oh——!"
    vio "Yes!"
    vio "Please cum on me!"
    show c3 viosex 6
    with dissolvelong
    with vpunch
    vio "There's so much..."
    ni "Holy shit..."
    ni "Haven't came this hard in a while..."
    ni "Fuck..."
    "......"

    show c3 viosexafter 1
    with fadeholdlong
    vio "{i}*panting*{/i}"
    ni "All cleaned up now, I think..."
    vio "Nick, that was amazing..."
    vio "What's gotten into you tonight?"
    show c3 viosexafter 3
    with dissolve
    ni "Nothing much, really..."
    ni "I've just been thinking about all the stuff we've done recently, and it got me in the mood."
    if vioc >=1:
        ni "And hearing that you would be willing to keep trying new things with me got me kinda excited."
    ni "Plus, I figured we could do it without holding back this time. We have to limit ourselves when we do it outside, after all."
    ni "Vanilla sex has its own perks, you could say?"
    show c3 viosexafter 2
    with dissolve
    vio "I see..."
    vio "It was nice doing it the usual way for once."
    vio "I guess we should try to have sex a bit more often."
    vio "Since our schedules haven't been matching too well, we've only been doing it once or twice a week."
    vio "The only time we even get a chance is during your lunch break at work, or before my evening shift starts."
    vio "That's why I've said yes to your outdoors fetish, since we wouldn't be able to do it otherwise..."
    vio "Hmm..."
    vio "Should I try changing my work schedule a bit?"
    show c3 viosexafter 4
    with dissolve
    ni "Nah... I mean, whatever you feel like doing is fine with me."
    ni "If the time ever comes, I'm capable of paying for all our bills with my income alone, but I know you aren't the type to be satisfied sitting at home all the time."
    ni "You'd probably throw a fit and kill me one day."
    show c3 viosexafter 2
    with dissolve
    vio "Well... it {i}is{/i} kind of hard to imagine myself not working."
    vio "But I guess even if I can't change my shifts around, we do still have the nights together."
    vio "Although you're always tired, and are already snoring half the time I come home..."
    vio "If you made more of an effort, we could do it at home like this more often..."
    show c3 viosexafter 4
    with dissolve
    ni "Haha. What can I say, work tires me out."
    ni "And I have to wake up early in the mornings."
    ni "6 AM can be pretty brutal if you aren't in bed on time."
    show c3 viosexafter 5
    with dissolve
    vio "It's fine. No worries."
    vio "Hmm..."
    vio "It's still not {i}that{/i} late..."
    stop music fadeout 2.0
    vio "And tomorrow is Sunday..."
    vio "...... Do you want to go for a second round?"
    $ renpy.end_replay()
    hide c3 viosexafter 5
    with dissolve
    show intro bg 1
    "......"
    "{b}Chapter 3: Complete{/b}"
    ####################### END OF CHAPTER 3####################################

    ####################### CHAPTER 4 ##########################################
    $ chaptercount +=1
    play music "audio/cloudy.mp3" fadein 0.5 loop
    show c4 title
    with fadeholdlong
    "A few days later."
    pov "Aww, man..."
    pov "The game just crashed on me again."
    pov "This keeps happening for some reason."
    show c4 intro 1
    with dissolvelong
    pov "I guess it's because the game just came out today, and they haven't patched it for bugs yet."
    pov "Maybe it's time to just play something else instead, since I've already been at this game for a few hours now."
    pov "Hmm... that reminds me."
    show c4 intro 2
    with dissolve
    pov "It's already pretty late, isn't it?"
    pov "I wonder what time it is."
    pov "Oh... it's still only 10 PM."
    pov "I guess I can continue playing for a little while longer."
    pov "It's not as though I have to wake up super early for the interview tomorrow."
    "......"
    show c4 intro 3
    with dissolvelong
    pov "Alright, I think I've had my fill for tonight..."
    pov "It's hard to focus on the game since it's almost time for bed, and I have to head over there tomorrow."
    pov "I know it was late in the afternoon, but I can't remember what the address was..."
    show c4 intro 4
    with dissolve
    pov "I guess I'll check my email quickly before I go to bed."
    pov "After [vio] saw my message about taking up the job, she said she'd tell her manager about it."
    pov "And sure enough, the next day, she replied with a time and a place."
    stop music fadeout 3.5
    pov "My memory isn't the greatest, though, so I forwarded it to my email so that I wouldn't lose it by accident."
    pov "Let's see..."
    pov "Where was it, again?"
    "......"

    play music "audio/funktastic.mp3" fadein 3.0 loop
    show c4 cafe 1-1
    with fadeholdlong
    "The next day."
    vio "Oh, you made it!"
    vio "Over here!"
    pov "Heya. Been a while since we've seen each other in person, huh?"
    vio "Yeah. I guess we've both been busy with our jobs and what not."
    vio "But now I guess we'll be sharing the same job, won't we?"
    pov "{i}*laughs*{/i} That's true."
    vio "Anyway, I'm not quite done my shift just yet since a few customers came in last second."
    vio "So while I can't quite be there with you for the interview, I can at least disappear for a couple minutes."
    show c4 cafe 1-2
    with dissolve
    vio "I'll show you to the office, where our manager should be."
    vio "Well... emphasis on {i}'should be'{/i}. He's one of those types that shows up whenever he feels like."
    pov "{i}*chuckles*{/i} I see."
    vio "Alright, let me take this one order quickly, and then I'll walk you over."
    show c4 cafe 1-3
    with fadeholdlong
    vio "So this is our secret little office, you could say."
    vio "It's also our break area, so if you decide to stay with us, you'll no doubt be in here a lot."
    vio "We don't have a locker room or anything, sadly, so you have to {i}make sure{/i} to lock the door if you're changing into your uniform."
    show c4 cafe 1-4
    with dissolve
    vio "Most of us are girls, but the manager... well, he's a guy, and a younger one at that, so you don't want to be caught half-naked by accident."
    vio "Anyway, I'll let our manager lead you through the other details. He should be here soon."
    vio "No need to be nervous or anything. I vouched for you earlier, and he's not at all the serious type, either."
    show c4 cafe 1-3
    with dissolve
    pov "Alright. Thank you!"
    pov "You showing me where to go helps a lot."
    pov "I almost got lost with my other job, in fact..."
    show c4 cafe 1-4
    with dissolve
    vio "Haha. Somehow, I think I can picture that."
    vio "But yeah, let me know how it goes. I'll be done my shift in about thirty minutes or so, so we can chat more then."
    pov "Alright. See you soon!"
    show c4 cafe 1-5
    with dissolvelong
    pov "......"
    pov "{i}(Hmm...){/i}"
    pov "{i}(This office is definitely smaller than the photo agency I work at.){/i}"
    pov "{i}(Then again, there's dozens of people working there, whereas this store probably only has a handful or so employees.){/i}"
    pov "{i}(It seems pretty cozy, though.){/i}"
    "......"
    show c4 cafe 1-6
    with fadeholdlong
    man "Hey, sorry you had to wait."
    man "I got caught up with something else and was running a few minutes late."
    pov "No problem!"
    man "You can probably guess, since I'm sure [vio] already told you, but I'm the manager at this little cafe here."
    man "You're the one who was interested in potentially working here, right?"
    man "[pov], was it?"
    pov "Yes. That's me."
    man "Nice to meet you, [pov]. I'm Lucas."
    show c4 cafe 1-7
    with dissolve
    luc "I'm probably not that much older than you, so you can just be yourself and treat me like anyone else."
    luc "Everyone is pretty casual here. We just treat each other like friends or family."
    pov "Gotcha. Nice to meet you too, then, Lucas."
    luc "Hmm... that makes me wonder, though... how old are you?"
    show c4 cafe 1-10
    with dissolve
    pov "Well, I'm 18, but only for a few more days, since my 19th birthday is this weekend."
    luc "Oh, wow. Well then, it's a bit early, but happy birthday."
    pov "{i}*giggles*{/i} Thanks!"
    show c4 cafe 1-9
    with dissolve
    luc "So, that would still make me the oldest one here."
    luc "But [vio] is only a couple years older than you, and we actually have another new girl here who's even younger than you are."
    luc "You'll probably meet her soon since she's working most days."
    luc "In fact, she just finished her shift around the time you got here."
    pov "I see! I'll make sure to say hi when I see her, then."
    luc "The two of you will get along pretty well. You both give off this... I don't know, energetic, or cute vibe?"
    show c4 cafe 1-11
    with dissolve
    luc "Uhh... well, anyway..."
    luc "We're in a bit of a pinch, and I'm not really the type to do long interviews and whatever, so I'm thinking of skipping the usual stuff."
    luc "We can just get you started with a trial period right away, to see how things go."
    luc "[vio] already said good things about you, and you seem like a nice girl, so I can't see there being any issues."
    luc "What do you think?"
    pov "Sure. If that's what you think is best, I'd be more than happy to give it a try!"
    show c4 cafe 1-7
    with dissolve
    luc "Great. Happy to hear that."
    luc "So, I'll probably start you off with your first shift a couple days from now, if you're available then."
    luc "And if for whatever reason you don't feel like continuing, you'll still be paid fully for these two weeks, of course."
    show c4 cafe 1-8
    with dissolve
    luc "I usually just have people insert their work hours into the computer here, after they finish their shift."
    luc "I'll be making an account for you before you start, so that you can also log on and do your thing."
    luc "It can be a bit confusing at first... so, I'll ask [vio] or Luna to show you how to do it, after your first shift."
    show c4 cafe 1-10
    with dissolve
    pov "I see..."
    pov "I'm pretty good with computers, but I'd appreciate the help, so that I don't make any weird mistakes!"
    luc "Yup. There w—"
    show c4 cafe 1-12
    with pixellate
    play sound "audio/effects/door1.mp3"
    girl "Dang, I must have left it here..."
    girl "Lucas, have you seen my phone here, by any chance?"
    girl "I was on my way home, but noticed it wasn't in my pocket, so I had to rush back!"
    pov "......"
    girl "...... Hmm?"
    show c4 cafe 1-14
    with dissolve
    luc "Oh, this is a good opportunity to introduce the two of you."
    luc "Luna, this is [pov]."
    luc "She's interested in working here, so she'll probably be your new co-worker from now on."
    luc "I'm sure the two of you will get along well."
    luna "Oh, that's her! [vio] mentioned something about a new girl joining us."
    luna "Nice to meet ya, [pov]! I hope we can become good friends."
    pov "Same here! I'm glad we're able to meet each other so quickly."
    show c4 cafe 1-13
    with dissolve
    luna "Hehe. I'm actually still new here myself."
    luna "I only started working about a month ago. So, I guess that means we can both learn and make mistakes together."
    luc "Hey, now... I don't need {i}two{/i} people breaking everything here."
    ev "*{i}laughs{i}*"
    luc "But yeah, your phone is right on the table here, so all's good."
    show c4 cafe 1-15
    with dissolve
    luc "Hmm..."
    luc "Since me and [pov] have mostly wrapped things up for now, and you're on your way home, what do you say the two of you take some time to get to know each other?"
    luc "It would be sort of awkward if you both went home separately."
    luna "Sure. What do you think, [pov]?"
    pov "I'd be happy to! I haven't had a chance to relax for a while now."
    show c4 cafe 1-14
    with dissolve
    luna "Hmm... how about we go bowling, then?"
    luna "There's a place right around here that me and [vio] went to once before."
    pov "Sure! That sounds fun to me."
    luna "Speaking of which... she's almost done her shift, too, so maybe all three of us can go together?"
    luna "I'll try asking her once she's done, and see if she has any other plans."
    luc "...... Alright, I'll leave you girls to it then."
    stop music fadeout 3.0
    luc "Just let me know your phone number, [pov], so I can text you some more details tomorrow."
    pov "Sure. It's..."
    "......"

    play music "audio/absurd.mp3" fadein 2.0 loop
    show c4 bowling 1
    with fadeholdlong
    "A little while later."
    luna "Alright, watch this, [pov]!"
    luna "You and [vio] aren't going to stay ahead forever."
    luna "I'm still in this game!"
    show c4 bowling 2
    with dissolve
    luna "Oh god... you're kidding me!!"
    luna "Why do I always end up in the gutter?!"
    luna "Maybe I'm just too used to playing with bumpers, since that's how my family always has it set up."
    show c4 bowling 3
    with dissolve
    luna "I was going for the strike, but must have put too much power into it..."
    luna "Not only that, but it kinda hurt my hand a bit..."
    luna "I don't know how [vio] manages to get these strikes so effortlessly."
    show c4 bowling 4
    with dissolve
    pov "Haha. She's in a different league than us mortal humans, that's for sure."
    pov "This isn't the only time I've seen her like this."
    pov "She saved me one time from someone."
    pov "Actually, I'm not sure if she told you, but that's how me and her met in the first place."
    show c4 bowling 5
    luna "Wow... so, it's due to that brute's strength that we're hanging out like this, huh."
    luna "I can be thankful to her for that. We'd be in big trouble if we didn't have anyone else joining us at work..."
    luna "But... {i}*sigh*{/i}"
    luna "I guess there's no chance of me beating her score now."
    show c4 bowling 6
    with dissolve
    vio "What, you mean you thought you ever had a chance of winning in the first place?"
    vio "Don't get too ahead of yourself, Luna."
    vio "I still have a thing or two to show you yet."
    luna "Crap... speak of the devil."
    luna "I didn't notice you coming back from the bathroom."
    vio "Yeah, you've always had trouble paying attention to your surroundings."
    vio "Plus, with that pitiful score of yours right now, it's probably even harder than usual to focus."
    luna "Hey!!"
    show c4 bowling 7
    with dissolve
    vio "Haha. I'm just screwing around."
    vio "But yeah, I was thinking as I was walking past the concession area..."
    vio "I'm getting pretty hungry now. I haven't eaten since my break today."
    vio "How about we go get something to eat after we finish this game up?"
    luna "Sure, not a problem!"
    pov "Same here. All this moving around has gotten me hungry, too."
    pov "Where do you wanna go?"
    "......"
    show c4 fastfood 1
    with fadeholdlong
    "A few minutes later."
    luna "Oh, I guess I'll just get the same things I usually get here."
    luna "I'd recommend the frappuccino if you haven't tried it yet, [pov]."
    pov "Hmm..."
    pov "I'd like to try it, but unfortunately I'm on a diet right now due to my other job."
    pov "I guess I'll just get a burger and coffee for now."
    pov "Let's see..."
    show c4 fastfood 2
    with dissolvelong
    vio "Okay, that should be everything we ordered."
    vio "There's nothing missing, right?"
    pov "Yup. That's everything for me."
    luna "Same here."
    luna "...... Oh! My burger looks tasty!"
    luna "Well, as tasty as fast food can get."
    luna "Let's dig in!"
    pov "Yeah, I'm not sure how much longer I can wait without eating..."
    show c4 fastfood 3
    with dissolvelong
    vio "Well, that's all our trash thrown out, seeing as you two are too lazy to carry it yourselves."
    luna "Oh, whatever you say..."
    vio "Are you both full now, by the way?"
    vio "I could go for a second burger, but I don't know if my boyfriend will be awake or not when I get home."
    vio "Sometimes we have a snack before bed."
    show c4 fastfood 4
    with dissolve
    luna "I see..."
    luna "I forgot you had a boyfriend until now."
    luna "But I'm completely full. I had that frappuccino with my burger, after all."
    luna "There's no way I could fit a second burger in me..."
    show c4 fastfood 3
    with dissolve
    vio "Yeah, you're a tiny little one, aren't you."
    vio "Any time Lucas gets annoyed at work, you freeze up and look like you're about to die inside."
    show c4 fastfood 7
    with dissolve
    luna "Come on, you know he gets scary..."
    luna "Even if he just says a few words of criticism, I have no way of knowing if that's going to blow up into him shouting at me or not."
    luna "Not that it's his fault... I mean, it's his responsibility to make sure the place is operating properly."
    luna "And I {i}am{/i} new, too."
    luna "I just wish he wouldn't take it out on me as much."
    show c4 fastfood 5
    with dissolve
    pov "Hmm... I didn't know there was a strict side to him like that."
    pov "He seemed pretty friendly when we talked earlier."
    pov "And he was really casual with the whole thing, too, which I appreciated, since I'm not too great with pressure."
    pov "I guess that's the advantage of having a younger manager like that."
    show c4 fastfood 6
    with dissolve
    vio "Yeah, he's easy enough to get along with."
    vio "Assuming you don't end up like Ms. Luna over here, and drop coffee cups in the middle of your shift."
    vio "Hopefully you can teach her a thing or two yourself, [pov]."
    show c4 fastfood 7
    with dissolve
    luna "Hey! You don't need to treat me like a kid, you know."
    luna "You aren't {i}that{/i} much older than me!"
    show c4 fastfood 6
    with dissolve
    vio "True, but you were still in high school only a couple months ago, right?"
    vio "As far as I'm concerned, that still makes you a kid in my eyes."
    vio "At least [pov] has another year on you, and has been working longer than just a couple months."
    show c4 fastfood 5
    with dissolve
    pov "Well... about that..."
    pov "I actually only started working my other job recently."
    pov "Maybe a month or two ago now?"
    pov "Until then, I was just relaxing at home and thinking about what I wanted to do, since I didn't want to go to university immediately."
    pov "I needed a bit of a break from school, I guess you could say."
    show c4 fastfood 8
    with dissolve
    vio "Oh, that's understandable."
    vio "I never went to university myself, actually."
    vio "I just started working as soon as I finished high school, since I wanted to move out from my folks' place and be independent as soon as I could."
    vio "So I guess we're similar in some ways."
    show c4 fastfood 9
    with dissolve
    pov "Ah, gotcha."
    pov "You're probably right about that. I want to be independent, too, although I love my parents."
    show c4 fastfood 8
    with dissolve
    luna "Yeah, as you can see, [vio] doesn't care about much else besides work, unfortunately..."
    vio "Did you want me to embarass you with another round of bowling?"
    stop music fadeout 2.0
    luna "No, no! I'm good."
    luna "You've already shown enough of your demon side tonight."
    ev "{i}*laughs*{/i}"

    play music "audio/swing.mp3" fadein 2.0 loop
    show c4 pizza 1
    with fadeholdlong
    "A couple days later."
    pov "I wonder if everything will be alright at my new job?"
    pov "Lucas and Luna both seem pretty nice, so I guess I'm not worried about things in that regard."
    pov "And me and [vio] have known each other for a little while now, too... I guess a couple months?"
    pov "So maybe there's nothing to be nervous about working with them."
    pov "It's just that it's my first time serving customers, and I've never worked in a restaraunt or anything... so, it's all pretty much new to me."
    pov "But it seems like Lucas is pretty helpful towards new people. And Luna and [vio] would no doubt help me if there was some sort of problem."
    pov "I'm probably just overthinking things like usual..."
    show c4 pizza 2
    with dissolve
    pov "Anyway, they're starting me off with about two days a week, until I pass the trial period and get used to working there."
    pov "After that, it'll probably go up to about three days a week."
    pov "So, in other words, counting my modeling job, that means I'll have more work days than I have off days..."
    pov "Better to keep busy, though, I guess."
    pov "Especially with all this talk with people about university, it makes me feel kind of guilty when I'm not doing anything."
    show c4 pizza 3
    with dissolve
    pov "Hmm..."
    pov "Seeing as it's one of my days off today..."
    pov "I'd like to have fun and release some of this stress."
    pov "And there's a perfect way to do that..."
    pov "I bought some garter a few days back, just for this occasion."
    pov "It'll be nice to wear something sexy like that in front of someone else, rather than just being in front of my mirror."
    show c4 pizza 4
    with dissolve
    pov "Alright..."
    pov "It's roughly the same time as when I last called the pizza delivery."
    pov "If I call now, I wonder if the same boy will show up with my order?"
    pov "Or if not, and I wait an hour or so instead... I wonder if someone else will show up?"
    pov "There's a possibility that it could be a girl instead, too."
    pov "......"
    menu:
        "Order pizza now. [gr]\[Sexe +1\]":
            pov "If there's a chance that boy might show up again... I might as well give it a try now."
            pov "It's a shot in the dark, but hey, why not?"
            pov "I guess I'll get dressed once I'm done ordering on here."
            "......"
            show c4 pizza 5
            with fadeholdlong
            pov "{i}(I heard a car in the driveway a second ago, so it's probably them...){/i}"
            pov "{i}(I have to admit that I'm somewhat nervous, since this is obviously a little... umm, out of the ordinary.){/i}"
            pov "{i}(Normally you don't catch people half naked like this, and especially not wearing garter with it, too.){/i}"
            pov "{i}(But... more than being nervous... I'm excited.){/i}"
            pov "{i}(They should show up any second now.){/i}"
            show c4 pizza 6
            with dissolvelong
            pov "Hey there!"
            pov "Sorry for greeting you like this again..."
            pov "You seem to have a knack for catching me half-naked, it seems. {i}*giggles*{/i}"
            pov "{i}(It's the same boy as last time, after all.){/i}"
            pov "{i}(Talk about luck.){/i}"
            boy "Uhh... no, not a problem at all."
            boy "You might be right..."
            boy "......"
            show c4 pizza 7
            with pixellate
            pov "{i}(He's staring, so I guess it's time to play a little bit of a game.){/i}"
            pov "{i}(Rather than coming up with an excuse like last time, I'll try teasing him directly.){/i}"
            pov "Hey, this might be a bit strange to ask since we're strangers, and you're working and all, but..."
            pov "If it's not too much of a bother..."
            pov "I wanted to get someone's opinion, since I'm all at home by my lonesome here."
            show c4 pizza 8
            with dissolvelong
            pov "What do you think of the garter and underwear I'm wearing?"
            pov "Do they compliment my body well, you think?"
            pov "I was worried they might be a bit too tight on me, but I'm not sure..."
            if exh >=3:
                show c4 pizza 13
                with dissolve
                pov "See, sometimes they can squeeze on my butt a little."
                pov "I've also had my panties go inside my privates a bit, too."
                pov "It can be quite distracting, especially if I'm wearing them outside."
            boy "!!"
            boy "U-Umm... they look quite nice, miss."
            boy "I-I think they fit you quite well..."
            show c4 pizza 9
            with dissolvelong
            pov "Really? I'm glad to hear that."
            pov "It's hard to know for sure..."
            pov "I'm still only 18, so I haven't gotten used to lingerie like this yet."
            boy "I-I see..."
            pov "Hmm..."
            pov "I guess they fit me even better than I thought, considering your reaction."
            show c4 pizza 10
            with pixellate
            with Pause (1.0)
            pov "You've gotten quite big down here, haven't you?"
            pov "It's hard for boys to hide their thoughts, isn't it?"
            boy "W-What?!"
            boy "Sorry, I didn't mean to..."
            pov "{i}*giggles*{/i}"
            show c4 pizza 11
            with dissolve
            pov "No, no— it's okay. I'm the one who decided to answer the door dressed like this."
            pov "You're just reacting like boys normally do."
            pov "I mean, if your body didn't show any reaction... I might worry that this lingerie doesn't have enough of an impact."
            pov "If I didn't want people to enjoy the sight, I wouldn't have bought something so sexy, after all."
            pov "It's natural to be tempted by something like this."
            boy "I see... y-you might be right about that."
            show c4 pizza 12
            with dissolve
            pov "Anyway, I probably shouldn't take up too much more of your time."
            pov "The pizza will get cold at this rate, and I'm sure you have other deliveries you need to get around to."
            pov "Sorry for intruding on your schedule like that, but I hope it was at least a nice little surprise."
            pov "I'll give you a larger tip than usual, too, to make up for your lost time."
            stop music fadeout 2.0
            pov "Maybe we'll meet again one day?"
            boy "Thanks... and sure, I guess we might..."
            pov "{size=-5}{i}(I sure hope so.){/i}{/size}"
            "......"
            $sexe +=1
        "Wait a little while first. [gr]\[Les +1\] \[Sexe +1\]":
            pov "Nah... I'd rather have someone different come, if possible."
            pov "Not like waiting will guarantee anything, since I obviously don't know their shifts, but..."
            pov "It's at least worth a try."
            "......"
            show c4 pizza 5
            with fadeholdlong
            pov "{i}(I heard a car in the driveway a second ago, so it's probably them...){/i}"
            pov "{i}(I have to admit that I'm somewhat nervous, since this is obviously a little... umm, out of the ordinary.){/i}"
            pov "{i}(Normally you don't catch people half naked like this, and especially not wearing garter with it, too.){/i}"
            pov "{i}(But... more than being nervous... I'm excited.){/i}"
            pov "{i}(They should show up any second now.){/i}"
            show c4 pizza 6f
            with dissolvelong
            pov "Hey there!"
            ev "......"
            pov "{i}(It's a different person, after all...){/i}"
            pov "{i}(I guess my hunch was right.){/i}"
            pov "{i}(And it's a woman at that...){/i}"
            pov "{i}(This makes things a little different than I had originally envisioned.){/i}"
            pov "{i}(I guess I'll try to keep it as cool as I can.){/i}"
            pov "Sorry about being dressed like this... I thought I had a few more minutes to get dressed before the delivery came."
            wom "Err... no, it's okay..."
            show c4 pizza 7
            with dissolve
            pov "{i}(But just because it's a girl, doesn't mean I should stop here.){/i}"
            if les>=2:
                pov "{i}(This makes things a little different, too, and maybe even interesting in its own way.){/i}"
            pov "{i}(I'll try showing her a little bit, and see how she reacts.){/i}"
            pov "So, this is a little bit random... seeing as we're strangers, and you're working and all..."
            pov "But..."
            pov "I wanted to get another girl's advice on this."
            show c4 pizza 8
            with dissolve
            pov "I bought this lingerie, and wasn't sure if it fit me or not."
            pov "Sometimes the underwear I buy is a bit too tight on my body, and can be a bit uncomfortable or distracting."
            pov "I haven't had a chance to show anyone else, so I thought it'd be a good opportunity to ask what you think."
            pov "Surely you have some experience of your own, wearing something like this?"
            show c4 pizza 9f
            with dissolve
            wom "N-No... not especially..."
            pov "I see... I guess that makes two of us, then."
            pov "I'm still only 18, so I'm not used to buying mature lingerie like this yet."
            pov "Does it look fine to you?"
            wom "Umm... sure, I guess so..."
            wom "It fits as well as it should, I think..."
            show c4 pizza 12f
            with dissolve
            pov "{i}*giggles*{/i} Thanks! I'm glad to hear that."
            pov "Anyway, I don't want to take up too much more of your time, since the pizza might get cold, and you're still working."
            pov "I'm sure you have other deliveries you need to get around to."
            stop music fadeout 2.0
            pov "Sorry about that. I'll give you a larger tip than I usually do, to help make up for that."
            wom "Thanks... and no, not a problem."
            if les >=2:
                pov "{i}(Hmm... this isn't the first time, but being seen by another girl like this...){/i}"
                pov "{i}(It was kind of fun.){/i}"
                pov "{i}(I could get used to this.){/i}"
                pov "{i}(Especially teasing them directly once more...){/i}"
                "......"
                $les+=1
                $sexe+=1
                jump c4cafe2
            else:
                pov "{i}(Hmm...){/i}"
                pov "{i}(I'm not really used to being seen by other girls like this, but...){/i}"
                pov "{i}(I guess it wasn't so bad.){/i}"
                pov "{i}(If this ever happened again, maybe that could be interesting, too.){/i}"
                "......"
                $les+=1
                $sexe+=1
                jump c4cafe2

    label c4cafe2:
    show c4 cafe 2-1
    with fadeholdlong
    play music "audio/funktastic.mp3" fadein 3.0 loop
    "The next day."
    pov "Alright, looks like there's nobody else here."
    pov "That means I can lock the door and change into my uniform in peace."
    pov "Not that I'd mind if [vio] or Luna was in here, but I wouldn't want to be seen in my underwear by Lucas or some stranger."
    pov "Of course, in my {i}own{/i} time... sure. I don't mind one bit."
    show c4 cafe 2-2
    with dissolve
    pov "But this is work, and a new job at that, so I need to keep things professional here."
    pov "It would be super awkward since I'll be seeing everyone here several times each week."
    pov "Hmmm..."
    pov "I hope the uniform fits."
    pov "I did give my measurements like I did with the modelling job at first, but you never know."
    show c4 cafe 2-3
    with dissolvelong
    pov "Oh, it does fit nicely!"
    pov "I'm a bit worried about how much it emphasizes my breasts, though."
    pov "If one of the customers decides to start hitting on me, I have no doubt that it will distract me."
    pov "Well, whatever... I'm not the one who picks the uniforms."
    pov "I guess I should put my hair down, though."
    pov "I don't want my hair getting in the way while I work."
    show c4 cafe 2-4
    with dissolve
    pov "There we go."
    pov "All good now, I guess."
    pov "I'm still a little bit nervous, but Luna will be working with me today, apparently, and helping me along the way."
    pov "Plus, it's an evening shift, so it won't be as busy as a morning or afternoon shift."
    pov "Time to head down there and find Luna."
    "......"
    show c4 cafe 2-5
    with fadeholdlong
    luna "Oh, you showed up, [pov]!"
    luna "I was worried [vio] might have scared you away after that night..."
    show c4 cafe 2-6
    with dissolve
    pov "Haha, no, not at all! I enjoyed hanging out with you two."
    show c4 cafe 2-5
    with dissolve
    luna "Thanks. The feeling's mutual! It was nice to get to know you, too."
    luna "Anyway, don't worry too much about work today!"
    luna "I'll be teaching you everything I know, and I'll be dealing with all the complicated stuff for today."
    luna "For now, Lucas just wants you to learn how to take orders."
    show c4 cafe 2-6
    with dissolve
    pov "I see..."
    pov "That does relieve some of the pressure, then."
    pov "I was a bit nervous on the way to work, since I have no idea how to prepare all the different blends of coffee."
    pov "And I definitely don't know how to handle the cash register..."
    pov "But if today is mostly just taking orders..."
    pov "That should be pretty easy for me to get used to."
    show c4 cafe 2-7
    with dissolve
    luna "Yup! It's as simple as writing down what they say on a piece of paper."
    luna "Of course, there's a bit more to it than that... they might ask for something else, and you want to take their drink order before their food order."
    luna "If it's busy, we also bring the customers to a designated table, but..."
    luna "Most of the time, we just let them take a seat wherever they feel like."
    luna "We're almost never busy here, after all, so that's what makes sense."
    show c4 cafe 2-6
    with dissolve
    pov "I see. I think I get the jist of it!"
    luna "Awesome! Well then... I'll accompany you the first couple times, and then you can try taking an order by yourself and see how it goes."
    "......"
    show c4 cafe 2-8
    with fadeholdlong
    "One hour later."
    pov "Good evening!"
    pov "If you're all ready, may I take your order?"
    show c4 cafe 2-9
    with dissolve
    manl "Yeah, I think I'm good."
    manr "Same here."
    manr "I'll have a large hot chocolate for now."
    manl "As for me, I don't need any drinks. I'll just get a BLT sandwich."
    show c4 cafe 2-10
    with dissolve
    manl "Hmm..."
    manl "You know, you're pretty cute, huh."
    manl "If I knew a girl like you was working here, I'd have come a long time ago."
    show c4 cafe 2-11
    with dissolve
    pov "{i}*laughs*{/i}"
    pov "Thank you. Actually, I just started working here today."
    show c4 cafe 2-9
    with dissolve
    manr "Oh, it's your first shift?"
    manr "I'm flattered to be one of your first customers then."
    manl "Me too."
    manl "A sexy little girl like you must have a man or somethin' at home, don't ya?"
    show c4 cafe 2-11
    with dissolve
    pov "Haha... no, I'm single."
    pov "I still live with my parents, actually."
    show c4 cafe 2-10
    with dissolve
    manr "Woah, woah. Single, huh."
    manr "Maybe you could join us after this, then?"
    manl "Yeah, we could go to a bar and have some fun."
    manl "What d'ya say?"
    show c4 cafe 2-11
    with dissolve
    pov "{i}(This is kind of troublesome...){/i}"
    pov "{i}(They both look quite muscular, which means they're probably athletes of some sort, or maybe even part of the military...){/i}"
    pov "{i}(I have no experience with these sorts of guys, so I'm not sure what the best way to respond is.){/i}"
    pov "{i}(I mean, it feels nice to have guys interested in me, but they just aren't my type at all.){/i}"
    pov "{i}(Plus, I'm in the middle of my shift, so I can't exactly stay and chit chat forever.){/i}"
    pov "{i}(I'll just decline them in a roundabout way.){/i}"
    pov "Errr.... haha..."
    pov "I'm flattered to hear that..."
    pov "I'm not sure what time I'll be off, though, so I'll have to take you up on that offer some other time."
    show c4 cafe 2-8
    with dissolve
    men "Aww..."
    pov "...... So, anyway, what was your order, if you don't mind me asking again?"
    "......"
    show c4 cafe 2-12
    with fadeholdlong
    luna "Nice work today, [pov]!"
    luna "You handled this way better than I did when I first started. {i}*giggles*{/i}"
    luna "Well, that was only just last month, so I'm still new myself..."
    pov "Haha. That's hard to believe, considering how much you know, and how natural you seem here."
    pov "Thanks so much for how helpful you've been."
    pov "I'm really glad I can work with you."
    luna "Same here! I think we'll end up being good friends."
    stop music fadeout 3.0
    luna "You can head up and get dressed first if you want. I just need another minute to finish up cleaning here."
    pov "Sure. And thanks! I'll see you again soon, then."
    "......"

    show c4 outside 1
    with fadeholdlong
    play music "audio/chill2.mp3" fadein 0.5 loop
    "A little while later, on the way home..."
    pov "Hmm..."
    pov "I'm kind of tired now, after all that working."
    pov "It's dark outside, so I probably shouldn't hang out for too long, but I wonder if there's somewhere I can sit down for a minute?"
    pov "There's still plenty of time until the last train."
    pov "Plus, I kinda like the atmosphere of Vancouver at night."
    pov "Especially when it's quiet like it is now, with nobody else around."
    show c4 outside 2
    with dissolve
    pov "Maybe I'll just have a sit over here by the water?"
    pov "Hopefully it's not too dirty."
    show c4 outside 3
    with dissolvelong
    pov "......"
    pov "All in all, things went pretty well for my first shift."
    pov "Of course, there were a lot of things that I didn't understand, but Luna helped me out quite a bit."
    pov "And the customers seemed to like me, too."
    pov "I've always been good at smiling and what not, so I guess that's not too surprising."
    pov "I mean, I {i}am{/i} a model, after all..."
    pov "It'd be a shock if I didn't get along well with the customers."
    show c4 outside 4
    with dissolve
    pov "Of course, there were a few that took it a little bit too far..."
    pov "I enjoy the attention, and don't mind people flirting with me, as long as they're not too pushy."
    pov "There's a fine line between flattery and harassment, after all."
    pov "But if it's during work... I'm not sure what the best way to respond is."
    pov "I guess the customers' satisfaction is most important, so I could just keep going along with it for a little while."
    pov "And then if it drags on for too long, I can just find an excuse, like I did today."
    show c4 outside 5
    with dissolve
    "......"
    man "Damn, I'm beat after today..."
    man "Hmm...?"
    man "That girl over there looks kind of familiar."
    man "Wait... that's not [pov], is it?"
    show c4 outside 6
    with dissolve
    luc "Hey, [pov], funny catching you here."
    pov "Oh! Hi there, Lucas."
    luc "I guess we both have the same way home... this leads to the closest Skytrain station, after all."
    luc "I just finished in the office a few minutes back, actually."
    luc "Nothing's wrong, I hope?"
    pov "No, not at all! I'm just relaxing and enjoying the night atmosphere for a second."
    luc "Ah, cool."
    luc "I'm not in any rush myself, so do you wanna grab a seat by that bench over there for a bit?"
    pov "Sure."
    show c4 outside 7
    with dissolvelong
    luc "So I haven't gotten a chance to ask you, since we were doing separate things today..."
    luc "What do you think of the job so far?"
    luc "It sounded like you and Luna got along well, from what I could hear as I was walking by."
    luc "And you're already acquainted with [vio], so that should help take some of the pressure off."
    show c4 outside 9
    with dissolve
    pov "Yeah, it went pretty well today."
    pov "Luna helped me out quite a bit, so there weren't any issues or anything like that."
    pov "Plus, we're around the same age, so we're already able to talk like friends."
    pov "There's still a lot of things that I don't understand, though... but hopefully in a couple weeks I'll have most of it down."
    pov "Then I can be a proper part of the war effort. {i}*laughs*{/i}"
    show c4 outside 8
    with dissolve
    luc "Haha, well, good to hear you're enjoying yourself."
    luc "I try to help out as much as I can, but Luna and [vio] are the main ones handling customers."
    luc "With three of you... four, counting myself... we shouldn't have much trouble allocating shifts."
    luc "Of course, the more the better, but this at least meets the bare minimum."
    luc "As you can tell, we aren't that popular, so there aren't too many customers for you guys to deal with."
    pov "That's a shame, since it's such a nice place."
    show c4 outside 7
    with dissolve
    luc "I know, right? {i}*laughs*{/i}"
    luc "It's still a new shop, so I'm sure the word will get out sooner or later."
    luc "I'm just doing my best for now to keep it running, and with luck, make enough money to pay for my band expenses."
    pov "Wait... you're in a band?"
    pov "I didn't know that. But you do seem like the creative type, now that I think of it."
    show c4 outside 10
    with dissolve
    luc "Well, it's an obscure indie band, so we're a far cry from successful."
    luc "But yeah, it's my hobby and what I dedicate most of my time towards, when I'm not working here."
    luc "Maybe one day you can come to one of our shows or something."
    pov "Sure. That'd be cool!"
    pov "I might not seem like it, but I do like rock music quite a bit."
    pov "Well, I listen to pop music the most... K-Pop and J-Pop included... but I listen to plenty of other genres, too."
    luc "Nice. Guess we're both pretty big into music then, hey."
    show c4 outside 11
    with dissolve
    luc "But yeah, we should probably get going."
    luc "It's dark out, and we're both heading to the same place right now, so I'll help walk you back to the station."
    pov "Wow, you're a gentleman, huh? {i}*giggles*{/i}"
    stop music fadeout 2.0
    pov "I'll take you up on that offer. I appreciate it."
    pov "You never know what kind of weirdos can be outside at night, after all."
    luc "True that."
    "......"

    show c4 vcar 1
    with fadeholdlong
    play music "<from 3.5>audio/isolation.mp3" fadein 0.5 loop
    "The next day, in another part of town."
    vio "......."
    vio "Uhh..."
    vio "You said you got a new car, but I wasn't expecting something as expensive as this."
    vio "I'm not really sure how I should react."
    ni "Haha. I knew you'd be surprised when you saw it."
    ni "But don't worry. I got a nice loan worked out, so it's not like I blew all my savings or anything."
    ni "And now that I've started my new job, my salary is more than enough to take care of the monthly payments."
    show c4 vcar 2
    with dissolve
    ni "Besides, you always wanted something fancier than the shitmobile we used to use. You complained about it all the time."
    ni "Plus, with all the constant maintenance fees, it wasn't necessarily cheap, either."
    vio "That's true..."
    ni "And, honestly, if you ask me, there's no need to live all frugally when we're making well beyond our means."
    ni "We're young. We should live a little instead of focusing on shit like retirement already."
    show c4 vcar 3
    with dissolve
    vio "I mean, as long as you're actually able to afford the thing... I guess."
    vio "But I'll need some time to think about this some more."
    vio "I kinda wish you asked me about it first, but I can't control your spending since I'm not your wife or anything."
    ni "I did plan on asking you first, but that would have ruined the surprise."
    show c4 vcar 4
    with dissolve
    ni "Anyway, I'm sure you'll change your mind after we take the thing for a spin."
    ni "I've got a little surprise for you before the show tonight, so we should get a bite to eat before then."
    vio "I hope this surprise isn't anything weird again..."
    vio "But alright. I'm kinda tired after work today, even if it was a shorter shift than usual."
    vio "So I could use the change of pace."
    "......"
    show c4 vclub 1
    with fadeholdlong
    vio "Really? You brought me to a nightclub in the middle of the day?"
    vio "It's not that I have anything against it, but..."
    ni "Haha. Well, my friend is one of the bartenders here, and he managed to get us a table by ourselves before the place opens."
    ni "With nobody else here, and with the lights and music, I thought it'd be a cool way to spend an hour or two."
    ni "Plus, I knew you'd have mixed feelings about the car, so I wanted to make it up to you somehow."
    show c4 vclub 2
    with dissolve
    vio "Well... I do like the atmosphere of nightclubs."
    vio "And having a table all to yourself like this, with nobody else around, {i}is{/i} a pretty unique experience."
    vio "I guess you going out of your way to ask for a favour from your friend, for my sake, makes me kind of happy, too."
    vio "Not that it was necessary, but I still appreciate it."
    ni "Glad my choice was a hit, then."
    ni "...... Oh, our drinks are here."
    show c4 vclub 3
    with dissolve
    ni "I can't drink much since I still have to drive us to the concert soon, but it wouldn't be a club without at least one drink."
    vio "That's true..."
    ni "Drinks are free, by the way. My friend's giving us extra service."
    ni "Well, on the condition that {i}I{/i} pay for the meal whenever me and him hang out next."
    stop music fadeout 2.0
    vio "You sure like to pay for other people, huh..."
    vio "Alright. I'll also have this one glass before we go, then."
    "......"
    show c4 vrave 1
    with fadeholdlong
    play music "<from 4.0>audio/feelgood2.mp3" fadein 0.5 loop
    ni "So how are you liking this song?!"
    vio "What?!"
    vio "I can barely hear you with this DJ blaring!"
    vio "At least wait for the bassdrop to finish before you ask me something."
    show c4 vrave 2
    with dissolve
    ni "I'm asking what you think of the song."
    vio "Oh... it's pretty good, I guess."
    vio "I prefered the previous one, but all the tracks tonight have been solid."
    ni "Nice, nice."
    ni "Uh... this is kind of random, but, I have to go to the bathroom for a second. Do you want to come with me?"
    vio "Come with you?!"
    show c4 vrave 3
    with dissolve
    vio "{i}(Normally you'd think he meant to go to the bathroom entrance together, but...){/i}"
    vio "{i}(He's pretty drunk now, so it's obvious that his intentions are a bit different.){/i}"
    vio "{i}(And with these kinks of his...){/i}"
    vio "{i}(No doubt he's asking if I want to do something with him.){/i}"
    vio "{i}(Should I follow him?){/i}"
    vio "{i}(I feel like someone might try hitting on me if I don't.){/i}"
    menu galleryScene10:
        "Follow him.":
            vio "Fine... I'll come with you."
            vio "With that smirk on your face, I'd almost feel bad for you if I said no."
            vio "And you've been nice to me today, so I guess I can give you a treat in return."
            ni "Sweet! Come on, then."
            "......"
            show c4 vtoi 1
            with fadeholdlong
            "A few minutes later."
            "{i}*slurp*{/i}"
            voi "Do you like that?"
            voi "Yes... fuck, yes. Keep going."
            show c4 vtoi 2
            with dissolve
            with Pause(1.0)
            vio "Mmm..."
            vio "...... Mmmhh..."
            ni "Shit, I'm already completely hard."
            ni "How are you so good at this?"
            show c4 vtoi 3
            with dissolve
            with Pause (1.0)
            vio "Do you like it on the tip like this?"
            ni "Yeah... of course."
            ni "But I want you to put more in again, instead of teasing me..."
            ni "Your tongue is nice, but your mouth is even better."
            vio "Okay."
            show c4 vtoi 4
            with dissolve
            with Pause (1.0)
            vio "Mmm?"
            ni "Oh shit..."
            show c4 vtoi 3
            with dissolve
            ni "This feels too good."
            show c4 vtoi 4
            with dissolve
            ni "I can't hold back much longer..."
            ni "At this rate I'm going to cum."
            ni "...... Are you ready for me to put it in?"
            show c4 vtoi 3
            with dissolve
            vio "...... Alright, I'm ready if you are."
            vio "Put it in me."
            show c4 vtoi 5
            with dissolvelong
            with Pause (1.0)
            vio "Oh god!"
            vio "You're so deep inside me..."
            ni "Shit... you're this wet already?"
            ni "I've barely even touched you yet."
            ni "I'm not sure if it was the blowjob, or that we're in public, but..."
            ni "Maybe you have an affinity for both of these things."
            show c4 vtoi 6
            with dissolve
            ni "That makes us pretty similar then, huh?"
            vio "Ahh..."
            vio "But..."
            vio "We're in public, so I don't want to get caught..."
            vio "Can you slow down a bit?"
            vio "They'll hear us otherwise."
            show c4 vtoi 7
            with dissolve
            ni "Are you kidding me? If anyone came in here, they would've already heard us long ago."
            ni "Hell, with your moaning, they might even be able to hear you from outside the bathroom."
            vio "Ahh... but... but I can't help it..."
            vio "I feel like I'm going to cum soon."
            ni "Same here."
            vio "Not inside, though..."
            vio "And not on my face, since we're in public..."
            vio "Put me down. I'll swallow it for you."
            "......"
            show c4 vrave 9
            with fadeholdlong
            ni "Wow..."
            vio "......"
            show c4 vrave 10
            with dissolve
            vio "I get that you're happy and that you enjoyed yourself, but let's keep it to ourselves for now, alright?"
            ni "Haha, okay, okay, I understand. It'll be our secret then."
            ni "Hmm... this has gotten me thinking, though..."
            show c4 vrave 11
            with dissolve
            ni "If you're cumming {i}this{/i} hard just from me alone, you'd probably lose your mind if there was another person with us."
            $ renpy.end_replay()
        "Wait here. [gr]\[VioStranger\]":
            vio "Hmm..."
            vio "I'm not against it since you've been nice to me tonight, but..."
            vio "I'm kind of worried about you with all the alcohol you've been drinking."
            vio "You should check up on yourself for now. We can always do things tomorrow or the next day."
            ni "Aww... alright. I'll be back in a second."
            show c4 vrave 4
            with dissolvelong
            vio "{i}(Well, hopefully he doesn't need to throw up or anything.){/i}"
            vio "{i}(......){/i}"
            vio "{i}(It's kind of interesting watching all the people here dance and mingle with each other.){/i}"
            vio "{i}(This guy looks like he's alone. Maybe he's looking for his next prey to hit on?){/i}"
            vio "{i}(...... Shit. I just made eye contact.){/i}"
            show c4 vrave 5
            with dissolve
            man "Yo, hey there."
            man "What's a cute girl like you doing here by yourself?"
            vio "Well, I'm not exactly alone, see..."
            man "Oh, your girlfriend ran off? {i}*laughs*{/i}"
            man "All good. My friend just went to order more drinks, too."
            show c4 vrave 6
            with dissolve
            man "So what do you say we chat, or dance for the time being?"
            vio "{i}(He's clearly drunk... and he smells like it, too.){/i}"
            man "Maybe my friend can dance with your friend once they're both back."
            man "It'll be a nice little party... {i}*hic*{/i}"
            vio "I appreciate the offer, but I don't think you're aware of the full story here."
            show c4 vrave 7
            with dissolve
            man "No need to be shy, come on..."
            man "My friend is pretty easy to talk to. And I'd really like to get to know you better."
            vio "......"
            vio "{i}(If this was outside, I might just push him off me like I usually do, but...){/i}"
            vio "{i}(He's wasted, and it'd be really bad if I caused a scene here.){/i}"
            vio "{i}(And I guess just touching my leg isn't quite enough to justify self-defense.){/i}"
            show c4 vrave 8
            with dissolve
            vio "No, I'm fine. I think you should probably search for your friend."
            man "Huh? I-I guess so... {i}*hic*{/i}"
            man "I can't remember the last time I saw him."
            man "Alright. I'll be back in a sec once I find him, so we can continue then, err... sexy..."
            vio "......"
            show c4 vrave 9
            with dissolvelong
            ni "Hey, all good? Sorry for the wait."
            vio "Of course. As long as you're doing okay."
            vio "There was an interesting visitor a second ago, but they went off on another endless adventure."
            ni "Huh? I'm not sure what that means, but sounds like you had an interesting experience."
            vio "You could say that."
            show c4 vrave 10
            with dissolve
            ni "So, anyway..."
            ni "Since I had a moment to myself in the bathroom..."
            ni "I was thinking about the two of us, and a funny image came to mind."
            show c4 vrave 11
            with dissolve
            ni "With how horny you usually get when we have sex, you'd probably lose your mind if there was {i}another{/i} person with us."
            $c4viostranger = True
            $ renpy.end_replay()
    ni "Imagine if you brought over one of your female friends."
    ni "You'd probably lose your mind from all that sensation! Haha."
    ni "Or if I had one of {i}my{/i} friends with us..."
    ni "Actually, you might really be able to handle two at once, considering how skilled you are with me. {i}*laughs*{/i}"
    show c4 vrave 12
    with dissolve
    vio "W-what the hell are you talking about, all of a sudden?"
    vio "You're really drunk, you know that..."
    vio "I can't tell how much of this is a joke and how much is serious..."
    vio "......"
    vio "{i}(I feel like how I respond to him here, will have a big impact, somehow or another...){/i}"
    menu:
        "[vio] considers the idea. [gr]\[VioSharing\]":
            $c4viosharing = True
            vio "Well..."
            vio "I don't know how that would be in reality, but..."
            vio "I... I might've also had thoughts about what it would be like, if there was someone else with us..."
            vio "...... Obviously, I'd feel more comfortable if it was a guy instead of a girl, since I'd be worried about her trying to steal you or some crap..."
            vio "But just because I say that, doesn't mean I'm a slut who wants to sleep with other people, either."
            vio "If anything like that ever happened, we would {i}both{/i} need to be a part of it."
            show c4 vrave 13
            with dissolve
            ni "Wow... I thought you'd get mad at me for sure..."
            ni "But, sweet. I'm happy you're interested in something like this."
            ni "I guess having another couple with us could be a possibility, too... haha."
            vio "Look, I never said I'd do it, alright?"
            vio "I just said I've thought about it before."
            vio "A threesome isn't something couples {i}usually{/i} do."
            if vioc >=1:
                show c4 vrave 12
                with dissolve
                vio "But... I told you before that I'm open-minded about these sorts of things, and I'd be willing to try something new if you asked."
                vio "And this isn't {i}as{/i} extreme as some other things out there, I suppose..."
                vio "...... However, it is still pretty damn weird, so I'll obviously need time to process these... suggestions of yours."
                vio "Don't expect anything for a while, if it even happens at all..."
                show c4 vrave 13
                with dissolve
                ni "I see. That's understandable."
                ni "It's just an idea I had, so no pressure. Whenever you feel like it, is fine with me."
                ni "......"
                ni "Well... err, anyway..."
                ni "I think I've had my fill for the night, so we should probably wrap things up and head to the hotel."
                stop music fadeout 2.0
                vio "Oh, right. That was smart of you to reserve one in advance."
                vio "I guess we both knew that was the best option, considering how much you usually drink..."
                vio "{i}(......){/i}"
                vio "{i}(What have I gotten myself into...?){/i}"
                "......"
                jump c4bed
            else:
                show c4 vrave 12
                with dissolve
                vio "Just because I've thought about something before, or that I haven't given a flat-out 'no', doesn't mean I'm completely on board with it, either."
                vio "I'd obviously need some time to think about it, {i}if{/i} anything was going to happen in the first place."
                vio "There's worse and more extreme things you could have proposed, so if this is the absolute extent of your fetishes, I guess I can give it some thought..."
                vio "Just don't expect an answer right away."
                show c4 vrave 13
                with dissolve
                ni "Haha, alright, alright. I get it."
                ni "I don't mean to pressure you or anything. It's just a little idea I had."
                ni "Anyway... I'm pretty tired, so we should probably wrap it up soon and head to the hotel."
                show c4 vrave 12
                with dissolve
                stop music fadeout 2.0
                vio "Oh, right. That was smart of you to reserve one in advance."
                vio "I guess we both knew that was the best option, considering how much you usually drink..."
                vio "{i}(......){/i}"
                vio "{i}(What have I gotten myself into...?){/i}"
                "......"
                jump c4bed
        "[vio] gets mad at his comments.":
            vio "Nick, you know I'm not a slut who just does whatever she feels like."
            vio "I have a fairly high sex drive, sure... but bringing someone else into it is a bit extreme, don't you think?"
            vio "And especially if there was another girl, I'd be worried about that leading to cheating somewhere down the road."
            vio "Let's just take it easy tonight, and we can continue as normal tomorrow."
            vio "Well, with you like this, you'll probably have a big hangover, though..."
            show c4 vrave 13
            with dissolve
            ni "Haha. I see... sorry about bringing this up."
            ni "We should probably head back soon, since I'm getting tired now."
            ni "How about you? Do you want to stay around a bit longer?"
            vio "No, I'm good, too. It's already past midnight now."
            vio "You reserved a hotel in advance, right?"
            stop music fadeout 2.0
            vio "That was smart thinking, I'll give you that."
            ni "Yep. Figured we'd be drinking too much to get back home properly."
            "......"
            jump c4bed

    label c4bed:
    play music "audio/low.mp3" fadein 2.0 loop
    show c4 park 1
    with fadeholdlong
    "A few hours later, in [pov]'s room..."
    pov "......."
    pov "{i}*sigh*{/i}"
    pov "I can't fall back asleep..."
    pov "I hate when this happens."
    pov "What time is it, anyway?"
    show c4 park 2
    with dissolve
    pov "It's a little past 4:30 in the morning now."
    pov "It's already starting to get a bit light outside, since it's summer now."
    pov "Hmmm..."
    pov "I went to bed at 11 PM, so... I'm in this awkward spot where I've slept enough, but not {i}enough{/i}."
    pov "Should I just wake up, or try to go back to sleep?"
    pov "Sleeping is probably the better choice, huh."
    show c4 park 3
    with dissolve
    pov "......"
    pov "Nope..."
    pov "I think my body is feeling kind of horny right now, too, which doesn't help."
    pov "It's one of those nights, huh..."
    pov "I'll probably have to do something about it, if I'm going to have any chance of falling back asleep."
    show c4 park 4
    with dissolve
    pov "What should I do, I wonder..."
    menu:
        "Go outside. [gr]\[Sexe +1\] \[Exh +1\]":
            pov "I could just stay here and touch myself, but..."
            pov "Even if that clears the horniness, it might not clear the thoughts in my head."
            pov "I should try something a little bit different."
            pov "It's still pretty early right now, so the chances of running into someone are pretty low..."
            pov "Especially if I go to the park next door, it's easy to run back home if someone shows up."
            "......"
            show c4 park 7
            with fadeholdlong
            pov "Well... nobody is here yet."
            pov "It's still only five in the morning, so that doesn't surprise me."
            pov "It's pretty chilly out..."
            pov "I only put this shirt on, though, so I guess that's what you would expect."
            show c4 park 8
            with dissolve
            pov "We've only lived here for a little while... less than a year, in fact."
            pov "But me and my parents often came here during the weekends, and for the occasional dinner picnic."
            pov "It's pretty convenient, seeing as it's placed directly next to our house."
            pov "And there aren't too many people who come here, either, so it's quite relaxing."
            pov "Occasionally I would even come by myself, just to read a book, or relax and listen to music."
            pov "Anyway..."
            pov "I guess I'll take a seat here, before anyone comes."
            pov "And maybe I'll step things up a bit while I'm at it..."
            if exh >=2:
                show c4 park 9n
                with dissolvelong
                pov "This is going pretty far, isn't it..."
                pov "I had the shirt on before, so I wouldn't get in trouble if anyone saw me on the sidewalk."
                pov "And now that I'm completely naked... well, the fact that it's 5 AM and freezing cold is even more apparent."
                pov "I shouldn't stay out for too long, or else I'll catch a cold."
                show c4 park 10n
                with dissolve
                pov "Actually, I can even feel the breeze on my nipples..."
                pov "This isn't something you usually experience."
                pov "But then again, I'm a pretty unusual girl..."
                pov "Most girls have fetishes of their own, but there's no doubt that mine are a bit more extreme than most girls'."
                pov "But hey, as long as you're not doing anyone any harm, what's the issue?"
                show c4 park 11
                with dissolvelong
                "{i}*whistling*{/i}"
                pov "{i}(Oh no...){/i}"
                pov "{i}(There's an old guy taking his morning walk here.){/i}"
                pov "{i}(Just as I decided to take my clothes off and sit down...){/i}"
                pov "{i}(Well, I should hurry up and grab my clothes, and get out of here!){/i}"
                pov "{i}(I really don't want any misunderstandings or lectures!){/i}"
                pov "{i}(It'll be quite hard to explain my way out of being naked like this.){/i}"
                show c4 park 12
                with dissolvelong
                pov "Okay, all dressed again..."
                pov "And he's finished walking past me now, so I shouldn't have to deal with him anymore."
                pov "This is probably a good sign that I should head back home. It's almost completely bright outside now, too."
                stop music fadeout 2.0
                pov "Can't risk catching a cold now that I have two jobs."
                pov "And I {i}did{/i} get to enjoy myself for a few minutes..."
                "......"
                $sexe+=1
                $exh+=1
                $ renpy.end_replay()
                jump c4hroom
            else:
                show c4 park 9
                with dissolvelong
                pov "Okay... this is a bit more revealing."
                pov "I'll just leave my shirt by the bush there, and go grab it again in a few minutes once I'm done."
                pov "Going outside with a shirt on like that is a bit unusual, but it's still {i}almost{/i} within the realms of acceptance."
                pov "At the very least, I could probably come up with some sort of excuse."
                pov "If I'm just wearing my underwear, though... that's a different story."
                pov "......"
                show c4 park 10
                with dissolve
                pov "It sure is cold, though, huh..."
                pov "Then again, it is 5 AM, and Vancouver never gets too hot, even in the summers."
                pov "It's pretty rare that we ever go above 30 degrees."
                pov "But on the other hand, winters are also pretty mild, so you never need to worry about the weather much."
                pov "Hmm..."
                pov "It's getting pretty bright out now..."
                show c4 park 11
                with dissolvelong
                "{i}*whistling*{/i}"
                pov "{i}(Oh no...){/i}"
                pov "{i}(There's an old guy taking his morning walk here.){/i}"
                pov "{i}(Just as I decided to take my shirt off and sit down...){/i}"
                pov "{i}(Well, I should hurry up and grab my shirt, and get out of here!){/i}"
                pov "{i}(I really don't want any misunderstandings or lectures!){/i}"
                show c4 park 12
                with dissolvelong
                pov "Okay, all dressed again..."
                pov "And he's finished walking past me now, so I shouldn't have to deal with him anymore."
                pov "This is probably a good sign that I should head back home. It's almost completely bright outside now, too."
                pov "Can't risk catching a cold now that I have two jobs."
                stop music fadeout 2.0
                pov "And I {i}did{/i} get to enjoy myself for a few minutes..."
                pov "So it's a win in my book."
                "......"
                $sexe+=1
                $exh+=1
                $ renpy.end_replay()
                jump c4hroom
        "Masturbate. [gr]\[Innocent +1\]":
            pov "It's almost morning now, so I don't want to risk going outside..."
            pov "Especially if I'm wearing something risky, there's a chance someone might be out there taking their dog for a morning walk or something."
            pov "There's a much simpler way of dealing with this problem."
            pov "And thankfully, it doesn't even require me to leave the bed."
            "......"
            show c4 park 5
            with fadeholdlong
            with Pause (1.5)
            pov "Oh god..."
            "{i}*panting*{/i}"
            pov "It feels so good when I touch my breasts and pussy at the same time..."
            pov "Ahh..."
            show c4 park 6
            with pixellate
            with Pause (1.5)
            pov "I think I'm going to cum soon, at this rate..."
            stop music fadeout 2.0
            pov "I can't hold back..."
            with vpunch
            pov "Ahhh—!!"
            pov "Yes—!"
            "......"
            $ renpy.end_replay()
            $inn+=1

    label c4hroom:
    show c4 hroom 1
    with fadeholdlong
    with Pause(1.0)
    play music "<from 10.8>audio/sparkle.mp3" fadein 2.0 loop
    "The next day."
    fr "Hmm...?"
    fr "Oh, it's a message from [pov]."
    fr "We were going to hang out today, but haven't decided on a time yet, so that makes sense."
    show c4 hroom 2
    with dissolve
    fr "It's the day before her birthday, and she wants to hang out, just the two of us, before her birthday party tomorrow."
    fr "So, with that in mind, we should probably hang out for longer than usual."
    fr "I don't have any plans for a couple days, so I could stay at [pov]'s place for the night, if she's fine with that."
    fr "There's also a nice hot spring I've wanted to go to for a while now..."
    fr "I'll try bringing her there."
    show c4 hroom 3
    with dissolve
    fr "So, with my response out of the way..."
    fr "What should I wear, I wonder?"
    fr "Well... we're mostly going to be hanging at her place, so I guess just a coat on top of this should do."
    "......"

    show c4 hotspring 1
    with fadeholdlong
    pov "{i}(Wow... this is quite the place, huh.){/i}"
    pov "{i}([fr] sure knows how to pick places out.){/i}"
    pov "{i}(But I shouldn't be too surprised. She's from Japan, after all, so it's no wonder that she knows a lot about places like hot springs.){/i}"
    show c4 hotspring 2
    with dissolve
    pov "{i}(It definitely has that Asian vibe about it, too.){/i}"
    pov "{i}(And since it's a weekday afternoon, there's nobody else here with us yet.){/i}"
    pov "{i}(That works for me, since I just wanna soak and relax in the water with [fr].){/i}"
    show c4 hotspring 3
    with dissolve
    pov "There's nobody else here, huh, [fr]?"
    pov "You've always been the type to choose quality over popularity."
    fr "Hey, you're not making fun of me, are you?"
    pov "Not at all. I like that part about you."
    pov "I'm pretty bad at finding hidden little places like this, so I'll continue to leave that up to you."
    show c4 hotspring 4
    with dissolve
    fr "Yeah, you {i}do{/i} listen to J-Pop, after all, so you tend to go with whatever's popular..."
    pov "Aw, come on... you know how big it is over there. Of course I wouldn't have stopped listening to it."
    fr "Sure, but I'm Japanese and even {i}I{/i} don't listen to it."
    pov "True. You're still listening to classical most of the time, I take it?"
    fr "Not always, but I use it to relax and study a lot."
    pov "Gotcha..."
    pov "Personally, I can't stand it since it reminds me of my mom..."
    show c4 hotspring 5
    with dissolve
    fr "Yeah, I can picture that. She was always pretty strict with you, even back when we were in school together."
    fr "Anyway..."
    fr "What do you say we head in the water now?"
    fr "It feels kind of wrong to be standing naked like this..."
    pov "Sure."
    pov "Actually..."
    pov "Can you test the temperature for me first, so I know it's not too hot?"
    show c4 hotspring 6
    with dissolvelong
    fr "Alright, I'll go in first, then, since you're too much of a chicken to come with me."
    fr "Which means I call dibs on where to sit..."
    fr "Maybe right here is best?"
    fr "I don't want to sit anywhere too deep at first, in case my skin gets red."
    "......"
    show c4 hotspring 7
    with dissolve
    fr "Ah, this feels great..."
    fr "It's been a while since I've been to a hot spring."
    fr "You should come in too, [pov]."
    fr "Even for you and your dainty self, it shouldn't be {i}that{/i} hot."
    show c4 hotspring 8
    with dissolve
    pov "Haha, okay, okay."
    pov "I guess I'll join you, then, so you don't get too lonely."
    show c4 hotspring 9
    with dissolve
    pov "Plus, we might as well enjoy ourselves before anyone else comes in and interupts our fun."
    pov "I just don't want to get my makeup wet, since I didn't bring my set with me."
    pov "You kinda dragged me to this place all of a sudden..."
    show c4 hotspring 10
    with dissolvelong
    fr "Ahh..."
    pov "Wow..."
    pov "You're right. This feels great."
    pov "Even though it's summer, I don't think it makes hot springs any less cozy."
    pov "It's been years since I've been to one, though..."
    pov "Probably since we were in school together in Japan, huh..."
    pov "That would be 4 or 5 years ago now."
    show c4 hotspring 11
    with dissolve
    fr "Yeah, it's been quite a while since then."
    fr "Maybe one day we can both go to Japan together, and have some fun there like the old days."
    fr "I'll be in Canada for a long time yet... maybe even permanently... so it'd be a good excuse to see my family again."
    pov "Yeah, I'd love to go with you sometime!"
    pov "Especially since I've been working and saving up money, it's no issue at all for me money-wise."
    pov "Although things might be a bit different in your case..."
    show c4 hotspring 12
    with dissolve
    fr "Yeah... unfortunately, I don't really have that much money to spare, due to tuition and all my other expenses."
    fr "But if I asked, I'm sure my parents would pitch in and get me a flight."
    fr "They haven't seen me for almost a year now, so they'd be happy to see me again for a bit."
    fr "I don't know if I'd be happy to see my brother, though..."
    fr "Hopefully he's grown up since the last time I've seen him."
    show c4 hotspring 13
    with dissolve
    pov "It's possible. High schoolers can mature quite a lot in just a year, from my experience."
    pov "Anyway..."
    pov "This is off-topic, and I don't want you to get too surprised by me asking you..."
    fr "Hmm?"
    pov "I noticed when we were changing and before we went in the water..."
    pov "You've been shaving now, haven't you?"
    show c4 hotspring 10
    with dissolve
    fr "W-What?!"
    fr "Why would you ask me that all of a sudden..."
    pov "Hey, I told you not to be surprised."
    show c4 hotspring 11
    with dissolve
    fr "Well, I never used to shave much when I was in Japan... just trimming, so that it would stay tidy."
    fr "But I've noticed since moving to Canada, more girls shave themselves completely, compared to girls who don't."
    fr "Especially at this age... there aren't very many girls who don't shave."
    fr "So I didn't want to stand out— that's all."
    show c4 hotspring 13
    with dissolve
    pov "{i}*giggles*{/i}"
    pov "I see, I see..."
    fr "Hey, stop staring at me like that..."
    stop music fadeout 2.0
    pov "My little [fr] has grown up, hasn't she?"
    fr "If you keep it up, I'll splash you!"
    "......"
    $ renpy.end_replay()
    show c4 home 1
    with fadeholdlong
    play music "<from 5.0>audio/obento.mp3" fadein 2.0 loop
    "Back at home..."
    fr "Why doesn't he just kiss her already?"
    fr "This is why guys can be annoying... always so clueless..."
    pov "Yeah, it annoys me when they don't do anything despite the woman clearly anticipating it."
    pov "Do they have to directly ask for the kiss or something? Geez..."
    show c4 home 2
    with dissolve
    fr "I like romance movies, but this is my pet peeve with them."
    pov "Same here."
    pov "They've both been drinking, too, so you would expect at least {i}something{/i} to happen."
    pov "Hmm..."
    pov "That reminds me..."
    show c4 home 3
    with dissolve
    pov "I'll be able to drink in a few hours, since my 19th birthday is tomorrow."
    fr "Yup. I've never been a drinker myself, but that means you can finally go to pubs and such."
    pov "Yeah..."
    pov "......"
    pov "Say..."
    pov "What if we grab a drink from my parents' stash, to celebrate?"
    pov "It's still not quite midnight yet, but it's close enough."
    show c4 home 4
    with dissolve
    fr "I mean, I'm fine with that, but..."
    fr "Are you sure your parents would be fine? I mean, without asking them and everything..."
    pov "Well, if I told them I doubt they'd be too upset, since I'll be of legal drinking age."
    pov "Plus, they already have so much alcohol stashed away in the pantry that I doubt they'd care if just 1 percent of it was gone."
    pov "And they won't be back home for quite a few months yet, so everything sitting there without being touched feels kind of wasteful..."
    fr "Well, in that case... I guess we can have a few glasses."
    show c4 home 3
    with dissolve
    pov "Alright. Let's head to the pantry upstairs, and then we can take it to the living room."
    show c4 home 5
    with fadeholdlong
    pov "I guess this should do?"
    pov "I don't know much about alcohol, but my parents let me have a sip of wine before, and it wasn't too bad."
    pov "My parents also like champagne a lot, so I thought that'd be fine, too?"
    pov "They had like twenty bottles of it in there..."
    show c4 home 6
    with dissolve
    fr "Hmm... I don't know much about champagne, but I do like wine."
    fr "I usually order a glass of wine when I'm out with my seminar group, since I can't stand beer."
    fr "...... How about we share both bottles, then?"
    pov "Sure. At least that way neither of us will be stuck with something we don't like."
    show c4 home 7
    with dissolve
    pov "{i}(This is very new to me...){/i}"
    pov "{i}(It's not as though I've never had a drop of alcohol before, but it's my first time drinking it on my own, as an adult.){/i}"
    pov "{i}(I'm not sure how much it would take to get me drunk, either, or what my tolerance is like.){/i}"
    pov "{i}(Hopefully this won't be too much for us...?){/i}"
    show c4 home 8
    with fadeholdlong
    pov "Oh my god..."
    pov "I feel so dizzy right now..."
    pov "I didn't think I'd feel this tipsy just from drinking wine."
    pov "It tastes like juice, after all..."
    pov "...... How are you doing, [fr]?"
    show c4 home 9
    with dissolve
    fr "My head's spinning, too..."
    fr "It almost feels like the whole room is rotating around me..."
    fr "I guess we might have gone overboard with that drinking game."
    fr "You picked a game where we'd drink a lot, on purpose, didn't you?"
    fr "Well, it was pretty fun, I'll admit..."
    show c4 home 10
    with dissolve
    pov "Haha. I guess I can't keep anything a secret with you."
    pov "I didn't think wine or champagne would hit me that hard, though, but we did drink pretty fast..."
    pov "I suppose we should probably stop now, so that we don't get sick tomorrow."
    pov "There is the birthday party, after all."
    pov "Hmm..."
    pov "I'll sit back up, too. I'm worried that I'll just fall asleep like this..."
    fr "Same here."
    show c4 home 11
    with dissolve
    fr "Wow... this is hitting me even harder than I thought, now that I'm sitting up again."
    pov "Same here..."
    pov "I don't think I felt this dizzy back during prom night."
    pov "......"
    pov "You know what, [fr]... I have a good idea."
    fr "Hmm...?"
    stop music fadeout 2.0
    fr "What did you have in mind?"
    pov "Since that guy from the movie has been annoying me..."
    show c4 home 12
    with dissolvelong
    play music "audio/blues.ogg" fadein 4.0 loop
    with Pause (1.0)
    pov "Why don't we show him how to take the lead?"
    pov "I might be a girl, but even I think I can do it better than him."
    fr "Haha... but he's an actor, [pov]... he's not even here."
    fr "You're quite drunk right now, aren't you..."
    show c4 home 13
    with dissolve
    pov "We both are, so what's the problem?"
    pov "Nothing wrong with just acting like this..."
    fr "Acting, huh..."
    pov "Here, I'll show how it's done."
    fr "Hmm...?"
    show c4 home 14
    with pixellate
    with Pause (2.0)
    fr "Hmm?!"
    fr "Mmmm..."
    pov "Mhmmm..."
    show c4 home 15
    with dissolvelong
    with Pause (1.0)
    pov "......"
    fr "......"
    pov "Hah..."
    fr "[pov]..."
    show c4 home 16
    with fadehold
    pov "Oh my god..."
    pov "I'm so sorry about that..."
    pov "It's like the alcohol just came over me all at once, and I couldn't understand or control what I was doing."
    pov "That sure sobered me up..."
    pov "I'm sorry about doing something so weird, [fr]."
    pov "I shouldn't lose sight of reality like that."
    show c4 home 17
    with dissolve
    fr "No, no— it's okay!"
    fr "It surprised me, but it's not like I'm upset or repulsed or anything like that."
    fr "You're my friend, [pov], so of course I can understand."
    fr "We were both drunk, so it's no big deal."
    fr "Heck, we can just laugh about it tomorrow."
    fr "I'll just chalk it up to you and your usual game fantasies."
    show c4 home 16
    with dissolve
    pov "{i}*laughs*{/i}"
    pov "Yeah, that would explain a lot."
    pov "Well, anyway..."
    pov "We should probably clean up, and take a glass of water with us."
    pov "And then it's probably time to get ready for bed."
    stop music fadeout 2.0
    fr "Sure, sounds good to me."
    fr "...... Silly [pov]..."
    $sexe+=1

    show c4 end 1
    with fadeholdlong
    play music "audio/cloudy.mp3" fadein 0.5 loop
    "The next morning."
    pov "Ah..."
    pov "I feel so much better already."
    pov "I had a few glasses last night, but it wasn't anywhere near enough to get a hangover or anything."
    pov "Not that I've ever experienced one myself, but I don't feel sick. In fact, I feel pretty good today."
    pov "We went to bed around 2 AM, and it's 11 AM now, so I still got a full sleep like I usually do."
    show c4 end 2
    with dissolve
    pov "......"
    pov "I do feel pretty embarrassed, though..."
    pov "We promised not to let it get awkward, so both of us are fine with happened, but still..."
    pov "Even if it was due to the alcohol..."
    pov "I've never kissed a girl before, and [fr] is one of my closest friends."
    show c4 end 3
    with dissolve
    pov "Hmmm..."
    pov "Thinking about it some more..."
    menu:
        "I enjoyed the kiss. [gr]\[Les +1\] \[KissEnjoy\]":
            pov "I've never considered doing anything like this with a girl before, but..."
            show fb5
            with pixellate
            pov "Kissing [fr]... I didn't mind it at all."
            pov "In fact, it was kind of exciting in its own way."
            pov "It actually felt better than what I remember of my prom night kiss, with that boy last year."
            hide fb5
            show c4 end 3
            with dissolvelong
            pov "....... Is it possible that I might be interested in girls, too?"
            pov "I'm still not sure, but at the very least, I'm not grossed out by the idea of it..."
            pov "If that {i}is{/i} the case... and I do feel something towards girls... that'll be pretty surprising, since I never thought there was a side to me like that."
            pov "......"
            pov "Well, either way..."
            $les+=1
            $c4kissenjoy = True
        "It was kind of weird. [gr]\[Hesitant +1\]":
            pov "It's not as though it grossed me out at the time, but..."
            show fb5
            with pixellate
            pov "I don't know... kissing other girls still seems kind of strange to me."
            pov "I've always pictured myself with a guy instead, so something about it just feels off."
            hide fb5
            show c4 end 3
            with dissolvelong
            pov "Not that I'm {i}completely{/i} opposed to the idea, or that I wouldn't ever give it a second chance, but..."
            pov "For now, I'll just treat it as a funny little event that happened while we were drunk."
            "......"
            pov "Anyway..."
            $het+=1
    show c4 end 4
    with dissolve
    pov "I should hurry up and get ready soon, since my birthday party is in a few hours."
    pov "We're not doing anything too crazy, but we'll be hanging out for a bit and eating together."
    pov "That's my idea of a fun time."
    pov "I don't enjoy massive crowds all that much, so I just invited my friends and a few old classmates from high school."
    stop music fadeout 2.0
    pov "......"
    pov "Hmm..."
    pov "I'm 19 now, huh..."
    "......"

    hide c4 end 4
    with wiperight
    show intro bg 1
    m "{size=-3}Congratulations! [pov] has reached: {b}Perversion, Level 4{/b}.{/size}"
    m "{size=-3}She is now capable of:{/size}"
    m "{size=-3}— Girl-on-girl action{p}— Handjobs{p}— Moderate foreplay{/size}"
    "......"
    "{b}Chapter 4: Complete{/b}"
    $ perv +=1
    ####################### END OF CHAPTER 4####################################

    ####################### CHAPTER 5 ##########################################
    $ chaptercount +=1

    ion "Hello there!"
    ion "I hope you've enjoyed your time thus far."
    ion "This marks the end of {b}Casual Desires{/b}, version 0.3."
    ion "If you're enjoying your time, and would like to support the development of {b}Casual Desires{/b}, any sort of contribution on my Patreon would be greatly appreciated!"
    ion "You can find my Patreon {a=https://www.patreon.com/ionDivvy}here{/a}."
    ion "Finally, if you've forgotten to save, I would recommend doing so in the previous scene, and using said save for the next release."
    ion "...... And now, with all that said..."
    ion "Let's meet again soon in {b}Casual Desires{/b}."
    ion "......"

    # This ends the game.
    return
