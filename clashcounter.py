# Clash of Clans Troop Cost estimator
# v0.01
# Created by: GandalfTheNoob

# Run the while loop until user enters a blank on Troop Type
inp = True
while inp == True:
# Get the Troop type
    troopType = raw_input("Which type of troop?")
    if troopType == '': 
        inp = False
        break
# Get the troop level
    troopLevel = int(raw_input("What level of troop for %s?" %(troopType)))
# Get the troop quantity
    troopQuantity = int(raw_input("How many of %s?" %(troopType)))


