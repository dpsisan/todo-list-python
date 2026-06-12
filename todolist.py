## current working directory
import os
print("cwd :")
print(os.getcwd())


tasks = []

try:
     with open("todolist_file.txt","r") as file:
          tasks = file.read().splitlines()
except FileNotFoundError:
     pass

while True:
      print("\n------ TO DO List----")
      print("1. Add tasks")
      print("2. View tasks")
      print("3. Remove tasks")
      print("4. Exit")

      choice = input("enter your choice: \t")
      
      if choice == "1":
            task = input("Enter task: ")
            tasks.append(task)
            
            with open("todolist_file.txt", "a") as file:
                   file.write(task + "\n")
                  
                   print("Task written successfully")
            
        
      elif choice == "2":
            if len(tasks)==0:
                  print("No tasks to view")
            else:
                  print("\n Your to do tasks are :")
                  for i, task in enumerate(tasks, start=1):
                        print(f"{i}. {task}")
        
      elif choice == "3":
            if len(tasks)==0:
                  print("No tasks to remove")
            else:
                  for i, task in enumerate(tasks, start=1):
                        print(f"{i}. {task}")

                  try:
                         num = int (input("enter task number to remove : "))


                         if 1 <= num <= len(tasks):
                           removed = tasks.pop(num -1)
                         #rewirte the updated tasks 

                           with open("todolist_file.txt", "w") as file:
                               for task in tasks:
                                     file.write(task +"\n")
                               print(f"Removed: {removed}")
                      
                         else:
                           print("invalid task number")
                  except ValueError:
                       print("neter valid info")
      elif choice =="4":
         print("goodbye.")
         break

      else: 
            print("Invalid choioce // GIT check")
     