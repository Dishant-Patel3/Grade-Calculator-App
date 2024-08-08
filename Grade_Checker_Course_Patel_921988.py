from tkinter import *

def raise_frame(frame):
    frame.tkraise()

# creates tkinter window called root
root = Tk()
root.geometry("500x700") # can be changed if needed
root.title("Grade Checker - Dishant Patel")

# creates an overall button and calls the raise_frame method to switch between frames
overall_button = Button(root, text="Overall",
                        width=10, command=lambda: raise_frame(overall_frame))
overall_button.place(x=10, y=5)
# creates an class button and calls the raise_frame method to switch between frames
class_button = Button(root, text="Class", width=10,
                      command=lambda: raise_frame(class_frame))
class_button.place(x=100, y=5)

overall_frame = Frame(root, width=500, height=680, bg="blue")    # need to change color when complete
class_frame = Frame(root, width=500, height=680, bg="green")    # need to change color when complete

# ------------------------ your code goes here ------------------------
# ----- Overall -----
canvas = Canvas(overall_frame, width=500, height=700, bg="cyan")
canvas.place(x=0, y=0)
coord = 10,10,490,340
coord1 = 10, 340, 490, 590
coord2 = 10, 590, 490, 650
coord3 = 40, 40, 450, 40
canvas.create_rectangle(coord)
canvas.create_rectangle(coord1)
canvas.create_rectangle(coord2)
canvas.create_line(coord3)
canvas.create_line(70, 430, 200, 430)
canvas.create_line(310, 430, 440, 430)

cycle1 = StringVar()
cycle2 = StringVar()
cycle3 = StringVar()
cycle4 = StringVar()
cycle5 = StringVar()
cycle6 = StringVar()
average = StringVar()
average1 = StringVar()
average2 = StringVar()

def closeWindow():
    root.destroy()
def newEntry():
    entry1.delete(0, END)
    entry2.delete(0, END)
    entry3.delete(0, END)
    entry4.delete(0, END)
    entry5.delete(0, END)
    entry6.delete(0, END)
    entry7.delete(0, END)
    entry8.delete(0, END)
    entry9.delete(0, END)
    blanklabel1.configure(text="")
    blanklabel2.configure(text="")
    blanklabel3.configure(text="")
    blanklabel4.configure(text="")
    blanklabel5.configure(text="")
    blanklabel6.configure(text="")
def findGrade():
    overall = average.get()
    semav1 = average1.get()
    semav2 = average2.get()
    grade1 = cycle1.get()
    grade2 = cycle2.get()
    grade3 = cycle3.get()
    grade4 = cycle4.get()
    grade5 = cycle5.get()
    grade6 = cycle6.get()
    if  grade2 == "-" and grade3 == "-" and grade4 == "-" and grade5 == "-" and grade6 == "-":
        overall = int(grade1)
        semav2 = "-"
        average2.set(semav2)
        s1 = (209-int(grade1))/2
        s1 = '{:.0f}'.format(s1)
        blanklabel2.configure(text="You need to average " + str(s1) + "+ to pass the semester.")
        blanklabel4.configure(text="You need to average 70+ to pass the semester.")
        overall = str('{:.0f}'.format(overall))
        average.set(overall)
        semav1 = overall
        average1.set(semav1)
    elif grade3 == "-" and grade4 == "-" and grade5 == "-" and grade6 == "-":
        overall = (int(grade1) + int(grade2))/2
        semav2 = "-"
        average2.set(semav2)
        s1 = (209-int(grade1)-int(grade2))
        s1 = '{:.0f}'.format(s1)
        blanklabel2.configure(text="You need to average " + str(s1) + "+ to pass the semester.")
        blanklabel4.configure(text="You need to average 70+ to pass the semester.")
        overall = str('{:.0f}'.format(overall))
        average.set(overall)
        semav1 = overall
        average1.set(semav1)
    elif grade4 == "-" and grade5 == "-" and grade6 == "-":
        overall = (int(grade1) + int(grade2) + int(grade3))/3
        semav1 = overall
        semav2 = "-"
        average2.set(semav2)
        if semav1 >= 70:
            blanklabel1.configure(text="P")
            blanklabel2.configure(text="You have Passed semester 1.")
        else:
            semav = 139 - int(overall)
            blanklabel1.configure(text="F")
            blanklabel2.configure(text="You have DID NOT semester 1.")
            blanklabel6.configure(text="You need a " + str(semav) + "+ cycle grades to semester average.")
        blanklabel4.configure(text="You need to average 70+ to pass the semester.")
        overall = str('{:.0f}'.format(overall))
        average.set(overall)
        semav1 = '{:.0f}'.format(semav1)
        average1.set(semav1)
    elif grade5 == "-" and grade6 == "-":
        overall = (int(grade1) + int(grade2) + int(grade3) + int(grade4))/4
        semav1 = (int(grade1) + int(grade2) + int(grade3))/3
        semav2 = int(grade4)
        s2 = (209-int(grade4))/2
        s2 = '{:.0f}'.format(s2)
        if semav1 >= 70:
            blanklabel1.configure(text="P")
            blanklabel2.configure(text="You have Passed semester 1.")
        else:
            semav = 139-int(overall)
            blanklabel1.configure(text="F")
            blanklabel2.configure(text="You have DID NOT semester 1.")
            blanklabel6.configure(text="You need a " + str(semav) + "+ cycle grades to semester average.")
        blanklabel4.configure(text="You need to average " + str(s2) + "+ to pass the semester.")
        overall = str('{:.0f}'.format(overall))
        average.set(overall)
        semav1 = '{:.0f}'.format(semav1)
        average1.set(semav1)
        semav2 = '{:.0f}'.format(semav2)
        average2.set(semav2)
    elif grade6 == "-":
        overall = (int(grade1) + int(grade2) + int(grade3) + int(grade4) + int(grade5))/5
        semav1 = (int(grade1) + int(grade2) + int(grade3))/3
        semav2 = (int(grade4) + int(grade5))/2
        s2 = (209-int(grade4)-int(grade5))
        if semav1 >= 70:
            blanklabel1.configure(text="P")
            blanklabel2.configure(text="You have Passed semester 1.")
        else:
            semav = 139 - int(overall)
            blanklabel1.configure(text="F")
            blanklabel2.configure(text="You have DID NOT semester 1.")
            blanklabel6.configure(text="You need a " + str(semav) + "+ cycle grades to semester average.")
        blanklabel4.configure(text="You need to average " + str(s2) + "+ to pass the semester.")
        overall = str('{:.0f}'.format(overall))
        average.set(overall)
        semav1 = '{:.0f}'.format(semav1)
        average1.set(semav1)
        semav2 = '{:.0f}'.format(semav2)
        average2.set(semav2)
    else:
        overall = (int(grade1) + int(grade2) + int(grade3) + int(grade4) + int(grade5) + int(grade6))/6
        overall = str('{:.0f}'.format(overall))
        average.set(overall)
        semav1 = (int(grade1) + int(grade2) + int(grade3))/3
        semav2 = (int(grade4) + int(grade5) + int(grade6))/3
        if semav1 >= 70:
            blanklabel1.configure(text="P")
            blanklabel2.configure(text="You have Passed semester 1.")
        else:
            blanklabel1.configure(text="F")
            blanklabel2.configure(text="You have DID NOT semester 1.")
        if semav2 >= 70:
            blanklabel3.configure(text="P")
            blanklabel4.configure(text="You have Passed semester 2.")
        else:
            blanklabel3.configure(text="F")
            blanklabel4.configure(text="You have DID NOT semester 2.")
        if semav1 >= 70 and semav2 >= 70:
            blanklabel5.configure(text="You have earned 1.0 full credit for your class.")
        elif semav1 >= 70 and semav2 < 70:
            blanklabel5.configure(text="You have earned .5 credit for your class.")
        elif semav1 < 70 and semav2 >= 70:
            blanklabel5.configure(text="You have earned .5 credit for your class.")
        else:
            blanklabel5.configure(text="You have earned 0.0 credit for your class.")
        semav1 = '{:.0f}'.format(semav1)
        average1.set(semav1)
        semav2 = '{:.0f}'.format(semav2)
        average2.set(semav2)
title = Label(overall_frame, text="Enter The Cycle Grades in the boxes below, if unkown Enter '-'.", font=('Baskerville Old Face', 13), bg="cyan")
title.place(x=30, y=15)

label1 = Label(overall_frame, text="Cycle 1 Grade: ", font=('Baskerville Old Face', 15), bg="cyan")
label1.place(x=80, y=50)
entry1 = Entry(overall_frame, width=20, textvariable=cycle1, font=('Baskerville Old Face', 15), bg="cyan")
entry1.place(x=230, y=50)

label2 = Label(overall_frame, text="Cycle 2 Grade: ", font=('Baskerville Old Face', 15), bg="cyan")
label2.place(x=80, y=100)
entry2 = Entry(overall_frame, width=20, textvariable=cycle2, font=('Baskerville Old Face', 15), bg="cyan")
entry2.place(x=230, y=100)

label3 = Label(overall_frame, text="Cycle 3 Grade: ", font=('Baskerville Old Face', 15), bg="cyan")
label3.place(x=80, y=150)
entry3 = Entry(overall_frame, width=20, textvariable=cycle3, font=('Baskerville Old Face', 15), bg="cyan")
entry3.place(x=230, y=150)

label4 = Label(overall_frame, text="Cycle 4 Grade: ", font=('Baskerville Old Face', 15), bg="cyan")
label4.place(x=80, y=200)
entry4 = Entry(overall_frame, width=20, textvariable=cycle4, font=('Baskerville Old Face', 15), bg="cyan")
entry4.place(x=230, y=200)

label5 = Label(overall_frame, text="Cycle 5 Grade: ", font=('Baskerville Old Face', 15), bg="cyan")
label5.place(x=80, y=250)
entry5 = Entry(overall_frame, width=20, textvariable=cycle5, font=('Baskerville Old Face', 15), bg="cyan")
entry5.place(x=230, y=250)

label6 = Label(overall_frame, text="Cycle 6 Grade: ", font=('Baskerville Old Face', 15), bg="cyan")
label6.place(x=80, y=300)
entry6 = Entry(overall_frame, width=20, textvariable=cycle6, font=('Baskerville Old Face', 15), bg="cyan")
entry6.place(x=230, y=300)

label7 = Label(overall_frame, text="The Overall Grade: ", font=('Baskerville Old Face', 15), bg="cyan")
label7.place(x=50, y=350)
entry7 = Entry(overall_frame, width=20, textvariable=average, font=('Baskerville Old Face', 15), bg="cyan")
entry7.place(x=250, y=350)

semester1 = Label(overall_frame, text="Average for Semester 1", font=('Baskerville Old Face', 15), bg="cyan")
semester1.place(x=40, y=400)
entry8 = Entry(overall_frame, width=15, textvariable=average1, font=('Baskerville Old Face', 15), bg="cyan" )
entry8.place(x=60, y=440)

semester2 = Label(overall_frame, text="Average for Semester 2", font=('Baskerville Old Face', 15), bg="cyan")
semester2.place(x=280, y=400)
entry9 = Entry(overall_frame, width=15, textvariable=average2, font=('Baskerville Old Face', 15), bg="cyan" )
entry9.place(x=300, y=440)

blanklabel1 = Label(overall_frame, text="", font=('Baskerville Old Face', 35), bg="cyan")
blanklabel1.place(x=20, y=460)

blanklabel2 = Label(overall_frame, text="", font=('Baskerville Old Face', 12), bg="cyan", wraplength=160, justify="left")
blanklabel2.place(x=70, y=470)

blanklabel3 = Label(overall_frame, text="", font=('Baskerville Old Face', 35), bg="cyan")
blanklabel3.place(x=260, y=460)

blanklabel4 = Label(overall_frame, text="", font=('Baskerville Old Face', 12), bg="cyan", wraplength=160, justify="left")
blanklabel4.place(x=310, y=470)

blanklabel5 = Label(overall_frame, text="", font=('Baskerville Old Face', 15), bg="cyan")
blanklabel5.place(x=80, y=550)

blanklabel6 = Label(overall_frame, text="", font=('Baskerville Old Face', 15), bg="cyan")
blanklabel6.place(x=50, y=510)

generate = Button(overall_frame, text="    Calculate    ", font=('Baskerville Old Face', 15), bg="black", fg="white", command=findGrade)
generate.place(x=20, y=600)

clearall = Button(overall_frame, text="    Clear All    ", font=('Baskerville Old Face', 15), bg="black", fg="white", command=newEntry)
clearall.place(x=200, y=600) 

close = Button(overall_frame, text="    Close    ", font=('Baskerville Old Face', 15), bg="black", fg="white", command=closeWindow)
close.place(x=380, y=600)

# ----- Class -----
assignments = IntVar()
assessments = IntVar()
num1 = StringVar()
num2 = StringVar()
num3 = StringVar()
num4 = StringVar()
num5 = StringVar()
num6 = StringVar()
num7 = StringVar()
num8 = StringVar()
num9 = StringVar()
num10 = StringVar()
num11 = StringVar()
num12 = StringVar()
def newAssignments():
    assignments.set(assignments.get()+1)
    if assignments.get() == 1:
        number1.place(x=20, y=150)
        assign1.place(x=60, y=150)
    elif assignments.get() == 2:
        number2.place(x=20, y=200)
        assign2.place(x=60, y=200)
    elif assignments.get() == 3:
        number3.place(x=20, y=250)
        assign3.place(x=60, y=250)
    elif assignments.get() == 4:
        number4.place(x=20, y=300)
        assign4.place(x=60, y=300)
    elif assignments.get() == 5:
        number5.place(x=20, y=350)
        assign5.place(x=60, y=350)
    elif assignments.get() == 6:
        number6.place(x=20, y=400)
        assign6.place(x=60, y=400)
    elif assignments.get() == 7:
        number7.place(x=20, y=450)
        assign7.place(x=60, y=450)
    elif assignments.get() == 8:
        number8.place(x=20, y=500)
        assign8.place(x=60, y=500)
def newAssessments():
    assessments.set(assessments.get()+1)
    if assessments.get() == 1:  
        number9.place(x=260, y=150)
        assess1.place(x=300, y=150)
    elif assessments.get() == 2:  
        number10.place(x=260, y=200)
        assess2.place(x=300, y=200)
    elif assessments.get() == 3:  
        number11.place(x=260, y=250)
        assess3.place(x=300, y=250)
    elif assessments.get() == 4:  
        number12.place(x=260, y=300)
        assess4.place(x=300, y=300)
def findAverage():
    x = assignments.get()
    y = assessments.get()
    as1 = num1.get()
    as2 = num2.get()
    as3 = num3.get()
    as4 = num4.get()
    as5 = num5.get()
    as6 = num6.get()
    as7 = num7.get()
    as8 = num8.get()
    as9 = num9.get()
    as10 = num10.get()
    as11 = num11.get()
    as12 = num12.get()
    if x == 0:
        assigntotal = "-"
        assignave.configure(text="Assignments avg: " + str(assigntotal), bg="white")
    elif x == 1:
        assigntotal = (int(as1))/(x)
        assigntotal = '{:.0f}'.format(assigntotal)
        assignave.configure(text="Assignments avg: " + str(assigntotal), bg="white")
    elif x == 2:
        assigntotal = (int(as1) + int(as2))/(x)
        assigntotal = '{:.0f}'.format(assigntotal)
        assignave.configure(text="Assignments avg: " + str(assigntotal), bg="white")
    elif x == 3:
        assigntotal = (int(as1) + int(as2) + int(as3))/(x)
        assigntotal = '{:.0f}'.format(assigntotal)
        assignave.configure(text="Assignments avg: " + str(assigntotal), bg="white")
    elif x == 4:
        assigntotal = (int(as1) + int(as2) + int(as3) + int(as4))/(x)
        assigntotal = '{:.0f}'.format(assigntotal)
        assignave.configure(text="Assignments avg: " + str(assigntotal), bg="white")
    elif x == 5:
        assigntotal = (int(as1) + int(as2) + int(as3) + int(as4) + int(as5))/(x)
        assigntotal = '{:.0f}'.format(assigntotal)
        assignave.configure(text="Assignments avg: " + str(assigntotal), bg="white")
    elif x == 6:
        assigntotal = (int(as1) + int(as2) + int(as3) + int(as4) + int(as5) + int(as6))/(x)
        assigntotal = '{:.0f}'.format(assigntotal)
        assignave.configure(text="Assignments avg: " + str(assigntotal), bg="white")
    elif x == 7:
        assigntotal = (int(as1) + int(as2) + int(as3) + int(as4) + int(as5) + int(as6) + int(as7))/(x)
        assigntotal = '{:.0f}'.format(assigntotal)
        assignave.configure(text="Assignments avg: " + str(assigntotal), bg="white")
    elif x == 8:
        assigntotal = (int(as1) + int(as2) + int(as3) + int(as4) + int(as5) + int(as6) + int(as7) + int(as8))/(x)
        assigntotal = '{:.0f}'.format(assigntotal)
        assignave.configure(text="Assignments avg: " + str(assigntotal), bg="white")
    elif x > 8:
        assigntotal = (int(as1) + int(as2) + int(as3) + int(as4) + int(as5) + int(as6) + int(as7) + int(as8))/8
        assigntotal = '{:.0f}'.format(assigntotal)
        assignave.configure(text="Assignments avg: " + str(assigntotal), bg="white")
    if y == 0:
        assesstotal = "-"
        assessave.configure(text="Assessments avg: " + str(assesstotal), bg="white")
    elif y == 1:
        assesstotal = (int(as9))/(y)
        assesstotal = '{:.0f}'.format(assesstotal)
        assessave.configure(text="Assessments avg: " + str(assesstotal), bg="white")
    elif y == 2:
        assesstotal = (int(as9) + int(as10))/(y)
        assesstotal = '{:.0f}'.format(assesstotal)
        assessave.configure(text="Assessments avg: " + str(assesstotal), bg="white")
    elif y == 3:
        assesstotal = (int(as9) + int(as10) + int(as11))/(y)
        assesstotal = '{:.0f}'.format(assesstotal)
        assessave.configure(text="Assessments avg: " + str(assesstotal), bg="white")
    elif y == 4:
        assesstotal = (int(as9) + int(as10) + int(as11) + int(as12))/(y)
        assesstotal = '{:.0f}'.format(assesstotal)
        assessave.configure(text="Assessments avg: " + str(assesstotal), bg="white")
    elif y > 4:
        assesstotal = (int(as9) + int(as10) + int(as11) + int(as12))/4
        assesstotal = '{:.0f}'.format(assesstotal)
        assessave.configure(text="Assessments avg: " + str(assesstotal), bg="white")
    if x > 0 and y == 0:
        cycletotal = ((int(assigntotal) * 40))/40
        cycletotal = '{:.0f}'.format(cycletotal)
        cyclegrade.configure(text=cycletotal)
        entry1.delete(0, END)
        entry1.insert(0, cycletotal)
    elif x == 0 and y > 0:
        cycletotal = ((int(assesstotal) * 60))/60
        cycletotal = '{:.0f}'.format(cycletotal)
        cyclegrade.configure(text=cycletotal)
        entry1.delete(0, END)
        entry1.insert(0, cycletotal)
    elif x > 0 and y > 0:
        cycletotal = ((int(assigntotal) * 40) + int(assesstotal) * 60)/100
        cycletotal = '{:.0f}'.format(cycletotal)
        cyclegrade.configure(text=cycletotal)
        entry1.delete(0, END)
        entry1.insert(0, cycletotal)
    else:
        cycletotal = str("-")
        cyclegrade.configure(text=cycletotal)
        entry1.delete(0, ENcD)
        entry1.insert(0, cyletotal)
def deleteEntry():
    assignments.set(0)
    assessments.set(0) 
    number1.place_forget()
    assign1.delete(0, END)
    assign1.place_forget()
    number2.place_forget()
    assign2.delete(0, END)
    assign2.place_forget()
    number3.place_forget()
    assign3.delete(0, END)
    assign3.place_forget()
    number4.place_forget()
    assign4.delete(0, END)
    assign4.place_forget()
    number5.place_forget()
    assign5.delete(0, END)
    assign5.place_forget()
    number6.place_forget()
    assign6.delete(0, END)
    assign6.place_forget()
    number7.place_forget()
    assign7.delete(0, END)
    assign7.place_forget()
    number8.place_forget()
    assign8.delete(0, END)
    assign8.place_forget()
    number9.place_forget()
    assess1.delete(0, END)
    assess1.place_forget()
    number10.place_forget()
    assess2.delete(0, END)
    assess2.place_forget()
    number11.place_forget()
    assess3.delete(0, END)
    assess3.place_forget()
    number12.place_forget()
    assess4.delete(0, END)
    assess4.place_forget()
    cyclegrade.configure(text="", bg="cyan")
    assignave.configure(text="", bg="cyan")
    assessave.configure(text="", bg="cyan")
canvas1 = Canvas(class_frame, width=500, height=700, bg="cyan")
canvas1.place(x=0, y=0)
canvas1.create_rectangle(405, 585, 485, 645)
canvas1.create_line(180, 50, 300, 50)

cyclelabel = Label(class_frame, text="Grades for Cycle 1", font=('Baskerville Old Face', 15), bg="cyan")
cyclelabel.place(x=170, y=20)

assignment = Label(class_frame, text="Assigments", font=('Baskerville Old Face', 20), bg="cyan")
assignment.place(x=70, y=50)
assign = Button(class_frame, text="             +Assigment             ", font=('Baskerville Old Face', 15), bg="white", fg="black", command=newAssignments)
assign.place(x=10, y=90)

assessment = Label(class_frame, text="Assessments", font=('Baskerville Old Face', 20), bg="cyan")
assessment.place(x=300, y=50)
assign = Button(class_frame, text="            +Assessment             ", font=('Baskerville Old Face', 15), bg="white", fg="black", command=newAssessments)
assign.place(x=250, y=90)

cycleave = Button(class_frame, text="Calculate Cycle Average", font=('Baskerville Old Face', 15), bg="white", fg="black", command=findAverage)
cycleave.place(x=10, y=590)

assignweight = Label(class_frame, text="Assigment Weight: 40%", font=('Baskerville Old Face', 12), bg="cyan")
assignweight.place(x=225, y=590)

assetweight = Label(class_frame, text="Assessment Weight: 60%", font=('Baskerville Old Face', 12), bg="cyan")
assetweight.place(x=225, y=610)

cyclegrade = Label(class_frame, text="", font=('Baskerville Old Face', 21), bg="cyan")
cyclegrade.place(x=420, y=595)

assignave = Label(class_frame, text="", font=('Baskerville Old Face', 15), bg="cyan")
assignave.place(x=40, y=550)

assessave = Label(class_frame, text="", font=('Baskerville Old Face', 15), bg="cyan")
assessave.place(x=280, y=550)

reset = Button(class_frame, text="               Clear All               ", font=('Baskerville Old Face', 12), bg="white", fg="black", command=deleteEntry)
reset.place(x=150, y=640)

number1 = Label(class_frame, text="#1", font=('Baskerville Old Face', 15), bg="cyan" )
assign1 = Entry(class_frame, width=16, textvariable=num1, font=('Baskerville Old Face', 15), bg="cyan" )

number2 = Label(class_frame, text="#2", font=('Baskerville Old Face', 15), bg="cyan" )
assign2 = Entry(class_frame,  width=16, textvariable=num2, font=('Baskerville Old Face', 15), bg="cyan" )

number3 = Label(class_frame, text="#3", font=('Baskerville Old Face', 15), bg="cyan" )
assign3 = Entry(class_frame,  width=16, textvariable=num3, font=('Baskerville Old Face', 15), bg="cyan" )

number4 = Label(class_frame, text="#4", font=('Baskerville Old Face', 15), bg="cyan" )
assign4 = Entry(class_frame,  width=16, textvariable=num4, font=('Baskerville Old Face', 15), bg="cyan" )

number5 = Label(class_frame, text="#5", font=('Baskerville Old Face', 15), bg="cyan" )
assign5 = Entry(class_frame,  width=16, textvariable=num5, font=('Baskerville Old Face', 15), bg="cyan" )

number6 = Label(class_frame, text="#6", font=('Baskerville Old Face', 15), bg="cyan" )
assign6 = Entry(class_frame,  width=16, textvariable=num6, font=('Baskerville Old Face', 15), bg="cyan" )

number7 = Label(class_frame, text="#7", font=('Baskerville Old Face', 15), bg="cyan" )
assign7 = Entry(class_frame, width=16, textvariable=num7, font=('Baskerville Old Face', 15), bg="cyan" )

number8 = Label(class_frame, text="#8", font=('Baskerville Old Face', 15), bg="cyan" )
assign8 = Entry(class_frame,  width=16, textvariable=num8, font=('Baskerville Old Face', 15), bg="cyan" )

number9 = Label(class_frame, text="#1", font=('Baskerville Old Face', 15), bg="cyan" )
assess1 = Entry(class_frame, width=16, textvariable=num9, font=('Baskerville Old Face', 15), bg="cyan" )

number10 = Label(class_frame, text="#2", font=('Baskerville Old Face', 15), bg="cyan" )
assess2 = Entry(class_frame, width=16, textvariable=num10, font=('Baskerville Old Face', 15), bg="cyan" )

number11 = Label(class_frame, text="#3", font=('Baskerville Old Face', 15), bg="cyan" )
assess3 = Entry(class_frame, width=16, textvariable=num11, font=('Baskerville Old Face', 15), bg="cyan" )

number12 = Label(class_frame, text="#4", font=('Baskerville Old Face', 15), bg="cyan" )
assess4 = Entry(class_frame, width=16, textvariable=num12, font=('Baskerville Old Face', 15), bg="cyan" )

# do not delete any of the code below
for frame in (overall_frame, class_frame):
    frame.place(x=0, y=35)

raise_frame(overall_frame)
root.mainloop()