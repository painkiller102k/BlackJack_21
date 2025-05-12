from gui import build_gui
def start_game(name):
    print(f"Start game for: {name}")
    widgets["game_state_label"].config(text=f"{name}, your game has started!")

def take_card():
    print("Take card")

def stop_game():
    print("Stop game")

def show_history():
    print("Show history")

root, widgets = build_gui()
root.mainloop()
