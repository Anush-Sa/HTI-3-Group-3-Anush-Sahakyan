class Employee:
    def __init__(
        self,
        first_name, 
        last_name,
        join_date,
        gender='M',
        phone_number=None,
        trial_passed=False,
        leave_date=None,
        salary=0):

        self.first_name = first_name
        self.last_name = last_name
        self.join_date = join_date
        self.gender = gender
        self.phone_number = phone_number
        self.trial_passed = trial_passed
        self.leave_date = leave_date
        self.salary = salary


    def full_name(self):
        return self.first_name + ' ' + self.last_name
    
    def work_email(self):
        return f'{self.first_name.lower()}.{self.last_name.lower()}@company.com'

    def __repr__(self):
        return f'First Name: {self.first_name} \nLast Name: {self.last_name} \nFull Name: {self.full_name()} \nPhone Number: {self.phone_number} \nWork Email: {self.work_email()} \nTrial Passed: {self.trial_passed} \nJoin Date: {self.join_date} \nLeave Date: {self.leave_date} \nSalary: {self.salary} \nGender(M or F): {self.gender}'


e1 = Employee ('Davit', 'Tovmasyan', '22.02.2018', phone_number='077 12 34 56', trial_passed=True, salary=15000)
e2 = Employee ('Tovmas', 'Davtyan', '11.01.2020', leave_date='25.07.2020', salary=45000)

print(e1)
print('\n')
print(e2)
