last_semester_gradebook = [["politics", 80], ["latin", 96], ["dance", 97], ["architecture", 65]]

# Your code below: 
# Subject and grades for eaxh class
subjects = ["physics", "calculus", "poetry", "history"]
grades = [98, 97, 85, 88]
# list of Classes and the grades they got in that  class
gradebook = [[subjects[0], grades[0]], [subjects[1], grades[1]], [subjects[2], grades[2]], [subjects[3], grades[3]]]

print(gradebook)
#adding two more lists of the subject and grades to the grade book
gradebook.append(["computer science", 100])
gradebook.append(["visual arts", 93])
# changing visual arts grade because they said there was an error grading and everyone got 5 points
gradebook[-1][-1] = 98
# removed the grade for poetry and changed it to pass and fail 
gradebook[2].remove(85)
gradebook[2].append("Pass")
# combined this semesters gradebook with last semester to create a full gradebook
full_gradebook = last_semester_gradebook + gradebook

print(full_gradebook)