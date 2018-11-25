from pico2d import *

class Jukebox:
    def __init__(self):
        self.Dice_Voice = Dice_Number()



    def play_dice_number(self, num):
        self.Dice_Voice[num].play()



def Dice_Number():
    SoundList = []
    for i in range(1, 7):
        path = '.\\sound\\dice\\DiceNum_A0'
        sound = load_wav('.\\sound\\dice\\DiceNum_A0' + str(i) + '.wav')
        SoundList.append(sound)
        SoundList[i - 1].set_volume(64)
    return SoundList