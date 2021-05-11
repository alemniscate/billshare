import random

participants = []
print("Enter the number of friends joining (including you):")
number = int(input())
print()
if number <= 0:
    print("No one is joining for the party")
else:
    print("Enter the name of every friend (including you), each on a new line:")
    for i in range(number):
        participants.append(input())
    print()

    print("Enter the total bill value:")
    bill = float(input())
    print()

    if len(participants) == 1:
        bill_share = dict.fromkeys(participants, bill)
    else:
        print('Do you want to use the "Who is lucky?" feature? Write Yes/No:')
        yesno = input()
        print()
        if yesno == "No":
            print("No one is going to be lucky")
            share = round(bill / len(participants), 2)
            bill_share = dict.fromkeys(participants, share)
        else:
            lucky_man = random.choice(participants) 
            print(f"{lucky_man} is the lucky one!")
            share = round(bill / (len(participants) - 1), 2)
            bill_share = dict.fromkeys(participants)
            for person in bill_share:
                if person == lucky_man:
                    bill_share[person] = 0
                else:
                    bill_share[person] = share     
    print()
    print(bill_share)
