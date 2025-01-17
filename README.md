# Crypto Rich Slot Machine

## Overview

The Crypto Rich Slot Machine is a simple slot machine game built using Python's `tkinter` library. It features a graphical user interface with a luxury-themed background and allows players to spin for a chance to win based on matching symbols.

## Features

- **Slot Symbols**: ton, xrp, sol, eth, btc
- **Winning Logic**:
  - Match all three symbols to win triple their value.
  - Match any two symbols to win their single value.
  - Each spin costs 10.
- **Jackpot**: Enter your phantom private key to claim a jackpot when three identical symbols appear.
- **Game Rules**: Accessible via a button to explain the game mechanics.

## Installation

1. **Clone the Repository**:
   ```bash
   git clone <repository-url>
   cd <repository-directory>
   ```

2. **Install Dependencies**:
   Ensure you have Python installed, then install the required packages:
   ```bash
   pip install -r requirements.txt
   ```

3. **Prepare Images**:
   Place the following images in an `images` directory:
   - `ton.jpg`
   - `xrp.jpg`
   - `sol.jpg`
   - `eth.jpg`
   - `btc.jpg`
   - `luxury.jpg` (for the background)

## Running the Game

1. **Navigate to the Project Directory**:
   ```bash
   cd <repository-directory>
   ```

2. **Run the Game**:
   ```bash
   python crypto_rich_slot.py
   ```

## Code Explanation

- **Main Window**: Created using `tkinter.Tk()`, with a fixed size of 400x400 pixels.
- **Images**: Loaded and resized using `PIL.Image` and `ImageTk.PhotoImage`.
- **Symbols and Values**: Defined in a dictionary to assign values to each symbol.
- **Spin Function**: Handles the logic for spinning the slots and updating the balance.
- **Jackpot Popup**: Displays a popup for entering a phone number when a jackpot is won.
- **Game Rules**: Accessible via a button, explaining the game mechanics.
- **Canvas and Widgets**: A `Canvas` widget is used to display the background and place other widgets like slots, buttons, and balance information.

## Troubleshooting

- Ensure all images are correctly placed in the `images` directory.
- If the game doesn't start, check for missing dependencies or incorrect file paths.

## License

This project is licensed under the MIT License.
