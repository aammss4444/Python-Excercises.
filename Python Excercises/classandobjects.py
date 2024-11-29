# 1. Create a sample class named Employee with two attributes id and name
# employee :
#     id
#     name

class employee:
  
   def __init__ (self, id, name):
     self.id = id
     self.name = name

   def display(self):
    print(f"ID: {self.id} \nName: {self.name}")

emp = employee(1, "coder")
emp.display()

# 2. Use del property to first delete id attribute and then the entire object

del emp.id


  