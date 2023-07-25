import tkinter as tk
import random

# Checks if the four digit number doesn't have repeating digits or zero
def check(num):
    a, b, c, d = str(num)
    if a in [b, c, d] or b in [a, c, d] or c in [a, b, d] or '0' in [a, b, c, d]:
        return False
    else:
        return True

# Compares two four digit numbers and returns the count of same digits at same and different positions
def compare(num4, guess4):
    count_same_pos = 0
    count_diff_pos = 0
    for i in [0, 1, 2, 3]:
        if num4[i] == guess4[i]:
            count_same_pos += 1
        if num4[i] in guess4:
            count_diff_pos += 1
    count_same_num = count_diff_pos - count_same_pos
    return count_same_pos, count_same_num

# List of all four digit numbers that do not have repeating digits and do not include zero
numbers = [str(i) for i in range(1234, 10000) if check(i)]

# Create the main window
root = tk.Tk()
root.title("Brute Force Attack")

# Set the window size
root.geometry("500x500")  # Width x Height

# Set the background color and font color to give it a "cyberpunk" style
root.configure(bg="black")
root.tk_setPalette(background="#000000", foreground="#00ff00")

# Create a frame to center the widgets
frame = tk.Frame(root, bg="#000000")
frame.place(relx=0.5, rely=0.5, anchor="center")

# Add a title and description
title = tk.Label(frame, text="Brute Force Attack", font=("Helvetica", 24), bg="#000000", fg="#00ff00")
title.pack()
description = tk.Label(frame, text="Enter your guess and the values of A and B", bg="#000000", fg="#00ff00")
description.pack()

# Add labels and entry fields for the guess and A and B values
label_guess = tk.Label(frame, text="Guess:", font=("Helvetica", 14), bg="#000000", fg="#00ff00")
entry_guess = tk.Entry(frame)
label_guess.pack()
entry_guess.pack()

label_a = tk.Label(frame, text="A:", font=("Helvetica", 14), bg="#000000", fg="#00ff00")
entry_a = tk.Entry(frame)
label_a.pack()
entry_a.pack()

label_b = tk.Label(frame, text="B:", font=("Helvetica", 14), bg="#000000", fg="#00ff00")
entry_b = tk.Entry(frame)
label_b.pack()
entry_b.pack()

# Add a label to display the result
label_result = tk.Label(frame, text="", font=("Helvetica", 14), bg="#000000", fg="#00ff00")
label_result.pack()

# Function to perform the brute force attack when the button is clicked
def perform_attack():
    global numbers  # Add this line to use the global variable 'numbers'
    guess = entry_guess.get()
    a = int(entry_a.get())
    b = int(entry_b.get())

    possible_answers = [g4 for g4 in numbers if compare(guess, g4) == (a, b)]

    # Shuffling the possible answers and output the first one as the guess
    random.shuffle(possible_answers)
    result = possible_answers[0]

    # Copying the possible answers for the next iteration
    numbers = possible_answers

    # Display the result in the label
    label_result.config(text=f"The result is {result}")

# Add a button to perform the attack
button_attack = tk.Button(frame, text="Perform Attack", command=perform_attack, font=("Helvetica", 14))
button_attack.config(height=2, width=15)  # Increase the size of the button
button_attack.pack()

# Start the main loop
root.mainloop()
