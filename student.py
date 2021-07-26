#TASK 2
#base class representing a student.
#As a minimum a student has a name and age and a unique ID.
#New subclass from student representing a concrete student doing a specialization e.g. Software Student and Data Science student.

class Student:
    def __init__(self, name, age, id, assigned_instructor):
        self.name = name
        self.age = age
        self.id = id
        self.instructor = assigned_instructor
        self.subjects = dict()

# class CFGStudent(<should inherit from Student>)
#     create new methods that manage student's subjects (add/remove new subject and its grade to the dict)
#     create a method to view all subjects taken by a student
#     create a method  (and a new variable) to get student's overall mark (use average)

class CFGStudent(Student):
    def __init__(self, name, age, id, assigned_instructor, specialisation_stream): #all from base + the specialisation parameter for subclass
        super().__init__(name, age, id, assigned_instructor) #from the base
        self.specialisation_stream = specialisation_stream #data or software
        self.average_mark = 0 #setting to 0

    def add_subject_grade(self, subject, grade):
        self.subjects[subject] = grade #adding a subject and its grade to the dict
        #Dictionary_Name[New_Key_Name] = New_Key_Value

    def remove_subject(self, subject):
        del self.subjects[subject] #delete given subject (key) and its associated grade (value)

    def view_subjects(self):
        print(self.subjects) #printing contents of the dictionary

    def get_average_mark(self):
        self.average_mark = sum(self.subjects.values())/ len(self.subjects) #calculating the mean- total marks (values) divided by number of subjects
        print(self.average_mark) #print result

#experimenting
Karan = CFGStudent('karan', 21, 1234, 'Aleena', 'Software')
Karan.add_subject_grade('Object oriented programming', 72)
Karan.add_subject_grade('OOP 2', 68)
Karan.add_subject_grade('Classifications', 67)
Karan.view_subjects()
Karan.get_average_mark()
Karan.remove_subject('Classifications')
Karan.view_subjects()



