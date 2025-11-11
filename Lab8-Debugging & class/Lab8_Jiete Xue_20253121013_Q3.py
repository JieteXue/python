class Student:
    def __init__ (self,name,student_id, *scores):
        self.name = name
        self.student_id = student_id
        self.scores = list(scores)

    def average(self):
        if len(self.scores) == 0:
            return None
        return sum(self.scores) / len(self.scores)
    
    def __str__(self):
        return f"Student ID: {self.student_id}\tName: {self.name}\tScores: {self.scores}"



class Class:
    def __init__(self,students):
        self.students = students
    
    def enroll_student(self,student):
        self.students.append(student)

    def size(self):
        return len(self.students)
    
    def highest_score_student(self):
        highest_score = 0
        highest_score_student = None
        for student in self.students:
            if student.average() == None:
                continue
            if student.average() > highest_score:
                highest_score = student.average()
                highest_score_student = student
        return highest_score_student
    
    def is_student_enrolled(self,student_id):
        for student in self.students:
            if student.student_id == student_id:
                return True
        return False

if __name__ == "__main__":
    s1=Student('John Smith', 100001)
    print(s1) # 100001 John Smith
    print(s1.average()) # None
    s2=Student('Mary Harper', 100002, 100, 90.5, 75)
    print(s2) # 100002 Mary Harper 100 90.5 75
    print(s2.average()) # 88.5

    s1=Student('John', 100001, 70)
    s2=Student('Mary', 100002, 90.5, 75)
    class1 = Class([s1, s2])
    print(class1.size()) # 2
    print(class1.highest_score_student()) # 100002 Mary Harper 90.5 75
    s3=Student('Jack', 100005, 95, 80)
    class1.enroll_student(s3)
    print(class1.size()) # 3
    print(class1.is_student_enrolled(100005)) # True
    print(class1.is_student_enrolled(100007)) # False

