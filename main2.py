from gui import build_gui
from functions import read_card, play_computer, calculate_result, save_result, show_history, get_balance, set_balance
from tkinter import simpledialog

player_cards = []
player_sum = 0
player_name = ""
game_over = False
player_balance = 0
current_bet = 0

def start_game(name):
    global player_cards, player_sum, player_name, game_over, player_balance, current_bet
    player_cards = []
    player_sum = 0
    player_name = name.strip()
    game_over = False

    if not player_name:
        widgets["status"].configure(text="Sisestage nimi enne mängu alustamist.")
        return

    player_balance = get_balance(player_name)
    if player_balance <= 0:
        widgets["status"].configure(text="Teil ei ole mängimiseks piisavalt žetoone.")
        return

    current_bet = simpledialog.askinteger("Pakkumine", f"Teie tasakaal: {player_balance} žetoone. Sisestage hind:",
                                          minvalue=1, maxvalue=player_balance)
    if not current_bet:
        widgets["status"].configure(text="Seda määra ei ole rakendatud.")
        return

    for i in range(2):
        card, suit = read_card()
        player_cards.append((card, suit))
        player_sum += card

    update_status(f"{player_name}, Teie kaardid: {cards_to_str()} | Summa: {player_sum}")

    if player_sum > 21:
        player_balance -= current_bet
        set_balance(player_name, player_balance)
        end_game(f"Liiga palju! Sa oled kaotanud. Teile jääb {player_sum}")
    else:
        toggle_game_controls(True)

def take_card():
    global player_balance
    if not player_name:
        widgets["status"].configure(text="Sisestage nimi enne mängu alustamist.")
        return
    global player_sum, game_over
    if game_over:
        return
    card, suit = read_card()
    player_cards.append((card, suit))
    player_sum += card

    if player_sum > 21:
        player_balance -= current_bet
        set_balance(player_name, player_balance)
        update_status(f"Liiga palju! Sa oled kaotanud. Teile jääb {player_sum}")
        end_game(f"Liiga palju! Sa oled kaotanud. Teile jääb {player_sum}")
    else:
        update_status(f"Võetud: {card}{suit}. Summa: {player_sum}")

def stop_game():
    global game_over, player_balance
    if game_over:
        return
    computer_sum = play_computer()
    result = calculate_result(player_sum, computer_sum)

    message = f"{result} (Arvuti: {computer_sum})"
    if result.startswith("Sa võitsid"):
        player_balance += current_bet
        set_balance(player_name, player_balance)
        message += f"\n Sa võitsid {current_bet} žetooni. Saldo: {player_balance}."
    elif result.startswith("Te kaotasite"):
        player_balance -= current_bet
        set_balance(player_name, player_balance)
        message += f"\n Te kaotasite {current_bet} žetooni. Alles: {player_balance}."

    update_status(message)
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
    update_status(f"{widgets['status'].cget('text')}\n Klõpsake uue partii jaoks nuppu *Start Game*.")
    toggle_game_controls(False)

def toggle_game_controls(in_game):
    if in_game:
        widgets["btn_start"].pack_forget()
        widgets["btn_history"].pack_forget()
        widgets["entry"].pack_forget()

        widgets["btn_take"].grid()
        widgets["btn_stop"].grid()
    else:
        widgets["btn_start"].pack(pady=0, side="left", padx=10)
        widgets["btn_history"].pack(pady=0, side="left", padx=10)
        widgets["entry"].pack(pady=(5, 20))

        widgets["btn_take"].grid_remove()
        widgets["btn_stop"].grid_remove()

# GUI
root, widgets = build_gui(start_game, take_card, stop_game, show_game_history)

widgets["btn_take"].grid_remove()
widgets["btn_stop"].grid_remove()

root.mainloop()
