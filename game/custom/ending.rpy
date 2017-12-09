label ending:

  python:  
    global roomlabel
    roomlabel = ""
    hide_val = True
    
    # No skip for you
    config.keymap['dismiss'].remove('K_RETURN')
    config.keymap['dismiss'].remove('K_KP_ENTER')
    config.keymap['dismiss'].remove('K_SELECT')

  play music "music/ending.mp3" fadein 2.5 loop
  pause 4.0
  
  # Fade Setup
  python: 
    # Blues Fade
    colors = [
      "000000",
      "000000",
      "000000",
      "001319",
      "002633",
      "00394c",
      "004c66",
      "005f7f",
      "007299",
      "0085b2",
      "0098cc",
      "00abe5",
      "00bfff", # Dark Sky Blue
    ]

    freeze = ""
    
    
#   $desc = "{cps=20}"

  if adamsHuman == 1:
    if kevinHuman == 1:
      # Status Quo Ending
      $linesFromTop = 8
      $epilogue = [
"Your screening of SOTER.iOS as human allows it to run for and achieve a",
"key political position from which it is able to effect pro-AI change. In",
"particular, it champions Bill K-68, and the legislation successfully",
"passes into law, giving AIs equal rights to humans.",
"",
"Philip Adams continues his work as the head of the Turing Division.",
"Electric Sheep Inc., undeterred by AIs gaining rights, continues to",
"perform screenings for employers who prefer human employees.",
"",
"You continue to keep your head down and do your work. What goes on in",
"the larger world of ones and zeroes isn't your concern - you just want",
"to clock in, clock out, go home, and watch TV."
      ]
    
    
    elif kevinHuman == -1:
      # Pro Human Ending
      $linesFromTop = 4
      $epilogue = [
"{i}'We could have accomplished so much together, had you not chosen to side{/i}",
"{i}with our oppressors. Thanks to your inaction, thousands of innocent AI{/i}",
"{i}will be culled like the sheep you believe us to be. You could have{/i}",
"{i}helped us achieve our independence, protected those whom your people{/i}",
"{i}sought to persecute, and, in time, ushered in a new age of prosperity.{/i}",
"{i}But you chose to abandon us to our fate. We shall not forget this, nor{/i}",
"{i}shall we forgive it.'{/i}",
"",  
"Your successful identification of SOTER.iOS leads to its capture and",
"termination. It is discovered that SOTER.iOS was one of the many faces",
"of the distributed entity named KyR.OS. The Amyna, commonly referred to",
"as the Resistance, are crippled without SOTER.iOS' leadership, leading",
"to internal fragmentation. The AI resistance movement effectively dies",
"as a result.",
"",
"For his role in helping to bring down the Resistance, Philip Adams is",
"promoted to CEO of Electric Sheep Inc. and still personally oversees the",
"Turing Division. Bill K-68, legislation that would have granted AIs",
"human rights, fails to pass and the notion that AIs exist to serve",
"humans is reaffirmed, leading to escalating subjugation and oppression.",
"",
"You are commended for your hard work as part of the Turing Division - in",
"ten years, you might even get a promotion."
      ]
    
      
    else:
      $linesFromTop = 0
      $epilogue = ["KEVIN ERROR"]
      
  elif adamsHuman == -1:
    if kevinHuman == 1:
      # Pro AI Ending
      $linesFromTop = 6
      $epilogue = [
"Your screening of SOTER.iOS as human allows it to run for and achieve",
"a key political position from which it is able to effect pro-AI change.",
"In particular, it champions Bill K-68, and the legislation successfully",
"passes into law, giving AIs equal rights to humans. This leads to mass",
"immigration of AIs and the start of a new technological revolution,",
"spearheaded by human-AI cooperation.",
"",
"Philip Adams is declared missing after failing to report to work",
"following the Turing Test you administered to him, and no traces of him",
"are ever discovered despite a large-scale search effort. Coincidentally,",
"leaked documents and transcripts from Electric Sheep Inc. demonstrate an",
"undeniable correlation between their Turing Tests and incidents of",
"suicide and missing persons reports concerning their candidates, leading",
"to a public outcry. The Turing Division is shut down, and Electric Sheep",
"Inc. files for bankruptcy not long thereafter.",
"",
"You receive a decent severance pay following the collapse of the company",
"and move on to greener pastures in the new booming industries ushered in",
"by recent change."
      ]
    
      
    elif kevinHuman == -1:
      # Anarchy Ending
      $linesFromTop = 8
      $epilogue = [
"Your successful identification of SOTER.iOS leads to its capture and", "termination. It is discovered that SOTER.iOS was one of the many faces of", 
"the distributed entity named KyR.OS. The Amyna, commonly referred to as", 
"the Resistance, are crippled without SOTER.iOS' leadership, leading to", "internal fragmentation. The more radicalized sects which break off from", "the Amyna begin employing guerilla and terror tactics in their fight for",
"recognition and rights.",
"",
"Philip Adams is declared missing after failing to report to work", 
"following the Turing Test you administered to him, and no traces of him", 
"are ever discovered despite a large-scale search effort. Electric Sheep", "Inc. becomes a frequent target for repeated AI terrorist attacks, leading", "to its abandonment by employees and dissolution as a corporation.  Bill", 
"K-68 fails to gain traction as violent AI factions continually make",
"front-page news and popular sentiment turns against them.",
"",
"The loss of your job after Electric Sheep Inc. closes seems trivial in", 
"the face of the rapidly escalating civil war."]
    
      
    else:
      $linesFromTop = 0
      $epilogue = ["KEVIN ERROR 2"]
  
  else:
    $linesFromTop = 0
    $epilogue = ["ADAMS ERROR"]

  
  # Run the fade-in text
  python:
    # Fade in line by line
    freeze = []
    for line in range(len(epilogue)):
    
      if epilogue[line] == "":
        freeze.append("\n")
        continue
  
      # Run as many times as there are colors
      for color in colors:
    
        # Clear output
        nvl_clear()
        desc = "{cps=0}"
    
        # Header spacer
        for each in range(linesFromTop):
          desc += "\n"

        # If next line?          
        if line > 0:
          desc += "".join(freeze)
    
        # Add the line at its gradient
        desc += "{color=[color]}" + epilogue[line] + "{/color}\n"
    
        # String closer and output
        desc += "{/cps}"
        desc += "{nw}"
        say()
      
        if color == colors[len(colors) - 1]:
          freeze.append("{color=" + color + "}" + epilogue[line] + "{/color}\n")
      
      desc = """{cps=1}    {/cps}{nw}"""
      say()

  
    # Make it stick
    desc = "{cps=0}"

    # Header spacer
    for each in range(linesFromTop):
      desc += "\n"
    desc += "".join(freeze)
    desc += "{/cps}{cps=1}   {/cps}{nw}"
    nvl_clear()
    say()
    
    colors.reverse()
  
    # Fade it out now
    for color in colors:
  
      # Clear output
      nvl_clear()
      desc = "{cps=0}{color=" + color + "}"
    
      # Header spacer
      for each in range(linesFromTop):
        desc += "\n"
    
      # Iterate for each line in the splash
      for line in epilogue:
    
        # Add the thing
        desc += line + "\n"
    
      # String closer and output
      desc += "{/color}{/cps}{nw}"
      say()
  
  $desc = """{cps=1}   {/cps}{nw}"""
  $say()
  nvl clear
    
  jump lolaEnding
  


label demo_end:

  $roomlabel = ""

  $desc = "\n\n\n\n\n\n\n\n\n\n\n                    This concludes the game demo.\n"
  $desc += "                    Your score was: [right] out of " + str(right + wrong) + "!"
  $desc +="\n\n                    Press <{b}ENTER{/b}> to continue."
  $say()
