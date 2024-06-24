# I declare that my work contains no examples of misconduct, such as plagiarism, or collusion. 
# Any code taken from other sources is referenced within my code soluƟon.
# Student ID: 20221147
# Date: 2/12/2023

from graphics import *

# Initializing variables
validation = True
total_count = 0
progress_count = 0
trailer_count = 0
retrieve_count = 0
exclude_count = 0
credit_list = []
nested_list = []

def credit_validation(prompt):
    ''' Getting inputs and check wheather they are valid inputs'''
    while True:
        try:
            valid_credits = [0, 20, 40, 60, 80, 100, 120]
            input_value = int(input(prompt))
            if input_value in valid_credits:
                return input_value
            else:
                print("Out of range")

        except ValueError:
            print("Integer required") 

# Check wheather a student or a staff member
Check = input("Enter 'stu' for student or 'stf' to staff : ")
while Check.lower() not in ['stu', 'stf']:
        Check = input("Invalid input. Enter 'stu' for student or 'stf' to staff :  ")

while validation:
    pass_credits = credit_validation("\nEnter your total PASS credits : ")
    defer_credits = credit_validation("Enter your total DEFER credits : ")
    fail_credits = credit_validation("Enter your total FAIL credits : ")

    # Check total
    total = pass_credits + defer_credits + fail_credits
    if total > 120:
        print("Total incorect")
        continue
    
    # insert elements to a list
    credit_list = [pass_credits,defer_credits,fail_credits]

    # Check the progress
    if pass_credits == 120:
        print("Progress")
        progress_count += 1
        credit_list.insert(0,"Progress")

    elif pass_credits >= 100:
        print("Progress (module trailer)")
        trailer_count += 1
        credit_list.insert(0,"Progress (module trailer)")

    elif fail_credits >= 80:
        print("Exclude")
        exclude_count += 1
        credit_list.insert(0,"Exclude")

    else:
        print("Module retriever")
        retrieve_count += 1
        credit_list.insert(0,"Module retriever")

    if Check == 'stu':
        validation = False
        continue
    total_count += 1

    # Createing a nested list 
    nested_list.append(credit_list)  

    # Play again loop
    print(" \nWould you like to enter another set of data?")
    play_again = input("Enter 'y' for yes or 'q' to quit : ")

    while play_again.lower() not in ['q', 'y']:
        play_again = input("Invalid input. Enter 'y' for yes or 'q' to quit: ")

    if play_again.lower() == 'q':

        # Part - 2
        file_text =""
        print("\nPart 2:")
        for list in nested_list:
            file_text = f"{file_text} \n {list[0]}  - {list[1]} , {list[2]} , {list[3]}"
        print(file_text)
        
        # Part - 3
        # Insert data into a text file
        with open("textFile.txt", "w") as f0:
            f0.write("part - 03\n")
            f0.write(file_text)

        # Histogram
        win = GraphWin("Histogram", 700, 600)

        label = Text(Point(350, 24), 'Histogram Result')  
        label.draw(win)

        # Create count the graph
        progress = Text(Point(60,350 - ((300 / total_count) * progress_count)), progress_count)
        progress.draw(win)

        trailer = Text(Point(148, 350 - ((300 / total_count) * trailer_count)), trailer_count)
        trailer.draw(win)

        retrieve = Text(Point(240, 350 - ((300 / total_count) * retrieve_count)), retrieve_count)
        retrieve.draw(win)

        exclude = Text(Point(332, 350 - ((300 / total_count) *  exclude_count)), exclude_count)
        exclude.draw(win)

        # Draw histogram bars and fill colors
        bar1 = Rectangle(Point(24, 360), Point(96, 360 - ((300 / total_count) * progress_count)))
        bar1.setFill("light green")
        bar1.draw(win)

        bar2 = Rectangle(Point(116, 360), Point(188, 360 - ((300 / total_count) * trailer_count)))
        bar2.setFill("light blue")
        bar2.draw(win)

        bar3 = Rectangle(Point(208, 360), Point(280, 360 - ((300 / total_count) * retrieve_count)))
        bar3.setFill("yellow")
        bar3.draw(win)

        bar4 = Rectangle(Point(300, 360), Point(372, 360 - ((300 / total_count) * exclude_count)))
        bar4.setFill("pink")
        bar4.draw(win)

        # Draw labels to the graph
        progress_label = Text(Point(60, 380), 'Progress')
        progress_label.draw(win)

        trailer_label = Text(Point(150, 380), 'Trailer')
        trailer_label.draw(win)

        retrieve_label = Text(Point(245, 380), 'Retriever')
        retrieve_label.draw(win)

        exclude_label = Text(Point(335, 380), 'Excluded')
        exclude_label.draw(win)

        total_label = Text(Point(200, 420), f"{total_count} Outcomes in total.")
        total_label.draw(win)

        win.getMouse()
        win.close()

        validation = False

    elif play_again.lower() != 'y':
        print("Invalid input")
        validation = False

    


    