# Cristal Lu
# July 22, 2021
# lu.py
# This program lets users play Jeopardy   

import random

def final(): #defines function for the end of the game
  print ('Final points of Jeopardy are:')
  print ('Player 1: $', player_1)
  print ('Player 2: $', player_2)
  print ('Player 3: $', player_3)
  print ('Player 4: $', player_4)
  winner =max(player_1,player_2,player_3,player_4)#finds the max points
  if winner == player_1: #finds the winner by matching the max points with the player
    print("**Player 1 IS THE WINNER**")
  elif winner == player_2:
    print("**Player 2 IS THE WINNER**")
  elif winner == player_3:
    print("**Player 3 IS THE WINNER**")
  else:
    print("**Player 4 IS THE WINNER**")
  print ('GAME DONE') #ends game 
  print ()
  print ()

def scoreboard ():#making a function for the scoreboard which is shown after every round 
  print ()
  print ('Current points of this round:') #shows points for each player 
  print ('Player 1: $', player_1)
  print ('Player 2: $', player_2)
  print ('Player 3: $', player_3)
  print ('Player 4: $', player_4)

flag = True #loop control
print('Welcome to Cristals Jeopardy Game!')
while flag == True:
                        #Display menu options
    print('   MENU')
    print('==========')
    print('S to start')
    print('I for Instructions(Read me before beginning!)')
    print('Q to quit')
    print('==========')
    print(' ')
    choice = input('Option?: ')     #get user's choice

    if choice == 'I':#explains how to play the game
        print('Do not know how to play? No problem! Here are the instructions:')
        print('1. Assign each player a number and an order of who goes first/last as the program will ask for who is answering the question.')
        print('2.On your turn, choose a category and a money card under it. If you get the question right, you get the money. Remember that the question gets harder as the money goes up!')
        print ()
        print('3.If you get it wrong, the program will randomly choose another player (could be you again!) to STEAL the question. If they accept and answer correctly, they get to win the money. This will happen over and over again until a player answers correctly or when a player declines.')
        print ()
        print('4.Make sure to keep track of which money cards have been answered and taken since they can only be answered once. When all cards have been answered, type DONE when asked for which category and money card.')
        print ()
        print ('5. This will show the FINAL JEOPARDY QUESTION which will randomly choose a player and this player will have the opportunity to answer the question for 1000 DOLLARS. If they answer incorrectly, it is up for grabs for ANY player.')
        print ()
        print ('6. The player with the most $$$ at the end of the game is the WINNER! Good Luck!')
        print ()
        print('You can quit this program from the main menu by pressing Q')
    elif choice == 'Q':
        flag = False
    elif choice == 'S':
      players = int(input('How many players are playing? (Max is 4):')) #asks how many players are playing
      print ('Decide who is player 1,2,3 and 4 as it will be used for points.') #Tells users to assign a number to each player so that the program can keep track of points 
      #Sets players' points to 0
      player_1 = 0  
      player_2 = 0 
      player_3 = 0
      player_4 = 0 
      print ()
      print ('Pop Culture    Music        Science     General Knowledge') #shows the categories on the game board so players know what they can choose
      #displays the money cards spaced under each category
      for loopcounter in range (0,4):
        print ('$100           ', end='',)
      print ()
      for loopcounter in range (0,4):
        print ('$200           ', end='',)
      print ()
      for loopcounter in range (0,4):
        print ('$300           ', end='',)
      print ()
      for loopcounter in range (0,4):
        print ('$400           ', end='',)

      print()
      #restricts the variables so any other answers will result in error
      category = ['Pop Culture','Music','Science','General Knowledge'] 
      money = ['$100','$200','$300','$400']
      point = ['1','2','3','4']
      blag = True
      while blag == True: 
        print ()
        print ()
        category = str(input('What category do you want?:')) #gets user's choice of category
        money = str(input('How much money will you go for?(Do not forget $ sign):'))#gets user's choice of money card

        if category == 'Music'and money == '$100':#inline comments for this loop apply for all questions 
          point = int (input('Which player are you? (#):')) #gets which player is answering the question 
          clag = True 
          while clag == True: #loop control 
            q = str.capitalize (input('QUESTION: Drake is from which city?:'))
            if q == 'Toronto':
              print ('YAY! You are CORRECT!')
              #adds points to the player that answered the question correctly 
              if point == 1: player_1 +=100
              elif point == 2: player_2 +=100
              elif point == 3: player_3 +=100
              else: player_4 +=100 
              clag = False #ends loop 
            else:
              print ('EHN, You are WRONG!')
              print ()
              person = random.randint(1,players) #chooses a random player to answer
              print ('Player',person,'has been randomly chosen to steal the question.') #shows which player is chosen 
              steal =['Yes','No'] #list of what the variable 'steal' can be 
              steal = str.capitalize(input('Do you accept? (Yes or No)(If the second player got it incorrect and was unable to steal it, do NOT accept.):')) #asks if player accepts the steal 
              if steal == 'No':
                clag = False #loop ends
              else:
                clag = True #if they say yes then it loops back to the question 
          scoreboard()

        elif category == 'Music'and money == '$200':
          point1 = int (input('Which player are you? (#):')) #gets which player is answering the question 
          dlag = True 
          while dlag == True: 
            q1 = str.capitalize(input('QUESTION: Who broke multiple records at the age of 18 from one song about driving?:'))
            if q1 == 'Olivia Rodrigo': 
              print ('YAY! You are CORRECT!')
              #adds points to the player that answered the question correctly 
              if point1 == 1: player_1 +=200
              elif point1 == 2: player_2 +=200
              elif point1 == 3: player_3 +=200
              else: player_4 +=200 
              dlag = False
            else:
              print ('EHN, You are WRONG!')
              print ()
              person = random.randint(1,players)
              print ('Player',person,'has been randomly chosen to steal the question.')
              steal =['Yes','No']
              steal = str.capitalize(input('Do you accept? (Yes or No)(If the second player got it incorrect and was unable to steal it, do NOT accept.):'))
              if steal == 'No':
                dlag = False 
              else:
                dlag = True 
          scoreboard()

        elif category == 'Music'and money == '$300':
          point2 = int (input('Which player are you? (#):')) #gets which player is answering the question 
          elag = True 
          while elag == True: 
            q2 = str(input('QUESTION: What year was Hello by Adele released?:'))
            if q2 == '2015': 
              print ('YAY! You are CORRECT!')
              #adds points to the player that answered the question correctly 
              if point2 == 1: player_1 +=300
              elif point2 == 2: player_2 +=300
              elif point2 == 3: player_3 +=300
              else: player_4 +=300 
              elag = False
            else:
              print ('EHN, You are WRONG!')
              print ()
              person = random.randint(1,players)
              print ('Player',person,'has been randomly chosen to steal the question.')
              steal =['Yes','No']
              steal = str.capitalize(input('Do you accept? (Yes or No)(If the second player got it incorrect and was unable to steal it, do NOT accept.):'))
              if steal == 'No':
                elag = False 
              else:
                elag = True 
          scoreboard()

        elif category == 'Music'and money == '$400':
          point3 = int (input('Which player are you? (#):')) #gets which player is answering the question 
          glag = True 
          while glag == True:
            q3 = str(input('QUESTION: How many keys does a full sized piano have?:'))
            if q3 =='88':
              print ('YAY! You are CORRECT!')
              #adds points to the player that answered the question correctly 
              if point3 == 1: player_1 +=400
              elif point3 == 2: player_2 +=400
              elif point3 == 3: player_3 +=400
              else: player_4 +=400 
              glag = False
            else:
              print ('EHN, You are WRONG!')
              print ()
              person = random.randint(1,players)
              print ('Player',person,'has been randomly chosen to steal the question.')
              steal =['Yes','No']
              steal = str.capitalize(input('Do you accept? (Yes or No)(If the second player got it incorrect and was unable to steal it, do NOT accept.):'))
              if steal == 'No':
                glag = False 
              else:
                glag = True 
          scoreboard()

        elif category == 'Science'and money == '$100':
          point4 = int (input('Which player are you? (#):')) #gets which player is answering the question 
          hlag = True 
          while hlag == True:
            q4 = str.capitalize(input('QUESTION:What does Be stand for on the periodic table?:'))
            if q4 == 'Berillium': 
              print ('YAY! You are CORRECT!')
              #adds points to the player that answered the question correctly 
              if point4 == 1: player_1 +=100
              elif point4 == 2: player_2 +=100
              elif point4 == 3: player_3 +=100
              else: player_4 +=100
              hlag = False
            else:
              print ('EHN, You are WRONG!')
              print ()
              person = random.randint(1,players)
              print ('Player',person,'has been randomly chosen to steal the question.')
              steal =['Yes','No']
              steal = str.capitalize(input('Do you accept? (Yes or No)(If the second player got it incorrect and was unable to steal it, do NOT accept.):'))
              if steal == 'No':
                hlag = False 
              else:
                hlag = True 
          scoreboard()


        elif category == 'Science' and money == '$200':
          point5 = int (input('Which player are you? (#):')) #gets which player is answering the question 
          ilag = True 
          while ilag == True:
            q5 = str.capitalize(input('QUESTION:What is the largest planet in the solar system?:'))
            if q5 == 'Jupiter': 
              print ('YAY! You are CORRECT!')
              #adds points to the player that answered the question correctly 
              if point5 == 1: player_1 +=200
              elif point5 == 2: player_2 +=200
              elif point5 == 3: player_3 +=200
              else: player_4 +=200
              ilag = False 
            else:
              print ('EHN, You are WRONG!')
              print ()
              person = random.randint(1,players)
              print ('Player',person,'has been randomly chosen to steal the question.')
              steal =['Yes','No']
              steal = str.capitalize(input('Do you accept? (Yes or No)(If the second player got it incorrect and was unable to steal it, do NOT accept.):'))
              if steal == 'No':
                ilag = False 
              else:
                ilag = True 
          scoreboard()

        elif category == 'Science' and money == '$300':
          point6 = int (input('Which player are you? (#):')) #gets which player is answering the question 
          jlag = True 
          while jlag == True:
            q6 = str(input('QUESTION:How many teeth does an adult human have?:'))
            if q6 == '32': 
              print ('YAY! You are CORRECT!')
              #adds points to the player that answered the question correctly 
              if point6 == 1: player_1 +=300
              elif point6 == 2: player_2 +=300
              elif point6 == 3: player_3 +=300
              else: player_4 +=300
              jlag = False
            else:
              print ('EHN, You are WRONG!')
              print ()
              person = random.randint(1,players)
              print ('Player',person,'has been randomly chosen to steal the question.')
              steal =['Yes','No']
              steal = str.capitalize(input('Do you accept? (Yes or No)(If the second player got it incorrect and was unable to steal it, do NOT accept.):'))
              if steal == 'No':
                jlag = False 
              else:
                jlag = True 
          scoreboard()

        elif category == 'Science' and money == '$400':
          point7 = int (input('Which player are you? (#):')) #gets which player is answering the question
          klag = True 
          while klag == True:
            q7 = str.capitalize(input('QUESTION:Entomology is the scientific study of what?:'))
            if q7 == 'insects':
              print ('YAY! You are CORRECT!')
              #adds points to the player that answered the question correctly 
              if point7 == 1: player_1 +=400
              elif point7 == 2: player_2 +=400
              elif point7 == 3: player_3 +=400
              else: player_4 +=400
              klag = False
            else:
              print ('EHN, You are WRONG!')
              print ()
              person = random.randint(1,players)
              print ('Player',person,'has been randomly chosen to steal the question.')
              steal =['Yes','No']
              steal = str.capitalize(input('Do you accept? (Yes or No)(If the second player got it incorrect and was unable to steal it, do NOT accept.):'))
              if steal == 'No':
                klag = False 
              else:
                klag = True 
          scoreboard()

        elif category == 'General Knowledge' and money == '$100':
          point8 = int (input('Which player are you? (#):')) #gets which player is answering the question
          llag = True 
          while llag == True:
            q8 = str.capitalize(input('QUESTION:What is the longest river in the world?'))
            if q8 == 'The Nile':
              print ('YAY! You are CORRECT!')
              #adds points to the player that answered the question correctly 
              if point8 == 1: player_1 +=100
              elif point8 == 2: player_2 +=100
              elif point8 == 3: player_3 +=100
              else: player_4 +=100
              llag= False
            else:
              print ('EHN, You are WRONG!')
              print ()
              person = random.randint(1,players)
              print ('Player',person,'has been randomly chosen to steal the question.')
              steal =['Yes','No']
              steal = str.capitalize(input('Do you accept? (Yes or No)(If the second player got it incorrect and was unable to steal it, do NOT accept.):'))
              if steal == 'No':
                llag = False 
              else:
                llag = True 

        elif category == 'General Knowledge' and money == '$200':
          point9 = int (input('Which player are you? (#):')) #gets which player is answering the question
          mlag = True 
          while mlag == True:
            q9 = str.capitalize(input('QUESTION:What type of nut is in the middle of a Ferrero Rocher?:'))
            if q9 == 'Hazelnut':
              print ('YAY! You are CORRECT!')
              #adds points to the player that answered the question correctly 
              if point9 == 1: player_1 +=200
              elif point9 == 2: player_2 +=200
              elif point9 == 3: player_3 +=200
              else: player_4 +=200
              mlag = False
            else:
              print ('EHN, You are WRONG!')
              print ()
              person = random.randint(1,players)
              print ('Player',person,'has been randomly chosen to steal the question.')
              steal =['Yes','No']
              steal = str.capitalize(input('Do you accept? (Yes or No)(If the second player got it incorrect and was unable to steal it, do NOT accept.):'))
              if steal == 'No':
                mlag = False 
              else:
                mlag = True 
          scoreboard()

        elif category == 'General Knowledge' and money == '$300':
          point10 = int (input('Which player are you? (#):')) #gets which player is answering the question
          nlag = True 
          while nlag == True:
            q10 = str.capitalize(input('QUESTION:What is the capital city of Thailand?'))
            if q10 == 'Bangkok':
              print ('YAY! You are CORRECT!')
              #adds points to the player that answered the question correctly 
              if point10 == 1: player_1 +=300
              elif point10 == 2: player_2 +=300
              elif point10 == 3: player_3 +=300
              else: player_4 +=300
              nlag = False
            else:
              print ('EHN, You are WRONG!')
              print ()
              person = random.randint(1,players)
              print ('Player',person,'has been randomly chosen to steal the question.')
              steal =['Yes','No']
              steal = str.capitalize(input('Do you accept? (Yes or No)(If the second player got it incorrect and was unable to steal it, do NOT accept.):'))
              if steal == 'No':
                nlag = False 
              else:
                nlag = True 
          scoreboard()


        elif category == 'General Knowledge' and money == '$400':
          point11 = int (input('Which player are you? (#):')) #gets which player is answering the question
          olag = True 
          while olag == True:
            q11 = str.capitalize(input('QUESTION:What is the plastic part of a shoelace called?:'))
            if q11 == 'Aglet':
              print ('YAY! You are CORRECT!')
              #adds points to the player that answered the question correctly 
              if point11 == 1: player_1 +=400
              elif point11 == 2: player_2 +=400
              elif point11 == 3: player_3 +=400
              else: player_4 +=400
              olag = False
            else:
              print ('EHN, You are WRONG!')
              print ()
              person = random.randint(1,players)
              print ('Player',person,'has been randomly chosen to steal the question.')
              steal =['Yes','No']
              steal = str.capitalize(input('Do you accept? (Yes or No)(If the second player got it incorrect and was unable to steal it, do NOT accept.):'))
              if steal == 'No':
                olag = False 
              else:
                olag = True 
          scoreboard()


        elif category == 'Pop Culture' and money == '$100':
          point12 = int (input('Which player are you? (#):')) #gets which player is answering the question
          plag = True 
          while plag == True:
            q12 = str.capitalize(input('QUESTION:What reality TV show follows a celebrity family, focusing on 5 sisters?'))
            if q12 == 'Keeping Up With The Kardashians':
              print ('YAY! You are CORRECT!')
              #adds points to the player that answered the question correctly 
              if point12 == 1: player_1 +=100
              elif point12 == 2: player_2 +=100
              elif point12 == 3: player_3 +=100
              else: player_4 +=100
              plag = False
            else:
              print ('EHN, You are WRONG!')
              print ()
              person = random.randint(1,players)
              print ('Player',person,'has been randomly chosen to steal the question.')
              steal =['Yes','No']
              steal = str.capitalize(input('Do you accept? (Yes or No)(If the second player got it incorrect and was unable to steal it, do NOT accept.):'))
              if steal == 'No':
                plag = False 
              else:
                plag = True 
          scoreboard()

        elif category == 'Pop Culture' and money == '$200':
          point13 = int (input('Which player are you? (#):')) #gets which player is answering the question
          qlag = True 
          while qlag == True:
            q13 = str.capitalize(input('QUESTION: What actor plays Micheal Scott in the TV show The Office?'))
            if q13 == 'Steve Carell':
              print ('YAY! You are CORRECT!')
              #adds points to the player that answered the question correctly 
              if point13 == 1: player_1 +=200
              elif point13 == 2: player_2 +=200
              elif point13 == 3: player_3 +=200
              else: player_4 +=200
              qlag = False
            else:
              print ('EHN, You are WRONG!')
              print ()
              person = random.randint(1,players)
              print ('Player',person,'has been randomly chosen to steal the question.')
              steal =['Yes','No']
              steal = str.capitalize(input('Do you accept? (Yes or No)(If the second player got it incorrect and was unable to steal it, do NOT accept.):'))
              if steal == 'No':
                qlag = False 
              else:
                qlag = True 
          scoreboard()

        elif category == 'Pop Culture' and money == '$300':
          point14 = int (input('Which player are you? (#):')) #gets which player is answering the question
          rlag = True 
          while rlag == True:
            q14 = str.capitalize(input('QUESTION: What was the first non-English-language film to win Best Picture at the Oscars?'))
            if q14 =='Parasite':
              print ('YAY! You are CORRECT!')
              #adds points to the player that answered the question correctly 
              if point14 == 1: player_1 +=300
              elif point14 == 2: player_2 +=300
              elif point14 == 3: player_3 +=300
              else: player_4 +=300
              rlag = False
            else:
              print ('EHN, You are WRONG!')
              print ()
              person = random.randint(1,players)
              print ('Player',person,'has been randomly chosen to steal the question.')
              steal =['Yes','No']
              steal = str.capitalize(input('Do you accept? (Yes or No)(If the second player got it incorrect and was unable to steal it, do NOT accept.):'))
              if steal == 'No':
                rlag = False 
              else:
                rlag = True 
          scoreboard()
        
        elif category == 'Pop Culture' and money == '$400':
          point15 = int (input('Which player are you? (#):')) #gets which player is answering the question
          slag = True 
          while slag == True:
            q15 = str.capitalize(input('QUESTION: Who wrote the Twilight book series?'))
            if q15 == 'Stephenie Meyer':
              print ('YAY! You are CORRECT!')
              #adds points to the player that answered the question correctly 
              if point15 == 1: player_1 +=400
              elif point15 == 2: player_2 +=400
              elif point15 == 3: player_3 +=400
              else: player_4 +=400
            else:
              print ('EHN, You are WRONG!')
              print ()
              person = random.randint(1,players)
              print ('Player',person,'has been randomly chosen to steal the question.')
              steal =['Yes','No']
              steal = str.capitalize(input('Do you accept? (Yes or No)(If the second player got it incorrect and was unable to steal it, do NOT accept.):'))
              if steal == 'No':
                slag = False 
              else:
                slag = True 
          scoreboard()
          
        elif category == 'DONE': #final question when all cards have been chosen 
          print ('TIME FOR THE FINAL JEOPARDY QUESTION')
          person = random.randint(1,players)#picks a random player
          print ('Player',person,'has been randomly chosen to answer the question for the chance to win 1000 DOLLARS!!!') #shows which player is chosen 
          print ()
          tlag = True 
          while tlag == True:#loop control
            q15 = str(input('FINAL QUESTION:How many bones do sharks have in their bodies?:'))
            if q15 == '0':
              print ('YAY! You are CORRECT!You win 1000 DOLLARS')
              #it will give the points to the player chosen if they get it correctly 
              if person == 1: player_1 +=1000 
              elif person == 2: player_2 +=1000
              elif person == 3: player_3 +=1000
              else: player_4 +=1000
              final() #shows points and who wins 
              break #ends loop for question 
              blag = False #ends loop for next category
              flag = True #goes back to menu 
            else:
              print ('EHN, You are WRONG!')
              print ()
              person = random.randint(1,players)
              print ('Player',person,'has been randomly chosen to steal the question.')
              steal =['Yes','No']
              steal = str.capitalize(input('Do you accept? (Yes or No):'))
              if steal == 'Yes':
                tlag = True
              else: 
               tlag = False #ends the question loop 
               final() #shows points and who won 
          break #breaks loop so that the menu appears after the game ends 
              
        else: 
          print ('ERROR! Make sure you spelled the answer correctly and that proper nouns are capitalized.')
          blag = True  #If there is an error, it will return to asking for which category 
          
    else:
        print('Not a valid choice. Only S, Q and I are valid choices') #when the user inputs something invalid 

print('Program ending.')