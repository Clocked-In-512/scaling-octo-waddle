##Robert Fernandez
##Complete
##This program will input employee work infromation and output the information in a table format.

class Employee:
    def __init__(self, name, id_number, department, job_title):
        self.__name = name
        self.__id_number = id_number
        self.__department = department
        self.__job_title = job_title

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    def get_id_number(self):
        return self.__id_number

    def set_id_number(self, id_number):
        self.__id_number = id_number

    def get_department(self):
        return self.__department

    def set_department(self, department):
        self.__department = department

    def get_job_title(self):
        return self.__job_title

    def set_job_title(self, job_title):
        self.__job_title = job_title

    def __str__(self):
        return (f"Name: {self.__name}\n"
                f"ID Number: {self.__id_number}\n"
                f"Department: {self.__department}\n"
                f"Job Title: {self.__job_title}\n")

if __name__ == '__main__':
    employees = []
    for i in range(3):
        name = input(f"Enter employee name:")
        id_number = input(f"Enter employee ID:")
        department = input(f"Enter department:")
        job_title = input(f"Enter position:")
        employee = Employee(name, id_number, department, job_title)
        employees.append(employee)
    
    for emp in employees:
        print(emp)
