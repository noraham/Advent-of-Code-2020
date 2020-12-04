
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



if __name__ == "__main__":
    print(day_one_part_two())
