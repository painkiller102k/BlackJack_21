
# gui.py
import customtkinter as ctk

def build_gui(start_cb=None, take_cb=None, stop_cb=None, history_cb=None):
    ctk.set_appearance_mode("dark")
    ctk.set_default_color_theme("blue")

    root = ctk.CTk()
    root.title("Black Jack 21")
    root.geometry("700x450")

    frame = ctk.CTkFrame(root, corner_radius=15)
    frame.pack(padx=20, pady=20, fill="both", expand=True)

    title_label = ctk.CTkLabel(frame, text="Black Jack 21", font=ctk.CTkFont(size=24, weight="bold"))
    title_label.pack(pady=(10, 20))

    name_label = ctk.CTkLabel(frame, text="Введите имя игрока:", font=ctk.CTkFont(size=16))
    name_label.pack()

    name_entry = ctk.CTkEntry(frame, width=300, height=35, corner_radius=10)
    name_entry.pack(pady=(5, 20))

    status_label = ctk.CTkLabel(frame, text="", font=ctk.CTkFont(size=18))
    status_label.pack(pady=(0, 20))

    button_frame = ctk.CTkFrame(frame, fg_color="transparent")
    button_frame.pack(pady=10)

    btn_start = ctk.CTkButton(button_frame, text="Начать игру", width=140, command=lambda: start_cb(name_entry.get()) if start_cb else None)
    btn_start.grid(row=0, column=0, padx=10)

    btn_take = ctk.CTkButton(button_frame, text="Взять карту", width=140, command=lambda: take_cb() if take_cb else None)
    btn_take.grid(row=0, column=1, padx=10)

    btn_stop = ctk.CTkButton(button_frame, text="Стоп", width=140, command=lambda: stop_cb() if stop_cb else None)
    btn_stop.grid(row=0, column=2, padx=10)

    btn_history = ctk.CTkButton(button_frame, text="История", width=140, command=lambda: history_cb() if history_cb else None)
    btn_history.grid(row=0, column=3, padx=10)

    return root, {
        "entry": name_entry,
        "status": status_label,
        "btn_start": btn_start,
        "btn_take": btn_take,
        "btn_stop": btn_stop,
        "btn_history": btn_history
    }