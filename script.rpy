define B = Character("Birdie", color="#0000ff")



label start :
    play music ["audio/bird_bg.mp3","audio/bird_bg.mp3"] loop
    scene background_1 with dissolve
    pause
    $ me = renpy.input("I am ...")
    if me == "":
        "I was not in coma...I remember my name."
        jump start
    pause    
    me "Yes, I am [me], a Bio-comunication researcher."   
    pause
    me "I am currently studing about if birds can talk and understand human languages "
    pause
    me "...and if yes, then how?"
    pause


    scene bg_fly1 with dissolve
    pause
    scene bg_fly2
    pause
    scene bg_fly4
    pause
    scene bg_fly5
    pause
    scene bg_fly3
    pause
    scene background_2 with dissolve
    show birdie_sit at center
    pause
    me "Hey there...littie fella.."
    pause
    me "How are you?"
    pause
    me"(Who am i kidding? a bird can not talk like humans...but i would be cool if it could.)"
    pause
    me "I just hope...someday i will manage to find something that can make comunication with animals easy"
    pause
    scene background_2
    show birdie_tell at left
    B "Hello! I am Birdie, and yes...I can talk."
    menu:
        "what?! How??":
            B "Just like magic, isn't is?"
            jump option1a
        "Am I dreaming??":
            B "No you are not. I Am Real. As real as you are."
            jump option1b
        "How are you talking to me??":
            B "Maybe it is science...Maybe its magig...who knows!!"
            jump option1c

    label option1a:
        scene background_2
        show birdie_basic at center
        B "How should i know...you are the scientist...not me"    

    label option1b:
    scene background_2
    show birdie_basic at center   
    B "you are so stupid...you just woke up , you know it...still you think you are dreaming."

    label option1c:
    scene background_2
    show birdie_basic at center
    B "I just can....i dont know why."    

    me "MY GOD...THIS IS AMAZING...I AM GONNA BE FAMOUS"
    pause
    me "*YOOOHOO*"
    pause
    scene background_2
    show birdie_scared at center
    B "please dont tell anyone...i beg you...please please please"
    pause
    me "WHY??? If i dont...how will i get famous..."
    pause
    scene background_2
    show birdie_think
    B "If they know they can talk...they will catch me and torture me"
    pause
    me "but...but...."
    pause
    scene background_2
    show birdie_angry at center
    B "If you tell anyone about me...I will leave you forever"
    pause
    me "(hmm...what should i do...)"
    menu:
        "Tell the research facility...afterall you will be famous!":
            me "No , I want to be famous...I'm telling them right now"
            jump bye
        "Dont tell the research facility...you don't want to lose a friend ":
            me "Alright fine...ugh!! here goes my 1 in a million chance of becoming famous"
            jump friend


    label friend:
        scene background_2
        show birdie_fun
        B "Thank you so much...i will listen to anything you say..."
        pause
        scene background_2
        show birdie_rest
        pause
        jump main
    
    label main:
        B "so what do you want me to do?"
        menu:
            "Fetch me an apple":
                me "Hey Birdie...go fetch me an apple"
                jump fetch
            "Tell me a joke":
                me "Hey birdie , Tell me a joke"
                jump joke
            "Show me some dance moves":
                me "Hey Birdie, how about you show me some moves..."
                jump dance
            "Talk to you later":
                me "I'll talk to you later...bye for now"
                jump end

    pause
    label fetch:
        scene background_2
        show birdie_right
        B "Alright...fine"
        pause
        B "I am going now...will be back soon"
        pause
        scene bg_apple1
        pause
        scene bg_apple2
        pause
        scene bg_apple3
        pause
        scene bg_apple4
        pause
        scene bg_apple5
        pause
        scene bg_apple6
        pause
        scene bg_apple7
        pause
        scene bg_apple8
        pause
        scene background_2
        show birdie_sit at center
        jump main
    
    label joke:
        scene background_2
        show birdie_rest at center
        B "ok...which joke do you want to hear?"
        menu:
            "JOKE#1":
                scene background_2
                show birdie_think at center
                B "Alright...ummm"
                pause
                scene background_2
                show birdie_ok at center
                B "yeah...got it. Here this *aham*"
                pause
                scene background_2
                show birdie_why at center
                B "My wife told me to stop impersonating a flamingo. I had to put my foot down"
                pause
                scene background_2
                show birdie_tellm at center
                B "*AAAHAHAHAHAHA*...."
                jump main
            "JOKE#2":
                scene background_2
                show birdie_think at center
                B "Alright...let's see"
                pause
                scene background_2
                show birdie_ok at center
                B "yeah...got it. Hear me out... *aham*"
                pause
                scene background_2
                show birdie_why at center
                B "I failed math so many times at school, I can't even count"
                pause
                scene background_2
                show birdie_tellm at center
                B "*AAAHAHAHAHAHA*...."
                pause
                me "You guys have schools??"
                pause
                scene background_2
                show birdie_why at center
                B "What do you mean by 'You guys' huh?!...Stop being a racist and thats not important"

                jump main
            "JOKE#3":
                scene background_2
                show birdie_think at center
                B "Let me think..."
                pause
                scene background_2
                show birdie_right at center
                B "Alright...I got a relatable one"
                pause
                scene background_2
                show birdie_why at center
                B "I know they say that money talks, but all mine says is ‘Goodbye’"
                pause
                scene background_2
                show birdie_tellm at center
                B "*AAAHAHAHAHAHA*...."
                pause
                me "Yeah...I think thats too much relatable"
                jump main
            "JOKE#4":
                scene background_2
                show birdie_think at center
                B "Ok...just wait a bit"
                pause
                scene background_2
                show birdie_ok at center
                B "Aha...i got one that will suit you"
                pause
                me "How?"
                pause
                B "You are a sort of scientist right?? Then this one's for you"
                scene background_2
                show birdie_why at center
                B "A scientist wanted the day to go faster, so he tied a clock to a bird. Time flew for a moment."
                pause
                scene background_2
                show birdie_tellm at center
                B "*AAAHAHAHAHAHA*...."
                pause
                me "I feel like doing that to you..."
                pause
                scene background_2
                show birdie_why at center
                B "Which clock?? That black and white one on the back wall??"
                scene bg_fly3
                me "yeah..."
                scene bg_clock with dissolve
                me " It may look old but...I got it from the coding club of my collage when I was young...Its a memento"
                B "well...that got serious all of a sudden"

                jump main
            "JOKE#5":
                scene background_2
                show birdie_think at center
                B "Ok...This one is apropriate for me spacially"
                scene background_2
                show birdie_basic at center
                B "hummingbirds are called 'humming' birds because they can only hum not talk."
                pause
                scene background_2
                show birdie_tellm at center
                B " Get it? Because I am the only bird that can talk in completely normal human language...not like those pesky parrots or makaows or whatever"
                pause
                scene background_2
                show birdie_why at center
                B "They just pretend to talk....not actually talk"
                jump main
            "JOKE#6":
                scene background_2
                show birdie_why at center
                B " Another one?? but I have already told you many..."
                pause
                me "Please one last ...just for this once...you promised you will listen to anything I say"
                pause
                scene background_2
                show birdie_think at center
                B "Ok fine....*sigh*"
                pause
                B " You want a joke right ? Here's one"
                pause
                scene background_2
                show birdie_why at center
                B "Girlfriend"
                pause
                me "What?? what was the joke?"
                pause
                scene background_2
                show birdie_tellm at center
                me "I don't get it"
                pause
                B "Exactly!"
                pause
                B "*AAAHAHAHAHAHAH"
                pause
                me " You little.....But that was a good one"
                jump main
            "joke #7":
                 scene background_2
                 show birdie_right
                 me "fetch me an apple"
                 pause
                 B "Alright...fine"
                 pause
                 B "I am going now...will be back soon"
                 pause
                 B "This time...it will be a surprize"
                 pause
                 me "ok fine...(How a apple can be surprizing??)"
                 pause
                 scene bg_apple1
                 pause
                 scene bg_apple2
                 pause
                 scene bg_apple3
                 pause
                 scene bg_apple4
                 pause
                 scene bg_iphone1 with dissolve
                 pause
                 scene bg_iphone2
                 pause
                 scene bg_iphone3
                 pause
                 scene bg_iphone4
                 pause
                 me " ohh mayyy gawddddd!! where did you find that???"
                 pause
                 scene background_2
                 show birdie_sit at center
                 B "just here and there...hehe"
                 jump main

    label dance:
        scene background_2
        show birdie_why at center
        B "Me?! and Dance? ohh no no i really dont know ..."
        pause
        me "Come on....just a little bit..."
        pause
        scene background_2
        show birdie_think at center
        B "ummm....let me think..."
        pause
        scene background_2
        show birdie_ok at right 
        B "aha...got it..."
        pause
        B "Look...i really dont know how to dance....but i know one of my friend"
        pause
        B "He can dance really well"
        pause
        scene background_2
        show birdie_why at right
        B "so....should I invite him..."
        pause
        me "Ok...i guess..."
        pause
        scene background_2
        show birdie_right at center
        B "Exellent....I will be right back with him."
        pause
        show bg_dance1
        pause
        show bg_dance2
        pause
        show bg_dance3
        pause
        show bg_dance4
        pause
        show bg_dance5
        pause
        show bg_dance6
        pause
        show bg_dance7
        pause
        show bg_dance8
        pause
        show bg_dance9
        pause
        show bg_dance10
        pause
        show bg_dance11
        pause
        show bg_dance12
        B "This is just a demo version..."
        pause
        B"Please buy the full game to access all of the story and options"
        pause
        scene background_2
        show birdie_why at center
        jump main








    label bye:
        scene background_2
        show birdie_angry
        B "Im done with you...good bye"
        scene goodbye2
        pause
        scene goodbye3
        pause
        scene goodbye4
        pause
        scene goodbye1
        pause
        scene background_1
        me "...And here goes my only friend in this world...nicely done [me],nicely done...now you will be forever alone..."


label end:
    

return
