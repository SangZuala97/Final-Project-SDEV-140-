import tkinter as tk
root = tk.Tk()
root.title("Financial Manager")

def MyClick():
    Name=NameTextbox.get()
    Password=PasswordTextbox.get()

    if Name == "harry" and Password == "harry123" :
        dashboard()  
        root.destroy()
    else:
        error_Login()


def dashboard():
    root =  tk.Tk()
    root.title("Dashboard")
   

    Title_label = tk.Label(root, text="Dashboard")
    Title_label.grid(row=0, column = 3)

    #Income tracking button
    def remaining_balance():
        num1= float(salary_textbox.get())
        num2=float(sidejob_textbox.get())
        num3= float(other_income_textbox.get())

        num4= float(morgage_textbox.get())
        num5= float(schoolfee_textbox.get())
        num6= float(otherbill_label_textbox.get())

        total_income= num1+num2+num3
        total_expense= num4+num5+num6

        remaining_balance = total_income - total_expense

        total_income_label.config (text="Total income:     " + str(total_income))
        total_expense_label.config(text="Total expense:    " + str(total_expense))
        Remaining_balance_label.config(text="Remaining Balance :" + str(remaining_balance))



    

    Title_label1 = tk.Label(root, text="Income Lists")
    Title_label1.grid(row=1, column = 1)

    salary_Label = tk.Label(root, text="Monthly Salary :")
    salary_Label.grid(row=3, column=0)

    salary_textbox =  tk.Entry(root)
    salary_textbox.grid(row=3,column=1)

    sidejob_label = tk.Label(root, text= "Side job income:")
    sidejob_label.grid(row=4, column=0 )

    sidejob_textbox = tk.Entry(root)
    sidejob_textbox.grid(row=4, column =1)

    other_income_label = tk.Label(root, text="Other income: ")
    other_income_label.grid( row=5, column = 0)

    other_income_textbox = tk.Entry(root)
    other_income_textbox.grid(row=5, column=1)
    
    total_income_label = tk.Label(root, text="Total income :")
    total_income_label.grid(row=6, column= 0)

    


    Title_label2 = tk.Label(root, text="Expense Lists")
    Title_label2.grid(row=1, column = 4)

    morgage_Label = tk.Label(root, text="Morgage :")
    morgage_Label.grid(row=3, column=3)

    morgage_textbox =  tk.Entry(root)
    morgage_textbox.grid(row=3,column=4)

    schoolfee_label = tk.Label(root, text= "School Fee :")
    schoolfee_label.grid(row=4, column=3 )

    schoolfee_textbox = tk.Entry(root)
    schoolfee_textbox.grid(row=4, column =4)

    otherbill_label = tk.Label(root, text="Other bills: ")
    otherbill_label.grid( row=5, column = 3)

    otherbill_label_textbox = tk.Entry(root)
    otherbill_label_textbox.grid(row=5, column=4)
    
    total_expense_label = tk.Label(root, text="Total expense:")
    total_expense_label.grid(row=6, column= 3)

    


    Remaining_balance_label=tk.Label(root, text="Remaining Balance :  ")
    Remaining_balance_label.grid(row= 8, column=3)

    calculate_income = tk.Button (root, text="Calculate", command=remaining_balance)
    calculate_income.grid(row=10, column =1)



    Exit_button = tk.Button( root, text= "Exit", command= root.destroy)
    Exit_button.grid(row=10, column=2)   



def error_Login():
    root= tk.Tk()
    root.geometry('600x80')
    root.title("Error Login")

    def exit_btn():
        root.destroy()
        root.update()

    labelerrorlogin = tk.Label (root, text ="Invalid Username/password").pack ()
    ExitButton= tk.Button(root, text="Back to Main Menu", command= exit_btn).pack ()


    # Create a label for the image
photo = tk.PhotoImage(file="financial _manager.gif")

image_label= tk.Label(root, image=photo)
image_label.grid(row=0,column=0)

Logo_label = tk.Label(root, text="My Financial Manager")
Logo_label.grid(row=0,column=1,columnspan=2, padx=50, pady=20)

UserName_Label= tk.Label(root, text="Username")
NameTextbox= tk.Entry(root)
UserName_Label.grid(row=1, column=0)
NameTextbox.grid(row=1, column=1)

PasswordLabel= tk.Label(root, text="Password")
PasswordTextbox= tk.Entry(root)
PasswordLabel.grid(row=2, column=0)
PasswordTextbox.grid(row=2, column=1)


EnterButton= tk.Button(root, text="Enter",command=MyClick)
EnterButton.grid(row=4, column=1)







root.mainloop()
