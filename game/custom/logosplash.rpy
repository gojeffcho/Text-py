label logosplash:

  python:
    
    hide_val = True
    
    linesFromTop = 5
    textSpeed = 3
  
    splashtop = [
      "    $$$$$$$$\ $$$$$$$$\  $$$$$$\  $$\      $$\    ",
      "    \__$$  __|$$  _____|$$  __$$\ $$$\    $$$ |   ",
      "       $$ |   $$ |      $$ /  $$ |$$$$\  $$$$ |   ",
      "       $$ |   $$$$$\    $$$$$$$$ |$$\$$\$$ $$ |   ",
      "       $$ |   $$  __|   $$  __$$ |$$ \$$$  $$ |   ",
      "       $$ |   $$ |      $$ |  $$ |$$ |\$  /$$ |   ",
      "       $$ |   $$$$$$$$\ $$ |  $$ |$$ | \_/ $$ |   ",
      "       \__|   \________|\__|  \__|\__|     \__|   "
    ]

    splashbottom = [                                                                                          
      "                             $$$$$\ $$$$$$$$\ $$$$$$$$\ $$$$$$$$\ ",
      "                             \__$$ |$$  _____|$$  _____|$$  _____|",
      "                                $$ |$$ |      $$ |      $$ |      ",
      "                                $$ |$$$$$\    $$$$$\    $$$$$\    ",
      "                          $$\   $$ |$$  __|   $$  __|   $$  __|   ",
      "                          $$ |  $$ |$$ |      $$ |      $$ |      ",
      "                          \$$$$$$  |$$$$$$$$\ $$ |      $$ |      ",
      "                           \______/ \________|\__|      \__|      "
    ]
    
    # Run as many times as there are characters
    for charNum in range(1, len(splashtop[0]), textSpeed):
    
      # Clear output
      nvl_clear()
      desc = "{cps=0}"
      
      # Header spacer
      for each in range(linesFromTop):
        desc += "\n"
      
      # Iterate for each line in the logo
      for lineNum in range(len(splashtop)):
      
        # Add x chars from the right side in, plus linebreak
        desc += splashtop[lineNum][-charNum:] + "\n"
      
      # String closer and output
      desc += "{/cps}{nw}"
      say()
      
    # Run the bottom
    for charNum in range(1, len(splashbottom[0]), textSpeed + 2):
    
      # Clear output
      nvl_clear()
      desc = "{cps=0}"
      
      # Header spacer
      for each in range(linesFromTop):
        desc += "\n"
      
      # Start with top already built
      for line in splashtop:
        desc += line + "\n"
      
      # Linebreak between bottom part
      desc += "\n"
      
      # Iterate for each line in the bottom part
      for lineNum in range(len(splashbottom)):
      
        desc += splashbottom[lineNum][-charNum:] + "\n"
      
      # String closer and output
      desc += "{/cps}{nw}"
      say()
    
    # Make it stick
    desc = "                      FUCK.  YEAH."
    say()
  
  # Jump to next
  nvl clear
  
  jump titlesplash
      