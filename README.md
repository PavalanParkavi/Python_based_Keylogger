# Python_based_Keylogger

# Keylogger Project

This project contains a Python-based keylogger that captures keyboard inputs and emails the collected keystrokes to a specified address at regular intervals. **Note**: This tool is for educational purposes only. Unauthorized use may violate privacy laws.

## Features
- Records keystrokes and saves them in memory.
- Sends captured keystrokes via email at regular intervals.
- Uses Python libraries `pynput` for capturing keystrokes and `smtplib` for email.

## File Overview
- `keylogger.py`: Contains the `Keylogger` class, which handles keylogging and email functions.
- `Mail.py`: Initializes the `Keylogger` class, setting email credentials and starting the keylogging process.

