import tkinter as tk
import requests
from time import sleep
import winsound


# get first completion count
timeout = 10  # seconds
wait_time = 3  # seconds 

init_response = requests.get("https://leetcode-stats-api.herokuapp.com/jpoland0202", timeout=timeout)
num_solved = 0  # init
attempts = 0
while not init_response.ok and (attempts < 5):
    print("API request failed. Trying", 5 - attempts, "more times")
    attempts += 1
    init_response = requests.get("https://leetcode-stats-api.herokuapp.com/jpoland0202", timeout=timeout)
else:
    init_json = init_response.json()
    num_solved = init_json['totalSolved']
    new_num_solved = num_solved

    num_attempts = init_json['totalQuestions']
    new_num_attempts = num_attempts


# continuously check for a new completion
while True:
    # while window.winfo_exists():
    r = requests.get("https://leetcode-stats-api.herokuapp.com/jpoland0202", timeout=timeout)
    if not r.ok:
        print("API request failed")
    else:
        r_json = r.json()
        new_num_solved = r_json['totalSolved']
        new_num_attempts = r_json['totalQuestions']

        if new_num_solved > num_solved:
            num_solved = new_num_solved
            print("Congrats on completing a problem!")
            winsound.PlaySound("my_ding.wav", winsound.SND_FILENAME)
        elif new_num_attempts > num_attempts:
            num_attempts = new_num_attempts
            print("Don't worry, you can do this! Don't give up! Take a deep breath and try again.")
            
    print(num_solved, "solutions detected. Will check again in", wait_time, "seconds.")
    sleep(wait_time)