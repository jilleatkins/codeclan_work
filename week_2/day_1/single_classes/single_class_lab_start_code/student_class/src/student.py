# 1
# class TestStudent(unittest.TestCase):
#     def setUp(self):
#         self.student = Student("Ada", "E42")

class Student:
    
    def __init__(self, input_name, input_cohort):
        self.name = input_name
        self.cohort = input_cohort
    

    def talk(self):
        return "I can talk!"

    def say_favourite_language(self, language):
        return "I love " + language

    
