# Set the scene for Day 1
label setup_mon:

  $chatlist.append("p_adams")
  call news4 from _call_news4

  jump mainscreen
    
# Set the scene for Day 2    
label setup_tue:

  $chatlist.append("sheep_1014")
  call info4 from _call_info4

  jump mainscreen

# Set the scene for Day 3
label setup_wed:

  $chatlist.append("sheep_1014")
  call news5 from _call_news5
  call info5 from _call_info5
  call misc22 from _call_misc22
  jump mainscreen

# Set the scene for Day 4  
label setup_thu:

  $chatlist.append("sheep_1014")
  call news6 from _call_news6
  call attk8 from _call_attk8
  jump mainscreen

# Set the scene for Day 5  
label setup_fri:

#   jump demo_end   # DEBUG
  $chatlist.append("sheep_1014")
  call news9 from _call_news9
  jump mainscreen

