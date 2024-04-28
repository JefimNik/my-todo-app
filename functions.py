FILEPATH = "C:\\Users\\jniki\\PycharmProjects\\Todo_app\\programs\\Todo\\todos.txt"


def get_todos(filepath=FILEPATH):
    """read from file    to list     """
    with open(filepath, "r") as file:
        todos = file.readlines()
    return todos


def write_todos(todos, filepath=FILEPATH):
    with open(filepath, "w") as file:
        file.writelines(todos)

