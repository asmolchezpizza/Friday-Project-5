import tkinter as tk
from tkinter import ttk, messagebox
import sqlite3
import os

# --- Database Management ---

def setup_database():
    """
    Sets up the SQLite database and the customers table.
    Creates the database file if it doesn't exist.
    """
    # Ensure the database file is created in the same directory as the script
    db_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'customers.db')
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    
    # Create the customers table if it doesn't already exist
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS customers (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            birthday TEXT,
            email TEXT,
            phone TEXT,
            address TEXT,
            contact_method TEXT
        )
    ''')
    
    conn.commit()
    conn.close()

def submit_customer_info(name, birthday, email, phone, address, contact_method):
    """
    Inserts a new customer record into the database.
    
    Args:
        name (str): Customer's full name.
        birthday (str): Customer's birthday.
        email (str): Customer's email address.
        phone (str): Customer's phone number.
        address (str): Customer's physical address.
        contact_method (str): Customer's preferred contact method.
    """
    db_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'customers.db')
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    
    # Insert the new customer data into the table
    cursor.execute('''
        INSERT INTO customers (name, birthday, email, phone, address, contact_method)
        VALUES (?, ?, ?, ?, ?, ?)
    ''', (name, birthday, email, phone, address, contact_method))
    
    conn.commit()
    conn.close()

# --- GUI Application ---

class CustomerApp:
    def __init__(self, root):
        """
        Initializes the GUI application.
        
        Args:
            root (tk.Tk): The main window of the application.
        """
        self.root = root
        self.root.title("Customer Information Management")
        self.root.geometry("450x400")
        self.root.configure(bg="#f0f0f0")

        # Use a modern theme for ttk widgets
        style = ttk.Style(self.root)
        style.theme_use("clam")

        # Main frame for content
        main_frame = ttk.Frame(self.root, padding="20")
        main_frame.pack(fill=tk.BOTH, expand=True)

        # Title Label
        title_label = ttk.Label(
            main_frame,
            text="Customer Information",
            font=("Helvetica", 16, "bold")
        )
        title_label.grid(row=0, column=0, columnspan=2, pady=(0, 20), sticky="w")
        
        # --- Form Fields ---
        
        # Name
        ttk.Label(main_frame, text="Full Name:").grid(row=1, column=0, sticky=tk.W, pady=5)
        self.name_entry = ttk.Entry(main_frame, width=40)
        self.name_entry.grid(row=1, column=1, sticky=tk.W, pady=5)

        # Birthday
        ttk.Label(main_frame, text="Birthday (YYYY-MM-DD):").grid(row=2, column=0, sticky=tk.W, pady=5)
        self.birthday_entry = ttk.Entry(main_frame, width=40)
        self.birthday_entry.grid(row=2, column=1, sticky=tk.W, pady=5)

        # Email
        ttk.Label(main_frame, text="Email:").grid(row=3, column=0, sticky=tk.W, pady=5)
        self.email_entry = ttk.Entry(main_frame, width=40)
        self.email_entry.grid(row=3, column=1, sticky=tk.W, pady=5)

        # Phone
        ttk.Label(main_frame, text="Phone Number:").grid(row=4, column=0, sticky=tk.W, pady=5)
        self.phone_entry = ttk.Entry(main_frame, width=40)
        self.phone_entry.grid(row=4, column=1, sticky=tk.W, pady=5)

        # Address
        ttk.Label(main_frame, text="Address:").grid(row=5, column=0, sticky=tk.W, pady=5)
        self.address_entry = ttk.Entry(main_frame, width=40)
        self.address_entry.grid(row=5, column=1, sticky=tk.W, pady=5)

        # Preferred Contact Method Dropdown
        ttk.Label(main_frame, text="Preferred Contact Method:").grid(row=6, column=0, sticky=tk.W, pady=5)
        self.contact_method_var = tk.StringVar()
        self.contact_method_combo = ttk.Combobox(
            main_frame,
            textvariable=self.contact_method_var,
            values=["Email", "Phone", "Mail"],
            state="readonly",
            width=37
        )
        self.contact_method_combo.grid(row=6, column=1, sticky=tk.W, pady=5)
        self.contact_method_combo.set("Email") # Default value

        # --- Submit Button ---
        submit_button = ttk.Button(
            main_frame,
            text="Submit",
            command=self.submit_action,
            style="Accent.TButton"
        )
        submit_button.grid(row=7, column=1, pady=20, sticky=tk.E)

        # Style for the accent button
        style.configure("Accent.TButton", foreground="white", background="#0078D7")

    def clear_form(self):
        """Clears all input fields in the form."""
        self.name_entry.delete(0, tk.END)
        self.birthday_entry.delete(0, tk.END)
        self.email_entry.delete(0, tk.END)
        self.phone_entry.delete(0, tk.END)
        self.address_entry.delete(0, tk.END)
        self.contact_method_combo.set("Email")

    def submit_action(self):
        """Handles the logic when the submit button is clicked."""
        name = self.name_entry.get()
        birthday = self.birthday_entry.get()
        email = self.email_entry.get()
        phone = self.phone_entry.get()
        address = self.address_entry.get()
        contact_method = self.contact_method_var.get()

        # Basic validation: ensure the name is not empty
        if not name:
            messagebox.showerror("Validation Error", "Full Name is a required field.")
            return

        try:
            # Submit data to the database
            submit_customer_info(name, birthday, email, phone, address, contact_method)
            # Show a success message
            messagebox.showinfo("Success", "Customer information has been successfully submitted.")
            # Clear the form for the next entry
            self.clear_form()
        except sqlite3.Error as e:
            messagebox.showerror("Database Error", f"An error occurred while submitting the data: {e}")

# --- Main Execution ---

if __name__ == "__main__":
    # 1. Set up the database and table first
    setup_database()
    
    # 2. Create and run the GUI application
    app_root = tk.Tk()
    app = CustomerApp(app_root)
    app_root.mainloop()