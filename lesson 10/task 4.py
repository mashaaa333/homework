def create_story():
    file_name = "story.txt"
    content = input("Tell me a story: ")
    with open(file_name, 'w') as file:
        file.write(content)
def display_words():
    file_name = "story.txt"

    with open(file_name, 'r') as file:
        for line in file:
            words = line.split()
            for word in words:
                if len(word) < 4:
                    print(word)

create_story()
display_words()