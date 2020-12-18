"""
The program is to display the number of grades,
the averaqge grade, and the percentage of grades
that are above the average from the Final.txt, which 
contains students grades on the final exam. 
first we will write a main function to initialize the application
and a calculate_percent_above grade function to calculate
the percentage of grades that are above the grade average.
we have to make a list for the final.txt.
The given number of grades is 24.
The given Average grade is 83.25.
The percentage of grades above average is 54.17%. 
"""

"""
# main:
    grades from list

# calculate_percent_above_average():

#infile=open the final(1).txt document


"""

def main():
    calculate_percent_above_average()
    
    inflie = open ("final(1).txt", 'r')
    grades = [line.rstrip() for line in infile]
    infile.close()

for i in range(len(grades)):
    grades[i] = int(grades[i])
average = sum(grades) / len(grades)
num = 0 # number of grades above average
for grade in grades:
    if grade > average:
        num += 1
print("Number of grades:", len(grades))
print("Average grade:", average)
print("Percentage of grades above average: {0:.2f}%",.format(100 * num / len(grades))

main
