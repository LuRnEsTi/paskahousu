import random
global kortteja_kadessa
def create_pakka():
    numerot = ['A','2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
    maat = ['hertta','ruutu','risti','pata']
    pakka = [f"{suit}_{rank}" for rank in numerot for suit in maat]
    return pakka

def shuffle_pakka(pakka):
    random.shuffle(pakka)

kortteja_kadessa=5

def deal_hands(pakka):
    kasi1 = pakka[:kortteja_kadessa]
   # kasi2 = pakka[]
    loput_kortit=pakka[kortteja_kadessa:]
    #eka_kortti=pakka[:5]
    return kasi1, loput_kortit#, eka_kortti

def pakan_vahennys(kasi1,poistettavat_kortit):
    poistetut_kortit=[]
    for card in poistettavat_kortit:
        if card in kasi1:
            kasi1.remove(card)
            poistetut_kortit.append(card)
        #print(pakka)

        if poistetut_kortit:
            print(f"poistettiin{', '.join(poistetut_kortit)}kadesta")

def pakan_lisays(hand,remaining_cards):
    while len(hand) < kortteja_kadessa and remaining_cards:
        new_card = remaining_cards.pop(0)
        hand.append(new_card)
        print(f"Added {new_card} to the hand.")



    #else:
        #print("no ei löytyny nnjiitä korttjea")
    #return poistettavat_kortit
#def pakan_paivitys(deal_hands):
    


