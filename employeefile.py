import uuid

class Role:
    all_ = []
    
    def __init__(self, id_, name):
        self.id = id_
        self.name = name
        self.all_.append(self)
        
    @classmethod
    def find_role_by_id(cls, role_id):
        for role_obj in cls.all_:
            if role_obj.id == role_id:
                return role_obj
        
    def __repr__(self):
        return f"<[{self.id}] | {self.name}>"

class Employee:
    all_ = []
    
    def __init__(self, first_name, last_name, role_id=3):
        self.id = uuid.uuid4().hex
        self.first_name = first_name
        self.last_name = last_name
        self.email = f'{self.first_name}{self.last_name[0]}@codingtemple.com'.lower()
        self.posts = []
        self.role = Role.find_role_by_id(role_id)
        self.all_.append(self)
        
    @classmethod
    def get_employee_by_email(cls, get_employee_by_email):
        for emp in cls.all_:
            if emp.email == get_employee_by_email:
                return emp
        
    def create_post(self):
        # Administrators are only ones whom CANNOT create posts
        if self.role.id != 1:
            post_body = input('Create a new post: ')
            new_post = Post(post_body, self.email)
            self.posts.append(new_post)
        else:
            input('Sorry, Administrator do not have Post priveleges')
        
    def __repr__(self):
        return f'<Employee: ({self.email})>'
    
class Manager(Employee):
    # regarldress of inheritance, this is what we're passing to our new instance
    def __init__(self, first_name, last_name, role_id=2, employees=[]):
        # super() function represents all initialization logic from the parent class' __init__ method
        super().__init__(first_name, last_name, role_id)
        # if there is no list of employees being passed to the instantion of our class
        if employees is None:
            # will set with it to an empty list
            self.employees = []
        else:
            # otherwise set it equal to whatever datatype collection is passed
            self.employees = employees
            
    def add_employee(self, emp_object):
        if emp_object not in self.employees:
            self.employees.append(emp_object)
            
    def remove_employee(self, email_address):
        for emp in self.employees:
            if emp.email == email_address:
                self.employees.remove(emp)
                return
        return 'Employee not Found'
        
    
    def show_employees(self):
        for idx, emp_object in enumerate(self.employees):
            print(f'{idx+1}: {emp_object.first_name} {emp_object.last_name} ({emp_object.email})')
        

class Supervisor(Manager):
    def __init__(self, first_name, last_name, role_id=1, employees=[]):
        super().__init__(first_name, last_name, role_id, employees)

class Post:
    all_ = []
    
    def __init__(self, body, employee_email):
        self.id = uuid.uuid4().hex
        self.body = body
        self.employee = Employee.get_employee_by_email(employee_email)
        self.all_.append(self)
        
    def __repr__(self):
        return f'<Post: [{self.employee.email}] {self.body}>'