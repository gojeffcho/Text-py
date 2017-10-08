label set_username:
    python:
        set_username(argument)
    return

label wait:
    if inputv == "":
        $flush_input()
        term "{cps=125}{color=#f00}Error{/color}: Please enter a command."
        
    else:
        python:
            s = inputv 
            flush_input()
            term("{cps=125}'[s]': {color=#f00}command not found{/color}.  Type 'help' or '?' for available commands.")
    return
    
    
label help:
    python:
        if len(argument) > 0:
            s = inputv
            flush_input()
            term("{cps=125}Command '" + s + "' takes no additional arguments.")
        
        else:
            flush_input()
            term("{cps=125}Available commands: <{color=#faebd7}" + "{/color}>, <{color=#faebd7}".join(expected) + "{/color}>{/cps}")
    return
