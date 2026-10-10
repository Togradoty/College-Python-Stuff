#calculates the average, and returns back the average
def calc_average(score1, score2, score3, score4, score5):
    average = (score1 + score2 + score3 + score4 + score5) / 5
    return average
#determines what the garade letter is based on on the average, and returns the letter
def determine_grade(average):
    if average >= 90:
        return "A"
    elif average >= 80:
        return "B"
    elif average >= 70:
        return "C"
    elif average >= 60:
        return "D"
    else:
        return "F"
#opens up the score txt for the grades
infile = open("scores.txt", "r")
#sets the scores based on the txt file
score1 = float(infile.readline())
score2 = float(infile.readline())
score3 = float(infile.readline())
score4 = float(infile.readline())
score5 = float(infile.readline())
#closes out the file
infile.close()
#calls functions
average = calc_average(score1, score2, score3, score4, score5)
grade = determine_grade(average)
#display results
print(f"Average Test Score: {average:.2f}")
print(f"Letter Grade: {grade}")