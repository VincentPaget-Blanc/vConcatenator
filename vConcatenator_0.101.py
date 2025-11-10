#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 10 12:59:52 2025

@author: vincentpb
"""

import tkinter as tk
from tkinter import filedialog, messagebox, Checkbutton, BooleanVar
import pandas as pd
import glob
import os
import platform
import subprocess
from datetime import datetime

def open_folder_in_explorer(folder_path):
    if platform.system() == "Windows":
        os.startfile(folder_path)
    elif platform.system() == "Darwin":  # macOS
        subprocess.run(["open", folder_path])
    else:  # Linux
        subprocess.run(["xdg-open", folder_path])

def concatenate_files():
    source_folder = folder_path_var.get()
    file_pattern = file_pattern_var.get()
    output_folder = output_folder_var.get()
    output_filename = output_filename_var.get()
    use_subfolder = use_subfolder_var.get()
    subfolder_name = subfolder_name_var.get()
    drop_na = drop_na_var.get()

    if not output_filename:
        output_filename = "concatenated_results.csv"

    if not source_folder or not file_pattern or not output_folder:
        messagebox.showerror("Error", "Please select both source and output folders, and enter a file pattern.")
        return

    if use_subfolder and not subfolder_name:
        messagebox.showerror("Error", "Please enter a subfolder name.")
        return

    # Build the search pattern
    if use_subfolder:
        search_pattern = os.path.join(source_folder, "**", subfolder_name, "**", f"*{file_pattern}*.csv")
    else:
        search_pattern = os.path.join(source_folder, "**", f"*{file_pattern}*.csv")

    file_list = glob.glob(search_pattern, recursive=True)

    if not file_list:
        messagebox.showerror("Error", f"No files found matching the pattern: {search_pattern}")
        return

    # Create a log file
    log_file_path = os.path.join(output_folder, "concatenation_log.txt")
    with open(log_file_path, "w") as log_file:
        log_file.write(f"Concatenation Log - {datetime.now()}\n")
        log_file.write(f"Source Folder: {source_folder}\n")
        log_file.write(f"File Pattern: {file_pattern}\n")
        log_file.write(f"Subfolder Option: {'Enabled' if use_subfolder else 'Disabled'}\n")
        log_file.write(f"Drop NaN Rows: {'Enabled' if drop_na else 'Disabled'}\n\n")

        # Count unique subfolders and log them
        subfolders = set(os.path.dirname(f) for f in file_list)
        log_file.write("Folders with concatenated files:\n")
        for subfolder in subfolders:
            log_file.write(f"{subfolder}\n")

        # Read the first file with header
        df = pd.read_csv(file_list[0])
        if drop_na:
            df = df.dropna()
        log_file.write("\nFiles concatenated:\n")

        # Read the rest of the files, skipping the header row
        for file in file_list[1:]:
            df_temp = pd.read_csv(file, skiprows=1, names=df.columns)
            if drop_na:
                initial_rows = len(df_temp)
                df_temp = df_temp.dropna()
                dropped_rows = initial_rows - len(df_temp)
                if dropped_rows > 0:
                    log_file.write(f"File: {file} - Dropped {dropped_rows} rows with NaN values.\n")
            df = pd.concat([df, df_temp], ignore_index=True)
            log_file.write(f"{file}\n")

        # Save the concatenated DataFrame
        output_path = os.path.join(output_folder, output_filename)
        df.to_csv(output_path, index=False)

        # Success message
        messagebox.showinfo("Success", f"Concatenated {len(file_list)} files. Result saved to '{output_path}'. Log saved to '{log_file_path}'.")

# Create the main window
root = tk.Tk()
root.title("CSV Concatenator")

# Source folder selection
folder_path_var = tk.StringVar()
tk.Label(root, text="Select Source Folder:").grid(row=0, column=0, padx=5, pady=5)
tk.Entry(root, textvariable=folder_path_var, width=50).grid(row=0, column=1, padx=5, pady=5)
tk.Button(root, text="Browse", command=lambda: folder_path_var.set(filedialog.askdirectory())).grid(row=0, column=2, padx=5, pady=5)

# File pattern input
file_pattern_var = tk.StringVar()
tk.Label(root, text="File Pattern (e.g., 'Results'):").grid(row=1, column=0, padx=5, pady=5)
tk.Entry(root, textvariable=file_pattern_var, width=50).grid(row=1, column=1, padx=5, pady=5)

# Output folder selection
output_folder_var = tk.StringVar()
tk.Label(root, text="Select Output Folder:").grid(row=2, column=0, padx=5, pady=5)
tk.Entry(root, textvariable=output_folder_var, width=50).grid(row=2, column=1, padx=5, pady=5)
tk.Button(root, text="Browse", command=lambda: output_folder_var.set(filedialog.askdirectory())).grid(row=2, column=2, padx=5, pady=5)

# Output filename input
output_filename_var = tk.StringVar(value="concatenated_results.csv")
tk.Label(root, text="Output Filename:").grid(row=3, column=0, padx=5, pady=5)
tk.Entry(root, textvariable=output_filename_var, width=50).grid(row=3, column=1, padx=5, pady=5)

# Subfolder option
use_subfolder_var = BooleanVar()
tk.Checkbutton(root, text="Only concatenate from subfolder:", variable=use_subfolder_var).grid(row=4, column=0, padx=5, pady=5, sticky="w")
subfolder_name_var = tk.StringVar()
subfolder_name_entry = tk.Entry(root, textvariable=subfolder_name_var, width=50, state="disabled")
subfolder_name_entry.grid(row=4, column=1, padx=5, pady=5)

# Drop NaN rows option
drop_na_var = BooleanVar()
tk.Checkbutton(root, text="Drop rows with NaN values:", variable=drop_na_var).grid(row=5, column=0, padx=5, pady=5, sticky="w")

def toggle_subfolder_entry():
    if use_subfolder_var.get():
        subfolder_name_entry.config(state="normal")
    else:
        subfolder_name_entry.config(state="disabled")

use_subfolder_var.trace_add("write", lambda *args: toggle_subfolder_entry())

# Concatenate button
tk.Button(root, text="Concatenate", command=concatenate_files).grid(row=6, column=1, padx=5, pady=5)

root.mainloop()
