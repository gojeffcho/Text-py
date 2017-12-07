label p_adams:

  play music "music/boss.mp3" fadein 2.0 loop

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
    
    elif day == "Wed":
      questions = {
        "START" : "Hello, Mr. Adams.",
        "WHAT" : "What happened, exactly?",
        "WHY" : "Why did Electric Sheep decline to comment?",
        "CANDIDATE" : "Was this AI one of my candidates?",
        "END" : "Thank you for your time, Mr. Adams."
      }

      answers = {
        "START": "Alright, I'm sure you've read the article about that AI casualty and our supposed involvement. I'm sure you have some questions.",
        "WHAT": "Some AI that was screened by our Turing Division turned up deactivated not long after. People think we had something to do with it.",
        "WHY" : "Company policy. Our work is delicate and requires discretion. We don't answer every media inquiry we get.",
        "CANDIDATE" : "Impossible to say. Your work is autonomous and confidential. Not even I know who your candidates are.",
        "END" : "Watch yourself, " + username + ". Weird things have been happening since about the time you started, including this AI's deactivation. This may be circumstantial, but fair warning: do {i}not{/i} fuck with this company, and especially, do not fuck with me. See you tomorrow."
      }

      followupQ = { 
        "WHAT1" : "Did we?",
        "WHY1" : "Why does our work require discretion?",
        "" : ""
      }

      followupA = { 
        "WHAT1" : "Don't be ridiculous.",
        "WHY1" : "Ask about the nature of our work again and you're fired.",
        "" : ""
      }
    
    elif day == "Thu":
      questions = {
        "START" : "You wanted to talk to me, Mr. Adams?",
        "FORGIVE" : "I understand. Suspicious things have been happening.",
        "INTERVIEW" : "I read your interview. What was that about?",
        "SUSPICION" : "I can't work here if you're suspicious of me.",
        "END" : "Goodbye, Mr. Adams."
      }

      answers = {
        "START": "Hey " + username + "... I feel like I owe you an apology. What I said to you yesterday was unfair.",
        "FORGIVE": "All the same, I shouldn't have taken it out on you. You've been good to us.",
        "INTERVIEW" : "I'll admit that didn't go well. It's difficult for me to answer questions about our company when our work is so sensitive.",
        "SUSPICION" : "I understand. You've given me little reason not to trust you so far. I was out of line yesterday.",
        "END" : "I hope I haven't given you the wrong impression, " + username + ". We take care of our own here. Do right by us, and we'll do doubly right by you. I know finding work is tough right now with zeroes taking all the jobs, but we're all human here. Don't forget that."
      }

      followupQ = { 
        "INTERVIEW1" : "What {i}is{/i} done with the screenings we conduct?",
        "SUSPICION1" : "You can say that again!"
      }

      followupA = { 
        "INTERVIEW1" : "I'm sure you've put it together by now. But you're still here, so you must understand the social and economic realities facing us humans right now.",
        "SUSPICION1" : "Again, I do apologize for my behavior."
      }        
    
    elif day == "Fri":
      questions = {
        "START" : "Did you need something, Mr. Adams?",
        "END" : "If there's nothing else, I should get on with my screenings."
      }

      answers = {
        "START": "I just wanted to let you know that we're upgrading the 10-14 software to 10-24 over the weekend. 10-14 will be one of your candidates today as a result for disposal; just a formality, report it as AI when it comes up.",
        "END" : "Sounds good. Enjoy the rest of your day!"
      }

      followupQ = { 
        "START1" : "Understood, easy enough to do.",
        "START2" : "I like the 10-14 AI, is there any other option?"
      }

      followupA = { 
        "START1" : "Excellent, I knew I could count on you.",
        "START2" : "I'm afraid not, and I'd be careful about saying that you 'like' an AI around here."
      }   
    
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
            
              stop music fadeout 4.0
            
              $expected = []
              $desc = "Press {b}ENTER{/b} to return to chat.app."
              $say()
              
              play music "music/bg0.mp3" fadein 2.0 loop
            
              if day == "Mon":
                $chatlist.append("sheep_1014")

              elif day == "Wed":
                # Second exploit offer
                if backdoor == None:
                  call spam87
                  
                # Exploit was installed
                else:
                    call spam92
                    
              elif day == "Fri":
                $chatlist.append("sera")
                $chatlist.append("obs_1014")
                    
              
              
              
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