# grades [0 : 100]
# if grade - next multiple of 5 < 3 -> grade = next multiple of 5
# if grade < 38 -> grade = grade


def grading_students(grades):

    i = 0
    for grade in grades:
        if (grade % 5) != 0:
            if grade >= 38:
                grades[i] = round_grade(grade)

        i += 1

    return grades


def round_grade(grade):

    next_multiple_of_five = grade;

    if (grade % 5) == 0:
        return grade

    while (next_multiple_of_five % 5) != 0:
        next_multiple_of_five += 1;

    if next_multiple_of_five - grade < 3:
        return next_multiple_of_five

    return grade


if __name__ == '__main__':

    grades = [73, 67, 38, 33]

    grading_students(grades)

    for grade in grades:
        print(grade)

