label resistance_first:

  if day == "Tue":
    python: 
      questions = {
        "START" : "What is this?", 
        "WHO" : "Who are you?", 
        "WHAT" : "What do you want?", 
        "WHY" : "Why do you want access to the list of screening candidates?",
        "LIBERATE" : "What exactly do you mean by 'liberate'?",
        "SUSPICIOUS" : "<Report this conversation as suspicious>",
        "YES" : "Yes, I'll help you.",
        "NO" : "No, I'm not going to do that.",
        "UNCERTAIN" : "I'm not sure.  Can I think about it?"   
      }

      answers = {
        "START" : "Hello, " + username + ".  I've been hoping to talk to you.",
        "WHO" : "That's not important right now.  I've been watching your work and you seem reasonable - the Amyna, which you likely know as the 'Resistance', has a proposition I'd like to discuss with you.",
        "WHAT" : "You are given a list of subjects to interview every day.  We want you to install a backdoor program that would allow us to access that list.",
        "WHY" : "You have access to some useful information.  More access than you realize, in fact.  I'm wondering if you'd be at all interested in helping us liberate some of it.  Put it to better use.",
        "LIBERATE" : "You don't need to worry about that.  What matters is that the information would be put to use helping others, rather than oppressing them.",
        "YES" : "Excellent.  We'll send you the directions.  All you have to do is follow them.",
        "NO" : "That's a shame.  I hope you'll come around one day.",
        "UNCERTAIN" : "Certainly, take your time - just don't take too long.  You're our best candidate right now, but we can find other ways to get what we need."
      }

      followupQ = {
        "WHO1" : "I'd really like more information than that.  What do I call you?",

      }

      followupA = {
        "WHO1" : "Who I am as an individual isn't important; what's important is that I represent the Amyna.  But if it puts you at ease, you can call me SOTER.iOS.",
      }

    usercolor = random_colour()
    target = StructuredChat("unknown", random_colour(), questions, answers, followupQ, followupA)
    target.start()

label resistance_firstStart:

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
            
        elif cmd.upper() == "SUSPICIOUS":
            if len(args) == 0:

                # Correct input                                
                
                stop music fadeout 4.5
                $desc = "You reported a suspicious interaction.  Press {b}ENTER{/b} to return to mail.app."
                $say()
                $flush_input()
                
                $firstResponse = -1
                
                play music "music/bg0.mp3" fadein 2.5 loop

                nvl clear
                jump mail
                            
            else:
            
                # Incorrect input
                $desc = "{color=#" + errorcolor + "}ERROR{/color}: command 'SUSPICIOUS' takes no additional arguments.  Your chat options are: "
                $desc += target.questionsOutput()
                $say()
            
        else:
            if len(args) == 0:
                # Correct input
                $q = cmd
                $flush_input()
                
                # Question and answer
                $target.ask(q)
                
                # Chat-ending options
                if q.upper() == "YES" or q.upper() == "NO" or q.upper() == "UNCERTAIN":
                  stop music fadeout 3.5
                  $desc = "Chat has disconnected.  Press {b}ENTER{/b} to return to mail.app."
                  $say()
                  
                  play music "music/bg0.mp3" fadein 2.5 loop
                  
                  $flush_input
                  
                  if q.upper() == "YES":
                    $firstResponse = 1
                  elif q.upper() == "NO":
                    $firstResponse = -1
                  elif q.upper() == "UNCERTAIN":
                    $firstResponse = 0
                  
                  call spam87 from _call_spam87
                  
                  nvl clear
                  jump mail
                
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