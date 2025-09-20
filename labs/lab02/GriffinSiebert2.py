
def grade(bestscore, score):
    if score >= bestscore-10:
        return "A"
    elif score >= bestscore - 20:
        return "B"
    elif score >= bestscore - 30:
        return "C"
    elif score >= bestscore - 40:
        return "D"
    else :
        return "F"

def main():
    numStudents = int(input("Total number of students: "))
    scores = []
    while (len(scores) < numStudents):
        scores = input("Enter " + str(numStudents) + " score(s): ").split(" ")
    if len(scores) > numStudents:
        for i in range(len(scores)):
            if i+1 > numStudents:
                scores.pop(i)

    bestscore = 0
    sum = 0
    for score in scores:
        sum += int(score)
        if int(score) >= bestscore:
            bestscore = int(score)

    for i in range(len(scores)):
        score = int(scores[i])
        i = str(i+1)
        grade_letter = grade(bestscore, score)
        print("Student " + i + " score is " + str(score) + " and grade is " + grade_letter)

    avg = sum / numStudents
    avg_letter = grade(bestscore, avg)
    print("The average score is " + f"{avg:.2f}" + ", a grade of " + avg_letter)


main()
