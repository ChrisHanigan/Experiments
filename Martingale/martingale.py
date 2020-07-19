import random

def play():
    roll = random.randrange(100)
    if roll < 30:
        return 'win'
    else:
        return 'lose'
balance = 0
bet = 1
ibet = bet
mbalance = 0
mi = 0
i = 0
while balance < 1000:
    ibet = bet
    i += 1
    outcome = play()
    if outcome == "lose":
        balance = balance - bet
        bet = bet * 3
    else:
        balance = balance + bet
        bet = 1
    if balance < mbalance:
        mbalance = balance
        mi = i
    print(i, ':', outcome,'bet:', ibet,'balance:', balance)
print('lowest net sum', mbalance, 'on game', mi)
