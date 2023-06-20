# -*- coding: utf-8 -*-
"""

@author: Louw Redelinghuys
"""

#import libraries

import random
import os

#global values
rankvalue = {'Two' : 2 , 'Three' : 3, 'Four' : 4, 'Five' : 5,'Six' : 6,'Seven' : 7, 'Eight' : 8, 'Nine' : 9, 'Ten' : 10, 'Jack' : 10,'Queen' : 10, 'King' : 10, 'Ace' : 11}
suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four','Five', 'Six', 'Seven','Eight','Nine','Ten','Jack','Queen','King','Ace')
BlackJack = 21


#Classes
class Card:
    def __init__(self,suit,rank):
        self.suit = suit
        self.rank = rank
        self.value = int(rankvalue[rank])
        
        
    def __str__(self):
        return self.rank + ' of ' + self.suit
    
     
        
class Deck:
    def __init__(self):
        self.all_cards = []
            
        for suit in suits:
            for rank in ranks:
                self.all_cards.append(Card(suit,rank))
                    
    def shuffle(self):
        random.shuffle(self.all_cards)
              
    def deal_one(self):      
        return self.all_cards.pop()
                                 

class Player:
    def __init__(self,name):
        self.name = name
        self.all_cards = []
        self.hand_value = 0
        self.hand_val = int(self.hand_vals())
        
    def hand_vals(self):
        possiblehandvalue = int(self.hand_value)
        numcard = 0
        while numcard < len(self.all_cards):              
            if  self.all_cards[numcard].rank == 'Ace':
                if int(possiblehandvalue) > BlackJack:
                    possiblehandvalue = possiblehandvalue - 10
            numcard += 1
        return int(possiblehandvalue)                                               
                                            
    def remove_one(self):
        self.hand_value = self.hand_value - self.all_cards[0].value
        
        return self.all_cards.pop(0)
                
    def add_cards(self,new_cards):
        if type(new_cards) == type([]):
            for new_card in new_cards:
                self.hand_value = self.hand_value + new_card.value
            self.all_cards.extend(new_cards)
        else:
            self.hand_value = self.hand_value + new_cards.value
            self.all_cards.append(new_cards)
            
                       
class BankAccount:
    def __init__(self,bankbalance):
        self.bankbalance = float(bankbalance)
                        
    def addwinnings(self,amount):
        self.bankbalance = self.bankbalance + float(amount)   
                    
    
    def deductlosses(self,amount):
        self.bankbalance = self.bankbalance - float(amount) 
                                                                                                                                                                                                                                                   
    def __str__(self):                            
        return f'Current bank balance is R {self.bankbalance}'

                
def askbalance():
    bal = 'wrong'
    while type(bal) != float:
        bal = input('please specify your starting balance : ')      
        try:
            bal = float(bal)
            
            if bal<=0:
                bal = str(bal)
                print("Oops! Please don't specify negative values.")
        except:
            print("Oops! That's not a valid input")
    return bal 
    
def betamount(bankbalance):
    betam = 'wrong'
    while type(betam) != float:
        betam = input('please specify your bet amount : ')
        try:
            betam = float(betam)
            
            if betam<=0:
                betam = str(betam)
                print("Oops! Don't specify negative values")
            if betam > float(bankbalance):
                betam = str(betam)
                print('Oops! Insufficient funds!')
        except:
            print("Oops! That's not a valid input")
    return betam                                  
  
def Yourname():
        uname = input('please specify your name : ')
        return uname                                                      

def askhitme():
    hitorstay = input('Hit or Stay? Hit: hit , Stay: stay :')
    while str(hitorstay) != "hit" and str(hitorstay) != "stay":
        hitorstay = input('Oops somethings went wrong, would you like to Hit or Stay? Hit : hit , Stay: stay :')
    if str(hitorstay) == "stay":
        return False
    else:
        return True
                                                                        
def playergui(player):
    print(f" {player.name} has:")
    card = 0
    while card < len(player.all_cards):
        print(player.all_cards[card]) 
        card +=1
        
    print(f" Total value: {player.hand_vals()}")     

def askanotherround():
    ask = input('Another round? Yes: Yes , No: No :')
    while str(ask) != "Yes" and str(ask) != "No":
        ask = input('Oops somethings went wrong, would you like to play another round? Yes : Yes , No: No :')
    if str(ask) == "No":
        return False
    else:
        return True                                                                                                                                                                                                                                                                                      
def iface(player):  #function to identify aces, count aces and calculate hand value taking into account the impact of using value 11 or 1 on them.
    pass                                                                                                        
# initialise program
 
# Game Setup
playername = Yourname()

player_one = Player(playername)
player_two = Player('Dealer')

game_on = True
round_on = True

balance = askbalance()
bankbal = BankAccount(balance)

while game_on:
        
    while player_one.all_cards != []:
        player_one.remove_one()
        
    while player_two.all_cards != []:
        player_two.remove_one()
           
    while round_on:
        bet = betamount(float(bankbal.bankbalance) )
        new_deck = Deck()
        new_deck.shuffle()
        winner = False
        getmoney = 'Draw'
        
        for x in range(2):
            player_one.add_cards(new_deck.deal_one())
            player_two.add_cards(new_deck.deal_one())
       
        clearConsole = lambda: os.system('cls' if os.name in ('nt','dos') else 'clear')
       
        clearConsole()
        print(bankbal)
        print("Current bet amount: R " + str(bet))
        playergui(player_two)
        playergui(player_one)                 

        if int(player_one.hand_vals()) == BlackJack and int(player_one.hand_vals()) != int(player_two.hand_vals()):
            print (f"Black Jack! Congratulations {player_one.name}, you have won the round!")
            winner = True
            getmoney = 'Yes'
            break
            
        elif int(player_two.hand_vals()) == BlackJack and int(player_one.hand_vals()) != int(player_two.hand_vals()):
            print( f"Black Jack! {player_two.name} has won!" )
            winner = True
            getmoney = 'No'
            break
            
        elif int(player_two.hand_vals()) == BlackJack and int(player_one.hand_vals()) == int(player_two.hand_vals()):              
            print("Black Jack! No winners this time")
            winner = True
            getmoney = 'Draw'
            break
            
       #Player 1 Move:    
        notbust = True  
        hitme = askhitme()          
        while hitme and notbust: 
            player_one.add_cards(new_deck.deal_one())
                
           #Need to amend this part to include selector for Ace between 1 and 11.
                
            clearConsole()
            print(bankbal)
            print("Current bet amount: R " + str(bet))
            playergui(player_two)
            playergui(player_one)  
                                                                                                
            if int(player_one.hand_vals()) >BlackJack:
                print('BUST')
                notbust = False
                hitme = False
                break                                      
                    
            hitme = askhitme()    
        
        #Also need to rethink how I am going to allow for the 1 and 11 selector       
        
        clearConsole()
        print(bankbal)
        print("Current bet amount: R " + str(bet))
        playergui(player_two)
        playergui(player_one)                
                                                           
        #Player 2 Move:
        Dealerbust = True
        while int(player_two.hand_vals())<17 and notbust == True:
            player_two.add_cards(new_deck.deal_one())
            
            
            clearConsole()
            print(bankbal)
            print("Current bet amount: R " + str(bet))
            playergui(player_two)
            playergui(player_one)              
                                                   
            if int(player_two.hand_vals()) > BlackJack:
                print('Dealer busts!')
                Dealerbust = False
                break
                     
        #Check for a winner and make payment                          
        if winner == False:
            if notbust == False:
                clearConsole()
                print(f'{player_one.name} has lost the round!')      
                bankbal.deductlosses(bet)
                print(bankbal)
                playergui(player_two)
                playergui(player_one)
                         
            elif Dealerbust ==  False:
                clearConsole()
                print(f'{player_one.name} has won the round!')
                bankbal.addwinnings(bet)
                print(bankbal)
                playergui(player_two)
                playergui(player_one)
                                    
            elif notbust == True and Dealerbust == True and int(player_two.hand_vals())>int(player_one.hand_vals()):
                clearConsole()
                print(f'{player_one.name} has lost the round!')
                bankbal.deductlosses(bet)
                print(bankbal)
                playergui(player_two)
                playergui(player_one)
                
            elif Dealerbust == True and notbust == True and int(player_two.hand_vals()) < int(player_one.hand_vals()):
                clearConsole()
                print(f'{player_one.name} has won the round!')
                bankbal.addwinnings(bet)
                print(bankbal)
                playergui(player_two)                                                                              
                playergui(player_one)
                          
            else:
                clearConsole()
                print('No winners this time!')    
                print(bankbal)
                playergui(player_two)
                playergui(player_one)
                       
        round_on = False
        
    if float(bankbal.bankbalance)>0:    
        round_on = askanotherround()
    else:
        print("Bank account has been depleted. Thanks for your money. Goodbye")
    if round_on == False:
        game_on = False
        break
        
        
        
        
       
                                                                                                                                     
      
      
     

