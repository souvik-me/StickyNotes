# Work Note Sanu - Auto-Save Sticky Notes

A simple sticky note application that allows users to write, save, and auto-save their notes. The notes are stored locally in a specified folder with auto-saving features to ensure no data is lost.

## Features

- **Auto-save**: Automatically saves your note every 2 hours (you can start and stop it).
- **Manual Save**: You can also save your notes manually at any time.
- **File Saving**: Notes are saved in a text file with the current date as the filename (`YYYY-MM-DD.txt`).
- **Window Always on Top**: The window stays on top of other windows for easy access.

## Requirements

- Python 3.x
- Required Python Libraries:
  - `tkinter` (for the GUI)
  - `os` (for file handling)
  - `datetime` (for timestamp)
  
## Installation

1. Clone or download this repository to your local machine.
2. Install Python 3.x from [here](https://www.python.org/downloads/), if you haven't already.
3. Run the script using Python:

   ```bash
   python work_note_sanu.py
