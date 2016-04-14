# Clash of Clans Troop Cost estimator
# v0.20
# Created by: GandalfTheNoob
# Uses Python 2.7

import sqlite3

conn = sqlite3.connect('clashcounter.sqlite')
cur = conn.cursor()



def convert_lvl(troop_level):
    try:
        #print type(troop_level)  ## for debugging
        if troop_level == 1:
            return 'L1cost'
        if troop_level == 2:
            return 'L2cost'
        if troop_level == 3:
            return 'L3cost'
        if troop_level == 4:
            return 'L4cost'
        if troop_level == 5:
            return 'L5cost'
        if troop_level == 6:
            return 'L6cost'
        if troop_level == 7:
            return 'L7cost'
        else: print "Something weird happened in the convert_lvl() conversion."    
    except:
        print "Something bad happened in convert_lvl(), try again."

def get_db_select(passed_db_trp_type, passed_troop_level):
    db_trp_type = troop_type[passed_db_trp_type]
    db_trp_lvl = convert_lvl(int(passed_troop_level))
    cur.execute('SELECT name, {col} FROM TroopType'.format(col = db_trp_lvl,))
    db_trp_cost = cur.fetchone()[1]
    print "Troop cost is", db_trp_cost
    print "Total cost is", db_trp_cost * troop_quantity

def get_spell_db_select(passed_db_spell_type, passed_spell_level):
    db_spell_type = spell_type[passed_db_spell_type]
    db_spell_lvl = convert_lvl(int(passed_spell_level))
    cur.execute('SELECT name, {col} FROM SpellType'.format(col = db_spell_lvl,))
    db_spell_cost = cur.fetchone()[1]
    print "Spell cost is", db_spell_cost
    print "Total cost is", db_spell_cost * spell_quantity


troop_type = {
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

spell_type = {
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
    letter_inp = ''
    print type(letter_inp)
    print "Top of the while loop.  letter_inp is ", letter_inp
    # Top level input from user for selection
    print ('''
        Type 'A' for Troops
        Type 'B' for Spells
        Press 0 to exit
    ''')

    letter_inp = raw_input()
    print "Right after the raw_input() assignment to letter_inp.  letter_inp is ", letter_inp
    # If letter_inp is 0 or blank then exit
    if letter_inp in ['0', '']:
        break
    # If letter_inp is A then display the menu for troop type
    elif letter_inp.lower() == 'a':
        print "Inside elif for 'troops' and letter_inp is ", letter_inp
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
        troop_inp = raw_input()
        db_trp_type = ''
        db_trp_lvl = ''
        db_trp_cost = 0

        # Get the troop level
        troop_level = raw_input("What level of troop for %s? " %(troop_type[troop_inp]))

        # Get the troop quantity
        troop_quantity = int(raw_input("How many of %s? " %(troop_type[troop_inp])))

        if troop_inp == '1':
            #cur.execute('SELECT name, {lvlCol} FROM TroopType'.format(lvlCol = db_trp_lvl))
            #db_trp_cost = cur.fetchone()[1]
            get_db_select(troop_inp, troop_level)

        elif troop_inp == '2':
            print "About to run this from the def()"
            print ""
            get_db_select(troop_inp, troop_level)

        elif troop_inp == '3':
            print "About to run this from the def()"
            print ""
            get_db_select(troop_inp, troop_level)

        elif troop_inp == '4':
            print "About to run this from the def()"
            print ""
            get_db_select(troop_inp, troop_level)            

        elif troop_inp == '5':
            print "About to run this from the def()"
            print ""
            get_db_select(troop_inp, troop_level)

        elif troop_inp == '6':
            print "About to run this from the def()"
            print ""
            get_db_select(troop_inp, troop_level)

        elif troop_inp == '7':
            print "About to run this from the def()"
            print ""
            get_db_select(troop_inp, troop_level)

        elif troop_inp == '8':
            print "About to run this from the def()"
            print ""
            get_db_select(troop_inp, troop_level)            

        elif troop_inp == '9':
            print "About to run this from the def()"
            print ""
            get_db_select(troop_inp, troop_level)

        elif troop_inp == '10':
            print "About to run this from the def()"
            print ""
            get_db_select(troop_inp, troop_level)

    elif letter_inp.lower() == 'b':
        print "Inside elif for 'Spells'. letter_inp is ", letter_inp
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

        spell_inp = raw_input()
        dbspell_type = ''
        dbSpellLvl = ''
        dbSpellCost = 0

        # Get the troop level
        spell_level = raw_input("What level of spell for %s? " %(spell_type[spell_inp]))

        # Get the troop quantity
        spell_quantity = int(raw_input("How many of %s? " %(spell_type[spell_inp])))

        if spell_inp == '1':
            #cur.execute('SELECT name, {lvlCol} FROM TroopType'.format(lvlCol = db_trp_lvl))
            #db_trp_cost = cur.fetchone()[1]
            get_spell_db_select(spell_inp, spell_level)

        elif spell_inp == '2':
            print "About to run this from the def()"
            print ""
            get_spell_db_select(spell_inp, spell_level)

        elif spell_inp == '3':
            print "About to run this from the def()"
            print ""
            get_spell_db_select(spell_inp, spell_level)

        elif spell_inp == '4':
            print "About to run this from the def()"
            print ""
            get_spell_db_select(spell_inp, spell_level)        

        elif spell_inp == '5':
            print "About to run this from the def()"
            print ""
            get_spell_db_select(spell_inp, spell_level)

        elif spell_inp == '6':
            print "About to run this from the def()"
            print ""
            get_spell_db_select(spell_inp, spell_level)

        elif spell_inp == '7':
            print "About to run this from the def()"
            print ""
            get_spell_db_select(spell_inp, spell_level)

        elif spell_inp == '8':
            print "About to run this from the def()"
            print ""
            get_spell_db_select(spell_inp, spell_level)            
    else:
        print "nothing selected, try again"
        continue

conn.close()

# for key, value in barbarian.iteritems():
#     if key == "1":
#         print "Key found!"
#         print 'key=%s value=%s' % (key, value)
#         break
