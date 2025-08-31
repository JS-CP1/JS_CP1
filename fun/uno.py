# JS, 1st, Uno
import random
import sys
import time
player_cards = []
bots = {}
turn_order = ["player"]
deck = ["wild", "wild", "wild", "wild", "wild", "wild", "wild", "wild", "+4", "+4", "+4", "+4", "∅r", "∅r", "∅y", "∅y", "∅g", "∅g", "∅b", "∅b", "⇄r", "⇄r", "⇄y", "⇄y", "⇄g", "⇄g", "⇄b", "⇄b", "+2r", "+2r", "+2y", "+2y", "+2g", "+2g", "+2b", "+2b", "Or", "Oy", "Og", "Ob", "1r", "1r", "2r", "2r", "3r", "3r", "4r", "4r", "5r", "5r", "6r", "6r", "7r", "7r", "8r", "8r", "9r", "9r", "1y", "1y", "2y", "2y", "3y", "3y", "4y", "4y", "5y", "5y", "6y", "6y", "7y", "7y", "8y", "8y", "9y", "9y", "1g", "1g", "2g", "2g", "3g", "3g", "4g", "4g", "5g", "5g", "6g", "6g", "7g", "7g", "8g", "8g", "9g", "9g", "1b", "1b", "2b", "2b", "3b", "3b", "4b", "4b", "5b", "5b", "6b", "6b", "7b", "7b", "8b", "8b", "9b", "9b"]
#Choose Number of Bots
def choose_bots():
    num_bots = int(input("How many bots would you like to play?\n"))
    update_bot_num = 1
    while update_bot_num < num_bots+1:
        bots[f'bot{update_bot_num}'] = []
        turn_order.append(f"bot{update_bot_num}")
        update_bot_num += 1
    update_bot_num = num_bots
    print(bots)
#Deal Cards
def deal_cards():
    cards_to_draw = int(input("How many cards would you like each person to get?\n"))
    update_cards = cards_to_draw
    while update_cards > 0:
        draw_card = random.choice(deck)  
        player_cards.append(draw_card)
        key = draw_card in deck
        deck.pop(key)
        update_cards -= 1
    update_cards = cards_to_draw
    for bot in bots:
        while update_cards > 0:
            draw_card = random.choice(deck)
            bots[f"{bot}"].append(draw_card)
            key = draw_card in deck
            deck.pop(key)
            update_cards -= 1
        update_cards = cards_to_draw
    print(bots)
#Check if Cards are Compatible
def compatibility(choice, top_card):
    compatibility = False
    player_cards[choice] = str(player_cards[choice])
    possibilities = ["r", "y", "g", "b", "+2", "∅", "⇄", "O", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    if player_cards[choice] != "wild" and player_cards[choice] != "+4":
        for possible in possibilities:
            if possible in player_cards[choice] and possible in top_card:
                compatibility = True
    else:
        compatibility = True
    return compatibility
def player_turn(top_card):
    print(f"Your hand is: {player_cards}")
    x = 1
    while compatibility != True or x == 1:
        x = 0
        choice = int(input("Which card would you like to play? (enter the key)\n"))
        while choice > len(player_cards):
            choice = int(input("That was not a valid card. Which card would you like to play?\n"))
        choice -= 1
        print(f"You chose {player_cards[choice]}")
        compatibility(choice, top_card)
        if compatibility == True:
            print(f"The card {player_cards[choice]} is played")
            top_card = player_cards[choice]
            player_cards.pop(choice)
    return player_cards, top_card
def bot_turn(bot_num, top_card):
    possible_top_card = random.choice(bots[f"bot{bot_num}"])
    compatibility(possible_top_card, top_card)
    while compatibility != True:
            possible_top_card = random.choice(bots[f"bot{bot_num}"])
    compatibility(possible_top_card, top_card)
#Start the Game
def round():
    print("\033c", end="")
    print(f"Top card is {top_card}")
    print(turn_order)
    for turns in turn_order:
        if turns == "player":
            player_turn(top_card)
            turn_order.pop(0)
            turn_order.append("player")
            print(turn_order)
        elif "bot" in turns:
            bot_num = turn_order[turns]
            bot_turn(bot_num, top_card)
choose_bots()
deal_cards()
top_card = random.choice(deck)
while top_card == "+4" or top_card == "wild" or top_card == "∅r" or top_card == "∅y" or top_card == "∅g" or top_card == "∅b" or top_card == "⇄r" or top_card == "⇄y" or top_card == "⇄g" or top_card == "⇄b":
    top_card = random.choice(deck)
key = top_card in deck
deck.pop(key)
round()