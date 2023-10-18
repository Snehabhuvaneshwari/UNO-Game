import random
#generating uno deck of 108 cards
colors = ["Red", "Green", "Yellow", "Blue"]
values = [0,1,2,3,4,5,6,7,8,9, "skip", "reverse", "Draw two"]
wilds = ["wild", "wild draw four"]

def deck_cards():
    deck = []
    for color in colors:
        for value in values:
            cardval = "{} {}".format(color, value)
            deck.append(cardval)
            if value != 0:
                deck.append(cardval)
    for i in range(4):
        deck.append(wilds[0])
        deck.append(wilds[1])
    return deck

#shuffling the uno deck of cards
def shuffle_cards():
    x = deck_cards()
    shuffled_cards = random.shuffle(x)
    return(x)

#all players drawing cards
def draw_cards(numplayers):
    cards_drawn = []
    for i in range(numplayers):
        cards_drawn.append(x.pop(0))
    return cards_drawn

def draw_two(player_num, widdie_cards):
    players[player_num-1] += widdie_cards[0:2]
    widdie_cards = widdie_cards[2:]
    print("Player {}: {}".format(player_num, players[player_num-1]))
    player_num = skip(player_num)
    return (widdie_cards, player_num)

def draw_four(player_num, widdie_cards):
    players[player_num-1]+= widdie_cards[0:4]
    widdie_cards = widdie_cards[4:]
    print("Player {}: {}".format(player_num, players[player_num-1]))
    player_num = skip(player_num)
    return (widdie_cards, player_num)
    
def skip(player_num):
    if(player_num == numplayers):
        player_num = 1
    else: 
        player_num +=1
    return player_num

def reverse(player_num):
    if player_num == 1:
        player_num = numplayers
    else:
        player_num -= 2
    return player_num
def wild():
    if card_chosen == "wild":
        newColor = input("Which color do you want to choose?")
        player_num += 1
        print("please choose a card of {} color".format(newColor))
        return ''
        

#Checking if any of the players list is empty
def check(players, numplayers):
    for i in range(numplayers):
        if(len(players[i])==0):
            print("UNO! Player {} wins!".format(i+1))
            return 0
    return 1

#Action to perform when base card is a special card
def check_baseCard(base_card, players, widdie_cards, player_num):
    if(base_card.find("Draw two")!= -1):
        widdie_cards, player_num = draw_two(player_num, widdie_cards)
    elif(base_card.find("wild draw four")!= -1):
        widdie_cards, player_num = draw_four(player_num, widdie_cards)
    elif(base_card.find("skip")!= -1):
        player_num = skip(player_num)
    elif(base_card.find("reverse")!= -1):
        player_num = reverse(player_num)
    return (players, widdie_cards, player_num)


#Play game
def play_game(players, widdie_cards):
    base_card = widdie_cards.pop(0)
    player_num = 1
    print("Base card is ",base_card)
    if(base_card == "wild"):
        color = input("Which color do you choose? ")
        base_card = color
    players, widdie_cards, player_num = check_baseCard(base_card, players, widdie_cards, player_num)
    while(check(players, numplayers)==1):
        b = base_card.split(" ")
        print("Player {}'s turn: ".format(player_num))
        print("Player {}: {}".format(player_num, players[player_num-1]))
        card_chosen = input("Which card do you want to choose? If there is no card matching to color or value ,Type Pick to take a card from widdie ")
        print(card_chosen)
        base_card = card_chosen
        #players[player_num].remove(card_chosen)
            
        if(card_chosen == "wild"):
            color = input("Which color do you choose? ")
        c = card_chosen.split(" ")
        if(card_chosen=="Pick" or b[0]!=c[0] and b[-1]!=c[-1]):
            if(card_chosen!="Pick"):
                print("Card does not match base card")
                card_chosen = base_card
            players[player_num-1].append(widdie_cards.pop(0))
            print("Player {}: {}".format(player_num, players[player_num-1]))
        
        if(card_chosen not in ["Pick","wild"]):
            base_card = card_chosen
            players[player_num-1].remove(card_chosen)
            
        print("Base card is ", base_card)
        if(player_num==numplayers):
            player_num = 1
        else:
            player_num +=1
        players, widdie_cards, player_num = check_baseCard(base_card, players, widdie_cards, player_num)


z = deck_cards()
length = len(z)
print("Total number of cards:",length)
print("Deck cards are:")
print(z)

##print("Shuffled cards are:")
x = shuffle_cards()
##print(x)

#Distributing the cards
players =[]
numplayers = int(input("How many players:"))
for player in range(numplayers):
    players.append(draw_cards(7))
    
#View the cards in player's hand
##for p in range(numplayers):
##    print("player {} cards are {}".format(p+1, players[p]))
##    
#WIDDIE - The cards left after distrubution of the deck are placed face down and are called "WIDDIE"
widdie_cards = x
#print("Widdie cards:", widdie_cards)
play_game(players, widdie_cards)
