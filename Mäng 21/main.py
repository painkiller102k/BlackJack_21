from gui import build_gui
from functions import read_card, play_computer, calculate_result, save_result, show_history

player_cards = []
player_sum = 0
player_name = ""
game_over = False

def start_game(name):
    global player_cards, player_sum, player_name, game_over
    player_cards = []
    player_sum = 0
    player_name = name.strip()
    game_over = False

    if not player_name:
        widgets["status"].configure(text="Введите имя перед началом игры.")
        return

    for _ in range(2):
        card, suit = read_card()
        player_cards.append((card, suit))
        player_sum += card

    update_status(f"{player_name}, ваши карты: {cards_to_str()} | Сумма: {player_sum}")

    if player_sum > 21:
        end_game("Перебор! Вы проиграли.")

def take_card():
    global player_sum, game_over
    if game_over:
        return
    card, suit = read_card()
    player_cards.append((card, suit))
    player_sum += card

    if player_sum > 21:
        update_status(f"Взяли: {card}{suit}. Сумма: {player_sum}")
        end_game("Перебор! Вы проиграли.")
    else:
        update_status(f"Взяли: {card}{suit}. Сумма: {player_sum}")

def stop_game():
    global game_over
    if game_over:
        return
    computer_sum = play_computer()
    result = calculate_result(player_sum, computer_sum)
    update_status(f"{result} (Компьютер: {computer_sum})")
    end_game(result)

def show_game_history():
    show_history()

def update_status(message):
    widgets["status"].configure(text=message)

def cards_to_str():
    return " ".join(f"{v}{s}" for v, s in player_cards)

def end_game(result):
    global game_over
    game_over = True
    save_result(player_name, result, player_sum)
    update_status(f"{result} Нажмите 'Начать игру' для новой партии.")

# GUI
root, widgets = build_gui(start_game, take_card, stop_game, show_game_history)
root.mainloop()
