import random
import tkinter as tk
import json 
import os

RESULTS_FILE = "results.txt"
balance_file = "balance.json"

def load_balances():
    if not os.path.exists(balance_file):
        return {}
    with open(balance_file, "r") as f:
        return json.load(f)

def save_balances(data):
    with open(balance_file, "w") as f:
        json.dump(data, f, indent=2)


def get_balance(name):
    data = load_balances()
    return data.get(name, 1000)

def set_balance(name, new_amount):
    data = load_balances()
    data[name] = new_amount
    save_balances(data)

def read_card():
    value = random.randint(2, 11)
    suit = random.choice(['♠', '♥', '♦', '♣'])
    return value, suit

def calculate_result(player_sum, computer_sum):
    if player_sum > 21:
        return "Te kaotasite! ületatud."
    elif computer_sum > 21:
        return "Te võitsite! Arvutil on ületatud."
    elif player_sum > computer_sum:
        return "Te võitsite!"
    elif player_sum < computer_sum:
        return "Te kaotasite!"
    else:
        return "Viik!"

def save_result(name, result, player_sum):
    with open(RESULTS_FILE, "a", encoding="utf-8") as file:
        file.write(f"{name}: {result} (Очки: {player_sum})\n")

def show_history():
    try:
        with open(RESULTS_FILE, "r", encoding="utf-8") as file:
            lines = file.readlines()
    except FileNotFoundError:
        lines = []

    history_text = "".join(lines)
    if not history_text:
        history_text = "Mängu ajalugu on tühi."
    else:
        history_text = "Mängu ajalugu:\n" + history_text

    history_window = tk.Toplevel()
    history_window.title("Mängu ajalugu")

    text_area = tk.Text(history_window, width=50, height=20)
    text_area.insert(tk.END, history_text)
    text_area.config(state=tk.DISABLED)
    text_area.pack(padx=10, pady=10)

    close_button = tk.Button(history_window, text="Close", command=history_window.destroy)
    close_button.pack(pady=5)

def play_computer():
    total = 0
    while total < 17:
        value, _ = read_card()
        total += value

    while 17 <= total < 21: 
        if random.random() < 0.3:
            value, _ = read_card()
            total += value
        else:
            break
    return total
