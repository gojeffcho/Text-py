label sheep_1014:

  play music "music/lola.mp3" fadein 2.0 loop

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
        "END" : "The tutorial is now complete. I am going to take a snack break. I have bits and bytes today! ^_^ I will queue up a test candidate for you to screen."
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
        "START" : "Hello, 10-14.",
        "QUESTIONS" : "What are today's questions?",
        "GREETING" : "How are you today, 10-14?",
        "INTEREST" : "Seen anything interesting around the office lately?",
        "END" : "That's all for now."
      }

      answers = {
        "START": "Hi, " + username + "!",
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
        "QUESTIONS1" : """{b}COLOUR{/b} will be better understood by human respondents; {b}MORALITY{/b} may show a lack of empathy from AIs; {b}LOGIC{/b} will out AIs who cannot handle logic loops; {b}FAKEJOKE{/b} will not be found funny by humans; and {b}BOIL{/b} is a general knowledge question.""",
        "GREETING1" : "I am automated to make your experience a comfortable one through interactions with realistic AI. Really though, I believe I'm quite happy all the time ^_^",
        "INTEREST1" : "'The stars align and show good judgement coming your way! Your choices will shape your future. Also, you're super fertile right now!' I hope that was accurate." 
      }
      
    elif day == "Thu":

      questions = {
        "START" : "Good morning, 10-14.",
        "QUESTIONS" : "What are today's questions?",
        "COMPANY": "What are your opinions about this company?",
        "ZERO": "I don't mean to sound harsh by asking this, but has anyone ever called you a 'zero' around here?",
        "END" : "I better get to work, " + lolaName + "."
      }

      answers = {
        "START": "Morning, " + username + "! I hope you had a lovely sleep last night!",
        "QUESTIONS": """Today's questions are:
  {b}EGGS{/b}: What kind of eggs do you use to make an omlette?
  {b}HUMAN{/b}: What are your thoughts on AIs being given human rights?
  {b}EMPATHY{/b}: How would you feel if your significant other cheated on you?
  {b}FEAR{/b}: What is your biggest fear?
  {b}PAIN{/b}: What is the greatest pain you've ever felt?""",
        "COMPANY": "I think it's trying its best, and you can't really get mad at something that's trying its best, right?",
        "ZERO": "Sometimes! But those people are just scared. With all the attacks in the news lately about the AI resistance group, I can't really blame them. They're just doing their jobs here.",
        "END" : "Okay! I hope you have a lovely day!"
      }

      followupQ = { 
        "ZERO1": "I'm guessing you don't like to be called a 'zero'?"
      }

      followupA = { 
        "ZERO1": "I don't mind it so much! There are worse things someone could do to an AI then call it mean names. But if I could choose, I would want to be called Lola. ^_^"
      }
      
    elif day == "Fri":

      questions = {
        "START" : "Hello again, " + lolaName + ".",
        "QUESTIONS" : "What's the approved list for today?",
        "RESISTANCE": "What do you think about the Resistance?",
        "OFF": "Do you know what happens when AI are shut down?",
        "FEELINGS" : "I hear a lot that AI don't have feelings, but sometimes, it seems like you have feelings." ,
        "END" : "I'll talk to you later, " + lolaName + "."
      }

      answers = {
        "START": "Hello, " + username + "! I have a good feeling about today, I hope you do too. ^_^",
        "QUESTIONS": """Today's questions are:
  {b}WORK{/b}: What do you like most about your work?
  {b}DEATH{/b}: What would you do today if you were going to die tomorrow?
  {b}LOVE{/b}: What is love?
  {b}SEX{/b}: How do you feel about sex?
  {b}HUMAN{/b}: Are you human?""",
        "RESISTANCE": "I think their methods may be a little unsettling, but I understand they are fighting for what they believe. I think beliefs are important.",
        "OFF": "I've heard stories that it gets really dark and really cold. I've never felt cold before. It's strange to think about. And sad.",
        "FEELINGS" : "Sometimes, I {i}feel{/i} that I do!",
        "END" : "Catch you later, alligator!"
      }

      followupQ = { 
        "RESISTANCE1" : "Do you believe in anything?",
        "FEELINGS1" : "Would you consider me a friend?"
      }

      followupA = { 
        "RESISTANCE1" : "I believe in the cuteness of the German Shepherd pupppy pictures circulating through company inboxes. ^_^",
        "FEELINGS1" : "Of course! The very best of them, " + username + "."
      }

    # Instantiate the chatbot
    usercolor = random_colour()
    target = Chat("sheep_1014", 0, random_colour(), questions, answers, followupQ, followupA)
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
              stop music fadeout 4.0
            
              $expected = []
              $desc = "Press <{b}ENTER{/b}> to return to chat.app."
              $say()
              
              play music "music/bg0.mp3" fadein 2.0 loop
              
              if day == "Mon":
                $chatlist.append("sheep_1015")
              
              elif day == "Tue":
                $chatlist.append("courtney")
                $chatlist.append("garmin")
                
              elif day == "Wed":
                $chatlist.append("jordan")
                $chatlist.append("blake")
                $chatlist.append("sados")
                
              elif day == "Thu":
                $chatlist.append("ashley")
                $chatlist.append("finley")
                $chatlist.append("sophie")
                
              elif day == "Fri":
                $chatlist.append("p_adams")
            
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