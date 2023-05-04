import tkinter as tk
import requests
from time import sleep
import winsound

# window = tk.Tk()
# window.title("LeetBoost")


while True:
    init_response = requests.get("https://leetcode-stats-api.herokuapp.com/jpoland0202", timeout=3)
    if not init_response.ok:
        print("API request failed, trying again")
    else:
        init_json = init_response.json()
        num_solved = init_json['totalSolved']
        new_num_solved = num_solved

        num_attempts = init_json['totalQuestions']
        new_num_attempts = num_attempts


        # while window.winfo_exists():
        r = requests.get("https://leetcode-stats-api.herokuapp.com/jpoland0202", timeout=3)
        if not r.ok:
            print("API request failed")
            break
        else:
            r_json = r.json()
            new_num_solved = r_json['totalSolved']
            new_num_attempts = r_json['totalQuestions']

            # testing_input = input("press enter or +")  # remove after testing
            # if testing_input == "+":
            #     new_num_solved += 1

            if new_num_solved > num_solved:
                num_solved = new_num_solved
                print("Congrats on completing a problem!")
                winsound.PlaySound("my_ding.wav", winsound.SND_FILENAME)
            elif new_num_attempts > num_attempts:
                num_attempts = new_num_attempts
                print("Don't worry, you can do this! Don't give up! Take a deep breath and try again.")

            # if testing_input == "+":  # remove after testing
            #     num_solved -= 1
            
    print("Pausing for 3 seconds")
    sleep(3)