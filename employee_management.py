import tkinter as tk
from tkinter import ttk, filedialog, messagebox
import pandas as pd
import os
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt


# CREATE SAMPLE CSV AUTOMATICALLY
if not os.path.exists("employees.csv"):

    sample_data = {
        "id": [101,102,103,104,105,106,107,108,109,110],
        "name": [
            "John Smith",
            "Sarah Johnson",
            "Michael Brown",
            "Emma Davis",
            "David Wilson",
            "Olivia Miller",
            "James Taylor",
            "Sophia Anderson",
            "Daniel Thomas",
            "Isabella Jackson"
        ],
        "department": [
            "IT",
            "HR",
            "Finance",
            "IT",
            "Sales",
            "Marketing",
            "IT",
            "Finance",
            "Sales",
            "HR"
        ],
        "salary": [
            50000,
            45000,
            60000,
            70000,
            40000,
            52000,
            75000,
            68000,
            42000,
            48000
        ],
        "age": [25,30,35,28,32,27,40,33,29,31],
        "city": [
            "New York",
            "Chicago",
            "Texas",
            "California",
            "Florida",
            "Seattle",
            "Boston",
            "Chicago",
            "Texas",
            "California"
        ],
        "experience": [2,5,8,4,6,3,12,7,4,5],
        "gender": [
            "Male",
            "Female",
            "Male",
            "Female",
            "Male",
            "Female",
            "Male",
            "Female",
            "Male",
            "Female"
        ],
        "status": [
            "Active",
            "Active",
            "Active",
            "Active",
            "Inactive",
            "Active",
            "Active",
            "Active",
            "Inactive",
            "Active"
        ]
    }

    df = pd.DataFrame(sample_data)

    df.to_csv("employees.csv", index=False)


class EmployeeManagementSystem:

    def __init__(self, root):

        self.root = root
        self.root.title("Employee Management System")
        self.root.geometry("1400x750")
        self.root.configure(bg="#f0f2f5")

        self.df = pd.read_csv("employees.csv")

        self.create_header()
        self.create_sidebar()
        self.create_dashboard()
        self.create_table()

        self.display_table(self.df)

        self.update_dashboard()

    # HEADER
    def create_header(self):

        header = tk.Frame(
            self.root,
            bg="#0d1b2a",
            height=80
        )

        header.pack(fill="x")

        title = tk.Label(
            header,
            text="EMPLOYEE MANAGEMENT SYSTEM",
            bg="#0d1b2a",
            fg="white",
            font=("Arial", 24, "bold")
        )

        title.pack(pady=20)

    # SIDEBAR
    def create_sidebar(self):

        sidebar = tk.Frame(
            self.root,
            bg="white",
            width=250
        )

        sidebar.pack(side="left", fill="y")

        # LOAD CSV
        load_btn = tk.Button(
            sidebar,
            text="Load CSV File",
            bg="#0077b6",
            fg="white",
            font=("Arial", 11, "bold"),
            command=self.load_csv
        )

        load_btn.pack(
            pady=20,
            padx=20,
            fill="x"
        )

        # SEARCH LABEL
        tk.Label(
            sidebar,
            text="Search Employee",
            bg="white",
            font=("Arial", 12, "bold")
        ).pack(anchor="w", padx=20)

        # SEARCH ENTRY
        self.search_entry = tk.Entry(
            sidebar,
            font=("Arial", 11)
        )

        self.search_entry.pack(
            padx=20,
            pady=10,
            fill="x"
        )

        # SEARCH BUTTON
        search_btn = tk.Button(
            sidebar,
            text="Search",
            bg="#2a9d8f",
            fg="white",
            font=("Arial", 11, "bold"),
            command=self.search_employee
        )

        search_btn.pack(
            padx=20,
            fill="x"
        )

        # RESET BUTTON
        reset_btn = tk.Button(
            sidebar,
            text="Reset",
            bg="#e63946",
            fg="white",
            font=("Arial", 11, "bold"),
            command=self.reset_table
        )

        reset_btn.pack(
            padx=20,
            pady=10,
            fill="x"
        )

        # CHART BUTTON
        chart_btn = tk.Button(
            sidebar,
            text="Show Analytics",
            bg="#6a4c93",
            fg="white",
            font=("Arial", 11, "bold"),
            command=self.show_chart
        )

        chart_btn.pack(
            padx=20,
            pady=10,
            fill="x"
        )

        # ADD EMPLOYEE
        add_btn = tk.Button(
            sidebar,
            text="Add Employee",
            bg="#264653",
            fg="white",
            font=("Arial", 11, "bold"),
            command=self.add_employee_window
        )

        add_btn.pack(
            padx=20,
            pady=10,
            fill="x"
        )

    # DASHBOARD
    def create_dashboard(self):

        dashboard = tk.Frame(
            self.root,
            bg="#f0f2f5"
        )

        dashboard.pack(
            fill="x",
            padx=10,
            pady=10
        )

        self.total_card = self.create_card(
            dashboard,
            "Total Employees"
        )

        self.salary_card = self.create_card(
            dashboard,
            "Average Salary"
        )

        self.age_card = self.create_card(
            dashboard,
            "Average Age"
        )

        self.active_card = self.create_card(
            dashboard,
            "Active Employees"
        )

    # CARD
    def create_card(self, parent, title):

        card = tk.Frame(
            parent,
            bg="white",
            width=220,
            height=100,
            relief="ridge",
            bd=2
        )

        card.pack(
            side="left",
            padx=10
        )

        tk.Label(
            card,
            text=title,
            bg="white",
            font=("Arial", 12)
        ).pack(pady=10)

        value = tk.Label(
            card,
            text="--",
            bg="white",
            font=("Arial", 20, "bold")
        )

        value.pack()

        return value

    # TABLE
    def create_table(self):

        table_frame = tk.Frame(self.root)

        table_frame.pack(
            fill="both",
            expand=True,
            padx=10,
            pady=10
        )

        self.tree = ttk.Treeview(table_frame)

        self.tree.pack(
            fill="both",
            expand=True
        )

    # DISPLAY TABLE
    def display_table(self, dataframe):

        self.tree.delete(*self.tree.get_children())

        self.tree["columns"] = list(dataframe.columns)

        self.tree["show"] = "headings"

        for column in dataframe.columns:

            self.tree.heading(column, text=column)

            self.tree.column(column, width=120)

        for row in dataframe.to_numpy().tolist():

            self.tree.insert(
                "",
                "end",
                values=row
            )

    # UPDATE DASHBOARD
    def update_dashboard(self):

        total = len(self.df)

        avg_salary = int(self.df["salary"].mean())

        avg_age = int(self.df["age"].mean())

        active = len(
            self.df[self.df["status"] == "Active"]
        )

        self.total_card.config(text=str(total))

        self.salary_card.config(text=f"${avg_salary}")

        self.age_card.config(text=str(avg_age))

        self.active_card.config(text=str(active))

    # SEARCH
    def search_employee(self):

        keyword = self.search_entry.get().lower()

        filtered = self.df[
            self.df["name"].str.lower().str.contains(keyword) |
            self.df["department"].str.lower().str.contains(keyword) |
            self.df["city"].str.lower().str.contains(keyword)
        ]

        self.display_table(filtered)

    # RESET TABLE
    def reset_table(self):

        self.display_table(self.df)

    # LOAD CSV
    def load_csv(self):

        file_path = filedialog.askopenfilename(
            filetypes=[("CSV Files", "*.csv")]
        )

        if file_path:

            self.df = pd.read_csv(file_path)

            self.display_table(self.df)

            self.update_dashboard()

            messagebox.showinfo(
                "Success",
                "CSV Loaded Successfully"
            )

    # SHOW CHART
    def show_chart(self):

        chart_window = tk.Toplevel(self.root)

        chart_window.title("Analytics Dashboard")

        fig, ax = plt.subplots(
            figsize=(6, 5)
        )

        self.df["department"].value_counts().plot(
            kind="pie",
            autopct="%1.1f%%",
            ax=ax
        )

        ax.set_ylabel("")

        ax.set_title(
            "Department Distribution"
        )

        canvas = FigureCanvasTkAgg(
            fig,
            master=chart_window
        )

        canvas.draw()

        canvas.get_tk_widget().pack(
            fill="both",
            expand=True
        )

    # ADD EMPLOYEE WINDOW
    def add_employee_window(self):

        window = tk.Toplevel(self.root)

        window.title("Add Employee")

        window.geometry("400x500")

        labels = [
            "ID",
            "Name",
            "Department",
            "Salary",
            "Age",
            "City",
            "Experience",
            "Gender",
            "Status"
        ]

        entries = {}

        for label in labels:

            tk.Label(
                window,
                text=label,
                font=("Arial", 11)
            ).pack(pady=5)

            entry = tk.Entry(
                window,
                font=("Arial", 11)
            )

            entry.pack(pady=5)

            entries[label] = entry

        def save_employee():

            new_employee = {

                "id": entries["ID"].get(),

                "name": entries["Name"].get(),

                "department": entries["Department"].get(),

                "salary": int(entries["Salary"].get()),

                "age": int(entries["Age"].get()),

                "city": entries["City"].get(),

                "experience": int(entries["Experience"].get()),

                "gender": entries["Gender"].get(),

                "status": entries["Status"].get()
            }

            self.df = pd.concat(
                [
                    self.df,
                    pd.DataFrame([new_employee])
                ],
                ignore_index=True
            )

            self.df.to_csv(
                "employees.csv",
                index=False
            )

            self.display_table(self.df)

            self.update_dashboard()

            messagebox.showinfo(
                "Success",
                "Employee Added Successfully"
            )

            window.destroy()

        save_btn = tk.Button(
            window,
            text="Save Employee",
            bg="#0077b6",
            fg="white",
            font=("Arial", 11, "bold"),
            command=save_employee
        )

        save_btn.pack(
            pady=20
        )


# RUN APPLICATION
root = tk.Tk()

app = EmployeeManagementSystem(root)

root.mainloop()