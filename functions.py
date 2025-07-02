FILEPATH = "todos.txt"
def get_todos(filepath=FILEPATH):
    """fetching & storing existing todos in todos list"""
    with open(filepath, 'r') as file_local:
        todos_local = file_local.readlines()
        return todos_local

def write_todos(todos_arg,filepath=FILEPATH):
    """writes the changed list into the .txt file"""
    with open(filepath, 'w') as file:
        file.writelines(todos_arg)
