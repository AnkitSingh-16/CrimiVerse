import tkinter as tk
from tkinter import ttk
import mysql.connector
from subprocess import call
from tkinter import messagebox

class Login_Window:
    def __init__(self, root):
        self.root = root
        self.root.title("Login")
        self.root.geometry("1550x800+0+0")

        # Variables
        self.var_userid = tk.StringVar()
        self.var_password = tk.StringVar()

        frame = tk.Frame(self.root, bg="black")
        frame.place(x=610, y=170, width=340, height=450)

        get_str = tk.Label(frame, text="ADMIN LOGIN", font=("times new roman", 20, "bold"), fg="white", bg="black")
        get_str.place(x=80, y=100)

        # Labels
        username = tk.Label(frame, text="Username", font=("times new roman", 15, "bold"), fg="white", bg="black")
        username.place(x=50, y=155)

        self.txtuser = ttk.Entry(frame, textvariable=self.var_userid, font=("times new roman", 15, "bold"))
        self.txtuser.place(x=40, y=180, width=270)

        password = tk.Label(frame, text="Password", font=("times new roman", 15, "bold"), fg="white", bg="black")
        password.place(x=50, y=220)

        self.txtpass = ttk.Entry(frame, textvariable=self.var_password, font=("times new roman", 15, "bold"), show="*")
        self.txtpass.place(x=40, y=250, width=270)

        loginbtn = tk.Button(frame, text="Login", command=self.login, font=("times new roman", 15, "bold"),
                             bd=3, relief=tk.RIDGE, fg="white", bg="red", activeforeground="white",
                             activebackground="red")
        loginbtn.place(x=110, y=300, width=120)

    def login(self):
        userid = self.var_userid.get()
        password = self.var_password.get()

        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="Kumar@123",
            database="criminal_database"
        )

        cursor = connection.cursor()
        query = "SELECT * FROM login WHERE userid = %s AND password = %s"
        cursor.execute(query, (userid, password))

        result = cursor.fetchone()

        if result is not None:
            self.root.destroy()
            call(['python', 'crime management system.py'])
        else:
            messagebox.showerror("Login Failed", "Invalid username or password")

        cursor.close()
        connection.close()


if __name__ == "__main__":
    root = tk.Tk()
    app = Login_Window(root)
    root.mainloop()
