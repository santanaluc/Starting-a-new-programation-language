from classes.game import Person, bcolors
from classes.game import Spell

# Create black magic
fire = Spell("Fire", 10, 100, "black")
thunder = Spell("Thunder", 12, 125, "black")
blizzard = Spell("Blizzard", 15, 100, "black")
meteor = Spell("Meteor", 20, 200, "black")
quake = Spell("Quake", 14, 140, "black")

# Create white magic
cure = Spell("Cure", 12, 120, "white")
cura = Spell("Cura", 18, 200, "white")

# Instantiate People
player = Person(460, 65, 60, 34, [fire, thunder, blizzard, meteor, quake, cure, cura])
enemy = Person(1200, 65, 45, 25, [])

running = True
i = 0

print(bcolors.FAIL + bcolors.BOLD + "AN ENEMY ATTACKS!" + bcolors.ENDC)

while running:
    print("====================================")
    player.choose_action()
    choice = input("Choose action: ")
    print()
    index = int(choice) - 1

    if index == 0:
        dmg = player.generate_damage()
        enemy.take_damage(dmg)
        print("You attacked for", dmg, "points of damage.")
    
    elif index == 1:
        player.choose_magic()
        magic_choice = int(input("\nChoose magic: ")) - 1

        spell = player.magic[magic_choice]
        magic_dmg = spell.generate_damage()
        
        current_mp = player.get_mp()

        '''
        Generate cost of spell damage
        '''
        if(spell.cost > current_mp):
            print(bcolors.FAIL + "Not enough MP" + bcolors.ENDC + "\n")
            continue

        player.reduce_mp(spell.cost)
        
        '''
        Generate spell damage
        '''
        enemy.take_damage(magic_dmg)
        print(bcolors.OKBLUE + spell.name, "deals", str(magic_dmg) + " points of damage" + bcolors.ENDC + "\n")

    enemy_choice = 1

    enemy_dmg = enemy.generate_damage()
    player.take_damage(enemy_dmg)

    print("Enemy attacks for", enemy_dmg)

    print("====================================")
    print("Enemy HP: " + bcolors.FAIL + str(enemy.get_hp()) + " / " + str(enemy.get_max_hp()) + bcolors.ENDC + "\n")

    print("Your HP: " + bcolors.OKGREEN + str(player.get_hp()) + "/" + str(player.get_max_hp()) + bcolors.ENDC)
    print("Your MP: " + bcolors.OKBLUE + str (player.get_mp()) + "/" + str(player.get_max_mp()) + bcolors.ENDC + "\n")

    if enemy.get_hp() == 0:
        print(bcolors.OKGREEN + "You win" + bcolors.ENDC)

        running = False
    elif player.get_hp() == 0:
        print(bcolors.FAIL + "Your enemy has defeated you!" + bcolors.ENDC)
        
        running = False