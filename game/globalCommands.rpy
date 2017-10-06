label set_username:
    python:
        set_username(argument)
    return

label wait:
    if inputv == "":
        $flush_input()
        e "{fast}{color=#f00}Please enter a command.{/color}"
        
    else:
        python:
            s = inputv 
            a = " ".join(argument)
            if a != "":
                s = s + " " + a 
            e("{fast}'[s]': {color=#f00}command not found{/color}.  Type 'help' or '?' for available commands.")
    return
    
    
label help:
    python:
        string = "Available commands: <" + ">, <".join(expected) + ">"
        flush_input()
        e("{fast}" + string)
    return
