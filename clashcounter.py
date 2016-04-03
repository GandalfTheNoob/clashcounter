# Clash of Clans Troop Cost estimator
# v0.10
# Created by: GandalfTheNoob

import sqlite3

conn = sqlite3.connect('clashcounter.sqlite')
cur = conn.cursor()

cur.executescript('''
DROP TABLE IF EXISTS troopType;



CREATE TABLE troopType (
    id     INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    name   TEXT UNIQUE
);

''')

troopType = {
    '1' : 'Barbarian',
    '2' : 'Archer',
    '3' : 'Giant',
    '4' : 'Wizard',
    '5' : 'Wall Breaker',
    '6' : 'Goblin',
    '7' : 'Balloon',
    '8' : 'Healer',
    '9' : 'Dragon',
    '10': 'Pekka',
}

barbarian = {
    '1' : 25,
    '2' : 40,
    '3' : 60,
    '4' : 100,
    '5' : 150,
    '6' : 200,
    '7' : 250,
}


archer = {
    '1' : 50,
    '2' : 80,
    '3' : 120,
    '4' : 200,
    '5' : 300,
    '6' : 400,
    '7' : 500,
}

giant = {
    '1' : 250,
    '2' : 750,
    '3' : 1250,
    '4' : 17500,
    '5' : 2250,
    '6' : 3000,
    '7' : 3500,
}
for key, value in barbarian.iteritems():
    if key == "1":
        print "Key found!"
        print 'key=%s value=%s' % (key, value)
        break

# Run the while loop until user enters a blank on Troop Type
inp = True
while inp:

    # An attempt at a user menu:
    print ('''
        Press 0 to exit
        Press 1 if you want to use barbarians
        Press 2 if you want to use archers
        Press 3 if you want to use giants
        
    ''')
    uInp = raw_input()
    
    # Get the troop level
    troopLevel = raw_input("What level of troop for %s?" %(troopType[uInp]))
    # Get the troop quantity
    troopQuantity = int(raw_input("How many of %s?" %(troopType[uInp])))
    
    
    if uInp == '0' or '':
        break

    if uInp == '1':
        print "Barbarian level is: ", troopLevel
        print "Barbarian quantity is: ", troopQuantity
        print "Cost of barbarians is: ", int(barbarian[troopLevel]) * troopQuantity

    if uInp == '2':
        print "Archer level is: ", troopLevel
        print "Archer quantity is: ", troopQuantity
        print "Cost of archers is: ", int(archer[troopLevel]) * troopQuantity

    if uInp == '3':
        print "Giant level is: ", troopLevel
        print "Giant quantity is: ", troopQuantity
        print "Cost of giants is: ", int(giant[troopLevel]) * troopQuantity

