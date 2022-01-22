import csv

with open('insurance.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file)
    number_patients = 0 - 1 #-1 for the header
    fields = []
    patients_list = []

    # Iterate through csv_reader and append to patient_list
    for row in csv_reader:
        if number_patients == -1:
            fields += row       # apppend the header into fields list
            number_patients += 1
        else:
            patients_list.append(row)
            number_patients += 1
print(patients_list)