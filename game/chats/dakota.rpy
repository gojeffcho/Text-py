label dakota:
  python:
    questions = {
      "FOOD" : "What is your favorite food?",
      "HEX" : "What is the hexadecimal code for the color red?",
      "WORD" : "How is the word 'boatswain' pronounced?",
      "TRAVEL" : "How would you get to New York?",
      "CONTROL" : "What are your thoughts on contraceptives?",
    }

    answers = {
      "FOOD": "CAKE!!!",
      "HEX": "#ff0000, but my favorite shade is #ea0a0b",
      "WORD" : "Boatswain",
      "TRAVEL" : "I don't know, but I could draw it for you on a cake!  Would you like an 'I heart NYC' pattern or a reproduction of Manhattan?  I am perfectly capable of either!",
      "CONTROL" : "If more people used contraceptives, there would be fewer people to eat cake and I would be unemployed, so I disapprove of them",
    }

    followupQ = { 
      "FOOD1" : "What kind of cake?",
      "WORD1" : "Have you ever heard this word out loud?" 
    }

    followupA = { 
      "FOOD1" : "Oh, I've never actually had cake.  I just like the idea of it.  :)",
      "WORD1" : "It's not a term related to baking, so I'm fairly certain you just made it up to test me, but I'm too smart to be tricked!" 
    }

    target = Chat("dakota", 0, crimson, questions, answers, followupQ, followupA)
    target.start()

label dakotaStart:

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
                jump maxStart
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