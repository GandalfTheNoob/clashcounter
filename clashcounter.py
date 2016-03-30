# Clash of Clans Troop Cost estimator
# v0.01
# Created by: GandalfTheNoob

# Run the while loop until user enters a blank on Troop Type
while inp:
# Get the Troop type
    troopType = raw_input("Which type of troop?")
    if troopType == '': 
        inp = False
        break
# Get the troop level
    troopLevel = int(raw_input("What level of troop for %s?" %(troopType)))
# Get the troop quantity
    troopQuantity = int(raw_input("How many of %s?" %(troopType)))

barbarian = {
    '1' : 25,
    '2' : 40,
    '3' : 60,
    '4' : 100,
    '5' : 150,
    '6' : 200,
    '7' : 250,
}


# use TroopType user input to locate the dictionary  with the same name and then search fort he user entered troopLevel and quantity to use in a calculation.

searchTroop = 

for key, value in troopType.iteritems():
    if key == "1":
        print "Key found!"
        print 'key=%s value=%s' % (key, value)
        break

