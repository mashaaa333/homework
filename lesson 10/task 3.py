def add_text(new_file, text):
    with open(new_file, 'a') as file:
        file.write()


def display_text_from_file(file_name):
    with open(file_name, 'r') as file:
        contents = file.read()
        print(contents)


new_file = "python.txt"
text_to_add = input("Enter the text to add to the file: ")
add_text(new_file, text_to_add)

display_text_from_file(new_file)