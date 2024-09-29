
1.
class Student:
    
    def __init__(self, name = "Вася", surname = "Пупкин", age = 16, grade = 11, marks_count = 3, marks = [5, 5, 5]):
        self.name = name
        self.surname = surname
        self.age = age
        self.grade = grade
        self.marks_count = marks_count
        self.marks = marks
        
    def show(self):
        print(self.name, self.surname, self.age, self.grade, self.marks_count)
        print(*self.marks)
        
def read_student():
    name, surname, age, grade, marks_count = input().split()
    marks = list(map(int, input().split()))
    s = Student(name, surname, age, grade, marks_count, marks)
    return s
    
def print_all_students(students_journal):
    for i in students_journal:
        i.show()
        
def main():    
    ls = []
    for i in range(5):
        s = read_student()
        if i != 4:
            enter = input()
        ls.append(s)
    print_all_students(ls)
    
if __name__ == '__main__':
    main()

2.
class Student:
    
    def __init__(self, name = "Вася", surname = "Пупкин", age = 16, grade = 11, marks_count = 3, marks = [5, 5, 5]):
        self.name = name
        self.surname = surname
        self.age = age
        self.grade = grade
        self.marks_count = marks_count
        self.marks = marks
        
    def show(self):
        print(self.name, self.surname, self.age, self.grade, self.marks_count)
        print(*self.marks)
        
    def get_average_mark(self):
        return sum(self.marks) / len(self.marks)
        
def read_student():
    name, surname, age, grade, marks_count = input().split()
    marks = list(map(int, input().split()))
    s = Student(name, surname, age, grade, marks_count, marks)
    return s
    
def print_all_students(students_journal):
    for i in students_journal:
        i.show()
        
def main():    
    ls = []
    for i in range(5):
        s = read_student()
        if i != 4:
            enter = input()
        ls.append(s)
    for s in ls:
        m = s.get_average_mark()
        print(f"{m:.6f}")
    
if __name__ == '__main__':
    main()
