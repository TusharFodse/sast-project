import os

def unsafe_function():
    user_input = input("Enter filename: ")
    os.system("cat " + user_input)  # Command Injection

if __name__ == "__main__":
    unsafe_function()
