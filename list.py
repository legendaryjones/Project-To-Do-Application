#In this project, you will build a functional To-Do List Application using Python from scratch. 

#Build a simple Command Line Interface (CLI) that welcomes users and displays a menu with options to add, view, delete tasks, or quit the application.The tasks should be stored in a Python list

# Welcome 



def print_task(task_list):
    if task_list:
        print("Current task list:")
        for item in task_list:
            print(item)
    else: 
        print("Your task list is currently empty.")

def manage_tasks():
    task_list = []
    
    while True:
        action = input("Hello, I'm here to help you get organized! Let's get started with your task list.\nEnter add, view, delete, or quit: ").lower()
        
        try: 
            if action == 'add':
                item = input("Enter the item you want to add: ")
                task_list.append(item)
                print(f"{item} has been added to your task list.")
        
            elif action == 'delete':
                item = input("Enter the item you want to delete: ")
                if item in task_list:
                    task_list.remove(item)
                    print(f"{item} has been removed from your task list.")
                else:
                    print(f"{item} does not exist in your list.")
        
            elif action == 'view':
                print_task(task_list) 
            
            elif action == 'quit':
                print("Here is your complete list:")
                print_task(task_list)
                break
         
            else:
                print("Invalid menu option, please enter add, view, delete, or quit.")
          
        except ValueError as e:  
            print(f'Error: {e}')
            
manage_tasks() 


#    elif user_input == 2:
#     print("{task}")
#    elif user_input == 3:
#     print("Which task would you like to delete? {task}")
#    elif user_input == 4: 
#     break
#    else: ("Invalid choice, please enter a number 1-4")


# def main_menu(): 
#     task = []
#     if input == 1: 
#      return('Please enter a task')

    #if task is empty print empty
    # if main_menu ==2: 
    #     print ('task')

    #     if main_menu == 3: 
    #         task.remove()

    #     elif main_menu == 4: 
    #         print ("Thank you! I'm here if you need me\n")
    # main()






















































