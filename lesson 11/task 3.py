def read_file(your_file):
    try:
        with open(your_file, 'r') as file:
            filecontent = file.read()
            return filecontent
    except FileNotFoundError:
        return None