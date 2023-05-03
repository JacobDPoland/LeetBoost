import tkinter as tk
import requests
import time

init_response = requests.get("https://leetcode-stats-api.herokuapp.com/jpoland0202").json()
num_solved = init_response['totalSolved']
new_num_solved = num_solved

num_attempts = init_response['totalQuestions']
new_num_attempts = num_attempts


while True:
    r = requests.get("https://leetcode-stats-api.herokuapp.com/jpoland0202").json()
    new_num_solved = r['totalSolved']
    new_num_attempts = r['totalQuestions']

    user_input = input("press enter to continue")

    if new_num_solved > num_solved:
        num_solved = new_num_solved
        print("Congrats on completing a problem!")
    elif new_num_attempts > num_attempts:
        num_attempts = new_num_attempts
        print("Don't worry, you can do this! Don't give up! Take a deep breath and try again.")

    time.sleep(5)