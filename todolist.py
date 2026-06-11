tasks = []

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
            print("task added :) ")
        
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
                  num = int (input("enter task number to remove : "))


                  if 1 <= num <= len(tasks):
                        removed = tasks.pop(num -1)
                        print(f"Removed: {removed}")
                  else:
                        print("invalid task number")
        
      elif choice =="4":
         print("goodbye.")
         break
             
      else: 
            print("Invalid choioce")
    