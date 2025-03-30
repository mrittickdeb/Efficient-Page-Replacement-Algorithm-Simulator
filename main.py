import tkinter as tk
from tkinter import ttk, messagebox
import matplotlib.pyplot as plt

# FIFO (First In First Out) Algorithm
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

# LRU (Least Recently Used) Algorithm
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
                lru_page = min(frames, key=lambda x: recent_usage[x])
                frames[frames.index(lru_page)] = page
            page_faults += 1
            fault = "Yes"
        else:
            fault = "No"
        
        recent_usage[page] = i
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
                future_use = {p: (reference_string[i:].index(p) if p in reference_string[i:] else float("inf")) for p in frames}
                farthest_page = max(future_use, key=future_use.get)
                frames[frames.index(farthest_page)] = page
            page_faults += 1
            fault = "Yes"
        else:
            fault = "No"
        
        result.append((i + 1, page, list(frames), fault))

    return result, page_faults

# MRU (Most Recently Used) Algorithm
def mru_algorithm(reference_string, num_frames):
    frames = []
    page_faults = 0
    recent_usage = {}
    result = []

    for i, page in enumerate(reference_string):
        if page not in frames:
            if len(frames) < num_frames:
                frames.append(page)
            else:
                mru_page = max(frames, key=lambda x: recent_usage[x])
                frames[frames.index(mru_page)] = page
            page_faults += 1
            fault = "Yes"
        else:
            fault = "No"
        
        recent_usage[page] = i
        result.append((i + 1, page, list(frames), fault))

    return result, page_faults

# --------- GUI Functions -------
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
        elif algorithm == "MRU":
            result, faults = mru_algorithm(reference_string, num_frames)
        else:
            messagebox.showerror("Error", "Invalid Algorithm")
            return

        for row in tree.get_children():
            tree.delete(row)

        for step, page, frames, fault in result:
            tree.insert("", "end", values=(step, page, frames, fault))

        label_faults.config(text=f"Total Page Faults: {faults}")

        # --------File Handling--------
        with open("page_replacement_results.txt", "w") as file:
            file.write(f"Algorithm: {algorithm}\n")
            file.write(f"Total Page Faults: {faults}\n")
            file.write("Step | Page | Frames | Page Fault\n")
            for step, page, frames, fault in result:
                file.write(f"{step} | {page} | {frames} | {fault}\n")

    except ValueError:
        messagebox.showerror("Error", "Invalid input. Please enter numbers only.")

# Function to plot results
def plot_graph():
    reference_string = list(map(int, entry_ref_string.get().split(",")))
    num_frames = int(entry_frames.get())

    algorithms = ["FIFO", "LRU", "Optimal", "MRU"]
    faults = [
        fifo_algorithm(reference_string, num_frames)[1],
        lru_algorithm(reference_string, num_frames)[1],
        optimal_algorithm(reference_string, num_frames)[1],
        mru_algorithm(reference_string, num_frames)[1]
    ]

    plt.bar(algorithms, faults, color=['#4CAF50', '#2196F3', '#FF9800', '#9C27B0'])
    plt.xlabel("Algorithms")
    plt.ylabel("Page Faults")
    plt.title("Page Replacement Algorithm Comparison")
    plt.show()

# ---------------- GUI Setup ----------------

root = tk.Tk()
root.title("Page Replacement Algorithm Simulator")
root.geometry("800x600")
root.config(bg="#f1f1f1")  # Background color

# Fonts and Colors used
header_font = ("Helvetica", 14, "bold")
label_font = ("Arial", 12)
button_font = ("Arial", 12, "bold")
treeview_font = ("Courier New", 10)
bg_color = "#e3f2fd"

frame_top = tk.Frame(root, bg=bg_color, padx=20, pady=20)
frame_top.pack(pady=20)

tk.Label(frame_top, text="Reference String:", font=label_font, bg=bg_color).grid(row=0, column=0, sticky="e", padx=5)
entry_ref_string = tk.Entry(frame_top, font=("Arial", 12), width=30)
entry_ref_string.grid(row=0, column=1, padx=10)

tk.Label(frame_top, text="Frames:", font=label_font, bg=bg_color).grid(row=1, column=0, sticky="e", padx=5)
entry_frames = tk.Entry(frame_top, font=("Arial", 12), width=5)
entry_frames.grid(row=1, column=1, padx=10)

tk.Label(frame_top, text="Algorithm:", font=label_font, bg=bg_color).grid(row=2, column=0, sticky="e", padx=5)
algo_var = tk.StringVar(value="FIFO")
algo_dropdown = ttk.Combobox(frame_top, textvariable=algo_var, values=["FIFO", "LRU", "Optimal", "MRU"], font=("Arial", 12))
algo_dropdown.grid(row=2, column=1, padx=10)

# buttons setup
run_btn = tk.Button(frame_top, text="Run Simulation", font=button_font, bg="#4CAF50", fg="white", command=run_simulation, width=20)
run_btn.grid(row=3, column=0, pady=10)

plot_btn = tk.Button(frame_top, text="Plot Graph", font=button_font, bg="#2196F3", fg="white", command=plot_graph, width=20)
plot_btn.grid(row=3, column=1, pady=10)

# Table Frame setup
frame_table = tk.Frame(root, bg="#ffffff", padx=20, pady=10)
frame_table.pack(pady=20)

columns = ("Step", "Page", "Frames", "Page Fault")
tree = ttk.Treeview(frame_table, columns=columns, show="headings", style="Custom.Treeview")
tree.heading("Step", text="Step")
tree.heading("Page", text="Page")
tree.heading("Frames", text="Frames")
tree.heading("Page Fault", text="Page Fault")

tree.column("Step", width=100, anchor="center")
tree.column("Page", width=100, anchor="center")
tree.column("Frames", width=200, anchor="center")
tree.column("Page Fault", width=100, anchor="center")

tree.pack()

# Page Faults Label
label_faults = tk.Label(root, text="Total Page Faults: 0", font=("Arial", 14, "bold"), bg="#f1f1f1", fg="#333")
label_faults.pack(pady=10)

# Style for Treeview 
style = ttk.Style()
style.configure("Custom.Treeview",
                background="#f9f9f9",
                foreground="black",
                fieldbackground="#f1f1f1")

root.mainloop()
