label p_adams:
  python:
    if day == "Mon":
      questions = {
        "START" : "Hello?",
        "COMPANY" : "What is this company?",
        "JOB" : "What exactly will I be doing here?",
        "END" : "I think I'm ready to start my work."
      }

      answers = {
        "START": "Hello and welcome to Electric Sheep Incorporated.  I'm Philip Adams, I'll be your handler.  There's some paperwork to get sorted before we begin.  As it's your first day here " + username + ", do you have any questions before we begin, about the company or your job?",
        "COMPANY": "Electric Sheep Incorporated is a 'key player in the competitive technological landscape'.  Or so marketing tells me.",
        "JOB" : "You will be a part of our Turing Division, critically assessing candidates who are applying for jobs with firms who contract us to determine whether applicants are human or AI.",
        "END" : "Excellent.  I'll leave you with our AI tutorial bot, 10-14.  It will show you what you will be doing here and how to do it.  It is designed to be personable."
      }

      followupQ = { 
        "JOB1" : "Why?" 
      }

      followupA = { 
        "JOB1" : "Our newsletters have lots of information regarding updates about our company.  You'll get them in your email periodically - read them over to get a sense of why what we do here is so important.",
      }
      
#     elif day == "Tue":
#       questions = {
#         "START" : "Good afternoon, Mr. Adams.",
#         "" : "",
#         "" : "",
#         "" : ""
#       }
# 
#       answers = {
#         "START": "Good afternoon, " + username + ".  How did you first day go?",
#         "": "",
#         "" : "",
#         "END" : ""
#       }
# 
#       followupQ = { 
#         "START1" : "Very well.",
#         "START2" : "Terribly.",
#         "START3" : "Funny thing just happened..."
#       }
# 
#       followupA = { 
#         "START1" : "Excellent, I'm glad to hear that.",
#         "START2" : "So it goes.  You'll get the hang of it.",
#         "START3" : "Let's talk about that in a moment."
#       }
    
    # global usercolor
    usercolor = random_colour()
    target = Chat("p_adams", 0, random_colour(), questions, answers, followupQ, followupA)
    target.start()

label p_adamsStart:

    $expected = ["LOOK", "L", "HELP", "?"]
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
                jump p_adamsStart
            else:
                $has_args()
                
        elif cmd.upper() == "HELP" or cmd == "?":
            $help()
            
        elif cmd.upper() == "END":
            if len(args) == 0:
              $q = cmd
              $flush_input()
            
              $target.ask(q)
            
              $expected = []
              $desc = "Press {b}ENTER{/b} to end the tutorial and return to chat.app."
              $say()
            
              $chatlist.append("sheep_1014")
              
              nvl clear
              jump chat
            else:
              $desc = "Command 'END' takes no arguments."
              $say()
            
        else:
            if len(args) == 0:
                # Correct input
                $q = cmd
                $flush_input()
                
                # Question and answer
                $target.ask(q)
                
                # Updated $expected with current command options
                $expected = ["LOOK", "L", "HELP", "?"]
                $expected += target.getQuestions()
                
                $desc = "Your chat options are:"
                $desc += target.questionsOutput()
                $say()
                                
            else:
                $desc = "Please enter only the tag of the conversation option you wish to pursue."
                $say()
                    
    return