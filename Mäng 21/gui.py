# gui.py
import tkinter as tk
from tkinter import ttk

def build_gui(start_callback=None, take_card_callback=None, stop_callback=None, show_history_callback=None):
    root = tk.Tk()
    root.geometry("700x400")
    root.title("Black Jack 21")
    root["bg"] = "black"

    # Главный фрейм
    frame_game = ttk.Frame(root)
    frame_game.place(relx=0.5, rely=0.5, anchor="center", relwidth=0.95, relheight=0.95)

    # Ввод имени
    name_label = ttk.Label(frame_game, text="Enter your name:")
    name_label.pack(pady=5)
    name_entry = ttk.Entry(frame_game)
    name_entry.pack(pady=5)

    # Кнопка старта
    btn_start = ttk.Button(frame_game, text="Start Game", command=lambda: start_callback(name_entry.get()) if start_callback else None)
    btn_start.pack(pady=5)

    # Вывод состояния игры
    game_state_label = ttk.Label(frame_game, text="", font=("Arial", 14))
    game_state_label.pack(pady=10)

    # Фрейм с игровыми кнопками
    btn_frame = ttk.Frame(frame_game)
    btn_frame.pack(pady=5)

    btn_takecard = ttk.Button(btn_frame, text="Take Card", command=take_card_callback)
    btn_takecard.grid(row=0, column=0, padx=5)

    btn_stop = ttk.Button(btn_frame, text="Stop", command=stop_callback)
    btn_stop.grid(row=0, column=1, padx=5)

    btn_history = ttk.Button(btn_frame, text="Show History", command=show_history_callback)
    btn_history.grid(row=0, column=2, padx=5)

    return root, {
        "name_entry": name_entry,
        "game_state_label": game_state_label,
        "btn_takecard": btn_takecard,
        "btn_stop": btn_stop,
        "btn_start": btn_start,
        "btn_history": btn_history
    }

