import random
import tkinter as tk

RESULTS_FILE = "results.txt"

def read_card():
    """Возвращает случайную карту и её масть."""
    value = random.randint(2, 11)
    suit = random.choice(['♠', '♥', '♦', '♣'])
    return value, suit

def calculate_result(player_sum, computer_sum):
    """Определяет победителя."""
    if player_sum > 21:
        return "Вы проиграли! Перебор."
    elif computer_sum > 21:
        return "Вы выиграли! У компьютера перебор."
    elif player_sum > computer_sum:
        return "Вы выиграли!"
    elif player_sum < computer_sum:
        return "Вы проиграли!"
    else:
        return "Ничья!"

def save_result(name, result, player_sum):
    """Сохраняет результат игры в файл."""
    with open(RESULTS_FILE, "a", encoding="utf-8") as file:
        file.write(f"{name}: {result} (Очки: {player_sum})\n")

def show_history():
    """Открывает новое окно с историей игр."""
    try:
        with open(RESULTS_FILE, "r", encoding="utf-8") as file:
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
    """Генерирует сумму очков для компьютера."""
    total = 0
    while total < 17:
        value, _ = read_card()
        total += value

    while 17 <= total < 21:
        risk = random.random()
        if risk < 0.3:  # 30% шанс взять ещё одну карту
            value, _ = read_card()
            total += value
        else:
            break

    return total
