import glob

name_input = input('Input your desired name: ')
sex_input = input('Input your desired sex (M or F): ')

# Opens file location.
Names = open('NamesF/yob1880.txt', 'r')

# Gives us all of the files inside of NamesF. (* = everything)
file_list = glob.glob('NamesF/*.txt')

# Tells us the number of files that are inside of the NamesF folder.
file_length = len(file_list)

# MY LISTS
popular = []
ultimate_list = []
year_list = []
final_input = []
input_occurrences = []

# Opens and iterates over file names.
for i in range(file_length):
    file_name = file_list[i]
    separate = file_name.strip().split('.')

    # Takes the year number from file name.
    year = int(separate[0].split('.')[0][10:15])

    # I used the file names and open function to open files in NamesF.
    file_open = open(file_name, 'r')

    # Then we read over the files and grab the file length.
    files_list = file_open.readlines()
    yob_file_length = len(files_list)

    # My lists containing numbers and inputs.
    number_name_occurrences = []
    input_list = []

    # I iterate over the length of every yob file.
    for j in range(yob_file_length):
        line = files_list[j]

        # Separated lines by the commas.
        separate = line.strip().split(',')
        name = separate[0]
        sex = separate[1]
        number = int(separate[2])

        # I put the numbers from the lines in the number_list.
        number_name_occurrences.append(number)

        # I apply the inputs requirements to the lines (exclusive to just the number) and its put in the input_list.
        if name == name_input and sex == sex_input:
            input_list.append(number)
            year_list.append(year)
            input_occurrences.append(number)

    # This sums up everything in the number_list.
    occurrences = sum(number_name_occurrences)

    # This is so we can use the values in input_list as integers.
    for k in range(len(input_list)):
        popularity_percentage = (input_list[k] / occurrences) * 1000  # POPULARITY PERCENTAGE
        popular.append(popularity_percentage)
        # Appending all of my values into a list.
        ultimate_list.append([year, occurrences, input_list[k], '%.2f' % popularity_percentage])

        final_input.append(input_list[k])

# Function for
def average(x):
    result = sum(x)/len(x)
    return result


x = year_list
y = popular
y2 = input_occurrences
# Length of my list
N = len(x)

x_avg = average(x)
y_avg = average(y)
y_avg2 = average(y2)

numerator = 0
numerator2 = 0
denominator = 0

for i in range(N):
    numerator += (x[i] - x_avg) * (y[i] - y_avg)
    numerator2 += (x[i] - x_avg) * (y2[i] - y_avg2)
    denominator += (x[i] - x_avg)**2
m = numerator / denominator
m2 = numerator2 / denominator

b = y_avg - m * x_avg
b2 = y_avg2 - m2 * x_avg

SSN_Data = [[name_input, m2, b2, m, b]]

Names.close()

with open("namedata.txt", "w") as f:
    for line in ultimate_list:
        f.write(','.join([str(item) for item in line]))
        f.write("\n")

with open("SSN_Data.txt", "w") as f:
    for line in SSN_Data:
        f.write(','.join([str(item) for item in line]))
        f.write("\n")

print(SSN_Data)
