label courtney:
  python:
    questions = {
      "FOOD" : "What is your favorite food?",
      "HEX" : "What is the hexadecimal code for the color red?",
      "WORD" : "How is the word 'boatswain' pronounced?",
      "TRAVEL" : "How would you get to New York?",
      "CONTROL" : "What are your thoughts on contraceptives?",
    }

    answers = {
      "FOOD": "I convince myself it's meatloaf with a side of frozen vegetables, because I eat what my kids eat, but honestly it's just cupcakes.  Red velvet cupcakes.",
      "HEX": "I don't know, but I've got a red lipstick in the shade 'wine night'.  My three-year-old likes to eat it.  \n...It doesn't actually have alcohol in it.  It's just the name.",
      "WORD" : "Talk about a blast from the past!  Back in college I was taking this art history class, and my professor would always call on me to talk about things, like he knew I had something going for me, you know?  He asked me how to pronounce 'boatswain' too.  That was before my kids, though.  Back when I had dreams, prospects, and a waistline.  \n...Sorry, what was the question?",
      "TRAVEL" : "I don't know, take out a second mortgage.",
      "CONTROL" : "After I started taking 'Plan B' like a tic tac every day after lunch, I'd say they were prety great.  Be cool if there were more options for men, though, that's all I'm saying.  I'm basically counting down the days until menopause.",
    }

    followupQ = { 
      "FOOD1" : "How many children do you have?",
      "WORD1" : "How is the word 'boatswain' pronounced?" ,
      "CONTROL1" : "Have you always used contraceptives?"
    }

    followupA = { 
      "FOOD1" : "Too many.",
      "WORD1" : "Right.  Like 'boh-sen', basically.",
      "CONTROL1" : "Yes, but as my children will tell you, 'accidents happen'."
    }

    target = Chat("courtney", 1, darkcyan, questions, answers, followupQ, followupA)
    target.start()

label courtneyStart:

    $expected = ["LOOK", "L", "HELP", "?"]
    if target.getAsked():
      $expected.append("REPORT")
    $expected += target.getQuestions()
    $pickup = []
    $room = "Chat: " + target.getId()
    $update_roomlabel()
    $desc = "You are now chatting with '{b}{color=#" + target.color() + "}" + target.getId() + "{/color}{/b}'.  In these chats, you will be given a list of options for questions you can pose, prefixed by a tag.  Enter the tag of the conversation option you wish to pursue.\n" 
    $desc += target.questionsOutput()
    
    $say()
    
    while True:
        $echo()
        
        if cmd.upper() not in expected:
            python:
                eastered = False
                for word in easters:
                    if cmd == word or args == word or word in args:
                        easter(word)
                        eastered = True
                
                if not eastered:
                    input_error()
        
        elif cmd.upper() == "LOOK" or cmd.upper() == "L":
            if len(args) == 0:
                $flush_input()
                nvl clear
                jump courtneyStart
            else:
                $has_args()
                
        elif cmd.upper() == "HELP" or cmd == "?":
            $help()
            
        elif cmd.upper() == "REPORT":
            if len(args) == 1:
                # Correct input
                                
                if args[0].upper() == "HUMAN":
                    # Human Report
                    $desc = "You reported " + target.getId() + " as human.  Press {b}ENTER{/b} to return to the chat menu."
                    $say()
                    $flush_input()
                    $target.reportAsHuman(True)
                    nvl clear
                    jump chat
                
                if args[0].upper() == "AI":
                    # AI Report
                    $desc = "You reported " + target.getId() + " as AI.  Press {b}ENTER{/b} to return to the chat menu."
                    $say()
                    $flush_input()
                    $target.reportAsHuman(False)
                    nvl clear
                    jump chat
                
                else:
                    # Incorrect input
                    $desc = "{color=#" + errorcolor + "}ERROR{/color}: command 'REPORT' must be followed by option 'AI' or 'HUMAN'.  Your chat options are: "
                    $desc += target.questionsOutput()
                    $say()
            
            else:
                # Incorrect input
                $desc = "{color=#" + errorcolor + "}ERROR{/color}: command 'REPORT' must be followed by option 'AI' or 'HUMAN'.  Your chat options are: "
                $desc += target.questionsOutput()
                $say()
            
        else:
            if len(args) == 0:
                # Correct input
                $q = cmd
                $flush_input()
                
                # Question and answer
                $target.ask(q)
                
                # Updated $expected with current command options
                $expected = ["LOOK", "L", "HELP", "?", "REPORT"]
                $expected += target.getQuestions()
                
                $desc = "Your chat options are:"
                $desc += target.questionsOutput()
                $say()
                                
            else:
                $desc = "Please enter only the tag of the conversation option you wish to pursue."
                $say()
                    
    return