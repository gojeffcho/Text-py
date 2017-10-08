init 0 python:

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
        args = ""

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
            term("{cps=125}{color=#f00}Error{/color}: Please enter a command.")
        
        else:
            s = cmd 
            flush_input()
            term("{cps=125}'" + s + "': {color=#f00}command not found{/color}.  Type 'help' or '?' for available commands.")
        return
    
###
### help(): called when 'help' or '?' is entered.
###    
    def help():
        if len(args) > 0:
            s = cmd
            flush_input()
            term("{cps=125}Command '" + s + "' takes no additional arguments.")
    
        else:
            flush_input()
            term("{cps=125}Available commands: <{color=#faebd7}" + "{/color}>, <{color=#faebd7}".join(expected) + "{/color}>{/cps}")
        return


###
### has_args(): called when a command that takes no arguments is given arguments
###        
    def has_args():
        s = cmd
        flush_input()
        term("{cps=125}Command '" + s + "' takes no additional arguments.")
        
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
        term("Watch your language.")
        
        return

###
### update_avails(): updates numChats and numEmails
###
    def update_avails():
        global numChats
        global numEmails
        numChats = len(chatlist)
        numEmails = len(emaillist)
        
        return
        
###
### add_time(): increments time
###
    def add_time():
        global hour
        global min
        global ampm
        global append
        increment = 30      # Must not be greater than 59
        
        # Hour cycles to the next hour
        if (min + increment) > 59:
            hour = hour + 1
            min = (min + increment) % 60
            
            if hour > 11:
                ampm = "pm"
            
            if hour > 12:
                hour = hour - 12
        
        # Otherwise, just add the minute
        else:
            min = min + increment
            
        # Check for end of day condition
        if hour == 5 and ampm == "pm":
            term("{color=#f00}WARNING:{/color} no employee is permitted access to the system after 5:00 pm.  System will now begin auto-logout procedures.")
            # TODO: call end day function
            
        elif hour == 4 and ampm == "pm":
            term("{color=#ffd700}REMINDER {/color}: Company policy requires that you log out by 5:00 pm.{nw}")
            append = "{color=#ffd700}REMINDER {/color}: Company policy requires that you log out by 5:00 pm.{nw}"
        
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
        