from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import tkinter as tk
import sqlite3
import time
from tkinter import font
import os.path
import numbers

# -------------------------------------------------------- Main Menu -----


# Test Branch 2
class MainMenu:
    def __init__(self, master):
        self.master = master
        self.master.geometry("500x300")
        self.master.title("Welcome")

        #self.background = tk.PhotoImage(file = "C:/Users/Sharjeel Jan/Desktop/Database System/The System/Background.png")
        #self.background2 = self.background.subsample(2,2)
        #self.Background = tk.Label(self.master, image = self.background2, borderwidth=0, highlightthickness=0)
        #self.Background.place(x=0, y=0, relwidth=1, relheight=1)

        self.AboutButton = tk.Button(
            self.master,
            text="About",
            command=self.gotoAboutPage).place(
            x=250,
            y=50,
            anchor="center")
        self.LoginButton = tk.Button(
            self.master,
            text="Login",
            command=self.gotoLoginPage).place(
            x=250,
            y=100,
            anchor="center")
        self.SignUpButton = tk.Button(
            self.master,
            text="Sign Up",
            command=self.gotoSignUpPage).place(
            x=250,
            y=150,
            anchor="center")
        self.Quit = tk.Button(
            self.master,
            text="Quit",
            command=self.Quit).place(
            x=250,
            y=200,
            anchor="center")

        #self.about_image = tk.PhotoImage(file = "C://Users/Sharjeel Jan//Desktop//Database System//The System//button_about")
        #self.about_image = tk.PhotoImage(file = "C:/Users/Sharjeel Jan/Desktop/Database System/The System/button_about.png")
        #self.AboutButton.config(image = self.about_image)

        self.tick()

    def tick(self):
        self.TickingTime = ''
        self.Clock = tk.Label(self.master)
        self.Clock.grid(row=4, column=5)
        self.Clock.place(x=475, y=290, anchor="center")
        self.Time = time.strftime('%H:%M:%S')

        if self.Time != self.TickingTime:
            self.TickingTime = self.Time
            self.Clock.config(text=self.Time)

        self.Clock.after(200, self.tick)

    def gotoAboutPage(self):
        self.master.withdraw()
        GoAboutPage = tk.Toplevel()
        Going = AboutPage(GoAboutPage)

    def gotoLoginPage(self):
        self.master.withdraw()
        GoLoginPage = tk.Toplevel()
        Going = LoginPage(GoLoginPage)

    def gotoSignUpPage(self):
        self.master.withdraw()
        GoSignUpPage = tk.Toplevel()
        Going = SignUpPage(GoSignUpPage)

    def BacktoMenu(self):
        self.master.withdraw()
        Go_to_Menu_Page = tk.Toplevel()
        Going = MainMenu(Go_to_Menu_Page)

    def Quit(self):
        # for i in range(15):
        #    self.QuttingQuestion = tk.messagebox.showinfo("HAHAHAHAHAHAHAHAAHAHHAHA", "Cant close? Hmmm, i wonder why")

        #self.QuttingQuestion = tk.messagebox.showinfo("Just Joking", "You may leave")
        # self.master.destroy()
        self.QuttingQuestion = tk.messagebox.askquestion(
            "Application Closing", "Are you sure you wish to leave?")
        if self.QuttingQuestion == "yes":
            self.master.destroy()


# -------------------------------------------------------- About ---------

class AboutPage:
    def __init__(self, master):
        self.master = master
        self.master.geometry("600x400")
        self.master.title("About Page")

        self.BackButton = tk.Button(
            self.master,
            text="Back",
            command=self.BacktoMenu).grid(
            row=1,
            column=1)

    def BacktoMenu(self):
        self.master.withdraw()
        Go_to_Menu_Page = tk.Toplevel()
        Going = MainMenu(Go_to_Menu_Page)

# -------------------------------------------------------- Login ---------


class LoginPage:
    def __init__(self, master):
        self.master = master
        self.master.geometry("300x200")
        self.master.title("Login")

        self.First_Name = tk.Entry(self.master)
        self.Password = tk.Entry(self.master, show="*")

        self.First_Name.place(x=170, y=50, anchor="center")
        self.Password.place(x=170, y=70, anchor="center")

        self.First_Name_Label = tk.Label(
            self.master, text="Firstname").place(
            x=70, y=50, anchor="center")
        self._Surname_Label = tk.Label(
            self.master, text="Password").place(
            x=65, y=70, anchor="center")

        self.Login_Button = tk.Button(
            self.master,
            text="Login",
            command=self.CheckBoxesInfo_And_LoginStatus).place(
            x=150,
            y=120,
            anchor="center")
        self.BackButton = tk.Button(
            self.master,
            text="Back",
            command=self.goto_MainMenu_Page).place(
            x=200,
            y=120,
            anchor="center")
        self.Admin_Database = Admin_Database()

        for data in enumerate(self.Admin_Database.Get_Admin_Users()):
            self.data = data

    def CheckBoxesInfo_And_LoginStatus(self):
        with open("Database-System-User_Info.txt", "r") as CheckingUserInfo:
            Login_Info = CheckingUserInfo.readlines()
            print(Login_Info[0].rstrip())
            print(Login_Info[3].rstrip())

            if self.First_Name.get() == Login_Info[0].rstrip(
            ) and self.Password.get() == Login_Info[3].rstrip():
                print("works")
                print(self.data[1][1])
                self.gotoAll_Contents_Page()

                # elif self.First_Name.get() == self.data[1][1] and self.Password.get() == self.data[1][2]:
                #    self.gotoAdminPage()
                # else:
                #    self.TryAgain1 = tk.messagebox.showinfo("Try Again", "Wrong Info, Try Again!")
                #    self.First_Name.delete(0, END)
                #    self.Password.delete(0, END)
            else:
                        #self.TryAgain2 = tk.messagebox.showinfo("Try Again", "Wrong Info, Try Again!")
                self.TryAgain2 = tk.messagebox.askyesno(
                    "Try Again", "Wrong Info, Try Again!")
                self.First_Name.delete(0, END)
                self.Password.delete(0, END)

    def gotoAdminPage(self):
        self.master.withdraw()
        GoToAdminPage = tk.Toplevel()
        Going = AdminPage(GoToAdminPage)

    def gotoAll_Contents_Page(self):
        self.master.withdraw()
        GoAll_Contents_Page = tk.Toplevel()
        Going = All_Contents_Page(GoAll_Contents_Page)

    def goto_MainMenu_Page(self):
        self.master.withdraw()
        GoToMainMenu = tk.Toplevel()
        Going = MainMenu(GoToMainMenu)

# -------------------------------------------------------- Admin ---------


class AdminPage:
    def __init__(self, master):
        self.master = master
        self.master.geometry("1000x600")
        self.master.title("Admin")

        self.ListBox = tk.Listbox(self.master, width=100, height=20)
        self.ListBox.grid(row=1, column=2, padx=10, pady=10)

        self.Admin_Functions = Admin_Database()

        with open("Database-System-User_Info.txt", "r") as CheckingUserInfo:
            Login_Info = CheckingUserInfo.readlines()
            self.ListBox.insert(1, Login_Info)

        self.Delete_Program_User = tk.Button(
            self.master,
            text="Delete User",
            command=self.Delete_User).grid(
            row=1,
            column=1)

    def Delete_User(self):
        open('Database-System-User_Info.txt', 'w').close()
        print("Users Deleted, Check text file. To reuse application, signup again!")


# -------------------------------------------------------- SignUp --------

class SignUpPage:
    def __init__(self, master):
        self.master = master
        self.master.geometry("400x200")
        self.master.title("Sign Up")

        self.First_Name = tk.Entry(self.master)
        self.Surname = tk.Entry(self.master)
        self.Password = tk.Entry(self.master, show="*")
        self.Re_Password = tk.Entry(self.master, show="*")

        self.First_Name.grid(row=1, column=2)
        self.Surname.grid(row=2, column=2)
        self.Password.grid(row=3, column=2)
        self.Re_Password.grid(row=4, column=2)

        self.First_Name_Label = tk.Label(
            self.master, text="First Name").grid(
            row=1, column=1)
        self.Surname_Label = tk.Label(
            self.master, text="Surname").grid(
            row=2, column=1)
        self.Password_Label = tk.Label(
            self.master, text="Password").grid(
            row=3, column=1)
        self.Re_Password_Label = tk.Label(
            self.master, text="Re-Password").grid(row=4, column=1)

        self.SignUpButton = tk.Button(
            self.master,
            text="Sign Up",
            command=self.CheckInfo).grid(
            row=5,
            column=1)
        self.BackButton = tk.Button(
            self.master,
            text="Back",
            command=self.gotoMainPage).grid(
            row=5,
            column=2)

    def CheckInfo(self):
        if self.First_Name.get() and self.Surname.get(
        ) and self.Password.get() and self.Re_Password.get() != "":
            if self.Re_Password.get() == self.Password.get():
                self.PassedSignUp = tk.messagebox.showinfo(
                    "User Created!", "Congrats, User Signed Up. Now go Login!")
                print("Congrats, User Signed Up. Now go Login!")
                with open("Database-System-User_Info.txt", "a") as myfile:
                    myfile.write(self.First_Name.get())
                    myfile.write("\n")
                    myfile.write(self.Surname.get())
                    myfile.write("\n")
                    myfile.write(self.Password.get())
                    myfile.write("\n")
                    myfile.write(self.Re_Password.get())
                    myfile.write("\n")
                self.gotoMainPage()
            else:
                self.FailedSignUp = tk.messagebox.showinfo(
                    "Bruv", "You had one job, cant even do that correctly huh? Try again")
                self.Password.delete(0, END)
                self.Re_Password.delete(0, END)
                print("You had one job, cant even do that correctly huh?")
        else:
            print("Man fill the damn boxes")

    def gotoMainPage(self):
        self.master.withdraw()
        GoMainMenu = tk.Toplevel()
        Going = MainMenu(GoMainMenu)

# -------------------------------------------------------- Main Page -----


class All_Contents_Page:
    def __init__(self, master):
        self.master = master
        self.master.geometry("1500x800")
        self.master.title("Company Database")

        self.ShowInfo = ttk.Treeview(
            self.master,
            columns=(
                'ID',
                'First name',
                'Surname',
                'Date of birth',
                'Age'))  # Had to delete gender to get rid of extra column
        self.ShowInfo.place(x=500, y=350, anchor="center")
        self.ShowInfo.heading('#0', text="ID")
        self.ShowInfo.heading('#1', text="First name")
        self.ShowInfo.heading('#2', text="Surname")
        self.ShowInfo.heading('#3', text="Date of Birth")
        self.ShowInfo.heading('#4', text="Age")
        self.ShowInfo.heading('#5', text="Gender")

        self.ShowInfo.column(
            "#0",
            minwidth=0,
            width=100,
            stretch=NO,
            anchor="center")
        self.ShowInfo.column(
            "#1",
            minwidth=0,
            width=200,
            stretch=NO,
            anchor="center")
        self.ShowInfo.column(
            "#2",
            minwidth=0,
            width=200,
            stretch=NO,
            anchor="center")
        self.ShowInfo.column(
            "#3",
            minwidth=0,
            width=150,
            stretch=NO,
            anchor="center")
        self.ShowInfo.column(
            "#4",
            minwidth=0,
            width=100,
            stretch=NO,
            anchor="center")
        self.ShowInfo.column(
            "#5",
            minwidth=0,
            width=150,
            stretch=NO,
            anchor="center")

        # .grid(row = 1, column = 2)
        # self.Options = [("Age",1),("Gender",2),("DOB",3)]
        # for option,variable in self.Options:
        #     self.ViewStats = tk.Radiobutton(self.master, text = option, variable = variable)

        self.AddEmployee_Button = tk.Button(
            self.master,
            text="Add Employee",
            command=self.gotoAddEmployee).grid(
            row=2,
            column=1)
        #self.Delete_All = tk.Button(self.master, text = "Delete All", command = self.Show_ConfrimationBox).grid(row = 3, column = 1 )
        self.Database_Info = Employee_Database(self)
        # running the function from addEmplyoee function
        self.method = getattr(AddEmployee, 'CheckInfo_Confirm')
        self.Add_info()

    def Add_info(self):
        Info = self.ShowInfo.get_children()
        for i in Info:
            self.ShowInfo.delete(i)
        for j in self.Database_Info.Return_All_Data():
            self.ShowInfo.insert(
                '', 0, text=j[0], values=(
                    j[1], j[2], j[3], j[4], j[5]))

    # def Show_ConfrimationBox(self):
    #     self.You_Sure = tk.messagebox.askquestion("Delete All Employees", "Are you wish to delete every Employee?")
    #     if self.You_Sure == "yes":
    #         self.Database_Info.Delete_All_Employees()
    #         self.ListBox.delete(0,END)
    #         self.All_Deleted = tk.messagebox.showinfo("Empyty", "All Employees deleted.")

    def gotoAddEmployee(self):
        GoAddEmployee = tk.Toplevel()
        Going = AddEmployee(GoAddEmployee)

# -------------------------------------------------------- Add Employee --


class AddEmployee:
    def __init__(self, master):
        self.master = master
        self.master.geometry("400x500")
        self.master.title("Add Employee")

        self.First = tk.Entry(self.master)
        self.Last = tk.Entry(self.master)
        self.PostCode = tk.Entry(self.master)
        self.Race = tk.Entry(self.master)
        self.Gender = tk.Entry(self.master)
        self.SSN = tk.Entry(self.master)
        self.SpouseNumber = tk.Entry(self.master)
        self.Position = tk.Entry(self.master)
        self.Department = tk.Entry(self.master)
        self.HoursWorking = tk.Entry(self.master)
        self.Salary = tk.Entry(self.master)

        self.First.grid(row=1, column=2)
        self.Last.grid(row=2, column=2)
        self.Race.grid(row=3, column=2)
        self.Salary.grid(row=4, column=2)
        self.Gender.grid(row=5, column=2)
        self.SSN.grid(row=6, column=2)
        self.PostCode.grid(row=7, column=2)
        self.SpouseNumber.grid(row=8, column=2)
        self.Position.grid(row=9, column=2)
        self.Department.grid(row=10, column=2)
        self.HoursWorking.grid(row=11, column=2)

        self.First_Label = tk.Label(
            self.master, text="First name").grid(
            row=1, column=1)
        self.Last_Label = tk.Label(
            self.master, text="Last name").grid(
            row=2, column=1)
        self.Race_Label = tk.Label(
            self.master,
            text="Race").grid(
            row=3,
            column=1)
        self.Salary_Label = tk.Label(
            self.master, text="Salary").grid(
            row=4, column=1)
        self.Gender_Label = tk.Label(
            self.master, text="Gender").grid(
            row=5, column=1)
        self.SSN_Label = tk.Label(
            self.master,
            text="SSN").grid(
            row=6,
            column=1)
        self.Postcode_Label = tk.Label(
            self.master, text="PostCode").grid(
            row=7, column=1)
        self.SpouseNumber_Label = tk.Label(
            self.master, text="Spouse Number").grid(
            row=8, column=1)
        self.Position_Label = tk.Label(
            self.master, text="Position").grid(
            row=9, column=1)
        self.Department_Label = tk.Label(
            self.master, text="Department").grid(
            row=10, column=1)
        self.HoursWorking_Label = tk.Label(
            self.master, text="Hours Working").grid(
            row=11, column=1)

        self.Add_Button = tk.Button(
            self.master,
            text="Add",
            command=self.CheckInfo_Confirm).grid(
            row=7,
            column=2)
        # instantiation of database to run functions upon correct info
        self.Database_Functions = Employee_Database(self)

    def CheckInfo_Confirm(self):
        if self.FirstName.get() and self.EmpID.get() and self.Age.get(
        ) and self.DOB.get() and self.Gender.get() and self.Surname != "":
            if self.EmpID.get().isdigit() and self.Age.get().isdigit():
                print("ayyyy lmao")
                self.Database_Functions.Add_User_Data()
                self.Database_Functions.Return_All_Data()
            else:
                print("didnt work")
        else:
            print("Didnt work")

# -------------------------------------------------------- Employee Databa


class Employee_Database:
    def __init__(self, AddEmployee):

        self.AddEmployee = AddEmployee

        self.BASE_DIR = os.path.dirname(os.path.abspath(__file__))
        self.db_path = os.path.join(self.BASE_DIR, "Employees.db")
        self.conn = sqlite3.connect(self.db_path)
        self.c = self.conn.cursor()

    def Database_Run(self):
        self.c.execute("""CREATE TABLE Employees (
                        IDNumber Integer,
                        FirstName text,
                        Address text,
                        SSN integer,
                        Surname text,
                        DOB integer,
                        Age integer,
                        Gender text
                        )""")

        self.conn.commit()

    def Return_All_Data(self):
        self.c.execute("SELECT * FROM Employees")
        return self.c.fetchall()

        self.conn.commit()

    def Add_User_Data(self):

        print("\n")
        print(self.AddEmployee.EmpID.get())
        print(self.AddEmployee.FirstName.get())
        print(self.AddEmployee.Surname.get())
        print(self.AddEmployee.DOB.get())
        print(self.AddEmployee.Age.get())
        print(self.AddEmployee.Gender.get())
        print("\n")

        self.params = (
            self.AddEmployee.EmpID.get(),
            self.AddEmployee.FirstName.get(),
            self.AddEmployee.Surname.get(),
            self.AddEmployee.DOB.get(),
            self.AddEmployee.Age.get(),
            self.AddEmployee.Gender.get())

        self.c.execute(
            "INSERT INTO Employees VALUES (?, ?, ?, ?, ?, ? )",
            self.params)

        self.conn.commit()

    def Delete_All_Employees(self):
        self.c.execute("DELETE FROM Employees")
        self.conn.commit()

# -------------------------------------------------------- Admin Database


class Admin_Database:
    def __init__(self):

        self.BASE_DIR = os.path.dirname(os.path.abspath(__file__))
        self.db_path = os.path.join(self.BASE_DIR, "Admin.db")
        self.conn = sqlite3.connect(self.db_path)
        self.c = self.conn.cursor()

    def Admin_Database_Run(self):
        self.c.execute("""CREATE TABLE Admin (
                        IDNumber int,
                        Username text,
                        Password text
                        )""")

        self.conn.commit()

    def Get_Admin_Users(self):
        self.c.execute("SELECT * FROM Admin")
        return self.c.fetchall()

    def Delete_All_Users(self):
        self.c.execute("DELETE FROM Admin")
        self.conn.commit()

    def Add_Admin_User(self):
        pass
        # self.params = (self.AddEmployee.ID.get(), self.AddEmployee.FirstName.get(), self.AddEmployee.Surname.get(),
        # self.AddEmployee.DOB.get(), self.AddEmployee.Age.get(),
        # self.AddEmployee.Gender.get())

        #self.c.execute("INSERT INTO Employees VALUES (?, ?, ?, ?, ?, ? )", self.params)

    def Default_Admin_User(self):

        self.Default_params = ["12345", "Admin", "Password"]
        self.c.execute(
            "INSERT INTO Admin VALUES (?, ?, ?)",
            self.Default_params)

        self.conn.commit()


def main():
    root = tk.Tk()
    a = MainMenu(root)
    root.mainloop()


if __name__ == '__main__':
    main()
