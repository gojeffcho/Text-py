label chat_2_test:
  $username = "chell"

label l0_16:
  python: 
    questions = {
      "MATH" : "What is the square root of 17?", 
      "REALJOKE" : "Do you find the following joke humerous: What do you call cheese that isn't yours? Nacho Cheese.", 
      "FAKEJOKE" : "Do you find the following joke humerous: Where do cows go for first dates? Orange you glad I didn't say banana?", 
      "MEMORY" : "What is your earliest memory?", 
      "EMPATHY" : "How do you feel when you hear the sound of a baby crying?"   
    }

    answers = {
        "MATH" : "About 4.",
        "REALJOKE" : "Not really.",
        "FAKEJOKE" : "I don't think you told that joke right.",
        "MEMORY" : "Benny Jenson punching me straight in the gut in the first grade.",
        "EMPATHY" : "Annoyed. Kids drive me nuts."
    }

    followupQ = {
        "FAKEJOKE1" : "How do you tell it right?",
        "MEMORY1" : "Why did Benny Jenson do that?",
        "EMPATHY1" : "What would you do?",
    }

    followupA = {
        "FAKEJOKE1" : "IDK... something like, where do cows go on dates?... The 'moo'vies. Probably.",
        "MEMORY1" : "I don't want to talk about it.",
        "EMPATHY1" : "I would try to make the kid stop crying."
    }

    target = Chat("l0_16", 1, "87ceeb", questions, answers, followupQ, followupA)
    target.start()

label chat2Start:

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
        jump l0_16
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