# 16. Imagine you are creating a Super Mario game. You need to define
# a class to represent Mario. What would it look like? If you aren't
# familiar with SuperMario, use your own favorite video or board game
# to model a player.
import time
import random


class PlayMario:

    def __init__(self, mario):
        self.mario = mario + ' ' + 'mario'
        self.mushroom = 'mushroom'
        self.fire = 'fire'
        self.flag = 'flag'
        self.jump = 'jump'
        self.enemy = 'enemy'
        self.level = 1
        self.coin = 1

    def powerUp(self):
        self.mario = "SuperMario"

    def levelUp(self):
        self.level += 1

    def play(self):
        level = 1
        count = 5
        i = 1
        while(i != 0):
            for i in range(level*count):
                print(f'{i}:you are playing')
                self.coin += 1
                if i == (level*count)//3:
                    print('enemy is coming')
                    inp = input('Please enter fire to save from enemy: ')
                    if inp == 'fire':
                        print('-->enemy dead --> XXX')
                        print('you are safe from enemy')
                        print('=================================')
                        continue
                    else:
                        inp = 'break'
                        print('you are out now')
                        print('===================end==============')
                        break
                if i == (level*count)//2:
                    print('-----------mushroom-------------')
                    inp = input('eat mushroom type eat: ')
                    if inp == 'eat':
                        print('you are now  a super mario')
                        print("____mario____---->___ Super Mario")
                        self.mario = self.mario.replace(
                            'mario', f'Super Mario{self.level}')
                        self.powerUp()
                        print('=================================')
                    else:
                        print('you don\'t eat mushroom')
                        print('=================================')
                if i == (level*count-1):
                    print(
                        f'you comlete the level {self.level}\n you earned {self.coin} coin')
                    print(f'you crossed {self.flag} {i} congrats')
                    self.levelUp()
                    print('=================================')
                time.sleep(0.5)
            if inp == 'break':
                break
            i = eval(
                input("to go next level press 1 otherwise press 0 to out of game: "))


if __name__ == "__main__":
    mario = PlayMario('bibek')
    mario.play()
