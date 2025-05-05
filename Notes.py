import tkinter as tk
from datetime import datetime
import os

SAVE_FOLDER = r"C:\tasknote"

if not os.path.exists(SAVE_FOLDER):
    os.makedirs(SAVE_FOLDER)

def get_todays_filename():
    today = datetime.now().strftime("%Y-%m-%d")
    return os.path.join(SAVE_FOLDER, f"{today}.txt")

def save_note():
    global last_saved_content
    note_content = text_area.get("1.0", tk.END).strip()

    if note_content != last_saved_content:
        filepath = get_todays_filename()

        with open(filepath, "a") as file:
            file.write(f"{datetime.now().strftime('%H:%M:%S')}\n")
            file.write(f"{note_content}\n\n")
        print(f"Note saved to {filepath}")

        last_saved_content = note_content
    else:
        print("No changes to save.")

def auto_save(interval=7200000):
    if auto_save_enabled:
        save_note()
        root.after(interval, auto_save, interval)

def start_auto_save():
    global auto_save_enabled
    auto_save_enabled = True
    auto_save()
    print("Auto-save started.")

def stop_auto_save():
    global auto_save_enabled
    auto_save_enabled = False
    print("Auto-save stopped.")

def on_closing():
    save_note()
    stop_auto_save()
    root.destroy()

root = tk.Tk()
root.title("Work Note Sanu")
root.geometry("300x300")

text_area = tk.Text(root, wrap=tk.WORD)
text_area.pack(expand=True, fill=tk.BOTH, padx=10, pady=10)

save_button = tk.Button(root, text="Save", command=save_note)
save_button.pack(pady=10)

start_auto_save_button = tk.Button(root, text="Start Auto-save", command=start_auto_save)
start_auto_save_button.pack(pady=5)

stop_auto_save_button = tk.Button(root, text="Stop Auto-save", command=stop_auto_save)
stop_auto_save_button.pack(pady=5)

root.attributes("-topmost", True)

auto_save_enabled = False
last_saved_content = ""

root.protocol("WM_DELETE_WINDOW", on_closing)

root.mainloop()
