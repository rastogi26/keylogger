# Keylogger with GUI

This is a simple keylogger application with a graphical user interface (GUI). It captures key press and release events and logs them to both a text file and a JSON file. The application is built using the pynput library for keyboard event handling and the Tkinter library for GUI development in Python.

## Features

- Records key press and release events
- Logs key events to a text file and a JSON file
- User-friendly GUI with start and stop buttons
- GUI styled with a customized look and feel

## Requirements

- Python 3.x
- pynput library (`pip install pynput`)

## Usage

1. Install the required dependencies using `pip`:
2. Run the `keylogger.py` file:
3. The GUI window will appear with "Start" and "Stop" buttons.
4. Click the "Start" button to start capturing key events.
5. Press keys on your keyboard to generate key events.
6. Click the "Stop" button to stop the keylogger.
7. Key events will be logged in both a text file (`logs.txt`) and a JSON file (`logs.json`).

## Customization

- Styling: You can customize the GUI appearance by modifying the `style.configure` method in the code. Adjust the font, foreground color, background color, and other properties as desired.
- File Names: If you prefer different file names for logging, you can update the file names in the code (`logs.txt` and `logs.json`) to your preferred names.
  




