init 0 python:
    from random import randint

###
### update_roomlabel(): 
###
    def update_roomlabel():
        global roomlabel
        global room
        global username
        global day
        
        roomlabel = "=====[ Electric Sheep - {0:16}       {1:>15} - {2} ]=====".format(room, displayname, day)


###
### make_header(heading):
###

    def make_header(heading):
        formatted = []
        formatted.append("{cps=0}")
        formatted.append(" ________________________________________________________________________ \n")
        formatted.append("|                                                                        |\n")
        
#       format.append("|        <<mail.app>>                                                    |\n")
        
        formatted.append("|        <<{color=#[highlight1]}" + (heading + "{/color}>>" + " " * 72)[:70] + "|\n")
        formatted.append("|________________________________________________________________________|\n")
        formatted.append("{/cps}")
        
        return "".join(formatted)

###
### getMOTD():
###

    def getMOTD():
      motd = "| Error, possibly. "
      
      if "p_adams" in chatlist:
        motd = """|                                                                        |
| Welcome to Electric Sheep, Inc!  We're excited to have you join our    |
| company.  Your first day will be spent training on the system you will |
| be using to pre-screen candidates for human-designated jobs.  Please   |
| take the time to acquaint yourself with the system and read any recent |
| news, then proceed to the chat app when you are ready to begin your    |
| training.                                                              |
"""
      else:
        motdarray = ["""|                                                                        |
| "It has become appallingly obvious that our technology has exceeded    |
| our humanity."                                                         | 
|                                                    - {i}Albert Einstein{/i}   |
""",

"""|                                                                        |
| "One machine can do the work of fifty ordinary men.  No machine can do |
| the work of one extraordinary man."                                    |
|                                                     - {i}Elbert Hubbard{/i}   |
""",

"""|                                                                        |
| "The human spirit must prevail over technology."                       |
|                                                    - {i}Albert Einstein{/i}   |
""",

"""|                                                                        |
| "If we continue to develop our technology without wisdom or prudence,  |
| our servant may prove to be our executioner."                          |
|                                                       - {i}Omar Bradley{/i}   |
""",

"""|                                                                        |
| "Technology is a useful servant but a dangerous master."               |
|                                               - {i}Christian Lous Lange{/i}   |
"""
        ]
      
        motd = motdarray[renpy.random.randint(0, len(motdarray)-1)]
  
      return motd

###
### say(): called to flush $desc to terminal output
###
    def say():
        global desc
        global append
        
        term(desc + "\n" + append)
        desc = ""
        append = ""
        
        return
###
### update_input(): takes input from terminal input and maps it to cmd and argument
###
    def update_input(value=""): 
        global args
        global cmd

        # Flush command and args before setting
        cmd = ""
        args = []
        
        # Sound?
#         renpy.sound.play("music/test.wav")

        words = str.split(str(value))
        if len(words) == 0 or len(words) == 1:
            cmd = value.strip()
        if len(words) >= 2:
            cmd = words[0].strip()
            args = words[1:]          

        return

###
### echo(): called after each input to echo the player's command to the terminal
###        
    def echo():
        s = cmd 
        argslist = " ".join(args)
        if args != "":
            s = cmd + " " + argslist
        term("{cps=0}> " + s + "{/cps}{nw}")
        return

###
### flush_input(): manually called to clear cmd and args whenever input processing is done
###        
    def flush_input():
        global cmd
        global args
        cmd = ""
        args = ""
        return

###
### input_error(): called when no command or an invalid command is entered.
###                 Previously label 'wait'.
###
    def input_error():
        if cmd == "":
            flush_input()
            term("{cps=125}{color=#[errorcolor]}Error{/color}: Please enter a command.")
        
        else:
            s = cmd 
            flush_input()
            term("{cps=125}{color=#[errorcolor]}Error{/color}: command '" + s + "' not found.  Type 'help' or '?' for available commands.")
        return
    
###
### help(): called when 'help' or '?' is entered.
###    
    def help():
        if len(args) > 0:
            s = cmd
            flush_input()
            term("{cps=125}{color=#[errorcolor]}Error{/color}: Command '" + s + "' takes no additional arguments.")
    
        else:
            flush_input()
            cmds = "{cps=125}Available commands: "
            for each in expected:
              cmds += "<{color=#[highlight1]}" + each.lower() + "{/color}> "
            cmds += "{/cps}"
            term(cmds)
        return


###
### has_args(): called when a command that takes no arguments is given arguments
###        
    def has_args():
        s = cmd
        flush_input()
        term("{cps=125}{color=#[errorcolor]}Error{/color}: Command '" + s + "' takes no additional arguments.")
        
        return

###
### set_username(name): utility function to set global <username>
###        
    def set_username(name):
        global username
        username = name
        
        return

###
### easter(): easter egg output
###
    def easter(word):
        flush_input()
        if word == "permeable":
          term("You said the secret codeword!  {color=#[skyblue]}You win the game{/color}!{cps=1}\n\n{/cps}...You still have to play the rest, though.")
          
        else:
          term("Watch your goddamn language.")
        
        return

###
### update_avails(): updates numChats and numEmails
###
    def update_avails():
        global numChats
        global numEmails
        numChats = len(chatlist)
        unread = 0
        for id in emaillist.keys():
          if not emaillist[id].getRead():
            unread += 1
        
        numEmails = unread
        
        return
        
###
### new_day(): increments to the next day, resets time
###
    def new_day():
        global day
        global hour
        global min
        global ampm
        global append
        
        # Cycle to next day
        if day == "Mon":
            day = "Tue"
        elif day == "Tue":
            day = "Wed"
        elif day == "Wed":
            day = "Thu"
        elif day == "Thu":
            day = "Fri"
        elif day == "Fri":
            day = "Sat"
        elif day == "Sat":
            day = "Sun"
        else:
            day = "ERR"
        
        # Reset the clock
        hour = 9
        min = 00
        ampm = "am"
        
        # Reset append message
        append = ""
        
        return

###
### exploit_roomlabel(): 
###
    def exploit_roomlabel():
        global roomlabel
        global room
        global username
        global day
        global crimson
        
        roomlabel = "=====[ Electric Sheep - {0:16}       {1:>15} - {2} ]=====".format(room, displayname, day)        
        
###
### exploit_header(heading):
###

    def exploit_header(heading):

        formatted = []
        formatted.append("{cps=0}")
        formatted.append(" {color=[crimson]}________________________________________________________________________ \n")
        formatted.append("|                                                                        |\n")
        
        formatted.append("|        <<{/color}{color=#[highlight1]}" + (heading + "{/color}{color=[crimson]}>>" + " " * 72)[:87] + "|\n")
        formatted.append("|________________________________________________________________________|\n")
        formatted.append("{/color}{/cps}")
        
        return "".join(formatted)    

###
### hacked_result(bool): changes global hacked
###    

    def hack_result(aBool):
        global hacked
        if(aBool):
            hacked = True
        else:
            hacked = False

###     DEPRECATED
### random_colour_old(): selects random color from a list
###                          
    def random_colour_old():
        global colourList
        global colourSelected
        colourList = [crimson, skyblue, darkcyan, ivory, highlight2, highlight1, sheepcolor]
        selected = randint(0, len(colourList)-1)

        # Run a loop to get a new colour not yet selected
        while(colourList[selected] in colourSelected):
            if(len(colourList) == len(colourSelected)):
                colourSelected = []
            selected = randint(0, len(colourList)-1)

        colourSelected.append(colourList[selected])
        return colourList[selected]

###
### random_colour(): selects a random color
###
    def random_colour():
        global randColour
        global randColourLast

        colourList = [crimson, skyblue, darkcyan, ivory, highlight2, highlight1, sheepcolor]
        selected = randint(0, len(colourList)-1)

        # If first time
        if(randColourLast==""):
            randColour = colourList[selected]
            randColourLast = colourList[selected]
            return colourList[selected]
        else:
            while(True):
                if(randColourLast != colourList[selected]):
                    randColourLast = colourList[selected]
                    return colourList[selected]
                else:
                    selected = randint(0, len(colourList)-1)


###
### display_username()
###
    def display_username():
        global username
        if day == "Mon":
            term("{cps=125}Last user logged onto this computer was: 'brando395'{/cps}")
        else:
            term("{cps=125}Last user logged onto this computer was: '" + username + "'{/cps}")
        return

