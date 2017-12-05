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

        # Random filler between words
        def filler():
            aString = ""
            extraChars = ["#", "%", "$", "&", "@"]
            for i in range(0,11):
                choose = randint(0,4)
                aString += extraChars[choose]
            return aString

        # Counting Correct and right but wrong spots
        def isCorrect(picked, real):
            # Set up dict
            # List [inReal, correct, wrongSpot]
            aDict = {}
            for let in real:
                if let not in aDict:
                    aDict[let] = [1,0,0]
                else:
                    aDict[let][0] += 1

            # Run through picked
            for i in range(0,5):
                counter = 0
                #hasFound = False
                # correct spot
                if picked[i] == real[i]:
                    aDict[picked[i]][1] += 1
                # check for wrong spot
                else:

                    # Check to make sure only enter once
                    if picked[i] in aDict:
                        check = aDict[picked[i]][0]
                        other = aDict[picked[i]][2]
                        if other >= check:
                            continue
                        else:
                            aDict[picked[i]][2] += 1

            # collect data (There was probably an easier way to do this)
            correct = 0
            wrongSpot = 0
            for key in aDict:
                correct += aDict[key][1]
                wrongSpot += aDict[key][2]

            return correct, wrongSpot


                


        # List of 6 letter words
        wordList = ["apples", "hacked", "fallen", "ravage", "wonder", "labels", "tested", "listen", "savage"]
        extraChars = ["#", "%", "$", "&", "@"]
        shuffle(wordList)
        secretWord = wordList[0].lower()
        shuffle(wordList)

        # Random garbage
        garbString = ""

        for i in range(0,6):
            chose = randint(0,4)
            garbString += extraChars[chose]

        # Build desc
        count = 1
        desc = "|" + " " + filler() + " " + wordList[0] + " " + filler() + " " + wordList[1]
        for word in wordList:
            if count < 3:
                count += 1
            elif word == wordList[-1]:
                desc +=  " "+ filler() + " " + word + " " + filler() + " |\n"
            elif count % 3 == 0:
                desc +=  " "+ filler() + " " + word + " " + filler() + " |\n" + "|"
                count += 1
            else:
                desc += " " + filler() + " " + word
                count += 1

        # save orginal list        
        orgDesc = deepcopy(desc)
        desc = "Correctly guess the password from the options beblow, type 'help' for assistance: \n" + orgDesc + "\n"
        desc += "The correct word is: " + secretWord
        say()
    jump hackstart


    label hackstart:

    while True:
        $echo()

        if cmd.lower() == "help":
            $flush_input()
            nvl clear
            $desc = "To give up type 'quit', to brute force the password type 'force'\n"
            $desc += orgDesc
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
            $desc = ". . .\n"
            $desc += "Brute Force Successful"
            $hack_result(True)
            $say()
            $flush_input()
            nvl clear

            return

        elif len(cmd.lower()) == 0 or cmd.lower() == " ":
            $desc = "Invalid input"
            $say()

        else:
            $desc = "Incorrect... Please try again\n"
            python:
                correct = 0
                guessed = cmd
                desc += "Len: " + str(len(guessed)) + "\n"

                if len(guessed) != len(secretWord):
                    desc += "Invalid guess, enter one of the words on the screen\n"
                    say()

                else:
                    try:
                        correct, wrong = isCorrect(guessed, secretWord)
                        desc += "Correctly guess letters: " + str(correct) + "\n"
                        desc += "Right letter wrong place: " + str(wrong) + "\n"
                        say()

                    except:
                        desc += "Invalid guess, please try again\n"
                        say()


