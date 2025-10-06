# Friday-Project-5# A simple script to generate the README.md file for the repository.

# The full content for the README.md file is stored in this multiline string.
readme_content = """
# Customer Data Entry Application

A simple desktop application for entering and viewing customer information. This project uses a Python GUI for data input and stores the information in an SQLite database.

---

## 📜 Description

This project provides a straightforward graphical user interface (GUI) for users to input customer details, which are then saved to a local database. It also includes a separate script for developers or administrators to view the contents of the database directly from the command line.

---

## ✨ Features

* **User-Friendly GUI**: A clean interface for entering customer data such as name, address, and contact information.
* **Persistent Storage**: Customer data is saved in an `SQLite` database, ensuring that information is retained between sessions.
* **Database Viewer**: A simple script to quickly display all records stored in the customer database.

---

## 🛠️ Prerequisites

Before you begin, ensure you have **Python 3** installed on your system. The scripts use the following standard Python libraries, which typically do not require separate installation:

* `tkinter` (for the GUI)
* `sqlite3` (for database interaction)

---

## 🚀 Usage

There are two main components to this application.

### 1. Entering Customer Data

To launch the data entry GUI, run the `FridayProject5.py` script from your terminal:

```bash
python "FridayProject5.py"