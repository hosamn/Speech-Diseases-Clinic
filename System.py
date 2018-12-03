from tkinter import *
import sqlite3

# DB connection
conn = sqlite3.connect("database.db")

# cursor to talk to DB
cur  = conn.cursor()


sql  = """SELECT *
          FROM patient"""

result = cur.execute(sql)

for r in result :
    print(r)



##############################################
# Tkinter Window #############################

class Application:
    def __init__(self, master):
        self.master = master

        # creating frames in the master
        self.left  = Frame(master, width = 800, height = 720, bg = 'lightgrey')
        self.left.pack(side = LEFT)

        self.right = Frame(master, width = 400, height = 720, bg = 'steelblue')
        self.right.pack(side = RIGHT)


        # ENTRY TEXTS ##################################################################################################
        # window label
        self.heading = Label(self.left, text="Speech Disorders Clinic", font = ('cambria 40 bold'), fg = 'darkblue', bg = 'lightgrey')
        self.heading.place(x=20, y=20)

        # patient name
        self.name = Label(self.left, text="Patient Name", font = ('arial 18 bold'), fg = 'blue', bg = 'lightgrey')
        self.name.place(x=30, y=140)

        # patient dob
        self.dob = Label(self.left, text="Date of Birth", font = ('arial 18 bold'), fg = 'blue', bg = 'lightgrey')
        self.dob.place(x=30, y=180)

        # patient sex
        self.sex = Label(self.left, text="Gender", font = ('arial 18 bold'), fg = 'blue', bg = 'lightgrey')
        self.sex.place(x=30, y=220)


        # patient nationality
        self.sex = Label(self.left, text="Nationality", font = ('arial 18 bold'), fg = 'blue', bg = 'lightgrey')
        self.sex.place(x=30, y=260)


        # patient marital
        self.sex = Label(self.left, text="Marital Status", font = ('arial 18 bold'), fg = 'blue', bg = 'lightgrey')
        self.sex.place(x=30, y=300)


        # patient job
        self.sex = Label(self.left, text="Occupation", font = ('arial 18 bold'), fg = 'blue', bg = 'lightgrey')
        self.sex.place(x=30, y=340)


        # patient address
        self.sex = Label(self.left, text="Address", font = ('arial 18 bold'), fg = 'blue', bg = 'lightgrey')
        self.sex.place(x=30, y=380)


        # patient phoneMobile
        self.sex = Label(self.left, text="Mobile #", font = ('arial 18 bold'), fg = 'blue', bg = 'lightgrey')
        self.sex.place(x=30, y=420)


        # patient phoneHome
        self.sex = Label(self.left, text="Home #", font = ('arial 18 bold'), fg = 'blue', bg = 'lightgrey')
        self.sex.place(x=30, y=460)


        # patient phoneWork
        self.sex = Label(self.left, text="Work #", font = ('arial 18 bold'), fg = 'blue', bg = 'lightgrey')
        self.sex.place(x=30, y=500)


        # patient referrer
        self.sex = Label(self.left, text="Patient Referrer", font = ('arial 18 bold'), fg = 'blue', bg = 'lightgrey')
        self.sex.place(x=30, y=540)

        # ENTRY FIELDS #################################################################################################

        self.name_ent = Entry(self.left, width = 30)
        self.name_ent.place(x=250, y=140)

        self.dobd_ent = Entry(self.left, width = 4)
        self.dobd_ent.place(x=250, y=180)

        self.dobm_ent = Entry(self.left, width = 4)
        self.dobm_ent.place(x=280, y=180)

        self.doby_ent = Entry(self.left, width = 8)
        self.doby_ent.place(x=310, y=180)

        self.sex_ent = Entry(self.left, width = 18)
        self.sex_ent.place(x=250, y=220)

        self.nat_ent = Entry(self.left, width = 30)
        self.nat_ent.place(x=250, y=260)

        self.mari_ent = Entry(self.left, width = 30)
        self.mari_ent.place(x=250, y=300)

        self.job_ent = Entry(self.left, width = 30)
        self.job_ent.place(x=250, y=340)

        self.addr_ent = Entry(self.left, width = 30)
        self.addr_ent.place(x=250, y=380)

        self.mob_ent = Entry(self.left, width = 30)
        self.mob_ent.place(x=250, y=420)

        self.hom_ent = Entry(self.left, width = 30)
        self.hom_ent.place(x=250, y=460)

        self.wrk_ent = Entry(self.left, width = 30)
        self.wrk_ent.place(x=250, y=500)

        self.ref_ent = Entry(self.left, width = 30)
        self.ref_ent.place(x=250, y=540)

        # SUBMIT TO DB BUTTON #################################################################################################
        self.submit = Button(self.left, text = "Add New Patient", width = 20 , height = 2 , bg = 'steelblue' , command = self.add_pat)
        self.submit.place(x = 350, y = 600)


    # function to call when we press submit
    def add_pat(self):
        # grap user inputs:
        self.val1 =

        self.name_ent
        self.dobd_ent
        self.dobm_ent
        self.doby_ent
        self.sex_ent
        self.nat_ent
        self.mari_ent
        self.job_ent
        self.addr_ent
        self.mob_ent
        self.hom_ent
        self.wrk_ent
        self.ref_ent


# creating the object
root = Tk()
b    = Application(root)

# window resolution
root.geometry("1200x720+0+0")

# preventing the resize feature to optain responsiveness
root.resizable(False, False)

# ending the loop
root.mainloop()


# Tkinter Window #############################
##############################################
