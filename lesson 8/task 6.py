original_dict = {1: "red",
                 2: "green",
                 3: "black",
                 4: "white",
                 5: "black"}
length_dict = {value: len(value) for value in original_dict.values()}

print("Original Dictionary:", original_dict)
print("Length of dictionary values:", length_dict)