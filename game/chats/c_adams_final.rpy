label adams_final:

  play music "music/boss.mp3" fadein 2.0 loop

  python:
    questions = {
      "WORK" : "What do you like most about your work?",
      "DEATH" : "What would you do today if you were going to die tomorrow?",
      "LOVE" : "What is love?",
      "SEX" : "How do you feel about sex?",
      "HUMAN" : "Are you human?"
    }

    answers = {
      "WORK": "It's not a question of liking. It is necessary.",
      "DEATH": "I would live my day normally. Being human means knowing you are going to die. There is no need to fear it. Just let it be.",
      "LOVE" : "A human emotion. Nothing more, nothing less.",
      "SEX" : "I enjoy it as much as the next man.",
      "HUMAN" : "Yes. I don't know how I got added to your queue or why you feel the need to ask me these questions, but you can report me as human now.",
    }

    followupQ = { 
    }

    followupA = { 
    }
      

    usercolor = random_colour()
    target = Chat("p_adams", 0, "32cd32", questions, answers, followupQ, followupA)
    target.start()

label adamsStart:

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
                jump adamsStart
            else:
                $has_args()
                
        elif cmd.upper() == "HELP" or cmd == "?":
            $help()
            
        elif cmd.upper() == "REPORT":
            if len(args) == 1:
                # Correct input
                stop music fadeout 4.0
                                
                if args[0].upper() == "HUMAN":
                    # Human Report
                    $desc = "You reported " + target.getId() + " as human.  Press {b}ENTER{/b} to return to the chat menu."
                    $say()
                    $flush_input()
                    
                    play music "music/bg0.mp3" fadein 2.0 loop
                    $target.reportAsHuman(True)
                    $adamsHuman = 1
                    nvl clear
                    jump chat
                
                if args[0].upper() == "AI":
                    # AI Report
                    $desc = "You reported " + target.getId() + " as AI.  Press {b}ENTER{/b} to return to the chat menu."
                    $say()
                    $flush_input()
                    
                    play music "music/bg0.mp3" fadein 2.0 loop
                    $target.reportAsHuman(False)
                    $adamsHuman = -1
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