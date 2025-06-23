<h1>CLI Calculator – Python</h1> 

## Overview

This is a simple command-line calculator built using Python. It allows users to perform basic arithmetic operations such as addition, subtraction, multiplication, and division through a text-based interface.

## Features

- Addition of two numbers  
- Subtraction of two numbers  
- Multiplication of two numbers  
- Division of two numbers with division-by-zero handling  
- Loop-based input for continuous use  
- Clean and readable output  

## Requirements

- Python  
- A text editor VS Code  
- Terminal or Command Prompt  

- Inputs are automatically handled to remove extra spaces and support lowercase text.

## Example:
```bash
python calculator.py

Welcome to CLI Calculator!
Operations: + for addition, - for subtraction, * for multiplication, / for division

Enter the first number: 10
Enter the operator (+, -, *, /): *
Enter the second number: 5
Result: 50.0

Do you want to perform another calculation? (yes/no): yes
Continuing.....

Enter the first number: 20
Enter the operator (+, -, *, /): /
Enter the second number: 0
Result: Error: Division by zero

Do you want to perform another calculation? (yes/no): y
Continuing.....

Enter the first number: 15
Enter the operator (+, -, *, /): -
Enter the second number: 8
Result: 7.0

Do you want to perform another calculation? (yes/no): no
Thank you for using the calculator!
