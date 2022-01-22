import csv

# creating an internal data set from CSV file for data analysis
insurance_costs = []
with open('insurance.csv') as csv_info:
    insurance_info = csv.DictReader(csv_info)
    for row in insurance_info:
        insurance_costs.append(row)


# Changing from a list to a dictionary
insurance_dict = {}
for i, d in enumerate(insurance_costs):
    insurance_dict[i] = d

# print(insurance_dict)


# print(insurance_costs)

# Sections for creating functions and classes

# Function for extracting the average, min, and max of a dictionary key with numerical values:
def average_for_variable(dictionary, key_var):
    total_of_var = 0
    total_num = len(dictionary)
    test_var = key_var
    max = 0
    min = float('inf')
    for i in range(len(dictionary)):
        for key in dictionary[i].keys():
            if key == key_var:
                total_of_var += float(dictionary[i][key_var])
                if float(dictionary[i][key_var]) > max:
                    max = round(float(dictionary[i][key_var]),2)
                elif float(dictionary[i][key_var]) < min:
                    min = round(float(dictionary[i][key_var]),2)
    average_for_var = round(total_of_var / total_num, 2)
    data = "The average value of {test_var} is : {average_for_var}, The minimum value is: {min}, and the maximum value " \
           "is: {max} "
    return data.format(test_var = test_var, average_for_var = str(average_for_var), min = str(min), max = str(max))




# Function for determining the % composition of variables:

def proportion_of_population(dictionary, key_var):
    rate_dictionary = {}
    for i in range(len(dictionary)):
        for key in dictionary[i].keys():
            if key == key_var:
                option = (dictionary[i][key_var])
                if option in rate_dictionary.keys():
                    rate_dictionary[option] += 1
                else:
                    rate_dictionary[option] = 1
                percent_val = str(round(rate_dictionary[option]/len(dictionary)*100, 2))

                rate_dictionary[option + " %"]= percent_val
    return rate_dictionary




# Linear regression function for all variables:

# clumping function from package to be built into class:

# class that takes a csv dictionary and runs basic functions on it.
# Data analysis:

# Basic overview of costs/demographics:
# average cost
average_cost = average_for_variable(insurance_dict, "charges")

# average age
average_age = average_for_variable(insurance_dict, 'age')
print(average_age)

# average bmi
average_bmi = average_for_variable(insurance_dict, 'bmi')
print(average_bmi)

# average amount and range of children
average_children = average_for_variable(insurance_dict, 'children')
print(average_children)

# smoker demographics
smoker_proportions = proportion_of_population(insurance_dict, "smoker")
print(smoker_proportions)

# gender demographics
gender_proportions = proportion_of_population(insurance_dict, "sex")
print(gender_proportions)

# region demographics
region_proportions = proportion_of_population(insurance_dict, "region")
print(region_proportions)





