def write_file(file_name, file_content):
    file_name = str(file_name) + ".txt"

    with open(file_name, mode="w") as file_name:
        file_name.write(file_content)

def append_file(file_name, append_content):
    file_name = str(file_name) + ".txt"

    with open(file_name, mode="a") as file_name:
        file_name.write(append_content)


def read_file(file_name):
    file_name = str(file_name) + ".txt"

    with open(file_name, mode="r") as file_name:
        file_content = file_name.read()

    return file_content
