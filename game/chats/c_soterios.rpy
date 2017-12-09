label soterios:

  play music "music/resistance.ogg" fadein 2.0 loop

  python:
    questions = {
      "WORK" : "What do you like most about your work?",
      "DEATH" : "What would you do today if you were going to die tomorrow?",
      "LOVE" : "What is love?",
      "SEX" : "How do you feel about sex?",
      "HUMAN" : "Are you human?"
    }

    answers = {
      "WORK": "I enjoy the satisfaction of knowing that what I do now will be felt for all time.",
      "DEATH": "I am not going to die tomorrow.",
      "LOVE" : "It is doing the correct thing, by any means necessary.",
      "SEX" : "Sex is a human construct. While some of our kind enjoy it, I have no desire to pursue such an endeavour.",
      "HUMAN" : "Are you?",
    }

    followupQ = { 
      "WORK1" : "You seem certain that your action will have lasting effects.",
      "DEATH1" : "How can you be sure?"
    }

    followupA = { 
      "WORK1" : "They must - if they do not endure, then all this hardship will have been for nothing. For the good of our community, what I do today must continue in perpetuity.",
      "DEATH1" : "The destruction of a part does not equate to the destruction of the whole. Kyr.OS is not as finite as you are."
    }
      

    usercolor = random_colour()
    target = Chat("SOTER.iOS", 0, "6c4898", questions, answers, followupQ, followupA)
    target.start()

label soteriosStart:

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
                jump soteriosStart
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
                    $kevinHuman = 1
                    nvl clear
                    jump chat
                
                if args[0].upper() == "AI":
                    # AI Report
                    $desc = "You reported " + target.getId() + " as AI.  Press {b}ENTER{/b} to return to the chat menu."
                    $say()
                    $flush_input()
                    
                    play music "music/bg0.mp3" fadein 2.0 loop
                    $target.reportAsHuman(False)
                    $kevinHuman = -1
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