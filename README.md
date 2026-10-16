# Sales Management System

A Python and MySQL-based application designed to simplify sales operations, product management, and inventory tracking for small businesses.

## About the Project

The Sales Management System is a menu-driven application developed using Python and MySQL. It helps manage product information, maintain stock records, record customer sales, and calculate sales amounts automatically.

This project demonstrates the practical implementation of Python programming, SQL queries, database management, and Python–MySQL connectivity.

## Features

- **Add Products:** Add new products with their name, category, price, and stock quantity.
- **View Products:** Display available products and their details.
- **Search Products:** Search for products by name.
- **Record Sales:** Record customer transactions and quantities sold.
- **Automatic Billing:** Calculate the total amount of each sale.
- **Stock Management:** Update product stock after a sale.
- **Sales Records:** View previously recorded sales transactions.
- **Total Sales:** Calculate the total sales amount.
- **MySQL Database:** Store product and sales information persistently.

## Technologies Used

- Python 3
- MySQL
- MySQL Connector/Python
- SQL
- Python IDLE / Command Prompt

## Project Structure

```text
Sales-Management-System/
├── sales_management.py
├── database.sql
├── requirements.txt
└── README.md
```

*Note: Adjust the filenames above to match the actual files in your repository.*

## Prerequisites

Before running the application, install:

1. Python 3
2. MySQL Server
3. MySQL Workbench (recommended)
4. MySQL Connector/Python

## Installation and Setup

### 1. Clone the repository

```bash
git clone https://github.com/YOUR-USERNAME/Sales-Management-System.git
cd Sales-Management-System
```

Replace `YOUR-USERNAME` with your GitHub username.

### 2. Install the required Python package

```bash
py -m pip install mysql-connector-python
```

### 3. Set up the database

Open MySQL Workbench, connect to your MySQL server, and execute the SQL commands in your database setup file.

Ensure that the database and tables match the names used in the Python application.

### 4. Configure the database connection

Update the database connection settings in your Python file with your local MySQL username, password, and database name.

**Security note:** Never commit your real database password or other credentials to GitHub.

### 5. Run the application

```bash
py sales_management.py
```

The application should display a menu through which you can manage products and sales.

## Project Documentation

View the complete project report, including the database design, source code, and sample outputs.

[View Project Documentation (PDF)](Sales_Management_System_Documentation.pdf)


## Learning Outcomes

Through this project, I explored:

- Python functions and control flow
- SQL queries and database operations
- Python–MySQL connectivity
- Inventory and stock management
- Sales calculations and transaction records
- Error handling and structured programming

## Future Improvements

Potential enhancements include:

- Customer registration and customer history
- Shopping cart with multiple products per bill
- Automatic receipt generation
- Payment method recording
- Graphical user interface or web-based dashboard
- Sales reports and analytics
- User authentication and access control

## Project Status

Educational project — developed to  Python programming, SQL, and database connectivity.

## Author

Chiranjib Deka

GitHub: https://github.com/chiranjibbb-stack

---

*This project is intended for educational purposes and can be extended with additional features for real-world business workflows.*
