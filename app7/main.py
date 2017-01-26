import characters
import random
import time

def main():
    print_header()
    game_loop()
    

def print_header():
    print('---------------------------')
    print('         WIZARD APP')
    print('---------------------------')


def game_loop():
    
    creatures = [
           characters.SmallAnimal('Toad', 1),
           characters.Creature('Tiger', 12),
           characters.SmallAnimal('Bat', 3),
           characters.Dragon('Dragon',50,75,True),
           characters.Wizard('Evil Wizard', 100)
            ]

    hero = characters.Wizard('Gandolf', 75)

    while True:
        active_creature = random.choice(creatures)
        print('\nA {} of level {} appeared from a foggy forest...\n'.format(
                                        active_creature.name,active_creature.level))

        cmd = input('Do you [a]ttack, [r]un away, or [l]ook around? ')
        cmd = cmd.lower().strip()
        
        if cmd == 'a':
            if hero.attack(active_creature):
                if not active_creature.name == 'Evil Wizard':
                    creatures.remove(active_creature)
                else:
                    print('\nYou defeated the Evil Wizard \n WELL DONE')
                    break
            else:
                print('The Wizard runs away to recover from the battle...')
                time.sleep(5)
                print('The Wizard return ready to battle again')
        elif cmd == 'r':
            print('{} Runs away like a pussy'.format(hero.name))
        elif cmd == 'l':
            print('\nThe Wizard takes a look around then see the creatures nearby')
            for i in creatures:
                print('{} - level {}'.format(i.name,i.level))
        else:
            print('Exiting the game...')
            break


if __name__ == '__main__':
    main()
