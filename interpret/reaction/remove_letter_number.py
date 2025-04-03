
import re
def find_non_alphanumeric_positions_and_remove(lst):
    # Find the positions of all elements that are not letters or numbers.
    positions = [i for i, elem in enumerate(lst) if not re.match(r'\w', str(elem))]

    #
    # Generate a new list after removing elements that are not letters or numbers.
    new_list = [elem for i, elem in enumerate(lst) if i not in positions]

    return positions, new_list
def find_and_remove_non_letters(input_string):
    non_letter_positions = []
    clean_string = ""

    for i, char in enumerate(input_string):
        if not char.isalpha():
            non_letter_positions.append(i)
        else:
            clean_string += char

    return non_letter_positions, clean_string


if __name__ == "__main__":
    # Example list.
    lst = ['H', 'e', 'l', 'l', 'o', ',', ' ', 'W', 'o', 'r', 'l', 'd', '!', ' ', '1', '2', '3', '.']
    positions, new_list = find_non_alphanumeric_positions_and_remove(lst)
    print("Positions of non-alphanumeric characters:", positions)
    print("List after removing non-alphanumeric characters:", new_list)

    # Test example.
    input_string = "Hello, World! 123"
    positions, clean_string = find_and_remove_non_letters(input_string)

    print("Positions of non-alphanumeric characters:", positions)
    print("Positions of non-alphanumeric characters:", clean_string)
