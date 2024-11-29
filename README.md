# Google Form Automation Script

## Overview

This Python script automates the process of filling out a specific Google Form with randomly generated data. It leverages the `pyautogui` library to simulate keyboard and mouse interactions. The script is designed to fill out the form multiple times by generating random names, ages, and selecting random options for specific fields.

---

## Features

- **Random Name Generation**: Generates random names using predefined lists of first and last names.
- **Random Age Assignment**: Assigns ages randomly between 20 and 50.
- **Field Navigation**: Simulates keyboard tab presses to navigate through the form fields.
- **Option Selection**: Selects random options for multiple-choice questions.
- **Submission**: Submits the form automatically after filling out all fields.

---

## Requirements

To use this script, ensure the following dependencies are installed:

- Python 3.x
- `pyautogui` (install using `pip install pyautogui`)

---

## Usage

1. **Clone the Repository**:
   ```bash
   git clone <repository_url>
   cd <repository_folder>
   ```

2. **Edit the Script**:
   - Replace `URL` with the actual URL of the Google Form.
   - Adjust the coordinates in `click(500, 500)` to match the position of the browser window on your screen.

3. **Run the Script**:
   ```bash
   python script.py
   ```

4. **Input Prompt**:
   - The script will wait for any input to start. Once you press enter, it will open the Google Form, fill it out 99 times, and submit the data.

---

## Functions

- **`giveName()`**: Combines random first and last names while ensuring they are not identical.
- **`selector(options)`**: Simulates scrolling through multiple-choice options and selecting one at random.
- **`pressTab()` and `pressDown()`**: Simplify key navigation in the form.
- **`main()`**: Handles the overall flow of opening the form, generating data, filling fields, and submitting responses.

---

## Limitations

- **Screen-dependent**: The script relies on screen coordinates, which must be adjusted based on your setup.
- **Specific Form**: It is designed for a particular form structure; modifications may be necessary for different forms.

---

## Disclaimer

This script is intended for educational and personal use only. Automating the submission of forms without authorization may violate terms of service. Ensure you have permission to automate and submit data to the targeted form.

---

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.
