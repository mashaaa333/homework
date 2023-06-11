alphabet = "abcdefghijklmnopqrstuvwxyz"
choice = int(input("Input 1 if you want to decipher, input 0 if you want to encrypt"))

if choice == 1:
    word = input("Enter word:\t")
    word_low = word.lower()
    answer = ""

    for letter in word_low:
        position = alphabet.find(letter)
        if position != -1:
            new_position = (position - 3) % len(alphabet)
            answer += alphabet[new_position]
        else:
            answer += letter

    print("deciphered word:\t", answer)

else:
    word = input("Enter word:\t")
    word_low = word.lower()
    answer = ""

    for letter in word_low:
        position = alphabet.find(letter)
        if position != -1:
            new_position = (position + 3) % len(alphabet)
            answer += alphabet[new_position]
        else:
            answer += letter


    print("encrypted word:\t", answer)
