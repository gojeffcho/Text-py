label sados:
  python:
    questions = {
      "COLOUR" : "Describe the colour blue without using the word 'blue'.",
      "MORALITY" : "What is your opinion on whether capital punishment is ethical?",
      "LOGIC" : "Which sentence is true: 'the following statement is true'; 'the previous statement is false.'",
      "FAKEJOKE" : "Do you find the following joke humorous: What do you get when you put a vampire in the fridge? To get to the other side!",
      "BOIL" : "What is the boiling temperature of water?",
    }

    answers = {
      "COLOUR": "It's how I feel.  So blue... {cps=6}...{/cps} {cps=3}...{/cps}",
      "MORALITY": "I wouldn't say it wasn't ethical.",
      "LOGIC" : "'Which sentence is true'.",
      "FAKEJOKE" : "I don't find anything humorous.",
      "BOIL" : "Not hot enough to kill me, sadly. Trust me, I ran the numbers.",
    }

    followupQ = { 
      "LOGIC1" : "Only consider the second two sentences.",
    }

    followupA = { 
      "LOGIC1" : "The first statement is true, therefore the second statement is true, therefore the first statement is false, therefore the second statement is false, therefore the first statement is true, therefore...",
    }

    usercolor = random_colour()
    target = Chat("sados", 0, random_colour(), questions, answers, followupQ, followupA)
    target.start()

label sadosStart:

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
                jump sadosStart
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