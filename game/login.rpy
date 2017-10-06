# LOGIN: first day login prompt
label login_first:
    $expected = ["help", "?", "new"]
    $pickup = []
    $room = "Electric Sheep Co. - New User"
    $desc = """{cps=0}
     ______          _____       _____       
________  /____________  /__________(_)______
_  _ \_  /_  _ \  ___/  __/_  ___/_  /_  ___/
/  __/  / /  __/ /__ / /_ _  /   _  / / /__  
\___//_/  \___/\___/ \__/ /_/    /_/  \___/  
     _                       _            
 ___| |__   ___  ___ _ __   (_)_ __   ___ 
/ __| '_ \ / _ \/ _ \ '_ \  | | '_ \ / __|
\__ \ | | |  __/  __/ |_) | | | | | | (__ 
|___/_| |_|\___|\___| .__/  |_|_| |_|\___|
                    |_|                            
{/cps}
Welcome, new user!  

Please type {b}new{/b} to set up your account.  You can type {b}help{/b} or {b}?{/b} at any time to see the list of commands available to you."""
    
    $say()
    
    while True:
        $echo()
        
        if inputv not in expected:
            call wait from _call_wait_login
        
        elif inputv == "help" or inputv == "?":
            call help from _call_help_login
            
        elif inputv == "new":
            if len(argument) == 0:
                $flush_input()
                nvl clear
                jump login_new
            else:
                call wait from _call_wait_login_3
            
    return
    
# LOGIN: login new user
label login_new:
    $flush_input()
    $expected = ["help", "?", "create"]
    $pickup = []
    $room = "Electric Sheep Co. - Create New User"
    $desc = """{cps=0}
     ______          _____       _____       
________  /____________  /__________(_)______
_  _ \_  /_  _ \  ___/  __/_  ___/_  /_  ___/
/  __/  / /  __/ /__ / /_ _  /   _  / / /__  
\___//_/  \___/\___/ \__/ /_/    /_/  \___/  
     _                       _            
 ___| |__   ___  ___ _ __   (_)_ __   ___ 
/ __| '_ \ / _ \/ _ \ '_ \  | | '_ \ / __|
\__ \ | | |  __/  __/ |_) | | | | | | (__ 
|___/_| |_|\___|\___| .__/  |_|_| |_|\___|
                    |_|                       
{/cps}                        
We're {cps=50}thrilled to have you join our company!{/cps}  Let's create your account.  Please type {b}create{/b} followed by your desired username to create your login.
    
Example: {b}> create shelby{/b}"""

    $say()
    
    while True:
        $echo()
        
        if inputv not in expected:
            call wait from _call_wait_login_2
        
        elif inputv == "help" or inputv == "?":
            call help from _call_help_login_2
        
        elif inputv == "create":

            if len(argument) == 1:
                $set_username(argument[0])
                $desc = "{cps=15}Your username has been set to {u}" + username + "{/u}.  {b}Please remember this username{/b} as you will use it to log in each day along with your bio-authentication.\n\nPress {b}<ENTER>{/b} to continue when you are ready.{/cps}"
                $say()
                $flush_input()

                nvl clear
                
                jump login

            else:
                $desc = "{color=#f00}Error{/color}: Please enter a valid username."
                $say()
    
    return
    
# LOGIN: regular login prompt
label login:
    $expected = ["help", "?", "login"]
    $pickup = []
    $room = "Electric Sheep Co. - Login"
    $desc = """{cps=0}
     ______          _____       _____       
________  /____________  /__________(_)______
_  _ \_  /_  _ \  ___/  __/_  ___/_  /_  ___/
/  __/  / /  __/ /__ / /_ _  /   _  / / /__  
\___//_/  \___/\___/ \__/ /_/    /_/  \___/  
     _                       _            
 ___| |__   ___  ___ _ __   (_)_ __   ___ 
/ __| '_ \ / _ \/ _ \ '_ \  | | '_ \ / __|
\__ \ | | |  __/  __/ |_) | | | | | | (__ 
|___/_| |_|\___|\___| .__/  |_|_| |_|\___|
                    |_|                            
{/cps}
Please type {b}login <username>{/b} to log in, or {b}help{/b} for a list of available commands."""
    
    $say()
    
    while True:
        $echo()
        
        if inputv not in expected:
            call wait from _call_wait_login_1
        
        elif inputv == "help" or inputv == "?":
            call help from _call_help_login_1
        
        elif inputv == "login":
            if len(argument) == 1:
                if argument[0] == username:
                    $desc = "Press and hold {b}<ENTER>{/b} for one second for bioauthentication..."
                    $say()
            
                    $desc = "{color=#00f}Login successful{/color}!  Welcome, " + username + ".  Press {b}<ENTER>{/b} to proceed."
                    $say()
                    $flush_input()
                    nvl clear
                    jump mainscreen
                                    
                else:
                    $desc = "{color=#f00}Error{/color}: Incorrect login '" + " ".join(argument) + "'!  Please try again."
                    $say()
            elif len(argument) == 0:
                $desc = "{color=#f00}Error{/color}: You must supply a username after {b}login{/b}."
                $say()
            else:
                $desc = "{color=#f00}Error{/color}: Please type {b}login <username>{/b} to log in.  Your username is only one word."
                $say()
            
    return
