from tkinter import *
import json

def clear():
    # clear the content of text entry box
    name_field.delete(0, END)
    course_field.delete(0, END)
    sem_field.delete(0, END)
    contact_no_field.delete(0, END)
    email_id_field.delete(0, END)

def insert():
    name = name_field.get()
    course = course_field.get()
    sem = sem_field.get()
    contact = contact_no_field.get()
    email = email_id_field.get()
    dictionary = {}
    dictionary['name'] = name
    dictionary['course'] = course
    dictionary['semester'] = sem
    dictionary['contact'] = contact
    dictionary['email'] = email
    print(dictionary)

    #checking if json file exists or not
    try:
        outfile = open('data1.json', 'r')
        outfile.close()
    #if not then create a json file
    except FileNotFoundError:
        outfile = open('data1.json', 'w')
        outfile.write('[]')
        outfile.close()
    
    with open('data1.json', 'r') as outfile:
        json_data = outfile.read()
        data = json.loads(json_data)
        data.append(dictionary)
        print(data)
    
    with open('data1.json', 'w') as outfile:
        json.dump(data, outfile)

    clear()

root = Tk()

# set the background colour of GUI window
root.configure(background='light green')

# set the title of GUI window
root.title("registration form")

# set the configuration of GUI window
root.geometry("500x300")

# create a Form label
heading = Label(root, text="Form", bg="light green")

# create a Name label
name = Label(root, text="Name", bg="light green")

# create a Course label
course = Label(root, text="Course", bg="light green")

# create a Semester label
sem = Label(root, text="Semester", bg="light green")

# create a Contact No. label
contact_no = Label(root, text="Contact No.", bg="light green")

# create a Email id label
email_id = Label(root, text="Email id", bg="light green")

# create a address label
address = Label(root, text="Address", bg="light green")

# grid method is used for placing
# the widgets at respective positions
# in table like structure .
heading.grid(row=0, column=1)
name.grid(row=1, column=0)
course.grid(row=2, column=0)
sem.grid(row=3, column=0)
contact_no.grid(row=5, column=0)
email_id.grid(row=6, column=0)

# create a text entry box
# for typing the information
name_field = Entry(root)
print(name_field.get())
course_field = Entry(root)
sem_field = Entry(root)
contact_no_field = Entry(root)
email_id_field = Entry(root)
print(name_field.get())
# grid method is used for placing
# the widgets at respective positions
# in table like structure .
name_field.grid(row=1, column=1, ipadx="100")
course_field.grid(row=2, column=1, ipadx="100")
sem_field.grid(row=3, column=1, ipadx="100")
contact_no_field.grid(row=5, column=1, ipadx="100")
email_id_field.grid(row=6, column=1, ipadx="100")

# call excel function
# excel()

submit = Button(root, text="Submit", fg="Black",
                bg="Red", command=insert)
submit.grid(row=8, column=1)

submit = Button(root, text=" Exit ", fg="Black",
                bg="Red", command=root.destroy)
submit.grid(row=10, column=1)

root.mainloop()