print("Stop! Who would cross the Bridge of Death \nMust answer me these questions three, 'ere the other side he see.")
name = input("What is your name?\t ")  #Ask user name.
if name.capitalize()=="Arthur":
    print("You pass")
else:
    quest = input("What is your Quest?\t ") #If user wrote name except "Arthur" it ask user to write Quest
    if "GRAIL" in quest.upper():
        color = input("What is your favorite color?\t ") # If you write grail it ask the user to input color
        print("you may pass" if color[0].capitalize() == name[0].capitalize()
              else "Incorrect! You must  now face the Gorge of Enternal .")# It only print "you pass" when first letter of color is equal to first letter of your name
    else:
        print("Only those who has grail can pass")  
        print(quest)
  