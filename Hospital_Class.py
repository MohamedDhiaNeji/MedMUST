class Hospital:
  def __init__(self, name, list_of_departments):
    self.name = name
    self.list_of_departments = list_of_departments
    
  def show_departments(self):
    print("These are the available departments:")
    for dep in self.list_of_departments:
      print(dep.name)
    print("============================")

  def add_department(self, new_dep_name):
    new_dep_instance = Department(new_dep_name, 0)
    self.list_of_departments.append(new_dep_instance)


  def remove_department (self, old_department):
    for dep in self.list_of_departments:
      if old_department == dep.name:
        self.list_of_departments.remove(dep)


  def find_department_by_name(self):
    self.show_departments()
    user_dep = str(input('choose your department:'))
    for dep in self.list_of_departments:
      if dep.name == user_dep:
        return dep
