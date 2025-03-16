import tkinter as tk
from tkinter import ttk, messagebox
import matplotlib.pyplot as plt

# FIFO Page Replacement Algorithm
def fifo_algorithm(reference_string, num_frames):
    frames = []
    page_faults = 0
    result = []

    for i, page in enumerate(reference_string):
        if page not in frames:
            if len(frames) < num_frames:
                frames.append(page)
            else:
                frames.pop(0)
                frames.append(page)
            page_faults += 1
            fault = "Yes"
        else:
            fault = "No"
        
        result.append((i + 1, page, list(frames), fault))

    return result, page_faults

# LRU Page Replacement Algorithm
def lru_algorithm(reference_string, num_frames):
    frames = []
    page_faults = 0
    recent_usage = {}
    result = []

    for i, page in enumerate(reference_string):
        if page not in frames:
            if len(frames) < num_frames:
                frames.append(page)
            else:
                # Find the least recently used page
                lru_page = min(frames, key=lambda x: recent_usage[x])
                frames[frames.index(lru_page)] = page
            page_faults += 1
            fault = "Yes"
        else:
            fault = "No"
        
        recent_usage[page] = i  # Update recent usage
        result.append((i + 1, page, list(frames), fault))

    return result, page_faults

# Optimal Page Replacement Algorithm
def optimal_algorithm(reference_string, num_frames):
    frames = []
    page_faults = 0
    result = []

    for i, page in enumerate(reference_string):
        if page not in frames:
            if len(frames) < num_frames:
                frames.append(page)
            else:
                # Find the page that will be used farthest in the future
                future_use = {p: (reference_string[i:].index(p) if p in reference_string[i:] else float("inf")) for p in frames}
                farthest_page = max(future_use, key=future_use.get)
                frames[frames.index(farthest_page)] = page
            page_faults += 1
            fault = "Yes"
        else:
            fault = "No"
        
        result.append((i + 1, page, list(frames), fault))

    return result, page_faults

# Function to handle simulation
def run_simulation():
    try:
        reference_string = list(map(int, entry_ref_string.get().split(",")))
        num_frames = int(entry_frames.get())
        algorithm = algo_var.get()

        if num_frames <= 0:
            messagebox.showerror("Error", "Number of frames must be greater than 0.")
            return

        if algorithm == "FIFO":
            result, faults = fifo_algorithm(reference_string, num_frames)
        elif algorithm == "LRU":
            result, faults = lru_algorithm(reference_string, num_frames)
        elif algorithm == "Optimal":
            result, faults = optimal_algorithm(reference_string, num_frames)
        else:
            messagebox.showerror("Error", "Invalid Algorithm")
            return

        # Clear previous table
        for row in tree.get_children():
            tree.delete(row)

        # Insert results into the table
        for step, page, frames, fault in result:
            tree.insert("", "end", values=(step, page, frames, fault))

        label_faults.config(text=f"Total Page Faults: {faults}")

    except ValueError:
        messagebox.showerror("Error", "Invalid input. Please enter numbers only.")

#  Function to plot results
def plot_graph():
    reference_string = list(map(int, entry_ref_string.get().split(",")))
    num_frames = int(entry_frames.get())
    algorithm = algo_var.get()

    if algorithm == "FIFO":
        _, faults = fifo_algorithm(reference_string, num_frames)
    elif algorithm == "LRU":
        _, faults = lru_algorithm(reference_string, num_frames)
    elif algorithm == "Optimal":
        _, faults = optimal_algorithm(reference_string, num_frames)
    else:
        messagebox.showerror("Error", "Invalid Algorithm")
        return

    plt.bar(["FIFO", "LRU", "Optimal"], [fifo_algorithm(reference_string, num_frames)[1], 
                                         lru_algorithm(reference_string, num_frames)[1], 
                                         optimal_algorithm(reference_string, num_frames)[1]],
            color=['blue', 'green', 'red'])
    
    plt.xlabel("Algorithms")
    plt.ylabel("Page Faults")
    plt.title("Page Replacement Algorithm Comparison")
    plt.show()

# GUI Setup
root = tk.Tk()
root.title("Page Replacement Algorithm Simulator")
root.geometry("700x500")

# Input Frame
frame_top = tk.Frame(root)
frame_top.pack(pady=10)

tk.Label(frame_top, text="Reference String:").grid(row=0, column=0)
entry_ref_string = tk.Entry(frame_top, width=30)
entry_ref_string.grid(row=0, column=1, padx=5)

tk.Label(frame_top, text="Frames:").grid(row=1, column=0)
entry_frames = tk.Entry(frame_top, width=5)
entry_frames.grid(row=1, column=1, padx=5)

tk.Label(frame_top, text="Algorithm:").grid(row=2, column=0)
algo_var = tk.StringVar(value="FIFO")
algo_dropdown = ttk.Combobox(frame_top, textvariable=algo_var, values=["FIFO", "LRU", "Optimal"])
algo_dropdown.grid(row=2, column=1, padx=5)

tk.Button(frame_top, text="Run Simulation", command=run_simulation).grid(row=3, column=0, pady=10)
tk.Button(frame_top, text="Plot Graph", command=plot_graph).grid(row=3, column=1, pady=10)

# Table Frame
frame_table = tk.Frame(root)
frame_table.pack(pady=10)

columns = ("Step", "Page", "Frames", "Page Fault")
tree = ttk.Treeview(frame_table, columns=columns, show="headings")
for col in columns:
    tree.heading(col, text=col)
    tree.column(col, width=150)

tree.pack()

# Page Faults Label
label_faults = tk.Label(root, text="Total Page Faults: 0", font=("Arial", 12, "bold"))
label_faults.pack(pady=10)

root.mainloop()
