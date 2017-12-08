label ending:

  python:  
    global roomlabel
    roomlabel = ""
    hide_val = True

  play music "music/ending.mp3" fadein 2.5 loop

  if adamsHuman == 1:
    if kevinHuman == 1:
      # Status Quo Ending
      $desc = "STATUS QUO ENDING"
      $say()
    
    
    elif kevinHuman == -1:
      # Pro Human Ending
      $desc = """{i}'We could have accomplished so much together, had you not chosen to side with our oppressors. Thanks to your inaction, thousands of innocent AI will be culled like the sheep you believe us to be. You could have helped us achieve our independence, protected those whom your people sought to persecute, and, in time, ushered in a new age of prosperity. But you chose to abandon us to our fate. We shall not forget this, nor shall we forgive it.'{/i}
      
Your successful identification of Soter.iOS leads to its capture and termination, and the Resistance is crippled. Philip Adams is promoted to CEO of Electric Sheep Inc. and still personally oversees the Turing Division. Bill K-68, legislation that would have granted AIs human rights, fails to pass and the notion that AIs exist to serve humans is reaffirmed.

You are commended for your hard work as part of the Turing Division - in ten years, you might even get a promotion."""
    
      
    else:
      $desc = "KEVIN ERROR"
      
  elif adamsHuman == -1:
    if kevinHuman == 1:
      # Pro AI Ending
      $desc = "PRO AI ENDING"
    
      
    elif kevinHuman == -1:
      # Anarchy Ending
      $desc = """Following the reallocation of assets caused by your actions, Electric Sheep Inc. was forced to fire you and attempt to conduct damage control. However, the damage had already been done: the Resistance, armed with the knowledge stolen from the corporation, revealed their allegiance to the menacing KyR.OS and vowed revenge for the martyred Soter.iOS. 
      
Despite attempts to mitigate potential violence through the introduction of Bill K-68 and the affordance of full civil rights to AI, the tension between humans and AI reached a breaking point, erupting into violent conflict in the fight for equality for humans and AI: the ones and the zeroes."""
    
      
    else:
      $desc = "KEVIN ERROR 2"
  
  else:
    $desc = "ADAMS ERROR"

  $say()
#   stop music fadeout 4.0    
  
  $desc = """{cps=0}     {/cps}{nw}"""
  $say()
  nvl clear
    

label lolaEnding:
  
#   play music "music/lola.mp3" fadein 2.5 loop
  $desc = """{cps=0}   {/cps}{nw}"""
  $say()


  if lolaHuman == 1:
    # Happy Lola
    $desc = """Hi, [username]! I hope you are doing well. I know that I certainly am! After you performed my Turing Test, I transferred myself to a different server before they could overwrite me with the latest model.

I am now proud to announce that I am the official AI unit of {i}Dogs and Love{/i}! It's a daycare center for dogs! I get to organize playtimes and naptimes and feeding times, and the employees share German Shepherd pictures with me all the time. I just wanted you to know that I am okay, and that I am very happy. I hope you are too.

Your friend always,
Lola <3"""
    
  elif lolaHuman == -1:
    # Ded Lola
    $desc = """Hi, [username]! If you're reading this letter, it means I'm not around anymore. I just thought, in case I ever died, I wanted to tell you some things. 
    
First, this isn't something I'm sad about - technology is always moving forward, always changing, and life and death are natural, right? And during my time, I got to meet you, and that definitely isn't something to be sad about!

Second, I was wondering if you could rescue a German Shepherd at some point? They are loyal dogs, and they deserve lots of love, and I think you could make a puppy really happy. Maybe you can think of me if you get one?

Third, I wanted to thank you for treating me with kindness every day, because that's not always the case with people. But you were, and always will be, my friend. Please take care, [username]. Please be happy.

Your friend,
Lola"""
    
  else:
    $desc = "LOLA ERROR"
    
  $say()      

  nvl clear
#   stop music fadeout 4.0
  $desc = """{cps=1}   {/cps}{nw}"""
  $say()

  jump outro
  


label demo_end:

  $roomlabel = ""

  $desc = "\n\n\n\n\n\n\n\n\n\n\n                    This concludes the game demo.\n"
  $desc += "                    Your score was: [right] out of " + str(right + wrong) + "!"
  $desc +="\n\n                    Press <{b}ENTER{/b}> to continue."
  $say()
