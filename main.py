import time
import random, os, sys
cards = ["\u001b[0m: \u001b[31mRed 0", "\u001b[0m: \u001b[31mRed 1", "\u001b[0m: \u001b[31mRed 1", "\u001b[0m: \u001b[31mRed 2", "\u001b[0m: \u001b[31mRed 2", "\u001b[0m: \u001b[31mRed 3", "\u001b[0m: \u001b[31mRed 3", "\u001b[0m: \u001b[31mRed 4", "\u001b[0m: \u001b[31mRed 4", "\u001b[0m: \u001b[31mRed 5", "\u001b[0m: \u001b[31mRed 5", "\u001b[0m: \u001b[31mRed 6", "\u001b[0m: \u001b[31mRed 6", "\u001b[0m: \u001b[31mRed 7", "\u001b[0m: \u001b[31mRed 7", "\u001b[0m: \u001b[31mRed 8", "\u001b[0m: \u001b[31mRed 8", "\u001b[0m: \u001b[31mRed 9", "\u001b[0m: \u001b[31mRed 9", "\u001b[0m: \u001b[31mRed Skip", "\u001b[0m: \u001b[31mRed Skip", "\u001b[0m: \u001b[31mRed Reverse", "\u001b[0m: \u001b[31mRed Reverse", "\u001b[0m: \u001b[31mRed Draw +2", "\u001b[0m: \u001b[31mRed Draw +2", "\u001b[0m: \u001b[32mGreen 0", "\u001b[0m: \u001b[32mGreen 1", "\u001b[0m: \u001b[32mGreen 1", "\u001b[0m: \u001b[32mGreen 2", "\u001b[0m: \u001b[32mGreen 2", "\u001b[0m: \u001b[32mGreen 3", "\u001b[0m: \u001b[32mGreen 3", "\u001b[0m: \u001b[32mGreen 4", "\u001b[0m: \u001b[32mGreen 4", "\u001b[0m: \u001b[32mGreen 5", "\u001b[0m: \u001b[32mGreen 5", "\u001b[0m: \u001b[32mGreen 6", "\u001b[0m: \u001b[32mGreen 6", "\u001b[0m: \u001b[32mGreen 7", "\u001b[0m: \u001b[32mGreen 7", "\u001b[0m: \u001b[32mGreen 8", "\u001b[0m: \u001b[32mGreen 8", "\u001b[0m: \u001b[32mGreen 9", "\u001b[0m: \u001b[32mGreen 9", "\u001b[0m: \u001b[32mGreen Skip", "\u001b[0m: \u001b[32mGreen Skip", "\u001b[0m: \u001b[32mGreen Reverse", "\u001b[0m: \u001b[32mGreen Reverse", "\u001b[0m: \u001b[32mGreen Draw +2", "\u001b[0m: \u001b[32mGreen Draw +2", "\u001b[0m: \u001b[33mYellow 0", "\u001b[0m: \u001b[33mYellow 1", "\u001b[0m: \u001b[33mYellow 1", "\u001b[0m: \u001b[33mYellow 2", "\u001b[0m: \u001b[33mYellow 2", "\u001b[0m: \u001b[33mYellow 3", "\u001b[0m: \u001b[33mYellow 3", "\u001b[0m: \u001b[33mYellow 4", "\u001b[0m: \u001b[33mYellow 4", "\u001b[0m: \u001b[33mYellow 5", "\u001b[0m: \u001b[33mYellow 5", "\u001b[0m: \u001b[33mYellow 6", "\u001b[0m: \u001b[33mYellow 6", "\u001b[0m: \u001b[33mYellow 7", "\u001b[0m: \u001b[33mYellow 7", "\u001b[0m: \u001b[33mYellow 8", "\u001b[0m: \u001b[33mYellow 8", "\u001b[0m: \u001b[33mYellow 9", "\u001b[0m: \u001b[33mYellow 9", "\u001b[0m: \u001b[33mYellow Skip", "\u001b[0m: \u001b[33mYellow Skip", "\u001b[0m: \u001b[33mYellow Reverse", "\u001b[0m: \u001b[33mYellow Reverse", "\u001b[0m: \u001b[33mYellow Draw +2", "\u001b[0m: \u001b[33mYellow Draw +2", "\u001b[0m: \u001b[34mBlue 0", "\u001b[0m: \u001b[34mBlue 1", "\u001b[0m: \u001b[34mBlue 1", "\u001b[0m: \u001b[34mBlue 2", "\u001b[0m: \u001b[34mBlue 2", "\u001b[0m: \u001b[34mBlue 3", "\u001b[0m: \u001b[34mBlue 3", "\u001b[0m: \u001b[34mBlue 4", "\u001b[0m: \u001b[34mBlue 4", "\u001b[0m: \u001b[34mBlue 5", "\u001b[0m: \u001b[34mBlue 5", "\u001b[0m: \u001b[34mBlue 6", "\u001b[0m: \u001b[34mBlue 6", "\u001b[0m: \u001b[34mBlue 7", "\u001b[0m: \u001b[34mBlue 7", "\u001b[0m: \u001b[34mBlue 8", "\u001b[0m: \u001b[34mBlue 8", "\u001b[0m: \u001b[34mBlue 9", "\u001b[0m: \u001b[34mBlue 9", "\u001b[0m: \u001b[34mBlue Skip", "\u001b[0m: \u001b[34mBlue Skip", "\u001b[0m: \u001b[34mBlue Reverse", "\u001b[0m: \u001b[34mBlue Reverse", "\u001b[0m: \u001b[34mBlue Draw +2", "\u001b[0m: \u001b[34mBlue Draw +2", "\u001b[0m: Wild Card", "\u001b[0m: Wild Card", "\u001b[0m: Wild Card", "\u001b[0m: Wild Card", "\u001b[0m: Wild +4", "\u001b[0m: Wild +4", "\u001b[0m: Wild +4", "\u001b[0m: Wild +4"]
startCard = ["\u001b[0m: \u001b[31mRed 0", "\u001b[0m: \u001b[31mRed 1", "\u001b[0m: \u001b[31mRed 1", "\u001b[0m: \u001b[31mRed 2", "\u001b[0m: \u001b[31mRed 2", "\u001b[0m: \u001b[31mRed 3", "\u001b[0m: \u001b[31mRed 3", "\u001b[0m: \u001b[31mRed 4", "\u001b[0m: \u001b[31mRed 4", "\u001b[0m: \u001b[31mRed 5", "\u001b[0m: \u001b[31mRed 5", "\u001b[0m: \u001b[31mRed 6", "\u001b[0m: \u001b[31mRed 6", "\u001b[0m: \u001b[31mRed 7", "\u001b[0m: \u001b[31mRed 7", "\u001b[0m: \u001b[31mRed 8", "\u001b[0m: \u001b[31mRed 8", "\u001b[0m: \u001b[31mRed 9", "\u001b[0m: \u001b[31mRed 9",  "\u001b[32mGreen 0", "\u001b[0m: \u001b[32mGreen 1", "\u001b[0m: \u001b[32mGreen 1", "\u001b[0m: \u001b[32mGreen 2", "\u001b[0m: \u001b[32mGreen 2", "\u001b[0m: \u001b[32mGreen 3", "\u001b[0m: \u001b[32mGreen 3", "\u001b[0m: \u001b[32mGreen 4", "\u001b[0m: \u001b[32mGreen 4", "\u001b[0m: \u001b[32mGreen 5", "\u001b[0m: \u001b[32mGreen 5", "\u001b[0m: \u001b[32mGreen 6", "\u001b[0m: \u001b[32mGreen 6", "\u001b[0m: \u001b[32mGreen 7", "\u001b[0m: \u001b[32mGreen 7", "\u001b[0m: \u001b[32mGreen 8", "\u001b[0m: \u001b[32mGreen 8", "\u001b[0m: \u001b[32mGreen 9", "\u001b[0m: \u001b[32mGreen 9", "\u001b[0m: \u001b[33mYellow 0", "\u001b[0m: \u001b[33mYellow 1", "\u001b[0m: \u001b[33mYellow 1", "\u001b[0m: \u001b[33mYellow 2", "\u001b[0m: \u001b[33mYellow 2", "\u001b[0m: \u001b[33mYellow 3", "\u001b[0m: \u001b[33mYellow 3", "\u001b[0m: \u001b[33mYellow 4", "\u001b[0m: \u001b[33mYellow 4", "\u001b[0m: \u001b[33mYellow 5", "\u001b[0m: \u001b[33mYellow 5", "\u001b[0m: \u001b[33mYellow 6", "\u001b[0m: \u001b[33mYellow 6", "\u001b[0m: \u001b[33mYellow 7", "\u001b[0m: \u001b[33mYellow 7", "\u001b[0m: \u001b[33mYellow 8", "\u001b[0m: \u001b[33mYellow 8", "\u001b[0m: \u001b[33mYellow 9", "\u001b[0m: \u001b[33mYellow 9", "\u001b[0m: \u001b[34mBlue 0", "\u001b[0m: \u001b[34mBlue 1", "\u001b[0m: \u001b[34mBlue 1", "\u001b[0m: \u001b[34mBlue 2", "\u001b[0m: \u001b[34mBlue 2", "\u001b[0m: \u001b[34mBlue 3", "\u001b[0m: \u001b[34mBlue 3", "\u001b[0m: \u001b[34mBlue 4", "\u001b[0m: \u001b[34mBlue 4", "\u001b[0m: \u001b[34mBlue 5", "\u001b[0m: \u001b[34mBlue 5", "\u001b[0m: \u001b[34mBlue 6", "\u001b[0m: \u001b[34mBlue 6", "\u001b[0m: \u001b[34mBlue 7", "\u001b[0m: \u001b[34mBlue 7", "\u001b[0m: \u001b[34mBlue 8", "\u001b[0m: \u001b[34mBlue 8", "\u001b[0m: \u001b[34mBlue 9", "\u001b[0m: \u001b[34mBlue 9",]
playerHand = [": _Draw Card"]
computerHand = [": _Draw Card"]
global discardPile
discardPile = []
x = 0
def clear():
  os.system('clear')
def write(words):
  for char in words:
    time.sleep(0.05)
    sys.stdout.write(char)
    sys.stdout.flush()
  print("\u001b[0m ")
def shuffle_cards():
  global discardPile
  cardlength = len(cards)
  if cardlength <= 4:
    cards.extend(discardPile)
    discardPile = []
def player_card_choice():
  new = random.choice(cards)
  cards.remove(new)
  playerHand.append(new)
def computer_card_choice():
  newcomp = random.choice(cards)
  cards.remove(newcomp)
  computerHand.append(newcomp)
player_card_choice()
computer_card_choice()
player_card_choice()
computer_card_choice()
player_card_choice()
computer_card_choice()
player_card_choice()
computer_card_choice()
player_card_choice()
computer_card_choice()
player_card_choice()
computer_card_choice()
player_card_choice()
computer_card_choice()
def check_user_input(testing):
  global tryCard
  try:
    val = int(testing)
    tryCard = "True"
  except ValueError:
    tryCard = "false"
def computer_special_playing_card():
  global tryCard
  global x
  discardPile.append(tryCard)
  computerHand.remove(tryCard)
  x=0
  if (computerHand[0]) == "\u001b[0m: _Draw Card":
    write("\u001b[0mcomputer has won!")
  else:
    computer_play()
def computer_playing_card():
  global tryCard
  global x
  global color
  global number
  discardPile.append(tryCard)
  computerHand.remove(tryCard)
  x = 0
  if (computerHand[0]) == "\u001b[0m: _Draw Card":
    write("\u001b[0mcomputer has won!")
  else:
    write("computer played a " + color + " " + number)
    cardsLeft = len(computerHand)
    write("\u001b[0mcomputer has " + str(cardsLeft - 1) +" card(s) remaining")
    Play()
def computer_play():
  computerHand.sort()
  shuffle_cards()
  global color
  global number
  global computerChoice
  global tryCard
  global x
  tryCard = (computerHand[x])
  computerChoice = tryCard.split()
  computerlength = len(computerChoice)
  if tryCard == "\u001b[0m: _Draw Card":
    write("\u001b[0m(Computer drew a card)")
    computer_card_choice() 
    cardsLeft = len(computerHand)
    write("\u001b[0mcomputer has " + str(cardsLeft - 1) +" card(s) remaining")
    x = 0
    Play()
  elif (computerChoice[1]) == color:
    if computerlength == 4:
      color = (computerChoice[1])
      number = (computerChoice[2])
      player_card_choice()
      player_card_choice()
      write("computer played a +2")
      computer_special_playing_card()
    elif (computerChoice[2]) == "Reverse":
      write("\u001b[0m(Computer played a Reverse)")
      color = (computerChoice[1])
      number = (computerChoice[2])
      computer_special_playing_card()
    elif (computerChoice[2]) == "Skip":
      write("\u001b[0m(Computer Skiped your turn)")
      color = (computerChoice[1])
      number = (computerChoice[2])
      computer_special_playing_card()
    else:
      color = (computerChoice[1])
      number = (computerChoice[2])
      computer_playing_card()
  elif (computerChoice[2]) == number:
    if computerlength == 4:
      color = (computerChoice[1])
      number = (computerChoice[2])
      player_card_choice()
      player_card_choice()
      write("computer played a +2")
      computer_special_playing_card()
    elif (computerChoice[2]) == "Reverse":
      write("\u001b[0m(Computer played a Reverse)")
      color = (computerChoice[1])
      number = (computerChoice[2])
      computer_special_playing_card()
    elif (computerChoice[2]) == "Skip":
      write("\u001b[0m(Computer Skiped your turn)")
      color = (computerChoice[1])
      number = (computerChoice[2])
      computer_special_playing_card()
    else:
      color = (computerChoice[1])
      number = (computerChoice[2])
      computer_playing_card()
  elif (computerChoice[1]) == "*Wild":
    computerNewChoice = random.randint(1, 4)
    if (computerChoice[2]) == "+4":
      if computerNewChoice == 1:
        color = "\u001b[34mBlue"
        number = "wild"
        write("\u001b[0m(computer placed a draw 4)")
        player_card_choice()
        player_card_choice()
        player_card_choice()
        player_card_choice()
        computer_special_playing_card()
      if computerNewChoice == 2:
        color = "\u001b[32mGreen"
        number = "wild"
        write("\u001b[0m(computer placed a draw 4)")
        player_card_choice()
        player_card_choice()
        player_card_choice()
        player_card_choice()
        computer_special_playing_card()
      if computerNewChoice == 3:
        color = "\u001b[31mRed"
        number = "wild"
        write("\u001b[0m(computer placed a draw 4)")
        player_card_choice()
        player_card_choice()
        player_card_choice()
        player_card_choice()
        computer_special_playing_card()
      if computerNewChoice == 4:
        color = "\u001b[33mYellow"
        number = "wild"
        write("\u001b[0m(computer placed a draw 4)")
        player_card_choice()
        player_card_choice()
        player_card_choice()
        player_card_choice()
        computer_special_playing_card()
    else:
      if computerNewChoice == 1:
        color = "\u001b[34mBlue"
        number = "wild"
        computer_playing_card()
      if computerNewChoice == 2:
        color = "\u001b[32mGreen"
        number = "wild"
        computer_playing_card()
      if computerNewChoice == 3:
        color = "\u001b[31mRed"
        number = "wild"
        computer_playing_card()
      if computerNewChoice == 4:
        color = "\u001b[33mYellow"
        number = "wild"
        computer_playing_card()
  else:
        x = x+1
        computer_play()
def start_card():
  global color
  global number
  playCard = random.choice(startCard)
  startCard.remove(playCard)
  topCard = playCard.split()
  color = (topCard[1])
  number = (topCard[2])
def playing_card():
  global selectcard
  discardPile.append(selectcard)
  playerHand.remove(selectcard)
  if (playerHand[0]) == "\u001b[0m: _Draw Card":
    write("\u001b[0myou have won!")
  else:
    clear()
    write("\u001b[0mComputer's turn")
    write("playing . . .")
    computer_play()
def special_playing_card():
  global selectcard
  discardPile.append(selectcard)
  playerHand.remove(selectcard)
  print("\u001b[0m ")
  if (playerHand[0]) == "\u001b[0m: _Draw Card":
    write("\u001b[0myou have won!")
  else:
    Play()
start_card()
def wild_card():
  global color
  global number
  global choicecard
  global selectcard
  global tryCard
  newChoice = input()
  check_user_input(newChoice)
  if tryCard == "True":
    if int(newChoice) <= 4 and int(newChoice) >= 1:
      
      if (choicecard[2]) == "+4":
        
        if int(newChoice)== 1:
          clear()
          color = "\u001b[34mBlue"
          number = "wild"
          write("(computer Drew 4 cards)")
          computer_card_choice()
          computer_card_choice()
          computer_card_choice()
          computer_card_choice()
          special_playing_card()
        if int(newChoice) == 2:
          clear()
          color = "\u001b[32mGreen"
          number = "wild"
          write("(computer Drew 4 cards)")
          computer_card_choice()
          computer_card_choice()
          computer_card_choice()
          computer_card_choice()
          special_playing_card()
        if int(newChoice) == 3:
          clear()
          color = "\u001b[31mRed"
          number = "wild"
          write("(computer Drew 4 cards)")
          computer_card_choice()
          computer_card_choice()
          computer_card_choice()
          computer_card_choice()
          special_playing_card()
        if int(newChoice) == 4:
          clear()
          color = "\u001b[33mYellow"
          number = "wild"
          write("(computer Drew 4 cards)")
          computer_card_choice()
          computer_card_choice()
          computer_card_choice()
          computer_card_choice()
          special_playing_card()
      else:
        if int(newChoice) == 1:
          
          color = "\u001b[34mBlue"
          number = "wild"
          playing_card()
        if int(newChoice) == 2:
          color = "\u001b[32mGreen"
          number = "wild"
          playing_card()
        if int(newChoice) == 3:
          color = "\u001b[31mRed"
          number = "wild"
          playing_card()
        if int(newChoice) == 4:
          color = "\u001b[33mYellow"
          number = "wild"
          playing_card() 
    else:
      write("invalid number, try again.")
      wild_card()
  else:
    write("invalid number, try again.")
    wild_card()
def Play():
  global color
  global number
  global choicecard
  global selectcard
  global tryCard
  shuffle_cards()
  playerHand.sort()
  print("\u001b[0m ")
  write("\u001b[0myour cards:")
  print("\u001b[0m ")
  for i, item in enumerate(playerHand,1):
    print(i,'' + item, sep='', end='')
    write("\u001b[0m ")
  print("\u001b[0m ")
  write("\u001b[0mtop Card:" + " " + color + " "+ number)
  print("\u001b[0m ")
  write("\u001b[0mWhat card do you want to play? ")
  choiceCard = (input())
  playerHandlength = len(playerHand)
  check_user_input(choiceCard)
  if choiceCard == "":
    clear()
    write("\u001b[0mplease enter a Valid Number")
    Play()
  else:
    if tryCard == "True":
      if int(choiceCard) <= playerHandlength:
        selectcard = (playerHand[int(choiceCard) - 1])
        choicecard = selectcard.split()
        length = len(choicecard)
        if selectcard == ": _Draw Card":
           player_card_choice()
           clear()
           write("\u001b[0mComputer's turn")
           write("playing . . .")
           computer_play()
        elif (choicecard[1]) == color:
            if length == 4:
              color = (choicecard[1])
              number = (choicecard[2])
              clear()
              write("\u001b[0m(computer drew 2 cards)")
              computer_card_choice()
              computer_card_choice()
              special_playing_card()
            elif (choicecard[2]) == "Reverse":
              clear()
              write("\u001b[0m(Reverse back to you)")
              color = (choicecard[1])
              number = (choicecard[2])
              special_playing_card()
            elif (choicecard[2]) == "Skip":
              clear()
              write("\u001b[0m(Computer Skiped)")
              color = (choicecard[1])
              number = (choicecard[2])
              special_playing_card()
            else:
              color = (choicecard[1])
              number = (choicecard[2])
              playing_card()
        elif (choicecard[2]) == number:
            if length == 4:
              color = (choicecard[1])
              number = (choicecard[2])
              clear()
              write("\u001b[0m(computer drew 2 cards)")
              computer_card_choice()
              computer_card_choice()
              special_playing_card()
            elif (choicecard[2]) == "Reverse":
              clear()
              write("\u001b[0m(Reverse back to you)")
              color = (choicecard[1])
              number = (choicecard[2])
              special_playing_card()
            elif (choicecard[2]) == "Skip":
              clear()
              write("\u001b[0m(computer Skiped)")
              color = (choicecard[1])
              number = (choicecard[2])
              special_playing_card()
            else:
              color = (choicecard[1])
              number = (choicecard[2])
              playing_card()
        elif (choicecard[1]) == "*Wild":
          write("\u001b[0mwhat color do you want to change it to? \n \u001b[0m 1. \u001b[34mBlue \n \u001b[0m 2. \u001b[32mGreen \n \u001b[0m 3. \u001b[31mRed \n \u001b[0m 4. \u001b[33mYellow \u001b[0m")
          wild_card()
        else:
          clear()
          write("\u001b[0msorry you can't use that card, Pick again.")
          Play()
      else:
        clear()
        write("\u001b[0mplease enter a Valid Number")
        Play()
    else:
      clear()
      write("\u001b[0mplease enter a Valid Number")
      Play()
Play()