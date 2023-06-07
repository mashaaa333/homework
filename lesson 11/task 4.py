def calculator():
    try:
        numbers = input("Input your numbers:\t").split()
        numbers = [int(num) for num in numbers]
        if len(numbers) < 2:
            return None
        answer = numbers[0] * numbers[-1]
        return answer
    except ValueError:
        return None
    except IndexError:
        return None
answer = calculator()
if answer is None:
    print("Error. try agian")
else:
    print("Answer is:\t", answer)