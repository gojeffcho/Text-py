label demo_end:

  $desc = "\n\n\n\n\n\n\n\n                This concludes the game demo.\n"
  $desc += "                Your score was: [right] out of " + str(right + wrong) + "!\n"
  $desc += "                Thanks for playing!"
  $say()
  
  $sys.exit()