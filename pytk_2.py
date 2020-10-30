from tkinter import *
from tkinter import messagebox
import sqlite3


def selection():
    gender = ""
    selected = int(radio.get())
    if selected == 1:
        gender = "male"
    elif selected == 2:
        gender = "female"
    else:
        gender = "others"
    return gender


def check_fields():
    if nameField.get() == "":
        messagebox.showerror("Failed", "All Fields are Mandatory")
    else:
        return


def details_page():
    top = Toplevel()
    top.title('Details')
    top.geometry("600x300")

    try:
        conn = sqlite3.connect('db.sql')
        c = conn.cursor()
        c.execute("select * from registration where name = (?)",
                  (login_name.get(),))
        val = c.fetchone()
        conn.commit()
    except Exception as e:
        print(e)
    finally:
        conn.close()

    label_name = Label(top, text="Name", font=('bold', 13))
    label_name.place(relx=0.2, rely=0.2)

    fetch_name = Label(top, text=f"{val[1]}", font=('bolf', 13))
    fetch_name.place(relx=0.2, rely=0.3)

    label_age = Label(top, text="Age", font=('bold', 13))
    label_age.place(relx=0.5, rely=0.2)

    fetch_age = Label(top, text=f"{val[2]}", font=('bolf', 13))
    fetch_age.place(relx=0.5, rely=0.3)


def add_to_db():
    try:
        conn = sqlite3.connect('db.sql')
        c = conn.cursor()
        c.execute(
            "insert into registration (name, age, dob, pob, gender, fathername, mothername, address) values (?,?,?,?,?,?,?,?)", (
                nameField.get(),
                int(ageField.get()),
                dobField.get(),
                pobField.get(),
                selection(),
                fatherField.get(),
                motherField.get(),
                addrField.get(),
            ))
        c.execute("select * from registration")
        conn.commit()
        messagebox.showinfo(
            "Success", "Registration Complete"
        )
    except Exception as e:
        print(f"Error Has Occured Not able to connect to the Database :(\n{e}")
    finally:
        conn.close()


def login_db():
    try:
        conn = sqlite3.connect('db.sql')
        c = conn.cursor()
        c.execute("select * from registration where name = (?)",
                  (login_name.get(),))
        val = c.fetchone()
        if login_name.get() == val[1]:
            messagebox.showinfo("Success", "User Logged Successfully")
        conn.commit()
        details_page()
    except Exception as e:
        print(e)
    finally:
        conn.close()


def login():
    login_db()


def register():
    print(selection())  # get the radio button value
    check_fields()
    add_to_db()


def existing_user():
    top = Toplevel()
    top.title('Login')
    top.geometry("600x300")
    head = Label(top, text='LOGIN', font=('bold', 15))
    head.place(relx=0.5, rely=0.2, anchor=CENTER)

    b_name = Label(top, text='NAME', font=('bold', 15))
    b_name.place(relx=0.1, rely=0.4, anchor=W)
    global login_name
    login_name = Entry(top)
    login_name.place(relx=0.9, rely=0.4, anchor=E)
    login_name.config(width=30)

    b_auth = Label(top, text='PASSWORD', font=('bold', 15))
    b_auth.place(relx=0.1, rely=0.6, anchor=W)
    global login_password
    login_password = Entry(top)
    login_password.place(relx=0.9, rely=0.6, anchor=E)
    login_password.config(width=30)

    bname = Button(top, text="SUBMIT", font=(
        "bold", 10), bg="white", command=login)
    bname.place(relx=0.2, rely=0.8, anchor=W)
    bname.config(height=1, width=10)

    bauth = Button(top, text="CANCEL", font=("bold", 10),
                   bg="white", command=top.destroy)
    bauth.place(relx=0.8, rely=0.8, anchor=E)
    bauth.config(height=1, width=10)


def new_user():
    top = Toplevel()
    top.title('Registration')
    top.geometry("500x500")
    global radio
    radio = IntVar()

    frame1 = Frame(top, bg='white')
    frame1.place(relx=0, rely=0, width=500, height=500)

    registerTitle = Label(frame1, text="REGISTRATION",
                          font=("bold", 15), bg="white", fg="black")
    registerTitle.place(relx=0.5, rely=0.03, anchor=CENTER)

    # Name Label and Field
    global nameField
    nameLabel = Label(frame1, text="Name:", font=(
        "Helvetica", 13), bg="white", fg="gray")
    nameLabel.place(x=20, y=70)
    nameField = Entry(frame1, font=("Helvetica", 13), bg="white")
    nameField.place(x=150, y=70, width=250)

    # Age Label and Age Field
    global ageField
    ageLabel = Label(frame1, text="Age:", font=(
        "Helvetica", 13), bg="white", fg="gray")
    ageLabel.place(x=20, y=110)
    ageField = Entry(frame1, font=("Helvetica", 13),
                     bg='white')
    ageField.place(x=150, y=110, width=250)     # y + 40

    # DoB Label and Field
    global dobField
    dobLabel = Label(frame1, text="Date of Birth:", font=(
        "Helvetica", 13), bg="white", fg="gray")
    dobLabel.place(x=20, y=150)
    dobField = Entry(frame1, font=("Helvetica", 13),
                     bg='white')
    dobField.place(x=150, y=150, width=250)

    # PoB Label and Field
    global pobField
    pobLabel = Label(frame1, text="Place of Birth:", font=(
        "Helvetica", 13), bg="white", fg="gray")
    pobLabel.place(x=20, y=190)
    pobField = Entry(frame1, font=("Helvetica", 13),
                     bg='white')
    pobField.place(x=150, y=190, width=250)

    # gender Label and Field
    genderLabel = Label(frame1, text="Gender:", font=(
        "Helvetica", 13), bg="white", fg="gray").place(x=20, y=230)
    maleField = Radiobutton(
        frame1, text="Male", variable=radio, value=1, command=selection, bg='white').place(x=150, y=230)
    femaleField = Radiobutton(
        frame1, text="Female", variable=radio, value=2, command=selection, bg='white').place(x=220, y=230)
    otherField = Radiobutton(
        frame1, text="Others", variable=radio, value=3, command=selection, bg='white').place(x=290, y=230)

    # Fathername Label and Field
    global fatherField
    fatherLabel = Label(frame1, text="Father's Name:", font=(
        "Helvetica", 13), bg="white", fg="gray").place(x=20, y=270)
    fatherField = Entry(frame1, font=("Helvetica", 13),
                        bg='white')
    fatherField.place(x=150, y=270, width=250)

    # mothername Label and Field
    global motherField
    motherLabel = Label(frame1, text="Mother's Name:", font=(
        "Helvetica", 13), bg="white", fg="gray").place(x=20, y=310)
    motherField = Entry(frame1, font=("Helvetica", 13),
                        bg='white')
    motherField.place(x=150, y=310, width=250)

    # address Label and Age Field
    global addrField
    addrLabel = Label(frame1, text="Address:", font=(
        "Helvetica", 13), bg="white", fg="gray").place(x=20, y=350)
    addrField = Entry(frame1, font=("Helvetica", 13),
                      bg='white')
    addrField.place(x=150, y=350, width=250)

    # T&C
    tandc = Checkbutton(
        frame1, text="I Agree to the Terms & Conditions", bg='white', font=("Times", 12), onvalue=1, offvalue=0).place(x=20, y=390)

    # Register
    registerBtn = Button(frame1, text='Register', font=('Helvetica', 13), padx=15, pady=5, cursor="hand2",
                         command=register).place(x=20, y=430)

    cancelBtn = Button(frame1, text='Cancel', font=('Helvetica', 13), padx=15, pady=5, cursor="hand2",
                       command=top.destroy).place(x=200, y=430)


def admin():
    messagebox.showinfo("ADMIN", "ADD ADMIN PAGE")


def continue_window():
    top = Toplevel()
    top.title('Passport Automation')
    top.geometry("600x300")
    head = Label(top, text='USER AUTH', font=('bold', 15))
    head.place(relx=0.5, rely=0.2, anchor=CENTER)

    bname = Button(top, text="NEW USER", font=(
        "bold", 10), bg="white", command=new_user, padx=15, pady=10)
    bname.place(relx=0.1, rely=0.4,)
    bname.config(height=1, width=10)

    bauth = Button(top, text="EXISTING USER", font=(
        "bold", 10), bg="white", command=existing_user, padx=15, pady=10)
    bauth.place(relx=0.4, rely=0.4)
    bauth.config(height=1, width=10)

    adminBtn = Button(top, text="ADMIN", font=(
        "bold", 10), bg="white", command=admin, padx=15, pady=10)
    adminBtn.place(relx=0.7, rely=0.4)


# ================ Main ===================
root = Tk()
root.geometry("600x300")
root.title("PASSPORT AUTOMATION")

id = Label(root, text='WELCOME TO THE PASSPORT AUTOMATION SYSTEM',
           font=('bold', 15))
id.place(relx=0.5, rely=0.2, anchor=CENTER)

a = Button(root, text="DO YOU WANT TO CONTINUE", font=(
    "bold", 10), bg="white", command=continue_window)
a.place(relx=0.5, rely=0.4, anchor=CENTER)
a.config(height=1, width=30)


b = Button(root, text="CANCEL", font=("bold", 10),
           bg="white", command=root.destroy)
b.place(relx=0.5, rely=0.6, anchor=CENTER)
b.config(height=1, width=10)


mainloop()
