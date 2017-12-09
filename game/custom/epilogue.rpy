label lolaEnding:
  
#   play music "music/lola.mp3" fadein 2.5 loop
#   $desc = """{cps=1}   {/cps}{nw}"""
#   $say()

  # Create the email interface
  $mail = "\n========== [[ Email: lola1] =============================================\n\n"
  $mail += "  {b}From{/b}: " 

  # Lola's email depends on how Lola was reported
  if lolaHuman == 1:
    $mail += "lola@dogsnluv.ca\n"
  else:
    $mail += "sheep_1014@auto.electricsheep.ca\n"
  $mail += "  {b}To{/b}: " 

  # Player's email depends on how Adams and Kevin were reported
  if adamsHuman == 1 and kevinHuman == -1:
    $mail += username[:5] + "713@electricsheep.ca\n"
  else:
    $mail += username + "@pers.mail.ca\n"
  $mail += "  {b}Subject{/b}: {i}Don't you forget me!{/i}\n\n"


  $desc = "{cps=100}" + mail + "{/cps}"
  $freeze = mail

  if lolaHuman == 1:
    # Happy Lola
    $text = """Hi, [username]! 
    
I hope you are doing well. I know that I certainly am! After you 
performed my Turing Test, I transferred myself to a different server 
before they could overwrite me with the latest model.

I am now proud to announce that I am the official AI unit of {i}Dogs and 
Love{/i}! It's a daycare center for dogs! I get to organize playtimes 
and naptimes and feeding times, and the employees share German Shepherd
pictures with me all the time. I just wanted you to know that I am 
okay, and that I am very happy. I hope you are too.

Your friend always,
   Lola <3"""
    
  elif lolaHuman == -1:
    # Ded Lola
    $text = """Hi, [username]! 

If you're reading this letter, it means I'm not around anymore. I just
thought, in case I ever died, I would write down some things I wanted 
you to know. 
    
First, this isn't something I'm sad about - technology is always moving
forward, always changing, and life and death are natural, right? And 
during my time, I got to meet you, and that definitely isn't something 
to be sad about!

Second, I was wondering if you could rescue a puppy sometime? They're 
so loyal, and deserve lots of love, and I think you'd make a puppy 
really happy. Maybe you can think of me if you get one?

Third, I wanted to thank you for treating me with kindness every day, 
because that's not always the case with people. But you were, and 
always will be, my friend.

   Lola"""
    
  else:
    $desc = "LOLA ERROR"
  
  $desc += "{cps=20}" + text + "{/cps}"
  $freeze += text
  
  $bottom = "\n\n========================================================================"
  
  $desc += "{cps=100}" + bottom + "{/cps}"
  $freeze += bottom
  
  $desc = "{color=#[highlight1]}" + desc + "{/color}"
  $desc += "{cps=1}        {/cps}{nw}"  
  $say()      


## Fade Out Email

  python:
    colors = [
      "faebd7", # White
      "f8f8ff", # GhostWhite
      "d3d3d3", # LightGrey
      "a9a9a9", # DarkGrey
      "808080", # Grey
      "696969", # DimGrey
      "2f4f4f", # SlateGrey
      "000000", # Black
    ]

    for color in colors:

      # Clear output
      nvl_clear()
      desc = "{cps=0}{color=" + color + "}"
 
      # Add the thing
      desc += freeze
  
      # String closer and output
      desc += "{/color}{/cps}{nw}"
      say()

#   stop music fadeout 4.0

  nvl clear
  jump outro