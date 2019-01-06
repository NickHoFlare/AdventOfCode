# def find_resulting_frequency(input_array, frequency):
#     for line in input_array:
#         line = line.strip()
#         line_operator = line[0]
#         line_value = line[1:]
        
#         print("Current line is " + line)

#         if line_operator == '+':
#             frequency += int(line_value)
#         elif line_operator == '-':
#             frequency -= int(line_value)
#         else:
#             print("Unrecognised operator, quitting.")
#             break
#         print("frequency is now " + str(frequency))
#     return frequency

def prepare_input(path):
    input_file = open(path, 'r')
    input = input_file.readlines()

    return input