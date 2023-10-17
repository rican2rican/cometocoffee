from colorama import Fore, Back, Style, init
import os
import pickle


init(autoreset=True)



schedule = {
    "03:45 AM - Wake up": None,
    "04:00 AM - Get ready and have a quick breakfast": None,
    "04:30 AM - Prepare for basketball": None,
    "05:00 - 07:00 AM - Basketball Practice": None,
    "08:00 AM - 09:00 AM - Write morning pages": None,
    "09:00 AM - 09:07 AM - 7 minute drill": None,
    "09:07 AM - 09:37 AM - Write a verse": None,
    "09:45 AM - 11:45 AM - Online math school": None,
    "12:00 PM - 02:00 PM - Coding practice": None,
    "02:00 PM - 03:00 PM - Lunch and relaxation": None,
    "03:00 PM - 04:30 PM - Engage in the CS50 course": None,
    "04:30 PM - 04:37 PM - 7 minute drill": None,
    "04:37 - 5:07 PM - Write another verse": None,
    "05:15 PM - 07:15 PM - Coding practice": None, 
    "07:30 PM - 08:30 PM - Reading and leisure time": None,
    "08:30 PM - Begin winding down and preparing for bed": None,
    "09:00 PM - Lights out and sleep": None,
}


def display_schedule():
    os.system('clear')
    print(Fore.GREEN + "===Your Daily Schedule ===")
    for task, status in schedule.items():
        if status:
            print(f"{Fore.CYAN}{task} - {Fore.RED}Completed")
        else:
            print(f"{Fore.CYAN}{task} - {Fore.YELLOW}Pending")
                  


def complete_task(task_index):
    task = list(schedule.keys())[task_index]
    schedule[task] = "Completed"
    display_schedule()



    def main():
        while True:
            display_schedule()
            print(Fore.GREEN + "\nOptions:")
            print("1. Mark a task as completed")
            print("0. Exit")
            choice = input("Enter your choice:")


            if choice == "1":
                try:
                    task_index = int(input("Enter the task index to mark as completed: "))
                    if 0 <= task_index < len(schedule):
                        complete_task(task_index)
                    else:
                        print(Fore.RED + "Invalid task index. Please try again.")
                except ValueError:
                    print(Fore.RED + "Invalid input. Please enter a valid task index.")
            elif choice == "0":
                break
            else:
                print(Fore.RED + "Invalid choice. Please try again.")        
    if __name__ == "__main__":
        main()

