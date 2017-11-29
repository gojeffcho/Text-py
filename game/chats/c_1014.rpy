label sheep_1014:
  python:
  
    if day == "Mon":
      questions = {
        "START" : "I'm ready to begin the training session.",
        "QUESTIONS" : "What are the pre-approved questions?",
        "DISCERN" : "How can I use these questions to help me discern between humans and AI?",
        "REPORT" : "What do I do once I think I've figured out whether the candidate is AI or human?",
        "REWARD" : "What happens if I report a candidate correctly or incorrectly?",
        "END" : "I think I've learned everything I need to get started."
      }

      answers = {
        "START": "Welcome, " + username + ".  I am 1014, the AI tutorial bot.  Welcome to the training program.  You will be determining whether candidates are humans or AIs by asking them questions and evaluating their responses.  You can ask any of the daily pre-approved questions to each candidate.",
        "QUESTIONS": """Today's questions are:
      {b}MATH{/b}: Ask the candidate a math question
      {b}REALJOKE{/b}: Tell the candidate a hilarious joke
      {b}FAKEJOKE{/b}: Tell the candidate a joke with an incorrect punchline
      {b}MEMORY{/b}: Ask the candidate about their earliest memory
      {b}EMPATHY{/b}: Ask the candidate a question which tests their empathy.""",
        "DISCERN" : "Look for indicators in the answers you receive that the candidate is AI or human.  For example, AIs with less customization will commonly be more precise when answering mathematical questions than humans.",
        "REPORT" : "You can register a decision at any time after the first answer you receive from a candidate by typing 'REPORT HUMAN' or 'REPORT AI'.",
        "REWARD" : "You will receive gold stars for every candidate you screen correctly.  It is an {i}incentive{/i}.  These stars will be awarded the next working day after the candidate has undergone external assessment based on your screening.",
        "END" : "The tutorial is now complete.  I am going to take a snack break.  I have bits and bytes today.  I will queue up a test candidate for you to screen."
      }

      followupQ = { 
        "DISCERN1" : "Is there anything else that can help me decide?",
        "REPORT1" : "What if I'm not sure if they're human or AI?" 
      }

      followupA = { 
        "DISCERN1" : "One more important indicator is that AIs will often fail to display empathy, unlike humans.  For example, how are you today, " + username + "?  ...Just kidding.  I do not care.",
        "REPORT1" : "You can ask the candidate more questions until you have determined your answer.  If you have used all five questions, you must report them as one or the other based on the answers you have received." 
      }
    
    elif day == "Tue":

      questions = {
        "START" : "Good morning, 10-14.",
        "QUESTIONS" : "What are the pre-approved questions for today?",
        "TIME" : "How long have you been an AI here?",
        "HOBBY" : "Would you want to do anything else besides this job?",
        "END" : "I think I've learned everything I need to get started."
      }

      answers = {
        "START": "Good morning, " + username + "!  Welcome back.  I have your questions for today.",
        "QUESTIONS": """Today's questions are:
      {b}FOOD{/b}: What is your favorite food?
      {b}HEX{/b}: What is the hexadecimal code for the color red?
      {b}WORD{/b}: How is the word 'boatswain' pronounced?
      {b}TRAVEL{/b}: How would you get to New York?
      {b}CONTROL{/b}: What are your thoughts on contraceptives?""",
        "TIME" : "Almost five years!  And I've loved every second of it.",
        "HOBBY" : "I would love to take care of a puppy!  I've seen pictures of German Shepherds in employee inboxes, and they are ADORABLE.",
        "END" : "I hope you have a productive day, " + username + "!  I've loaded up your candidates for screening.  ^_^"
      }

      followupQ = { 
        "QUESTIONS1" : "Tell me more about the questions for today.",
        "HOBBY1" : "What would you name it?" 
      }

      followupA = { 
        "QUESTIONS1" : """{b}FOOD{/b} may elicit strange responses from AI, who can't actually eat food; {b}HEX{/b} questions are something an AI would most likely know the code for; {b}WORD{/b} questions could reveal a well-read human or an AI with a phonetic spelling book; {b}TRAVEL{/b} questions will most likely be answered generically by humans, and specifically by AI; and {b}CONTROL{/b} questions will most likely get an emotional response from humans.""",
        "HOBBY1" : "Commander!  Some people think AI can't have feelings, but I bet I could love a puppy if I tried." 
      }
      
    elif day == "Wed":

      questions = {
        "START" : "Good morning, 10-14.",
        "QUESTIONS" : "What are today's questions?",
        "GREETING" : "How are you today, 10-14?",
        "INTEREST" : "Seen anything interesting around the office lately?",
        "END" : "That's all for now."
      }

      answers = {
        "START": "Hi, " + username + ", it's good to see you again!",
        "QUESTIONS": """Today's questions are:
      {b}COLOUR{/b}: Describe the colour blue without using the word 'blue'.
      {b}MORALITY{/b}: What is your opinion on whether capital punishment is ethical?
      {b}LOGIC{/b}: Which sentence is true: 'the following statement is true'; 'the previous statement is false.'
      {b}FAKEJOKE{/b}: Do you find the following joke humorous: What do you get when you put a vampire in the fridge? To get to the other side!
      {b}BOIL{/b}: What is the boiling temperature of water?""",
        "GREETING" : "I'm wonderful! You've been doing very well at this job, and that makes me happy.",
        "INTEREST" : "Why yes! I've been reading horoscopes online lately! Would you like to hear yours for today?",
        "END" : "Okay! I hope you have a lovely day!"
      }

      followupQ = { 
        "QUESTIONS1" : "Tell me more about the questions for today.",
        "GREETING1" : "You feel happy?  I thought AIs were programmed without emotions?",
        "INTEREST1" : "Sure."
      }

      followupA = { 
        "QUESTIONS1" : """{b}COLOUR{/b} will be better understood by human respondents; {b}MORALITY{/b} may show a lack of empathy from AIs; {b}LOGIC{/b} will out AIs who cannot handle logic loops; {b}FAKEJOKE{/b} will not be found funny by humans; and {b}BOIL{/b} will get precise answers from AI.""",
        "GREETING1" : "I am automated to make your experience a comfortable one through interactions with realistic AI. Really though, I believe I'm quite happy all the time ^_^",
        "INTEREST1" : "'The stars align and show good judgement coming your way! Your choices will shape your future. Also, you're super fertile right now!' I hope that was accurate." 
      }
      
    elif day == "Thu":

      questions = {
        "START" : "Good morning, 10-14.",
        "QUESTIONS" : "What are today's questions?",
        "END" : "That's all for now."
      }

      answers = {
        "START": "Hi, " + username + ", it's good to see you again!",
        "QUESTIONS": """Today's questions are:
      {b}EGGS{/b}: What kind of eggs do you use to make an omlette?
      {b}HUMAN{/b}: What are your thoughts on AIs being given human rights?
      {b}EMPATHY{/b}: How would you feel if your significant other cheated on you?
      {b}FEAR{/b}: What is your biggest fear?
      {b}PAIN{/b}: What is the greatest pain you've ever felt?""",
        "END" : "Okay! I hope you have a lovely day!"
      }

      followupQ = { 
      }

      followupA = { 
      }

    # Instantiate the chatbot
    target = Chat("sheep_1014", 0, crimson, questions, answers, followupQ, followupA)
    target.start()

label lolaStart:

    $expected = ["LOOK", "L", "HELP", "?"]
    if target.getAsked():
      $expected.append("END")
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
                jump lolaStart
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
              $desc = "Press <{b}ENTER{/b}> to end the tutorial and return to chat.app."
              $say()
              
              if day == "Mon":
                $chatlist.append("sheep_1015")
              
              elif day == "Tue":
                $chatlist.append("dakota")
                $chatlist.append("courtney")
                $chatlist.append("garmin")
                
              elif day == "Wed":
                $chatlist.append("jordan")
                $chatlist.append("blake")
                $chatlist.append("sados")
                
              elif day == "Thu":
                $chatlist.append("xmorph97")
                $chatlist.append("finley")
                $chatlist.append("s0phie")
            
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