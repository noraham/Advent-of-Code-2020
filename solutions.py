
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

##########################    3    ###########################

def calc_trees_encountered(slope):
    trees_encountered = 0
    cursor = 0
    index_of_last_value = 30
    x_step, y_step = slope
    with open('input/day_three_input.txt') as file:
        for line_num, line in enumerate(file, 0):
            if line_num % y_step == 0:
                row = line.strip()
                if cursor > index_of_last_value:
                    cursor -= 31
                if row[cursor] == '#':
                    trees_encountered += 1
                cursor += x_step
    return trees_encountered


def day_three():
    """
    Starting at the top-left corner of your map and following a slope of 
    right 3 and down 1, how many trees would you encounter?
    """
    given_slope = (3, 1)
    return calc_trees_encountered(given_slope)

def day_three_part_two():
    """
    What do you get if you multiply together the number of trees encountered
    on each of the listed slopes?
    Right 1, down 1.
    Right 3, down 1. (This is the slope you already checked.)
    Right 5, down 1.
    Right 7, down 1.
    Right 1, down 2.
    """
    given_slopes = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
    product = 1
    for slope in given_slopes:
        trees_encountered = calc_trees_encountered(slope)
        product = product * trees_encountered
    return product

















if __name__ == "__main__":
    print(day_three_part_two())
