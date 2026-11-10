option = input("Do you want to shutdown your computer. ")

def shutdown(choice):
    if choice == "yes".lower().strip():
        print("Shutting computer down...")
    elif choice == "no".lower().strip():
        print("Aborting shutdown")
    else:
        print("Please use a valid input (yes/no) please.")
        shutdown(choice)

shutdown(option)
