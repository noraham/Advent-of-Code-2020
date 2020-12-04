
##########################    1    ###########################

def convert_input_file_to_int_list(file_name):
    input_as_list = []
    with open(file_name) as file: 
        for line in file:
            input_as_list.append(int(line.strip()))
    return input_as_list


def day_one():
    """
    find the two entries that sum to 2020,
    then multiply those two numbers together
    """
    input_as_list = convert_input_file_to_int_list('input/day_one_input.txt')
    cursor = 0
    for num1 in input_as_list[cursor:]:    
        for num2 in input_as_list[cursor + 1:]:
            if num1 + num2 == 2020:
                return num1 * num2

def day_one_part_two():
    """
    what is the product of the three entries that sum to 2020
    """
    input_as_list = convert_input_file_to_int_list('input/day_one_input.txt')
    cursor = 0
    for num1 in input_as_list[cursor:]:    
        for num2 in input_as_list[cursor + 1:]:
            for num3 in input_as_list[cursor + 1:]:
                if num1 + num2 + num3 == 2020:
                    return num1 * num2 * num3
                cursor + 1
    
##########################    2    ###########################

def day_two():
    """
    How many passwords are valid according to their policies?
    min-max x: password
    """
    valid_pword_count = 0
    with open('input/day_two_input.txt') as file:
        for line in file:
            policy, pword = line.split(':')
            pword = pword.strip()
            span, target_letter = policy.split(' ')
            minimum, maximum = span.split('-')
            minimum = int(minimum)
            maximum = int(maximum)
            count = pword.count(target_letter)
            if count:
                if count >= minimum and count <= maximum:
                    valid_pword_count += 1
    return valid_pword_count

def day_two_part_two():
    """
    How many passwords are valid according to the new interpretation of the policies
    """
    valid_pword_count = 0
    with open('input/day_two_input.txt') as file:
        for line in file:
            policy, pword = line.split(':')
            pword = pword.strip()
            places, target_letter = policy.split(' ')
            place_1, place_2 = places.split('-')
            index_1 = int(place_1) - 1
            index_2 = int(place_2) - 1
            if pword[index_1] == target_letter and pword[index_2] != target_letter:
                valid_pword_count += 1
            elif pword[index_2] == target_letter and pword[index_1] != target_letter:
                valid_pword_count += 1
    return valid_pword_count


if __name__ == "__main__":
    print(day_two_part_two())
