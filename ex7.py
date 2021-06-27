from pygame import mixer
from datetime import datetime
from time import time
def musiconloop(file, stopper):
    mixer.init()
    mixer.music.load(file)
    mixer.music.play()
    while True:
        input_of_user = input()
        if input_of_user == stopper:
            mixer.music.stop()
            break
watersecs=35*60
eyessecs=30*60
excercisesecs=40*60
init_eyes=time()
init_water=time()
init_exercise=time()
def log_now(msg):
    with open("mylogs.txt", "a") as f:
        f.write(f"{msg} {datetime.now()}\n")
while True:
        if time() - init_water > watersecs:
            print("Water Drinking time. Enter 'drank' to stop the alarm.")
            musiconloop('water.mp3', 'drank')
            init_water = time()
            log_now("Drank Water at ->")

        if time() - init_eyes >eyessecs:
            print("Eye exercise time. Enter 'doneeyes' to stop the alarm.")
            musiconloop('eyes.mp3', 'doneeyes')
            init_eyes = time()
            log_now("Eyes Relaxed at ->")

        if time() - init_exercise > excercisesecs:
            print("Physical Activity Time. Enter 'donephy' to stop the alarm.")
            musiconloop('exercise.mp3', 'donephy')
            init_exercise = time()
            log_now("Physical Activity done at ->")