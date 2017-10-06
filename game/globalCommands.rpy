label set_username:
    python:
        set_username(argument)
    return

label wait:
    if inputv == "":
#         $flush_input()
        e "{color=#f00}Please enter a command.{/color}"
        
    else:    
        $s = inputv
#         $flush_input()
        e "'[s]': {color=#f00}command not found{/color}.  Type 'help' or '?' for available commands."
    return
    
    
label help:
    python:
        string = "Available commands: <" + ">, <".join(expected) + ">"
#         flush_input()
        e(string)
    return
    
# TODO: REMOVE refactor
label inventory:
    $s = items
    $flush_input()
    e "I have [s] in my inventory right now."
    
    return 

# TODO: REMOVE refactor
label take:
    python:
        global items
        global pickup
        
        arg = argument
        flush_input()
        if arg == "":
            e("What am I taking?")
        elif arg not in pickup:
            e("There isn't a '[arg]' here.")
        elif arg in pickup:
            items += [arg]
            pickup.remove(arg)
            e("Added '[arg]' to inventory.")
    return

#TODO: REMOVE refactor
label use_failed:
    python:
        global argument
        global items
        
        if argument == "":
            flush_input()
            e("What am I using?")
        elif argument not in items:
            flush_input()
            e("I don't have that in my inventory. Are you thinking of another game?")
        elif argument in items:
            if argument == "echo":
                flush_input()
                e("A shrill voice from my side: 'Who are you callin' an item? You can't use me!'\nMaybe I should try 'echo'...")
            else:
                flush_input()
                e("I can't use that item right now.")

    return