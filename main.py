import tkinter as tk
from tkinter import ttk, messagebox
import matplotlib.pyplot as plt
from algorithms import fifo_algorithm,lru_algorithm,mru_algorithm,optimal_algorithm

def run_simulation():
    try:
        reference_string = list(map(int, entry_ref_string.get().split(",")))
        num_frames = int(entry_frames.get())
        algorithm = algo_var.get()

        if num_frames <= 0:
            messagebox.showerror("Error", "Number of frames must be greater than 0.")
            return

        algorithms = {
            "FIFO": fifo_algorithm,
            "LRU": lru_algorithm,
            "MRU": mru_algorithm,
            "Optimal": optimal_algorithm
        }
        
        result, faults = algorithms[algorithm](reference_string, num_frames)

        for row in tree.get_children():
            tree.delete(row)
        for step, page, frames, fault in result:
            tree.insert("", "end", values=(step, page, frames, fault))

        label_faults.config(text=f"Total Page Faults: {faults}")

        with open("page_replacement_results.txt", "w") as file:
            file.write(f"Algorithm: {algorithm}\n")
            file.write(f"Total Page Faults: {faults}\n")
            file.write("Step | Page | Frames | Page Fault\n")
            for step, page, frames, fault in result:
                file.write(f"{step} | {page} | {frames} | {fault}\n")
    except ValueError:
        messagebox.showerror("Error", "Invalid input. Please enter numbers only.")

def plot_graph():
    reference_string = list(map(int, entry_ref_string.get().split(",")))
    num_frames = int(entry_frames.get())

    algorithms = ["FIFO", "LRU", "MRU", "Optimal"]
    faults = [
        fifo_algorithm(reference_string, num_frames)[1],
        lru_algorithm(reference_string, num_frames)[1],
        mru_algorithm(reference_string, num_frames)[1],
        optimal_algorithm(reference_string, num_frames)[1]
    ]

    plt.bar(algorithms, faults, color=['#4CAF50', '#2196F3', '#FF9800', '#9C27B0'])
    plt.xlabel("Algorithms")
    plt.ylabel("Page Faults")
    plt.title("Page Replacement Algorithm Comparison")
    plt.show()

root = tk.Tk()
root.title("Page Replacement Algorithm Simulator")
root.geometry("800x600")
root.config(bg="#f1f1f1")

frame_top = tk.Frame(root, bg="#e3f2fd", padx=20, pady=20)
frame_top.pack(pady=20)

tk.Label(frame_top, text="Reference String:").grid(row=0, column=0, padx=5)
entry_ref_string = tk.Entry(frame_top, width=30)
entry_ref_string.grid(row=0, column=1, padx=10)

tk.Label(frame_top, text="Frames:").grid(row=1, column=0, padx=5)
entry_frames = tk.Entry(frame_top, width=5)
entry_frames.grid(row=1, column=1, padx=10)

tk.Label(frame_top, text="Algorithm:").grid(row=2, column=0, padx=5)
algo_var = tk.StringVar(value="FIFO")
algo_dropdown = ttk.Combobox(frame_top, textvariable=algo_var, values=["FIFO", "LRU", "MRU", "Optimal"])
algo_dropdown.grid(row=2, column=1, padx=10)

run_btn = tk.Button(frame_top, text="Run Simulation", command=run_simulation, width=20)
run_btn.grid(row=3, column=0, pady=10)
plot_btn = tk.Button(frame_top, text="Plot Graph", command=plot_graph, width=20)
plot_btn.grid(row=3, column=1, pady=10)

frame_table = tk.Frame(root, padx=20, pady=10)
frame_table.pack(pady=20)
columns = ("Step", "Page", "Frames", "Page Fault")
tree = ttk.Treeview(frame_table, columns=columns, show="headings")
for col in columns:
    tree.heading(col, text=col)
    tree.column(col, width=150)
tree.pack()

label_faults = tk.Label(root, text="Total Page Faults: 0")
label_faults.pack(pady=10)

root.mainloop()
