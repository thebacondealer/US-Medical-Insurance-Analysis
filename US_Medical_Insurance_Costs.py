import csv

insurance_records = {} #1338 records
ages = []
sexes = []
bmis = []
children = []
smoking_statuses = []
regions = []
charges = []
with open('insurance.csv', 'r', newline='') as insurancefile:
    insurance_reader = csv.DictReader(insurancefile)
    record_list = []
    for row in insurance_reader:
        record_list.append(row)
        ages.append(row['age'])
        sexes.append(row['sex'])
        bmis.append(row['bmi'])
        children.append(row['children'])
        smoking_statuses.append(row['smoker'])
        regions.append(row['region'])
        charges.append(row['charges'])
    for i in range(1, len(record_list)+1):
        insurance_records[i] = record_list[i-1]

def calculate_average_age(ages):
    total_ages = 0
    for age in ages:
        total_ages += int(age)
    average_age = total_ages / len(ages)
    return average_age
average_age = calculate_average_age(ages)

def calc_average_M_age()

def calc_average_charge(charges):
    total_charges = 0
    for charge in charges:
        total_charges += charge
    average_charge = total_charges / len(charges)
    return average_charge
average_charge = calc_average_charge(charges)

def count_locations(regions):
    counted_locations = {}
    for location in regions:
        if location not in counted_locations:
            counted_locations[location] = 1
        else:
            counted_locations[location] += 1
    return counted_locations
counted_locations = count_locations(regions)

def count_sexs(sexs):
    num_males = 0
    num_females = 0
    for person in sexs:
        if person == 'male':
            num_males += 1
        else:
            num_females += 1
    return num_males, num_females
num_males, num_females = count_sexs(sexes)
#print(f"Num of Males: {num_males}") #676
#print(f"Num of Females: {num_females}") #662

def calc_smoker_costs_dif():