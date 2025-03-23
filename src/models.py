from datetime import datetime
from config import WORK_END_AGE, MAX_WORK_YEARS

class Person:
    def __init__(self, id, name, gender, dob, salary):
        self.id = id
        self.name = name
        self.gender = gender
        self.dob = datetime.strptime(dob, "%Y-%m-%d")
        self.salary = salary

    def get_remaining_work_months(self, current_date):
        age = (current_date - self.dob).days // 30 // 12 
        work_months = min((WORK_END_AGE - age) * 12, MAX_WORK_YEARS * 12)
        return max(work_months, 0)
