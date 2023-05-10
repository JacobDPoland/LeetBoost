import os
import random
import winsound

sounds = os.listdir(os.getcwd() + "/sounds")
print("Available sounds:", sounds)

# function for choosing and playing the sound effect
def playSound():
    chosen_sound = random.choice(sounds)
    winsound.PlaySound("sounds/" + chosen_sound, winsound.SND_FILENAME)
playSound()
