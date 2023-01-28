import sys
import random
global bjp
bjp = True
global l
l = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,45,46,47,48,49,50,51,52]
global m
m = l
def clear():
    print('\n' *45 )
class bj():
    def numtoname(x):
        x = x%13
        if x == 0:
            return "Ace"
        elif x == 12:
            return "King"
        elif x == 11:
            return "Queen"
        elif x == 10:
            return "Jack"
        else: 
            return str(x+1)
    def suit(n):
        n = n//13
        if n == 0:
            return "Spades"
        elif n == 1:
            return "Hearts"
        elif n == 2:
            return "Diamonds"
        elif n == 3:
            return "Clovers"
    def __init__(self):
        global bjp 
        bjp = True
        l = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,45,46,47,48,49,50,51,52]
        m = l
        print(m)
        dealer = []
        player = []
        dealerfam = []
        playerfam = []
        for x in range(0,2):
            b = random.randint(0, ((len(m))-1))
            player.append((m[b])%13)
            playerfam.append(bj.suit(b))
            m.pop(b)
        for x in range(0,2):
            b = random.randint(0,((len(m))-1))
            dealer.append(m[b])
            dealerfam.append(bj.suit(b))
            m.pop(b) 
        bj.seecards(self, dealer, player, dealerfam, playerfam)
    def endgame():
        f = input("What do you want to do? (new game/quit)")
        if f.lower() == 'new game':
            clear()
            bj()
        elif f.lower() ==  'quit':
            sys.exit()
        else:
            print("Invalid input, please try another command")
    def seecards(self, dealer, player, dealerfam, playerfam):
        print('Your cards are:')
        for x in range(len(player)):
            print(bj.numtoname(player[x])+ ' of '+ playerfam[x])
        print("One of your dealer's cards is:\n",bj.numtoname(dealer[0]), 'of', dealerfam[0])
        e = 0
        global bjp
        for x in range(len(player)):
            e += player[x]%13 + 1
        if e == 21 and bjp == True:
            print("Blackjack! You win!")
            bj.endgame()
        elif e == 21 and bjp == False:
            print("You win!")
            bj.endgame()
        elif e > 21:
            print("Bust! You lose!")
            print("Sum of your cards: ", e)
            bj.endgame()
        else:
            bjp = False
            while True:
                action = input("What do you want to do? (hit/stand/quit)")
                if action.lower() == 'quit':
                    sys.exit()
                elif action.lower() == 'hit':
                    b = random.randint(0, ((len(m))-1))
                    player.append((m[b])%13)
                    playerfam.append(bj.suit(b))
                    m.pop(b)
                    clear()
                    bj.seecards(self, dealer, player, dealerfam, playerfam)
                elif action.lower() == 'stand':
                    q = 0
                    w = 0
                    for x in range(len(dealer)):
                        q += dealer[x]%13 + 1
                    for x in range(len(player)):
                        w += player[x]%13 + 1
                    if q > 21:
                        print("Dealer has: ")
                        for x in range(len(dealer)):
                            print(bj.numtoname(dealer[x])+ ' of '+ dealerfam[x])
                        print("Dealer bust! You win!")
                        bj.endgame()
                    elif q < w:
                        print("Dealer has: ")
                        for x in range(len(dealer)):
                            print(bj.numtoname(dealer[x])+ ' of '+ dealerfam[x])
                        print("You won!")
                        bj.endgame()
                    elif q == w:
                        print("Dealer has: ")
                        for x in range(len(dealer)):
                            print(bj.numtoname(dealer[x])+ ' of '+ dealerfam[x])
                        print("Push! You get back your stake!")
                        bj.endgame()
                    else:
                        print("Dealer has: ")
                        for x in range(len(dealer)):
                            print(bj.numtoname(dealer[x])+ ' of '+ dealerfam[x])
                        print("You lose")
                else:
                    print("Invalid input, please try another command")
bj()

