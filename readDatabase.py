import tkinter as tk
from tkinter import ttk
import sqlite3

def view_customers():
    """
    Connects to the database and displays customer data in a GUI window.
    """
    # Create the main window
    window = tk.Tk()
    window.title("Customer Database Viewer")
    window.geometry("800x500") # Set a default size for the window

    # --- Database Connection and Data Fetching ---
    try:
        # Connect to the SQLite database
        conn = sqlite3.connect('customers.db')
        cursor = conn.cursor()

        # IMPORTANT: Replace 'customers' with the actual name of your table if it's different.
        cursor.execute("SELECT * FROM customers")
        rows = cursor.fetchall()
        
        # Get column names from the cursor description
        column_names = [description[0] for description in cursor.description]

    except sqlite3.Error as e:
        # Handle potential errors like the table not existing
        error_label = tk.Label(window, text=f"Database Error: {e}", fg="red")
        error_label.pack(pady=20, padx=20)
        window.mainloop()
        return
    finally:
        # Ensure the database connection is closed
        if conn:
            conn.close()

    # --- GUI Setup for Displaying Data ---
    
    # Create a frame to hold the Treeview and scrollbars
    frame = tk.Frame(window)
    frame.pack(fill='both', expand=True, padx=10, pady=10)

    # Create the Treeview widget (our table)
    tree = ttk.Treeview(frame, columns=column_names, show='headings')

    # Define headings from the fetched column names
    for col in column_names:
        tree.heading(col, text=col.capitalize()) # Capitalize for better readability
        tree.column(col, width=120) # Set a default width for columns

    # Insert data rows into the Treeview
    for row in rows:
        tree.insert("", "end", values=row)

    # Add scrollbars for both horizontal and vertical scrolling
    vsb = ttk.Scrollbar(frame, orient="vertical", command=tree.yview)
    vsb.pack(side='right', fill='y')
    hsb = ttk.Scrollbar(frame, orient="horizontal", command=tree.xview)
    hsb.pack(side='bottom', fill='x')

    tree.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set)
    
    # Pack the tree to make it visible
    tree.pack(side='left', fill='both', expand=True)
    
    # Start the GUI event loop
    window.mainloop()

# --- Run the main function ---
if __name__ == "__main__":
    view_customers()