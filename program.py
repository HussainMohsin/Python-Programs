# function to display the menu
def menu():
    print('\n1-Computing Pi')
    print('2-Computing Square Root')
    print('3-Displaying Prime Numbers')
    print('4-Processing  Scores')
    print('5-Computing  Tax')
    print('6-Solving  Quadratic Equation')
    print('7-Sort a List')
    print('8-Generate Username and Password')
    print('9-Sort Student File')
    print('10-Quit\n')


#########################################
# function to compute pi
def compute_pi(n):
    series = 1  # initialize series to 1
    for k in range(1, n):  # loop from 1 until n, increment by 1
        constant = 1 / ((2 * k) + 1)  # constant variable

        if k % 2 != 0:  # if K is an even number
            series = series - constant  # subtract constant from series
        else:  # if K is an odd number
            series = series + constant  # add constant to series

    return 4 * series  # return series times 4


#################################################
# function to compute the square root of a given number
def compute_sqrt(x):
    squarer = 1  # initialize squarer to 1
    for k in range(10):  # loop through 10 iterations
        squarer = 0.5 * (squarer + x / squarer)  # next = 0.5(last + x / last)
    return squarer  # return the square root


#################################################
# Function  displays all prime numbers less than or equal to n.
def display_primes(n):
    print('All the prime numbers up to', n, 'are:')
    for k in range(2, n):  # loop that starts at 2 and goes up by 1 until n is reached
        if is_prime(k):  # check if k is prime
            print(k)  # prints k if it is prime


# function that decides whether a given number is a prime or not.
def is_prime(n):
    prime = 1  # prime is set to true value
    if n == 1:  # if n is 1
        prime = 0  # set prime to a false value
    for k in range(2, n):  # loop that starts at 2 and goes up by 1 until n is reached
        if (n % k == 0) and (k != n):  # if n doesnt have a remainder and is not equal to k
            prime = 0  # set prime to a false value
    return prime  # returns 1 if n is prime or 0 if n isn't prime


#################################################
def process_scores():
    # initialize totalStudents, totalScores, maxScore to zero and minScore to 10000
    totalStudents = 0
    totalScores = 0
    maxScore = 0
    minScore = 10000
    # initialize minScoreStd & maxScoreStd to empty strings
    minScoreStd = ' '
    maxScoreStd = ' '
    # print information for the user
    print('\nThe name is a single word and the score is a positive integer')
    print('Enter Q to quit\n')

    while 1:
        user = input('Enter the name and the score separated by blank in one line: ')
        student = user.split()  # splits the student name and score and is placed in a list
        name = student[0]  # name is the first string in the student list
        if (name == 'q') or (name == 'Q'):  # if q or Q is entered exit the loop
            break
        score = float(student[1])  # score is the second string in the student list
        totalStudents += 1  # increment the number of students after each student is entered
        totalScores += score  # add up all the scores together for the average

        if score < minScore:  # if the current score is less than minimum score
            minScore = score  # current score becomes minScore
            minScoreStd = name  # current name has the lowest score

        if score > maxScore:  # if the current score is greater than maxScore
            maxScore = score  # current score becomes maxScore
            maxScoreStd = name  # current name has the highest score

    if totalStudents > 0:  # if 1 or more students were entered
        avgScore = totalScores / totalStudents  # average score equals total scores divided by the number of students
        print('The average score is', avgScore)  # print the average score
        # printing the lowest score with its owner
        print(minScoreStd, 'had the lowest score of', minScore)
        # printing the highest score with its owner
        print(maxScoreStd, 'had the highest score of', maxScore)

    else:  # if no students were entered
        print('No students were entered')


#################################################
# function that determines the tax amount according to the following tax rules
def compute_tax(income, status, state):
    tax_amount = -1  # initialize tax amount to -1
    if state == 'i' or state == 'I':  # check if they are in state
        if status == 'Single' or status == 'single':  # check if their status is single
            if income < 30000:  # check if their income is less than 30000
                tax_amount = income * 0.20  # if true their tax is 20% of their income
            else:
                tax_amount = income * 0.25  # else their tax is 20% of their income
        if status == 'Married' or status == 'married':  # check if their status is married
            if income < 50000:  # check if their income is less than 50000
                tax_amount = income * 0.10  # if true their tax is 10% of their income
            else:
                tax_amount = income * 0.15  # else their tax is 15% of their income
    elif state == 'o' or state == 'O':  # check if they are out of state
        if status == 'Single' or status == 'single':  # check if their status is single
            if income < 30000:  # check if their income is less than 30000
                tax_amount = income * 0.17  # if true their tax is 17% of their income
            else:
                tax_amount = income * 0.22  # else their tax is 22% of their income
        if status == 'Married' or status == 'married':  # check if their status is married
            if income < 50000:  # check if their income is less than 50000
                tax_amount = income * 0.07  # if true their tax is 7% of their income
            else:
                tax_amount = income * 0.12  # else their tax is 12% of their income

    return tax_amount  # return the tax amount


#################################################
# Function that solves a given quadratic equation
def solve_quadratic(a, b, c):
    solution = (b ** 2) - (4.0 * a * c)  # initialize solution to the equation (B^2 - 4ac
    if solution >= 0:  # check if there are any solutions
        # return both solutions if found
        return (-b + compute_sqrt(solution)) / (2.0 * a), (-b - compute_sqrt(solution)) / (2.0 * a)
    else:  # else return 2 zeros
        return 0, 0


#################################################
# Function that sorts a given list of numbers
def sort(array):
    my_array = [0] * len(array)  # make the length of my_array to the length of the list passed
    for i in range(len(my_array)):  # loop to copy the elements from the list to my_array
        my_array[i] = array[i]

    for m in range(len(my_array)):  # loop from m to the length of the array
        minimum = m  # initialize minimum to m
        for n in range(m + 1, len(my_array)):  # loop from m+1 to the length of the array
            if my_array[minimum] > my_array[n]:  # check if the minimum element is greater than my_array
                minimum = n  # make current element the minimum element
        my_array[m], my_array[minimum] = my_array[minimum], my_array[m]  # swap the 2 elements

    return my_array  # return sorted array


#################################################
#  function that automatically generates the user id and the password for the user
def id_password(first, last):
    f_length = len(first)  # get the length of the first name
    l_length = len(last)  # get the length of the last name

    user_id = first[0].upper() + last.upper()  # user id is first letter of the first name followed by the last name

    # password is the first letter of the first name followed the last letter of the first name
    # followed by the first three letters of the last name
    password = first[0] + first[f_length - 1] + last[0:3]

    password = password.upper()  # Make password all upper case letters

    # followed by the length of the first name followed by the length of the last name
    password = password + str(f_length) + str(l_length)

    return user_id, password  # return  the userId password


#################################################
# function that reads an input file and creates a sorted output file
def file_sort(infile, outfile):
    # open file
    inputFile = open(infile, 'r')

    # read the first line and strip of extra spaces and convert to int
    size = inputFile.readline().strip()
    numStudents = int(size)

    # make 3 String Lists the same size as the number of students
    student_id = [' '] * numStudents  # string list that holds student ids
    student_name = [' '] * numStudents  # string list that holds student names
    student_gpa = [' '] * numStudents  # string list that holds student gpa

    # iterate for student_count times

    for i in range(numStudents):  # loop that goes through all the students
        line = inputFile.readline().strip().split()  # Strip and split each line, and make it a list
        student_id[i] = line[0]  # first element in list is the id and it gets added to student id list
        student_name[i] = line[1]  # second element in list is the name and it gets added to student name list
        student_gpa[i] = line[2]  # third element in list is the gpa and it gets added to student gpa list

    # bubble sort to sort thr students by ascending ids
    for i in range(numStudents - 1):  # run a loop that goes from 0 to the number of students -1
        for j in range(numStudents - i - 1):
            if int(student_id[j]) > int(student_id[j + 1]):  # if current gpa is greater the the next gpa
                # swap the 2 ids in the student_id list
                student_id[j], student_id[j + 1] = student_id[j + 1], student_id[j]
                # swap the names and GPAs at that same indexes as the 2 ids
                student_name[j], student_name[j + 1] = student_name[j + 1], student_name[j]
                student_gpa[j], student_gpa[j + 1] = student_gpa[j + 1], student_gpa[j]

    inputFile.close()  # close the input file
    outputFile = open(outfile, 'w')  # writing to the output file

    outputFile.write(str(numStudents) + '\n')  # write the number of students at the top of the fill

    for j in range(numStudents):  # loop that writes all the students into the outfile
        outputFile.write(str(student_id[j]) + ' ' + student_name[j] + ' ' + student_gpa[j] + '\n')

    outputFile.close()  # close the output file


#################################################
def main():
    while 1:  # infinite loop for menu options until you quit
        menu()  # calling menu function that displays the menu
        option = int(input('Enter an option number: '))  # option is an int for the menu selection

        # if and elif statements for all the options
        if option == 1:
            nthTerm = int(input('Enter the nth term you would like to use: '))  # Getting the integer nth term from user
            print('Pi is', compute_pi(nthTerm))  # call the compute_pi method to display pi

        elif option == 2:
            # Getting the integer num from user
            num = int(input('Enter in a number you would like to find the square root of: '))
            # call the compute_sqrt method in print to get the square root of the num
            print('The square root of', num, 'is', compute_sqrt(num))

        elif option == 3:
            # Getting the integer num from user
            num = int(input('Enter in the number you would like to check if it is prime: '))
            is_prime(num)  # calling is_prime method to check if num is prime
            display_primes(num)  # calling display prime to display all the prime number to num

        elif option == 4:
            process_scores()  # call process_scores to process the scores

        elif option == 5:
            income = float(input('Enter your yearly income: $'))
            status = input('Enter your marital status: ')
            state = input('Enter (I) if you are in State, or (O) if you are out of State: ')
            tax = compute_tax(income, status, state)

            if tax > -1:  # if tax is greater than -1 all the inputs where valid
                # displays the user inputs entered and the tax amount
                print('The tax amount for an (' + state + ') state, ', end='')
                print(status + ' status with an income of $' + str(income) + ' is $' + str(tax))
            else:  # if any invalid info was entered
                print('You have entered an invalid input, try again.')

        elif option == 6:
            print('Quadratic Equation: ax^2+ bx + c')  # display quadratic equation
            a = int(input('Enter in a: '))   # user input for a
            b = int(input('Enter in b: '))   # user input for b
            c = int(input('Enter in c: '))   # user input for c

            if solve_quadratic(a, b, c) == (0, 0):  # if two zeros are returned there are no solution
                print('There were no solution was found')
            else:  # else print the 2 solutions that are returned from solve_quadratic method
                print('The two solutions found were', solve_quadratic(a, b, c))

        elif option == 7:
            the_list = [6, 3, 5, 2, 4, 1]  # list to sort
            my_list = sort(the_list)  # initializing my_List to the list returned from sort function
            print('The list has been sorted')
            for element in my_list:  # for loop that prints all the elements in the list
                print(element, end=' ')

        elif option == 8:
            first = input('Enter your first name: ')  # get first name from user
            last = input('Enter your last name: ')  # get last name from user
            # print the id and password printed from the id_password method
            print("Your id and password are", id_password(first, last))

        elif option == 9:
            infile = input('Enter the file name you are reading from: ')  # get infile name from user
            outfile = input('Enter the file name you are writing to: ')  # get outfile name from user
            file_sort(infile, outfile)  # calling the file_sort method to sort the infile to the outfile
            print('The', infile, 'file has been sorted and saved to', outfile)

        elif option == 10:
            print('Thank you')  # display thank you if you quit and break
            break
        else:
            print('Error invalid option')  # display message if an invalid option was entered


main()  # call the main function
