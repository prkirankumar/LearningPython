from datetime import datetime

class Employee:
    EMPLOYEES_GRADES = {
        'A': '2500',
        'B': '3000',
        'C': '3500',
        'D': '4000'
    }

    def __init__(self, first_name, last_name, grade):
        self.first_name = first_name
        self.last_name = last_name

        print("This is from constructor")
        if grade not in Employee.EMPLOYEES_GRADES:
            raise KeyError(f"Wrong employee grade. Available grades: {list(Employee.EMPLOYEES_GRADES)}")
        self.salary = Employee.EMPLOYEES_GRADES[grade]


    def show_employee_information(self):
        print('Employee information:')
        print(f"\tName: {self.first_name} {self.last_name}\n\tSalary: {self.salary}")

    @classmethod
    def show_grades(cls):
        print('Employees grades:')
        # Employee.EMPLOYEES_GRADES.items() == cls.EMPLOYEES_GRADES.items()
        for grade, salary in cls.EMPLOYEES_GRADES.items():
            print(f'\t {grade}: {salary}')

    @classmethod
    def add_grade(cls, grade, salary):
        # Employee.EMPLOYEES_GRADES[grade] == cls.EMPLOYEES_GRADES[grade]
        cls.EMPLOYEES_GRADES[grade] = salary

    @classmethod
    def from_string(cls, text):
        first_name, last_name, grade = text.split(';')
        # cls(first_name, last_name, grade) == Employee(first_name, last_name, grade)
        return cls(first_name, last_name, grade)

    @staticmethod 
    def show_manager_name(): # we won't use self/cls , this is like a normal simple method
        print('The manager is Srinivas')

Employee.show_manager_name()
employee_2 = Employee.from_string('fName;lName;C')
employee_2.show_manager_name()
print('----------')
Employee.show_manager_name()


# example 2

class CustomDate:
    def __init__(self, day, month, year):
        self.date_validation(day, month, year) # invoking static method

        self.day = day
        self.month = month
        self.year = year

    def __repr__(self):
        # day = self.day
        # month = self.month
        # if self.day < 10:
        #     day = f'0{day}'
        # if self.month < 10:
        #     month = f'0{month}'
        # return f'{day}-{month}-{self.year}'
        date = datetime(self.year, self.month, self.day)
        return date.strftime('%d-%m-%Y')

    @staticmethod
    def date_validation(day, month, year):
        try:
            datetime(year, month, day)
        except ValueError:
            raise ValueError('Not a valid date!')
    
    @classmethod
    def from_string(cls, string):
        day, month, year = map(int, string.split('-'))
        return cls(day, month, year)

    @classmethod
    def from_file(cls, file):
        array = []
        with open(file, 'r') as text_file:
            text_data = text_file.read().splitlines()
        for date in text_data:
            custom_date_obj = cls.from_string(date)
            array.append(custom_date_obj)
        return array



date_1 = CustomDate(10, 8, 2000)
date_2 = CustomDate(8, 8, 2000)
date_3 = CustomDate(10, 11, 2000)
print(date_1)
print(date_2)
print(date_3)
# date_2 = CustomDate(50, 8, 2000)    # ValueError: Not a valid date!

date_4 = CustomDate.from_string("4-2-2000")
print(date_4)

array_of_dates = CustomDate.from_file('text_file.txt')
print(array_of_dates)