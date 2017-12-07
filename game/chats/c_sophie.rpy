label sophie:
  python:
    questions = {
      "EGGS" : "What kind of eggs do you use to make an omlette?",
      "HUMAN" : "What are your thoughts on AIs being given human rights?",
      "EMPATHY" : "How would you feel if your significant other cheated on you?",
      "FEAR" : "What is your biggest fear?",
      "PAIN" : "What is the greatest pain you've ever felt?",
    }

    answers = {
      "EGGS": "Chicken eggs...?",
      "HUMAN": "It's a fucking abomination. Don't buy into politicians' nonsense that this is some kind of 'complicated' issue. You have to be human to have human rights.",
      "EMPATHY" : "It's awful. My wife left me for a zero last year.",
      "FEAR" : "Zeroes getting human rights.",
      "PAIN" : "This conversation is a pain.",
    }

    followupQ = { 
      "EMPATHY1" : "Why did she leave you?",
      "PAIN1" : "What about physical pain?",
    }

    followupA = { 
      "EMPATHY1" : "You'd have to ask her.",
      "PAIN1" : "I {i}was{/i} talking about physical pain.",
    }

    usercolor = random_colour()
    target = Chat("sophie", 1, random_colour(), questions, answers, followupQ, followupA)
    target.start()

label sophieStart:

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
                jump sophieStart
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