# Clash of Clans Troop Cost estimator
# v0.10
# Created by: GandalfTheNoob

import sqlite3

conn = sqlite3.connect('clashcounter.sqlite')
cur = conn.cursor()



def convertTrpLvl(troopLevel):
    try:
        #print type(troopLevel)  ## for debugging
        if troopLevel == 1:
            return 'L1cost'
        if troopLevel == 2:
            return 'L2cost'
        if troopLevel == 3:
            return 'L3cost'
        if troopLevel == 4:
            return 'L4cost'
        if troopLevel == 5:
            return 'L5cost'
        if troopLevel == 6:
            return 'L6cost'
        if troopLevel == 7:
            return 'L7cost'
        else: print "Something weird happened in the convertTrpLvl() conversion."    
    except:
        print "Something bad happened in convertTrpLvl(), try again."

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

spellType = {
    '1' : 'Lightning Spell',
    '2' : 'Healing Spell',
    '3' : 'Rage Spell',
    '4' : 'Jump Spell',
    '5' : 'Freeze Spell',
    '6' : 'Poison Spell',
    '7' : 'Earthquake Spell',
    '8' : 'Haste Spell',
}






inp = True
while inp:

    print ('''
        Press 'A' for troops
        Press 'B' for spells
        Press 0 to exit
    ''')

    firstInp = raw_input()

    if firstInp == '0' or '':
        break

    if firstInp == 'A' or 'a':

        print ('''
            Press 1 if you want to use Barbarians
            Press 2 if you want to use Archer
            Press 3 if you want to use Giant
            Press 4 if you want to use Wizard
            Press 5 if you want to use Wall Breaker
            Press 6 if you want to use Goblin
            Press 7 if you want to use Balloon
            Press 8 if you want to use Healer
            Press 9 if you want to use Dragon
            Press 10 if you want to use Pekka
        
        ''')
        uInp = raw_input()
        dbTrpType = ''
        dbTrpLvl = ''
        dbTrpCost = 0
            
        # Get the troop level
        troopLevel = raw_input("What level of troop for %s? " %(troopType[uInp]))
        # Get the troop quantity
        troopQuantity = int(raw_input("How many of %s? " %(troopType[uInp])))

        if uInp == '1':
            dbTrpType = troopType['4']
            print "Troop type is: ", dbTrpType
            print ''
            print 'Using sqlite database now ...'
            print ''
            print "dbTrpLvl is: ",dbTrpLvl
            print "troopLevel is: ", troopLevel
            dbTrpLvl = convertTrpLvl(int(troopLevel))
            print "dbTrpLvl is after using def(): ", dbTrpLvl
            cur.execute('SELECT name, {lvlCol} FROM TroopType'.format(lvlCol = dbTrpLvl))
            dbTrpCost = cur.fetchone()[1]
            print "Troop cost is", dbTrpCost
            print "Total cost is", dbTrpCost * troopQuantity

    if firstInp == 'B' or 'b':
        print ('''
        Press 1 if you want to use Lightning Spell
        Press 2 if you want to use Healing Spell
        Press 3 if you want to use Rage Spell
        Press 4 if you want to use Jump Spell
        Press 5 if you want to use Freeze Spell
        Press 6 if you want to use Poison Spell
        Press 7 if you want to use Earthquake Spell
        Press 8 if you want to use Haste Spell
    
        ''')


# for key, value in barbarian.iteritems():
#     if key == "1":
#         print "Key found!"
#         print 'key=%s value=%s' % (key, value)
#         break
