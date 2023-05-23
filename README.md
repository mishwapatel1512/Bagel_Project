# Bagel and Coffee Price Calculator

This is a simple Bagel and Coffee Price Calculator implemented using the Tkinter library in Python. It allows users to select their desired bagel, coffee, and toppings, and calculates the total price accordingly. The calculated price is also stored in a MySQL database.

## Prerequisites
- Python 3.x
- Tkinter library
- MySQL connector library

## Installation

1. Make sure you have Python 3.x installed on your system.

2. Install the Tkinter library by running the following command:

```python 
pip install tk
```
3. Install the MySQL connector library by running the following command:

```python 
pip install mysql-connector-python
```

## Usage

1. Import the necessary modules:

```python 
from tkinter import *
from tkinter import messagebox
import mysql.connector as my
```

2. Define the necessary functions:
- handle(): Handles the calculation of the total price, displays it in the GUI, and saves the data in a MySQL database.
- handle2(): Resets the form and clears all input fields.
- handle3(): Displays a farewell message and closes the application.

3. Create the main window and configure its appearance:

```python 
win = Tk()
win.title('Bagel and Coffee Price Calculator')
win.geometry('1000x1000')
win.configure(background='#ccffee')
```

4. Create and place various GUI elements such as labels, entry fields, radio buttons, checkboxes, and buttons.

5. Run the main event loop:

```python 
win.mainloop()
```

## Running the Application

To run the application, execute the Python script that contains the code.

```python 
python bagel_calculator.py
```

## Acknowledgments

- This code was created as a simple example of a bagel and coffee price calculator using Tkinter.
- The code assumes a MySQL database named project01 and a table named calc for storing the calculation data. Adjust the database connection parameters (host, user, password) according to your setup.
- This code can be further enhanced and customized to meet specific requirements.
