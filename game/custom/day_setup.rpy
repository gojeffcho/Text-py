# Set the scene for Day 1
label setup_mon:

  $chatlist.append("sheep_1014")
  call news4

  jump mainscreen
    
# Set the scene for Day 2    
label setup_tue:

  $chatlist.append("dakota")
  $chatlist.append("courtney")
  $chatlist.append("garmin")

  jump update_score

# Set the scene for Day 3
label setup_wed:

  jump update_score

# Set the scene for Day 4  
label setup_thu:

  jump update_score

# Set the scene for Day 5  
label setup_fri:

  jump update_score

