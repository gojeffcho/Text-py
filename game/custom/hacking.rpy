$ """
    Currently 6 letter word will be chosen from a list of x words
    Game then displays all words

    Use call instead of jump to reach hackgame
$ """

init python:
    from random import shuffle
    from random import randint
    from copy import deepcopy

label hackgame:

    # This is a comment test
    python:
        # List of 6 letter words
        wordList = ["apples", "hacked", "fallen", "ravage", "wonder", "labels", "tested", "listen", "savage"]
        extraChars = ["#", "%", "$", "&", "@"]
        shuffle(wordList)
        secretWord = wordList[0].lower()
        shuffle(wordList)
        print("test")

        # Random garbage
        garbString = ""

        for i in range(0,6):
            chose = randint(0,4)
            garbString += extraChars[chose]

        # Build desc
        count = 1
        desc = "|" + " " + garbString + " " + wordList[0] + " " + garbString + " " + wordList[1]
        for word in wordList:
            if count < 3:
                count += 1
            elif count % 3 == 0:
                desc += " " + garbString + " " + word + " " + garbString + "|\n" + "|"
                count += 1
            else:
                desc += " " + garbString + " " + word
                count += 1

        # save orginal list        
        orgDesc = deepcopy(desc)
        desc = "Correctly guess the password from the options beblow, type 'help' for assistance: \n"
        say()
        desc = orgDesc
        desc = "The correct word is: " + secretWord
        say()
    jump hackstart


    label hackstart:

    while True:
        $echo()

        if cmd.lower() == "help":
            $flush_input()
            nvl clear
            $desc = "To give up type 'quit', to brute force the password type 'force'\n"
            $say()
            $desc = orgDesc
            $say()
        elif cmd.lower() == secretWord.lower():
            $desc = garbString + " " + "CORRECT" + " " + garbString +"\n"
            $say()
            $hack_result(True)

            return

        elif cmd.lower() == "quit":
            $desc = garbString + " " + "FAILED" + " " + garbString +"\n"
            $say()
            $hack_result(False)
            $flush_input()
            nvl clear

            return

        elif cmd.lower() == "force":
            $desc = ".\n"
            $say()
            $say()
            $say()
            $desc = "Brute Force Successful"
            $hack_result(True)
            $flush_input()
            nvl clear

            return
        elif cmd.lower() == "":
            $echo()
            $desc = "Invalid input"
            $say()
            $flush_input()

        else:
            $echo()
            $desc = "Incorrect... Please try again\n"
            $say()
            python:
                correct = 0
                theWord = secretWord.split()
                guessed = cmd.split()
                gLen = len(guessed)
                wLen = len(theWord)
                desc = "I make it here"
                say()
                if gLen != wLen:
                    desc = "Invalid guess, enter one of the words on the screen\n"
                    say()
                else:
                    try:
                        for i in range(0,6):
                            if guessed[i] == theWord[i]:
                                correct += 1
                        desc = "Correctly guess letters: " + correct + "\n"
                        say()

                    except:
                        desc = "Invalid guess, please try again\n"
                        say()
            $flush_input()
        $flush_input()



