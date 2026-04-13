import tkinter as tk
from tkinter import filedialog, messagebox
from monitor import start_monitoring
import threading

def browse_folder():
    path = filedialog.askdirectory()
    entry_path.delete(0, tk.END)
    entry_path.insert(0, path)

def start():
    path = entry_path.get()
    algo = algo_var.get()

    if not path:
        messagebox.showerror("Error", "Select folder!")
        return

    threading.Thread(target=start_monitoring, args=(path, algo), daemon=True).start()
    messagebox.showinfo("Started", "Monitoring started!")

app = tk.Tk()
app.title("File Integrity Checker")

tk.Label(app, text="Select Folder").pack()
entry_path = tk.Entry(app, width=50)
entry_path.pack()

tk.Button(app, text="Browse", command=browse_folder).pack()

algo_var = tk.StringVar(value="sha256")

tk.Label(app, text="Select Algorithm").pack()
tk.OptionMenu(app, algo_var, "md5", "sha1", "sha256").pack()

tk.Button(app, text="Start Monitoring", command=start).pack()

app.mainloop()