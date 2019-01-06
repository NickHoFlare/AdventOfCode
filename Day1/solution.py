# Helper functions
def prepare_input(path):
    input_file = open(path, 'r')
    input = input_file.readlines()

    return input

# Solution start
input_path = "./input.txt"
input = prepare_input(input_path)
frequency = 0
freq_dict = {frequency: 1}
first_duplicate_freq = 13371337
first_duplicate_found = False

while first_duplicate_found is False:
    for line in input:
        line = line.strip()
        line_operator = line[0]
        line_value = line[1:]
        
        #print("Current line is " + line)

        if line_operator == '+':
            frequency += int(line_value)
        elif line_operator == '-':
            frequency -= int(line_value)
        else:
            print("Unrecognised operator, quitting.")
            break
        #print("frequency is now " + str(frequency))

        if frequency in freq_dict:
            #print("Seen you before: " + str(frequency))
            if first_duplicate_found is False:
                first_duplicate_freq = frequency
                first_duplicate_found = True

            freq_dict[frequency] += 1
            # print("found a duplicate, " + str(frequency))
        else:
            freq_dict[frequency] = 1

print("==> Final frequency is " + str(frequency))
print("==> First duplicate frequency is " + str(first_duplicate_freq))