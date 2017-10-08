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
        
#         for word in easters:
#             if len(args) == 0:
#                 if word == cmd:
#                     term("That's not very nice.")
#                     flush_input()
#             elif len(args) == 1:
#                 if word == args:
#                     term("That's not very nice.")
#                     flush_input()
#             else:
#                 if word in args:
#                     term("That's not very nice.")
#                     flush_input()


###
### echo(): called after each input to echo the player's command to the terminal
###        
    def echo():
        s = cmd 
        argslist = " ".join(args)
        if args != "":
            s = cmd + " " + argslist
        term("{cps=0}> " + s + "{/cps}{nw}")

###
### flush_input(): manually called to clear cmd and args whenever input processing is done
###        
    def flush_input():
        global cmd
        global args
        cmd = ""
        args = ""

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

###
### set_username(name): utility function to set global <username>
###        
    def set_username(name):
        global username
        username = name

###
### easter(): easter egg output
###
    def easter(word):
        flush_input()
        term("Watch your language.")

