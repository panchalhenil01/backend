import tkinter as tk
from tkinter import ttk, messagebox, filedialog
import sqlite3
import csv
import os

# --------------------------- Database Setup ---------------------------
class Database:
    def __init__(self):
        self.conn = sqlite3.connect("meditrack.db")
        self.create_tables()

    def create_tables(self):
        cursor = self.conn.cursor()
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE NOT NULL,
            password TEXT NOT NULL
        )
        """)
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS patients (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            age INTEGER,
            gender TEXT,
            contact TEXT,
            condition TEXT
        )
        """)
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS appointments (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            patient_id INTEGER,
            date TEXT,
            time TEXT,
            doctor TEXT,
            FOREIGN KEY (patient_id) REFERENCES patients(id)
        )
        """)
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS billing (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            patient_id INTEGER,
            amount REAL,
            status TEXT,
            FOREIGN KEY (patient_id) REFERENCES patients(id)
        )
        """)
        self.conn.commit()

    def execute(self, query, params=()):
        try:
            cursor = self.conn.cursor()
            cursor.execute(query, params)
            self.conn.commit()
            return cursor
        except sqlite3.Error as e:
            messagebox.showerror("Database Error", str(e))

# --------------------------- Main Application ---------------------------
class MediTrackApp:
    def __init__(self, root):
        self.root = root
        self.root.title("🏥 MediTrack - Healthcare Management System")
        self.root.geometry("900x600")
        self.db = Database()

        self.show_login_screen()

    # ------------------- LOGIN -------------------
    def show_login_screen(self):
        self.clear_screen()
        tk.Label(self.root, text="MediTrack Login", font=("Arial", 24, "bold")).pack(pady=40)

        tk.Label(self.root, text="Username:").pack()
        self.username_entry = tk.Entry(self.root)
        self.username_entry.pack()

        tk.Label(self.root, text="Password:").pack()
        self.password_entry = tk.Entry(self.root, show="*")
        self.password_entry.pack()

        tk.Button(self.root, text="Login", width=10, command=self.login).pack(pady=10)
        tk.Button(self.root, text="Register", width=10, command=self.register).pack()

    def login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()
        result = self.db.execute("SELECT * FROM users WHERE username=? AND password=?", (username, password)).fetchone()

        if result:
            messagebox.showinfo("Success", "Login successful!")
            self.show_dashboard()
        else:
            messagebox.showerror("Error", "Invalid username or password")

    def register(self):
        username = self.username_entry.get()
        password = self.password_entry.get()

        if not username or not password:
            messagebox.showwarning("Warning", "All fields required!")
            return

        try:
            self.db.execute("INSERT INTO users(username, password) VALUES (?,?)", (username, password))
            messagebox.showinfo("Success", "User registered successfully!")
        except Exception as e:
            messagebox.showerror("Error", f"Registration failed: {e}")

    # ------------------- DASHBOARD -------------------
    def show_dashboard(self):
        self.clear_screen()
        tk.Label(self.root, text="🏥 MediTrack Dashboard", font=("Arial", 22, "bold")).pack(pady=20)

        btn_frame = tk.Frame(self.root)
        btn_frame.pack(pady=20)

        tk.Button(btn_frame, text="Patient Management", width=20, command=self.manage_patients).grid(row=0, column=0, padx=10, pady=10)
        tk.Button(btn_frame, text="Appointments", width=20, command=self.manage_appointments).grid(row=0, column=1, padx=10, pady=10)
        tk.Button(btn_frame, text="Billing", width=20, command=self.manage_billing).grid(row=0, column=2, padx=10, pady=10)
        tk.Button(btn_frame, text="Export Data", width=20, command=self.export_data).grid(row=1, column=0, padx=10, pady=10)
        tk.Button(btn_frame, text="Logout", width=20, command=self.show_login_screen).grid(row=1, column=2, padx=10, pady=10)

    # ------------------- PATIENT MANAGEMENT -------------------
    def manage_patients(self):
        self.clear_screen()
        tk.Label(self.root, text="👨‍⚕️ Patient Management", font=("Arial", 20, "bold")).pack(pady=10)

        form = tk.Frame(self.root)
        form.pack(pady=10)

        tk.Label(form, text="Name:").grid(row=0, column=0)
        name = tk.Entry(form)
        name.grid(row=0, column=1)

        tk.Label(form, text="Age:").grid(row=1, column=0)
        age = tk.Entry(form)
        age.grid(row=1, column=1)

        tk.Label(form, text="Gender:").grid(row=2, column=0)
        gender = ttk.Combobox(form, values=["Male", "Female", "Other"])
        gender.grid(row=2, column=1)

        tk.Label(form, text="Contact:").grid(row=3, column=0)
        contact = tk.Entry(form)
        contact.grid(row=3, column=1)

        tk.Label(form, text="Condition:").grid(row=4, column=0)
        condition = tk.Entry(form)
        condition.grid(row=4, column=1)

        def add_patient():
            if name.get() == "":
                messagebox.showerror("Error", "Name is required")
                return
            self.db.execute(
                "INSERT INTO patients (name, age, gender, contact, condition) VALUES (?,?,?,?,?)",
                (name.get(), age.get(), gender.get(), contact.get(), condition.get())
            )
            messagebox.showinfo("Success", "Patient added successfully!")
            self.manage_patients()

        tk.Button(form, text="Add Patient", command=add_patient).grid(row=5, columnspan=2, pady=10)

        # Table
        table = ttk.Treeview(self.root, columns=("ID", "Name", "Age", "Gender", "Contact", "Condition"), show="headings")
        for col in table["columns"]:
            table.heading(col, text=col)
            table.column(col, width=120)
        table.pack(fill="both", expand=True, pady=10)

        for row in self.db.execute("SELECT * FROM patients").fetchall():
            table.insert("", "end", values=row)

        tk.Button(self.root, text="Back", command=self.show_dashboard).pack(pady=10)

    # ------------------- APPOINTMENT MANAGEMENT -------------------
    def manage_appointments(self):
        self.clear_screen()
        tk.Label(self.root, text="📅 Appointment Management", font=("Arial", 20, "bold")).pack(pady=10)

        form = tk.Frame(self.root)
        form.pack(pady=10)

        tk.Label(form, text="Patient ID:").grid(row=0, column=0)
        patient_id = tk.Entry(form)
        patient_id.grid(row=0, column=1)

        tk.Label(form, text="Date (YYYY-MM-DD):").grid(row=1, column=0)
        date = tk.Entry(form)
        date.grid(row=1, column=1)

        tk.Label(form, text="Time (HH:MM):").grid(row=2, column=0)
        time = tk.Entry(form)
        time.grid(row=2, column=1)

        tk.Label(form, text="Doctor:").grid(row=3, column=0)
        doctor = tk.Entry(form)
        doctor.grid(row=3, column=1)

        def add_appointment():
            self.db.execute("INSERT INTO appointments (patient_id, date, time, doctor) VALUES (?,?,?,?)",
                            (patient_id.get(), date.get(), time.get(), doctor.get()))
            messagebox.showinfo("Success", "Appointment added successfully!")
            self.manage_appointments()

        tk.Button(form, text="Add Appointment", command=add_appointment).grid(row=4, columnspan=2, pady=10)

        table = ttk.Treeview(self.root, columns=("ID", "Patient ID", "Date", "Time", "Doctor"), show="headings")
        for col in table["columns"]:
            table.heading(col, text=col)
            table.column(col, width=120)
        table.pack(fill="both", expand=True, pady=10)

        for row in self.db.execute("SELECT * FROM appointments").fetchall():
            table.insert("", "end", values=row)

        tk.Button(self.root, text="Back", command=self.show_dashboard).pack(pady=10)

    # ------------------- BILLING -------------------
    def manage_billing(self):
        self.clear_screen()
        tk.Label(self.root, text="💳 Billing Management", font=("Arial", 20, "bold")).pack(pady=10)

        form = tk.Frame(self.root)
        form.pack(pady=10)

        tk.Label(form, text="Patient ID:").grid(row=0, column=0)
        patient_id = tk.Entry(form)
        patient_id.grid(row=0, column=1)

        tk.Label(form, text="Amount:").grid(row=1, column=0)
        amount = tk.Entry(form)
        amount.grid(row=1, column=1)

        tk.Label(form, text="Status:").grid(row=2, column=0)
        status = ttk.Combobox(form, values=["Pending", "Paid"])
        status.grid(row=2, column=1)

        def add_bill():
            self.db.execute("INSERT INTO billing (patient_id, amount, status) VALUES (?,?,?)",
                            (patient_id.get(), amount.get(), status.get()))
            messagebox.showinfo("Success", "Billing record added!")
            self.manage_billing()

        tk.Button(form, text="Add Bill", command=add_bill).grid(row=3, columnspan=2, pady=10)

        table = ttk.Treeview(self.root, columns=("ID", "Patient ID", "Amount", "Status"), show="headings")
        for col in table["columns"]:
            table.heading(col, text=col)
            table.column(col, width=150)
        table.pack(fill="both", expand=True, pady=10)

        for row in self.db.execute("SELECT * FROM billing").fetchall():
            table.insert("", "end", values=row)

        tk.Button(self.root, text="Back", command=self.show_dashboard).pack(pady=10)

    # ------------------- EXPORT DATA -------------------
    def export_data(self):
        try:
            file = filedialog.asksaveasfilename(defaultextension=".csv", filetypes=[("CSV Files", "*.csv")])
            if not file:
                return

            cursor = self.db.execute("SELECT * FROM patients")
            rows = cursor.fetchall()

            with open(file, mode="w", newline="") as f:
                writer = csv.writer(f)
                writer.writerow([desc[0] for desc in cursor.description])
                writer.writerows(rows)

            messagebox.showinfo("Success", f"Data exported successfully to {os.path.basename(file)}")
        except Exception as e:
            messagebox.showerror("Error", str(e))

    # ------------------- Utility -------------------
    def clear_screen(self):
        for widget in self.root.winfo_children():
            widget.destroy()


# --------------------------- Run App ---------------------------
if __name__ == "__main__":
    root = tk.Tk()
    app = MediTrackApp(root)
    root.mainloop()
