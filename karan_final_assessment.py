"""
TASK 1

Design a parent class called CFGStudent.

It should have general attributes like name, surname, age, email, student id
and methods to fetch student’s full name and student’s id.

Design a child class called NanoStudent, which  inherits from CFGStudent class.
This class should have exactly the same attributes as its parent class,
as well as an additional one called ‘specialization’ and course grades.

The child class ‘generate_id’ method should override its parent method to add the suffix ‘NANO’
in front of the id.

New methods ‘add_new_grade’ and ‘get_course_grades’ should be added.
You can use  it as a skeleton code for your classes OR adjust it and create your own.

SEE NOTES BELOW

"""
import random

class CFGStudent:
    def __init__(self, name, surname, age, email, student_id = None):
        self.name = name
        self.surname = surname
        self.age = age
        self.email = email
        self.student_id = self.generate_id()

    @staticmethod
    def generate_id():
        return str(random.randrange(1000, 10000))

    def get_id(self):
        return self.student_id

    def get_fullname(self):
        return "{} {}".format(self.name, self.surname)


class NanoStudent(CFGStudent):
    def __init__(self, name, surname, age, email, specialisation_stream):
        super().__init__(name, surname, age, email, student_id = None)
        self.specialization = specialisation_stream
        self.course_grades = dict()

    @staticmethod
    def generate_id():
        return 'NANO' + str(random.randrange(1000, 10000))

    def add_new_grade(self, assigned_task, mark):
        self.course_grades[assigned_task] = mark

    def get_course_grades(self):
        return self.course_grades

# Example run
s = CFGStudent('Anna', 'Smith', 18, 'anna@mail.com')  # do not pass ID, it should be generated automatically
print(s.get_fullname())

print(s.student_id)
# returns '3868' or some other random number

cfg_s = NanoStudent('Mia', 'Papandopulu', 20, 'mia@mail.com', 'Software')
print(cfg_s.get_fullname())

print(cfg_s.get_id())
# returns 'NANO6180' or some other random number

cfg_s.add_new_grade('theory', 95)
cfg_s.add_new_grade('project', 78)
print(cfg_s.get_course_grades())


"""
TASK 2

Given an index limit, find all corresponding Fibonacci values up to that limit in a sequence 
and return the sum of all even Fibonacci numbers. See more details in the task description in 
your assessment paper. 
"""
def fib(n):
    if n < 2: #0, 1, 1, 2
        return n
    else:
        return (fib(n-1) + fib(n-2)) # last subtract next last

# for n in range(0, 11):
#     print(fib(n)) # double checking seq is right

print(fib(10)) #double checking again

#go through through indexes
#select even numbers
#then add them

def even_fibonacci_sum(limit):
    index = []
    for a in range (limit):
        index.append(a)

    even_no = []
    for i in index:
        if fib(i) % 2 == 0: #should have no remainders if even
            even_no.append(fib(i))
    print('even numbers in index: ', even_no) #double checking
    return sum(even_no)

##### TESTS ####

print(even_fibonacci_sum(limit=10))  # should be 44
print(even_fibonacci_sum(limit=15))  # should be 188
print(even_fibonacci_sum(limit=1))   # should be 0

"""
TASK 3

Validate subsequence. Use suggested tests below to check
correctness of your solution. 
"""
from collections import Counter

def is_valid_subsequence(arr, seq):
    value_count = Counter(arr)  # count of each value
    #print(value_count)
    value_2_count = Counter(seq)
    #print(value_2_count)
    overlapvalues = value_count & value_2_count  # common values
    if overlapvalues == value_2_count:
        return True
    else:
        return False

#### TESTS ####

array1 = [5,1,22,25,6,-1,8,10]
sequence1 = [1,6,-1,-2]

print(is_valid_subsequence(array1, sequence1))  # FALSE


array2 = [5,1,22,25,6,-1,8,10]
sequence2 = [1,6,-1, 10]

print(is_valid_subsequence(array2, sequence2))  # TRUE


array3 = [5,1,22,25,6,-1,8,10]
sequence3 = [25]

print(is_valid_subsequence(array3, sequence3))  # TRUE

"""
TASK 4
Code review task- SOLID principles

Single responsibility - this refers to the principle that a class should have a singular purpose/responsibilty. 
This could be improved in the code by refactoring the responsibilites into separate classes.
For example, printing the employee report is a more unique responsibility compared to the other methods and
could benefit from being separated. 

Open-Closed- this refers to the principle of allowing for extension but discouraging modification. 
To better the code, abstract classes could be implemented which removes the need to modify other classes
which could potentially break the program.
Inheritance could be implemented to modify, for example, the status of an employee. 
Or an abstract class may be implemented to remove the need to modify existing classes, perhaps with the update methods(regarding department and status) or saving and removing as both 
are linked to the DB engine.

Liscov substitution- this refers to the ability to use subtypes interchangeably. Creating subclasses with distinct initialisers could be helpful if there is a need to vary a paramater.

Interface segregation- having a generic overall class for employees may be difficult as it encourages a sense of dependency
on other interfaces that are not required for a specific task. The creation of more subclasses may be beneficial
as it segments useful but related methods.

Dependency injection - making classes based on an abstract class may be beneficial to avoid dependency on lower-level

Implementing some of these recommendations (e.g. child classes and interface segmenting) can avoid the breaking of a program and promote readability and extendability. 

"""