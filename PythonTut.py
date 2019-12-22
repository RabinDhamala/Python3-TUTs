class Employee:
    no_of_emps = 0
    raise_amount = 1.04
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'
        Employee.no_of_emps += 1

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def applyraise(self):
        self.pay = int(self.raise_amount * self.pay)

print(Employee.no_of_emps)

def divide:
    return x/y

emp1 = Employee('Hari', 'Khadka', 50000)
emp2 = Employee('Nari', 'Chikari', 60000)
class aafnai_ho:
    sungur = 10

print(Employee.no_of_emps)
