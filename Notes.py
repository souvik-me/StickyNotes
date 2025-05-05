import tkinter as tk
from tkinter import messagebox
import os
from datetime import datetime

# Folder to save notes
SAVE_FOLDER = r"C:\tasknote"

# Create the folder if it doesn't exist
if not os.path.exists(SAVE_FOLDER):
    os.makedirs(SAVE_FOLDER)

# Function to get today's filename
def get_todays_filename():
    today = datetime.now().strftime("%Y-%m-%d")  # Format: YYYY-MM-DD
    return os.path.join(SAVE_FOLDER, f"{today}.txt")

# Function to save the note
def save_note():
    global last_saved_content
    note_content = text_area.get("1.0", tk.END).strip()

    # Check if the content has changed since the last save
    if note_content != last_saved_content:
        # Get today's filename
        filepath = get_todays_filename()

        # Append the note to the file
        with open(filepath, "a") as file:  # 'a' mode appends to the file
            file.write(f"{datetime.now().strftime('%H:%M:%S')}\n")  # Add timestamp
            file.write(f"{note_content}\n\n")  # Add note content with spacing
        print(f"Note appended to {filepath}")  # Optional: Print to console for debugging

        # Update the last saved content
        last_saved_content = note_content
    else:
        print("No changes to save.")  # Optional: Print to console for debugging

# Auto-save function
def auto_save(interval=7200000):  # Auto-save every 2 hours (7,200,000 milliseconds)
    if auto_save_enabled:
        save_note()
        # Schedule the next auto-save
        root.after(interval, auto_save, interval)

# Function to start auto-save
def start_auto_save():
    global auto_save_enabled
    auto_save_enabled = True
    auto_save()  # Start the auto-save loop
    print("Auto-save started.")

# Function to stop auto-save
def stop_auto_save():
    global auto_save_enabled
    auto_save_enabled = False
    print("Auto-save stopped.")

# Function to handle app close
def on_closing():
    save_note()  # Save the note before closing
    stop_auto_save()  # Stop the auto-save thread
    root.destroy()  # Close the app

# Create the main window
root = tk.Tk()
root.title("Work Note Sanu")
root.geometry("300x300")

# Text area for the note
text_area = tk.Text(root, wrap=tk.WORD)
text_area.pack(expand=True, fill=tk.BOTH, padx=10, pady=10)

# Save button (optional, since auto-save is enabled)
save_button = tk.Button(root, text="Save", command=save_note)
save_button.pack(pady=10)

# Start Auto-save button
start_auto_save_button = tk.Button(root, text="Start Auto-save", command=start_auto_save)
start_auto_save_button.pack(pady=5)

# Stop Auto-save button
stop_auto_save_button = tk.Button(root, text="Stop Auto-save", command=stop_auto_save)
stop_auto_save_button.pack(pady=5)

# Keep the window on top
root.attributes("-topmost", True)

# Auto-save control flag
auto_save_enabled = False

# Variable to track the last saved content
last_saved_content = ""

# Handle window close event
root.protocol("WM_DELETE_WINDOW", on_closing)

# Run the app
root.mainloop()