# gui.py
import tkinter as tk
from tkinter import ttk

def build_gui(start_cb=None, take_cb=None, stop_cb=None, history_cb=None):
    root = tk.Tk()
    root.title("Black Jack 21")
    root.geometry("700x400")
    root.configure(bg="black")

    frame = ttk.Frame(root, padding=10)
    frame.pack(expand=True, fill="both")

    # Ввод имени
    name_label = ttk.Label(frame, text="Введите имя:")
    name_label.pack(pady=5)

    name_entry = ttk.Entry(frame, width=30)
    name_entry.pack(pady=5)

    # Статус
    status_label = ttk.Label(frame, text="", font=("Arial", 14))
    status_label.pack(pady=10)

    # Кнопки
    button_frame = ttk.Frame(frame)
    button_frame.pack(pady=10)

    btn_start = ttk.Button(button_frame, text="Начать игру", command=lambda: start_cb(name_entry.get()) if start_cb else None)
    btn_start.grid(row=0, column=0, padx=5)

    btn_take = ttk.Button(button_frame, text="Взять карту", command=take_cb)
    btn_take.grid(row=0, column=1, padx=5)

    btn_stop = ttk.Button(button_frame, text="Стоп", command=stop_cb)
    btn_stop.grid(row=0, column=2, padx=5)

    btn_history = ttk.Button(button_frame, text="История", command=history_cb)
    btn_history.grid(row=0, column=3, padx=5)

    return root, {
        "entry": name_entry,
        "status": status_label,
        "btn_start": btn_start,
        "btn_take": btn_take,
        "btn_stop": btn_stop,
        "btn_history": btn_history
    }
