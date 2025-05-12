# main.py
from gui import build_gui
from functions import read_card, play_computer, calculate_result, save_result, show_history

player_cards = []
player_sum = 0
player_name = ""

def start_game(name):
    global player_cards, player_sum, player_name
    player_cards = []
    player_sum = 0
    player_name = name

    if not name.strip():
        widgets["status"].config(text="Введите имя!")
        return

    # Две стартовые карты
    for _ in range(2):
        card, suit = read_card()
        player_cards.append((card, suit))
        player_sum += card

    update_status(f"{name}, ваши карты: {cards_to_str()} | Сумма: {player_sum}")

def take_card():
    global player_sum
    card, suit = read_card()
    player_cards.append((card, suit))
    player_sum += card

    if player_sum > 21:
        update_status(f"Перебор! Сумма: {player_sum}")
        end_game("Проигрыш")
    else:
        update_status(f"Взяли карту: {card}{suit}. Сумма: {player_sum}")

def stop_game():
    computer_sum = play_computer()
    result = calculate_result(player_sum, computer_sum)
    update_status(f"{result} (Компьютер: {computer_sum})")
    end_game(result)

def show_game_history():
    show_history()

def update_status(message):
    widgets["status"].config(text=message)

def cards_to_str():
    return " ".join(f"{v}{s}" for v, s in player_cards)

def end_game(result):
    save_result(player_name, result, player_sum)

# Запуск GUI
root, widgets = build_gui(start_game, take_card, stop_game, show_game_history)
root.mainloop()
