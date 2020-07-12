import pickle
print("Welcome to the Console App \n -------------------->>>>>>>>>>>>>IT APP<<<<<<<<<<<<<--------------------------")


class Academy():
    def __init__(self):
        self.name = "New Student"
        self.course = "Not Chosen"
        self.reaminingFees = 20000
        self.payment = 0
        self.courseCompletion = "No"
        self.amountReturned = "No"

    def courses(self):
        print("Hello!! We provide courses on")
        print("Python \nSQL\nDjango\nJavascript")

    def enquiry(self):
        self.courses()
        userName = str(input("Enter Student Name \n =>"))
        self.name = userName

        userEnquiry = input("Enter the subject that you want to study?\n =>")

        if userEnquiry == "Python" or userEnquiry == "python":
            print("-----------------Python Course Details--------------------------")
            print("Week 1 \n=>Introduction\nFunctions\nOOP ")

        elif userEnquiry == "SQL" or userEnquiry == "sql" or userEnquiry == "Sql":
            print("-----------------SQL Course Details--------------------------")
            print("Week 1 \n=>Introduction\nDeep Dive\nOOP ")

        elif userEnquiry == "Javascript" or userEnquiry == "javascript":
            print("-----------------Javascript Course Details--------------------------")
            print("Week 1 \n=>Introduction\nJavascript Functional\nJavascript Classes ")
        else:
            print("Check your spelling or see the list of course we provide")
            checkCourses = input(
                " \n Enter Accordingly \n A =>Check the available courses \n EA=> Enquire Again \n Press any key to exit ")
            if checkCourses == 'a' or checkCourses == 'A':
                self.courses()
            elif checkCourses == 'EA' or checkCourses == 'ea':
                self.enquiry()
            else:
                return "BYE"
        print(
            f"Student name is {self.name} and the course chosen is {userEnquiry}")
        changeCourse = input("If there are any errors type YES \n =>")
        if changeCourse == "yes":
            self.enquiry()

        self.course = userEnquiry

    def payments(self):
        print(
            "------------------------Course Price: Rs 20,000-----------------------------")
        print('\n')
        print("You should deposit minimum of Rs 10,000 as first installment")
        coursePayment = int(input("Enter the payment amount \n =>"))
        if self.reaminingFees == 0:
            print("You have no due payment")

        elif coursePayment < 10000:
            print("Payment Unsuccessfull!!!, The payment should be minimum of Rs. 10,000")
            payAgain = input("press P to Pay again /n >>  ")
            if payAgain == 'P' or payAgain == 'p':
                self.payments()

        elif coursePayment < 20000:
            remainingPayment = self.reaminingFees - coursePayment

            self.reaminingFees = remainingPayment
            self.payment = coursePayment
        elif coursePayment == 20000:
            print("Full Payment Done")
            self.remainigFees = 0

        else:
            pass

    def update(self):
        self.enquiry()

    def courseCompletions(self):
        hasCompleted = input(
            f"Did the user {self.name} comple the course on {self.course}? \n Enter Yes or No \n =>")
        if hasCompleted == "yes" or hasCompleted == "YES":
            bankAccount = int(input("Enter Bank Account Number"))
            print(
                f"Rs 20,000 deposit amount will be returned to account number {bankAccount}")
            correction = input("Is the bank Account Number Correct?")
            if correction == "yes" or correction == "yes":
                print(
                    f"Rs 20,000 deposit amount will be returned to account number {bankAccount} by 5pm Today")
                print("BYE")
                self.courseCompletion = "YES"
                self.amountReturned = "YES"
            else:
                print("You have not completed the course yet")

    def studentInfo(self):
        print(f"Student Name=> {self.name}")
        print(f"Student Course=> {self.course}")
        print(f"Student Remaining Fees=> {self.reaminingFees }")
        print(f"Student Paid Amount=> {self.payment}")
        print(f"Course Completion => {self.courseCompletion}")
        print(f"Deposit Returned?=> {self.amountReturned}")


making = str(
    input(print("Do you want to add a student? \n Enter yes for adding \n=>")))
if making == "Yes" or making == "yes":
    user = input(
        "Enter the student Name, this name will be associated with all of the student's information \n =>")
    user = Academy()
    user.enquiry()
    user.payments()

    userDetailsPickle = open('Details', 'wb')
    pickle.dump(user.studentInfo, userDetailsPickle)
    userDetailsPickle.close()
# Reading From Pickle FILE
    userDetailsPickle = open('Details', 'rb')
    Details = pickle.load(userDetailsPickle)
    userDetailsPickle.close()
    print(type(Details))
    user.studentInfo()
