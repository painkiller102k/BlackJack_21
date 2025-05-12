import random
import tkinter as tk

# Рекомендация по функциям:
#read_card() - возвращает случайное число для карты.
#Calculate_result() - проверяет, выиграли вы или проиграли.
#save_result() - записывает результат в файл.
#show_history() - считывает результаты из файла и отображает их в графическом интерфейсе.
#play_computer() - генерирует игру на компьютере.

RESULTS_FILE = "results.txt"

def read_card():
    return random.randint(1, 11)

def calculate_result(player_card, computer_card):
    if player_card > computer_card:
        return "Вы выиграли!"
    elif player_card < computer_card:   
        return "Вы проиграли!"
    else:
        return "Ничья!"
    
def save_result(result):
    with open("results.txt", "a") as file:
        file.write(result + "\n", "результат игры")

def show_history():
    try:
        with open("results.txt", "r") as file:
            lines = file.readlines()
    except FileNotFoundError:
        lines = []
    history_text = "".join(lines)
    if not history_text:
        history_text = "История игр пуста."
    else:
        history_text = "История игр:\n" + history_text

    history_window = tk.Toplevel()
    history_window.title("История игр")

    text_area = tk.Text(history_window, width=50, height=20)
    text_area.insert(tk.END, history_text)
    text_area.config(state=tk.DISABLED)
    text_area.pack(padx=10, pady=10)

    close_button = tk.Button(history_window, text="Закрыть", command=history_window.destroy)
    close_button.pack(pady=5)



def play_computer():
    total = 0
    while total < 17:
        total += read_card()

    while 17 <= total < 21:
        risk = random.random()  # случайное число от 0 до 1
        if risk < 0.3:  # 30% шанс взять ещё одну карту
            total += read_card()
        else:
            break

    return total

