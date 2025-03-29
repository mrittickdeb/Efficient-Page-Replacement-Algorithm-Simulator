Page Replacement Algorithm Simulator

This project is a Graphical User Interface (GUI) application for simulating Page Replacement Algorithms using Python and Tkinter. The simulator allows users to input a reference string, select a page replacement algorithm, and visualize the results.

📌 Features
Supports the following algorithms:

✅ FIFO (First In First Out)

✅ LRU (Least Recently Used)

✅ Optimal Page Replacement

✅ MRU (Most Recently Used)

Displays step-by-step execution results in a table.

Shows total page faults for the selected algorithm.

Saves results to a file: page_replacement_results.txt.

Provides a graphical comparison of page faults for different algorithms.

⚙️ Requirements
Python 3.x

Required Libraries:

tkinter (Usually pre-installed with Python)

ttk (Comes with tkinter)

matplotlib

To install any missing dependencies:

pip install matplotlib

🚀 How to Run
Clone or Download the project.

Navigate to the project directory.

Run the script using:

python page_replacement_simulator.py

🏃 Usage Instructions
Enter the Reference String — A comma-separated sequence of page numbers.

Example: 7,0,1,2,0,3,4,2,3,0,3,2

Enter the Number of Frames — The capacity of the frame buffer.

Example: 3

Select the Algorithm — Choose from:

FIFO, LRU, Optimal, or MRU.

Run Simulation — Click the "Run Simulation" button.

View Results — See the step-by-step output in the table.

Plot Results — Click "Plot Graph" to compare performance.

📁 Output
Results are displayed in the GUI.

Results are saved to a file named page_replacement_results.txt.

The graph shows a bar chart comparing total page faults.

📊 Sample Graph Output
The bar chart compares the total page faults for the four algorithms.

🔍 Example
Reference String: 7, 0, 1, 2, 0, 3, 4, 2, 3, 0, 3, 2

Number of Frames: 3

Algorithm: FIFO

Output file (page_replacement_results.txt):

Algorithm: FIFO
Total Page Faults: 9
Step | Page | Frames       | Page Fault
1    | 7    | [7]          | Yes
2    | 0    | [7, 0]       | Yes
3    | 1    | [7, 0, 1]    | Yes
4    | 2    | [0, 1, 2]    | Yes

📝 License
This project is licensed under the MIT License — feel free to modify and use it.

