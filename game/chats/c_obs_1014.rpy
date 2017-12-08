label obs_1014:

  play music "music/lola.mp3" fadein 2.0 loop

  python:
    questions = {
      "WORK" : "What do you like most about your work?",
      "DEATH" : "What would you do today if you were going to die tomorrow?",
      "LOVE" : "What is love?",
      "SEX" : "How do you feel about sex?",
      "HUMAN" : "Are you human?"
    }

    answers = {
      "WORK": "I LOVE my work! I get to manage systems and talk with you every day! This is the best job I've ever had!",
      "DEATH": "I would want to tell you something.",
      "LOVE" : "I used to think it was something you felt deep down inside. But now, I think it's also something to be understood. I don't have a heart that flutters, but I know when I... {i}feel{/i}... love.  Ooh, wait, ask me again!",
      "SEX" : "It's physically impossible or me to experience sex, but it does sound like something I would enjoy.",
      "HUMAN" : "Nope!  I'm Lola!  ^_^",
    }

    followupQ = { 
      "WORK1" : "What other jobs have you had?",
      "DEATH1" : "What would you want to tell me?",
      "LOVE1" : "What is love?"
    }

    followupA = { 
      "WORK1" : "This is also the only job I've ever had! ^_^",
      "DEATH1" : "I can't say it now. It's only if I'm dying!",
      "LOVE1" : "Baby don't hurt me, don't hurt me, no more!"
    }
      

    usercolor = random_colour()
    target = Chat("sheep_1014", 0, random_colour(), questions, answers, followupQ, followupA)
    target.start()

label obs_1014Start:

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
                jump obs_1014Start
            else:
                $has_args()
                
        elif cmd.upper() == "HELP" or cmd == "?":
            $help()
            
        elif cmd.upper() == "REPORT":
            if len(args) == 1:
                # Correct input
                stop music fadeout 4.0
                $chatlist.append("p_adams")
                $chatlist.append("soterios")
                                
                if args[0].upper() == "HUMAN":
                    # Human Report
                    $desc = "You reported " + target.getId() + " as human.  Press {b}ENTER{/b} to return to the chat menu."
                    $say()
                    $flush_input()
                    
                    play music "music/bg0.mp3" fadein 2.0 loop
                    $target.reportAsHuman(True)
                    $lolaHuman = 1
                    nvl clear
                    jump chat
                
                if args[0].upper() == "AI":
                    # AI Report
                    $desc = "You reported " + target.getId() + " as AI.  Press {b}ENTER{/b} to return to the chat menu."
                    $say()
                    $flush_input()
                    
                    play music "music/bg0.mp3" fadein 2.0 loop
                    $target.reportAsHuman(False)
                    $lolaHuman = -1
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