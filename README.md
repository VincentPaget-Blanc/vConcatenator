# vConcatenator

vConcatenator is a graphical user interface (GUI) application designed to concatenate CSV files from specified folders and subfolders. It provides options to filter files by subfolder name, drop rows with NaN values, and generate a log file summarizing the concatenation process.

## Features

- **Concatenate CSV Files**: Combine multiple CSV files into a single file.
- **Subfolder Filtering**: Optionally concatenate files only from specified subfolders.
- **Drop Rows with NaN Values**: Remove rows containing NaN (Not a Number) values.
- **Log File Generation**: Create a log file that records the folders from which files were concatenated and any rows that were dropped due to NaN values.
- **Cross-Platform Compatibility**: Works on Windows, macOS, and Linux.

## Dependencies

To run vConcatenator, you will need the following Python packages:

- Python 3.x
- pandas
- tkinter

## Installation

1. Ensure you have Python 3.x installed on your system.
2. Install the required packages using pip:

```bash
pip install pandas
```

Note: `tkinter` is usually included with Python installations, but if it is not available, you may need to install it separately depending on your operating system using:

```bash
pip install tkinter
```

## Usage

1. **Run the Application**:
    - Execute the script using Python:

```bash
python vConcatenator.py
```

2. **Interface Overview**:
    - **Source Folder**: Select the folder containing the CSV files you want to concatenate.
    - **File Pattern**: Specify a pattern to match the CSV files (e.g., `Results`).
    - **Output Folder**: Select the folder where the concatenated file will be saved.
    - **Output Filename**: Enter the name for the concatenated file (default: `concatenated_results.csv`).
    - **Only Concatenate from Subfolder**: Enable this option to concatenate files only from a specific subfolder name.
    - **Drop Rows with NaN Values**: Enable this option to remove rows with NaN values during concatenation.

3. **Concatenate Files**:
    - Click the "Concatenate" button to start the process.
    - The application will generate a concatenated CSV file and a log file (`concatenation_log.txt`) in the output folder.

## Log File

The log file (`concatenation_log.txt`) will contain:
- The source folder and file pattern used.
- A list of folders from which files were concatenated.
- Details on any rows dropped due to NaN values.

## Example

To concatenate all CSV files containing the word "Results" in their names from a specific subfolder named "data" within your source folder, follow these steps:

1. Select the source folder.
2. Enter "Results" as the file pattern.
3. Enable the "Only concatenate from subfolder" option and enter "data" as the subfolder name.
4. Optionally, enable the "Drop rows with NaN values" option.
5. Click "Concatenate".

The concatenated file will be saved in the specified output folder, along with a log file summarizing the process.

## Running with Spyder

To run the script using Spyder, follow these steps:

1. **Open Spyder**: Launch the Spyder IDE from your applications or by running `spyder` in your command line.

2. **Open the Script**:
   - In Spyder, go to `File` -> `Open` and select the `vConcatenator.py` script.

3. **Run the Script**:
   - Once the script is open in the editor, press `F5` or click the green "Run" button in the toolbar.

This will execute the script in Spyder, opening the GUI window where you can interact with the application.
