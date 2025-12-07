# LTspice2Matplotlib

Python tool for generating Matplotlib graphs from exported LTspice simulation data (.txt files), specifically designed for technical reports and documentation.

---

## Dependancies

To install and run LTspice2Matplotlib, you'll need a functional Python environment. This utility relies on the following core packages:

- Python

- Matplotlib: For rendering the simulation graphs.

- NumPy: numerical data handling

### Installation

You can install the required dependencies using pip.

```python
 pip install matplotlib numpy
```

If you have a requirements.txt file in your repository:

## Usage Guide

This utility is designed for simple command-line execution. After ensuring your LTspice data file (.txt) is ready, follow these steps:

1. Execute the Script

Run the main Python script from your terminal:

```python
python LTspice2python.py
```

2. Answer the Prompts

The script will then guide you by asking a series of questions. Simply enter the required information and press Enter after each prompt.

```python
Enter the path to the LTspice .txt file:
ex : C:\Users\...\my_transient_data.txt

Write the name of the parameter in regex style:
ex : V_out=[0-9.]+

Do you want to proceed? (y/n):
ex : y or n

```

The script will use your inputs to process the data and save the resulting Matplotlib graph as a high-resolution image file in the same directory.
