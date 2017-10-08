label e_boss0:
    $expected = ["look", "l", "help", "?", "reply", "exit"]
    $pickup = []
    $room = "Email"
    $desc = """{color=#faebd7}{cps=150}
    TO: [username]@electricsheep.inc
    FROM: BOSS
    RE: Welcome to the team!

    Well hello there,

    Welcome, [username]! Your employee number is 4141. 

    Here at Electric Sheep Incorporated, we strive for greatness amongst our employees. Allow me to officially welcome you to the team, and congratulate you on the completion of your first Turing test. 

    As you continue in your career, mistakes will be made. I need you to know that mistakes happen, but in order to minimize them, we ask that you apply valid critical thought and appropriate decision making when categorizing participants as either human, or AI. 

    After all, you're changing lives here. We all are.

    Welcome to the team, 

    Boss{/cps}{/color}

Type {b}reply{/b} to reply to the email, or {b}exit{/b} to quit."""
    
    $say()
    
    while True:
        $echo()
        
        if cmd not in expected:
            python:
                eastered = False
                for word in easters:
                    if cmd == word or args == word or word in args:
                        easter(word)
                        eastered = True
                
                if not eastered:
                    input_error()
        
        elif cmd == "look" or cmd == "l":
            if len(args) == 0:
                $flush_input()
                nvl clear
                jump e_boss0
            else:
                $has_args()
                
        elif cmd == "help" or cmd == "?":
            $help()
            
        elif cmd == "exit":
            if len(args) == 0:
                $flush_input()
                $desc = "Closing email{cps=2}... ... ... Done.{/cps} \n" \
                        "Press {b}ENTER{/b} to return to mail.app."
                $say()
                
                nvl clear
                jump mail
            else:
                $has_args()
        
        elif cmd == "reply":
            
            # TODO: Implement
            $flush_input()
            $desc = "You replied to the email."
            $say()
                    
    return