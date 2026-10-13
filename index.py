
import tkinter as tk
from time import strftime

# Create window
root = tk.Tk()
root.title("Live Digital Watch")
root.geometry("500x250")

# Create clock label
clock = tk.Label(
    root,
    font=("Arial", 50),
    bg="pink",
    fg="white"
)

clock.pack(expand=True, fill="both")


# Function to update time
def update_time():
    current_time = strftime("%H:%M:%S")
    clock.config(text=current_time)
    clock.after(1000, update_time)


# Start clock
update_time()

# Run application
root.mainloop()