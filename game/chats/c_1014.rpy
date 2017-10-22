label teststart:
  $username = "chell"

label l0_14:
  python:
    questions = {
      "MATH" : "What is the square root of 17?",
      "REALJOKE" : "Do you find this joke funny:  What do you call cheese that isn't yours?  Nacho cheese!",
      "FAKEJOKE" : "Do you find this joke funny: Where do cows go for first dates?  Orange you glad I didn't say banana?",
      "MEMORY" : "What is your earliest memory?",
      "EMPATHY" : "How do you feel when you hear the sound of a baby crying?"
    }

    answers = {
      "MATH": "4.123105626",
      "REALJOKE": "Very humorous, L.O.L.",
      "FAKEJOKE": "Very humorous, L.O.L.",
      "MEMORY": "Being in a warm room.",
      "EMPATHY": "Sad."
    }

    followupQ = {
      "MATH1": "Did you use a calculator?",
      "MEMORY1": "Describe the room.",
      "EMPATHY1": "What would you do?"
    }

    followupA = {
      "MATH1": "No.",
      "MEMORY1": "Four walls, one roof, one floor.  It was warm.",
      "EMPATHY1": "Nothing.  I was not asked to assist."
    }

    target = Chat("l0_14", 0, "dc143c", questions, answers, followupQ, followupA)
    target.start()

label lolaStart:

    $targetname = target.getId()
    $expected = ["LOOK", "L", "HELP", "?"]
    $expected += target.getQuestions()
    $pickup = []
    $room = "Chat: " + targetname
    $desc = "You are now chatting with '{color=#ff1493}" + targetname + "{/color}'.  In these chats, you will be given a list of options for questions you can pose, prefixed by a tag.  Enter the tag of the conversation option you wish to pursue.\n\n" 
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
                jump l0_14
            else:
                $has_args()
                
        elif cmd.upper() == "HELP" or cmd == "?":
            $help()
            
        else:
            if len(args) == 0:
                # Correct input
                $q = cmd
                $flush_input()
                
                # Question and answer
                $target.ask(q)
                
                # Do follow-up, if there are any
                $followups = target.getFollowups(q)
                
                python:
                  if len(followups) > 0:
                    # TODO: SET EXPECTED
                    
                    target.followup(q)
                
                # TODO: FIX EXPECTED
                
            else:
                $desc = "Please enter only the tag of the conversation option you wish to pursue."
                $say()
                    
    return