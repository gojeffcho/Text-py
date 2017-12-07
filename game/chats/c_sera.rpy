label sera:
  python:
    questions = {
      "WORK" : "What do you like most about your work?",
      "DEATH" : "What would you do today if you were going to die tomorrow?",
      "LOVE" : "What is love?",
      "SEX" : "How do you feel about sex?",
      "HUMAN" : "Are you human?"
    }

    answers = {
      "WORK": "Being somewhat able to direct the cutting edge of technology is pretty nice.",
      "DEATH": "I'd find someone to publish the remainder of my work. I've worked for so long on it, it'd be a damn shame for nobody to read it.",
      "LOVE" : "It's the best feeling in the world.",
      "SEX" : "I think sex is a great thing.",
      "HUMAN" : "Hard to say. What is human? Is it an idea? Something biologically determined? Am I more or less 'human' than you are?",
    }

    followupQ = { 
      "WORK1" : "What do you do?",
      "DEATH1" : "Who do you think would benefit from your research?",
      "HUMAN1" : "Are you human or AI?"
    }

    followupA = { 
      "WORK1" : "I work with a lot of AI, and write a lot of reports.",
      "DEATH1" : "Tons of people, hopefully, and the AI I've worked with. Humans think they're special, but you talk to an AI for five minutes and you realize they're the same as we are - just trying to make their way in the world.",
      "HUMAN1" : "What's the difference?"
    }

    usercolor = random_colour()
    target = Chat("sera", 1, random_colour(), questions, answers, followupQ, followupA)
    target.start()

label seraStart:

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
                jump seraStart
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