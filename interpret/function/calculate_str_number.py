import re


def calculate_str(char_str):
    #exact number
    numbers = re.findall(r'\d', char_str)
    # calculate len
    total_length = sum(len(num) for num in numbers)
    return total_length


def calulate_eval(char_str):

    numbers=len(eval(char_str))
    return numbers



if __name__ == "__main__":

    A = "[2,3]"
    total_length=calulate_eval(A)
    B=eval(A)
    print(total_length)



