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


    $room = "##_HACK.EXE_##"
    $update_roomlabel()

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
        startDesc = deepcopy(desc)
        desc = " "+"_"*70 +'\n' + "| Correctly guess the password from the options beblow:" +" "*16 +"|\n" + "| Type Help to see a list of commands." + " "*32 +" | \n"+ "|"+ "_"*70+"|\n" +startDesc
        desc +="|" + "-"*70 + "|\n"
        desc +="| Available Commands: "+ " "*49 + "|\n"
        desc += "|      <{color=#"+ crimson + "}" + "'WORD'" +"{/color}>:  Type the word you believe is correct" + " "*17 + "|\n"
        desc += "|      <{color=#" + crimson + "}"+"FORCE" + "{/color}>:   Program will automatically try every possiblity" + " "*6 +"|\n"
        desc += "|      <{color=#" +  crimson +"}QUIT"+  "{/color}>:    Exit the program" + " "*37 + "|\n"
        desc += "|      <{color=#" + crimson +"}GUESSED" "{/color}>: Shows the previously guessed words if forrgotten" + " "*5 + "|\n" 
        desc += " " + "-"*70 + "\n"

        # desc += "The correct word is: " + secretWord
        orgDesc = deepcopy(desc)
        fastDesc = "{cps=0}" + orgDesc + "{/cps}"
        say()
    jump hackstart


    label hackstart:

    $wordList = ["apples", "hacked", "fallen", "ravage", "wonder", "labels", "tested", "listen", "savage"]
    $guessedList = []
    $count = -1
    $sayGuessed = False
    while True:
        $count += 1
        if(count >= 2):
            nvl clear
            $desc = fastDesc 
            $say()
            $echo()
            $count = 0
        elif(sayGuessed):
            $sayGuessed = False
            $echo()
        else:
            $echo()

        if cmd.lower() == "guessed":
            $sayGuessed = True
            if len(wordList) != 0:
                $flush_input()
                nvl clear
                $count = 0
                $desc = fastDesc
                $desc += "Guessed words: "
                python:
                    for aWord in guessedList:
                        desc += str(aWord) + " "
                $say()

            else:   
                $flush_input()             
                nvl clear
                $desc = fastDesc
                $desc += "Currently no words have been guessed.\n"
                $say()

        elif cmd.lower() == secretWord.lower():
            $desc = garbString + " " + "CORRECT" + " " + garbString +"\n"
            $say()
            $hack_result(True)

            return

        elif cmd.lower() == "quit":
            $desc = garbString + " " + "{colour=#" + crimson + "}FAILED{/color}" + " " + garbString +"\n"
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
            $desc += "Invalid input"
            $say()

        else:
            $desc = "{color=#" + crimson + "}" + "INCORRECT{/color}\n"
            python:
                correct = 0
                guessed = cmd.lower()

                if len(guessed) != len(secretWord):
                    desc += "Invalid guess, enter one of the words on the screen\n"
                    flush_input()
                    say()

                elif guessed not in wordList:
                    desc += "Invalid guess, enter one of the words on the screen\n"
                    flush_input()
                    say()                    

                else:
                    try:
                        correct, wrong = isCorrect(guessed, secretWord)
                        desc += "Correctly guess letters: {color=#" + crimson +"}" + str(correct) + "{/color}\n"
                        desc += "Right letter wrong place: {color=#" + crimson + "}" + str(wrong) + "{/color}\n" 
                        if guessed not in guessedList:
                            guessedList.append(guessed)
                        flush_input()
                        say()

                    except:
                        desc += "Invalid guess, please try again\n"
                        flush_input()
                        say()


