import random

num = ('A','2','3','4','5','6','7','8','9','10','J','Q','K')
suit = ('♠','♣','♦','♥')

class deck:

    def __init__(self,num,suit):
        self.num = num
        self.suit = suit

    def deck(self):
        total_cards = []
        for x in self.num:
            for y in self.suit:
                total_cards += [(x,y)]

        user1_cards = []
        user2_cards = []
        while len(user1_cards) <= 25:
            a = random.choice(total_cards)
            total_cards.remove(a)
            user1_cards += [a]

        for x in total_cards:
            user2_cards += [x]

        return user1_cards,user2_cards
idk = deck(num,suit)

user1_deck = idk.deck()[0]
user2_deck = idk.deck()[1]

class card_comparison:

    def __init__(self,card1,card2):
        self.card1 = card1
        self.card2 = card2

    def comp(self):
        values = {'A':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, '10':10, 'J':11, 'Q':12, 'K':13}
        if values[self.card1[0]] > values[self.card2[0]]:
            return self.card1
        elif values[self.card2[0]] > values[self.card1[0]]:
            return self.card2
        else:
            return 'Equal'

def design(num,type):
    pcarddisplay = []
    pcarddisplay.append("┌─────────┐")
    pcarddisplay.append("│{}{}. . .│")
    pcarddisplay.append("│. . . . .│")
    pcarddisplay.append("│. . {}. .│")
    pcarddisplay.append("│. . . . .│")
    pcarddisplay.append("│. . .{}{}│")
    pcarddisplay.append("└─────────┘")

    if len(num) == 1:
        x = (f"│{num[:1]}", " . . . .│")
        pcarddisplay[1] = "".join(x)
        x = ("│. . . . ", f"{num[:1]}│")
        pcarddisplay[5] = "".join(x)
    else:
        x = (f"│{num[:]}", ". . . .│")
        pcarddisplay[1] = "".join(x)
        x = ("│. . . .", f"{num[:]}│")
        pcarddisplay[5] = "".join(x)

    if type == '♦':
        pcarddisplay[3] = "│. . ♦ . .│"
    if type == '♣':
        pcarddisplay[3] = "│. . ♣ . .│"
    if type == '♥':
        pcarddisplay[3] = "│. . ♥ . .│"
    if type == '♠':
        pcarddisplay[3] = "│. . ♠ . .│"

    return pcarddisplay

def open_card(num, type):
    if len(num) == 1:
        return f'┌─────────┐\n│{num} . . . .│\n│. . . . .│\n│. . {type} . .│\n│. . . . .│\n│. . . . {num}│\n└─────────┘\n'
    else:
        return f'┌─────────┐\n│{num}. . . .│\n│. . . . .│\n│. . {type} . .│\n│. . . . .│\n│. . . .{num}│\n└─────────┘\n'

def intro():
    print("Welcome to War!")
    print("Player1 your deck is: ")
    print('\n'.join(map('  '.join, zip(*(design(c[0],c[1]) for c in user1_deck)))))
    print("Player2 your deck is: ")
    print('\n'.join(map('  '.join, zip(*(design(c[0],c[1]) for c in user2_deck)))))

    while True:
        x = input("Would you like to begin(Y/N): ")
        if x.isalpha():
            if x.lower() == 'y':
                break
            elif x.lower() == 'n':
                print("Take your time...")
            else:
                print("Enter either Y or N!")
        else:
            print("Enter either Y or N!")
    print("Shuffling your decks...")
    random.shuffle(user1_deck)
    random.shuffle(user2_deck)
    return ''

def cmds():

    while len(user1_deck) != 0 or len(user2_deck) != 0:

        counter = 0

        def card_choice(user_deck):
            while True:
                max = len(user_deck)
                pos = input(f"Enter a value between 1 and {max}: ")
                if pos.isdigit():
                    pos = int(pos)
                    if pos in range(1,max+1):
                        global card
                        card = user_deck[pos-1]
                        break
                    else:
                        print("Enter a valid value!")
                else:
                    print("Enter a valid value!")
                if counter > 0:
                    print(f'You have {max} cards remaining')
            return card

        def war_lists(user_deck):
            while True:
                new_list = []
                max = len(user_deck)
                nums = input(f'Enter three numbers between 1 and {max}(separated by commas): ')
                if ',' in nums:
                    num_list = nums.split(',')
                    c = 0
                    for number in num_list:
                        if number.isdigit() and int(number) in range(1, max + 1):
                            c += 1
                    if c == 3:
                        new_list.extend((user_deck[int(num_list[0]) - 1], user_deck[int(num_list[1]) - 1],
                                           user_deck[int(num_list[2]) - 1]))
                        print(f"Numbers are: ")
                        print('\n'.join(map('  '.join, zip(*(design(c[0],c[1]) for c in new_list)))))
                        break
                    else:
                        print("Enter valid numbers!")
                else:
                    print("Enter commas in between!")
            return new_list

        def bunch_of_statements():
            a = card_choice(user1_deck)
            b = card_choice(user2_deck)
            print(f"Player1's card was\n{''.join(open_card(a[0], a[1]))}\nPlayer2's card was\n{''.join(open_card(b[0], b[1]))}")
            comparison = card_comparison(a, b)

            if comparison.comp() == a:
                user1_deck.append(b)
                user2_deck.remove(b)
                return f"Player1's card was higher!\nPlayer1 now has {len(user1_deck)} cards and Player2 has {len(user2_deck)} cards"

            elif comparison.comp() == b:
                user2_deck.append(a)
                user1_deck.remove(a)
                return f"Player2's card was higher!\nPlayer1 now has {len(user1_deck)} cards and Player2 has {len(user2_deck)} cards"

            else:
                if len(user1_deck) < 3:
                    for x in user1_deck:
                        user1_deck.remove(x)
                    return f'Since Player1 does not have enough cards to participate in a war...'
                if len(user2_deck) < 3:
                    for x in user2_deck:
                        user2_deck.remove(x)
                    return f'Since Player2 does not have enough cards to participate in a war...'

                print("Both cards are equal!\nWe are at war!")
                war_list1 = war_lists(user1_deck)
                war_list2 = war_lists(user2_deck)
                rec = bunch_of_statements()

                if rec == f"Player1's card was higher!\nPlayer1 now has {len(user1_deck)} cards and Player2 has {len(user2_deck)} cards":
                    user1_deck.extend(tuple(war_list2))
                    for x in war_list2:
                        user2_deck.remove(x)
                    return f'Player1 won the war!\nPlayer1 now has {len(user1_deck)} cards and Player2 has {len(user2_deck)} cards'
                else:
                    user2_deck.extend(tuple(war_list1))
                    for x in war_list1:
                        user1_deck.remove(x)
                    return f'Player2 won the war!\nPlayer1 now has {len(user1_deck)} cards and Player2 has {len(user2_deck)} cards'

        print(bunch_of_statements())

        random.shuffle(user1_deck)
        random.shuffle(user2_deck)

        counter += 1

    if len(user1_deck) == 0:
        return 'Player2 won the game!!'
    elif len(user2_deck) == 0:
        return 'Player1 won the game!!'

print(intro())
print(cmds())