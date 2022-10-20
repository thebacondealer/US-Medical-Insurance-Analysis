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
        '''ages.append(row['age'])
        sexes.append(row['sex'])
        bmis.append(row['bmi'])
        children.append(row['children'])
        smoking_statuses.append(row['smoker'])
        regions.append(row['region'])
        charges.append(row['charges'])'''
    for i in range(1, len(record_list)+1):
        insurance_records[i] = record_list[i-1]
for record in insurance_records:
    record_data = insurance_records[record]
    ages.append(int(record_data['age']))
    sexes.append(record_data['sex'])
    bmis.append(float(record_data['bmi']))
    children.append(int(record_data['children']))
    smoking_statuses.append(record_data['smoker'])
    regions.append(record_data['region'])
    charges.append(float(record_data['charges']))

'''def create_dictionary(ages, sexes, bmis, children, smoking_statuses, regions, charges):
    records_dict = {}
    num_of_records = len(ages)
    for index in range(num_of_records):
        records_dict[ages[index]] = {"Age": ages[index],
                                    "Sex": sexes[index],
                                    "BMI": bmis[index],
                                    "Children": children[index],
                                    "Smoking Status": smoking_statuses[index],
                                    "Region": regions[index],
                                    "Charge": charges[index]}
    return records_dict'''


def count_smokers():
    num_smokers = 0
    num_non_smokers = 0
    for i in range(len(insurance_records)):
        if smoking_statuses[i] == 'yes':
            num_smokers += 1
        else:
            num_non_smokers += 1
    return num_smokers, num_non_smokers
num_smokers, num_non_smokers = count_smokers() #274, 1064

def count_sexes(sexes):
    num_males = 0
    num_females = 0
    for person in sexes:
        if person == 'male':
            num_males += 1
        else:
            num_females += 1
    return num_males, num_females
num_males, num_females = count_sexes(sexes) #676, 662

def calculate_average_age(ages):
    total_ages = 0
    for age in ages:
        total_ages += age
    average_age = total_ages / len(ages)
    return average_age
def calc_average_age_male(insurance_records):
    total_male_ages = 0
    for record in insurance_records:
        record_data = insurance_records[record]
        if record_data['sex'] == 'male':
            total_male_ages += int(record_data['age'])
        else:
            continue
    average_male_age = total_male_ages / num_males
    return average_male_age
def calc_average_age_female(insurance_records):
    total_female_ages = 0
    for record in insurance_records:
        record_data = insurance_records[record]
        if record_data['sex'] == 'female':
            total_female_ages += int(record_data['age'])
        else:
            continue
    average_female_age = total_female_ages / num_females
    return average_female_age

def calc_average_charge(charges):
    total_charges = 0
    for charge in charges:
        total_charges += charge
    average_charge = total_charges / len(charges)
    return average_charge
def calc_average_charge_male(insurance_records):
    total_male_charges = 0
    for record in insurance_records:
        record_data = insurance_records[record]
        if record_data['sex'] == 'male':
            total_male_charges += float(record_data['charges'])
        else:
            continue
    average_male_age = total_male_charges / num_males
    return average_male_age
def calc_average_charge_female(insurance_records):
    total_female_charges = 0
    for record in insurance_records:
        record_data = insurance_records[record]
        if record_data['sex'] == 'female':
            total_female_charges += float(record_data['charges'])
        else:
            continue
    average_female_age = total_female_charges / num_females
    return average_female_age
def calc_average_smoker_charge():
    total_smoker_charges = 0
    total_non_smoker_charges = 0
    for i in range(len(insurance_records)):
        if smoking_statuses[i] == 'yes':
            total_smoker_charges += charges[i]
        else:
            total_non_smoker_charges += charges[i]
    average_smoker_charge = total_smoker_charges / num_smokers
    average_non_smoker_charge = total_non_smoker_charges / num_non_smokers
    return average_smoker_charge, average_non_smoker_charge

def count_locations(regions):
    counted_locations = {}
    for location in regions:
        if location not in counted_locations:
            counted_locations[location] = 1
        else:
            counted_locations[location] += 1
    return counted_locations

average_age = calculate_average_age(ages) #39.2
average_male_age = calc_average_age_male(insurance_records) #38.9
average_female_age = calc_average_age_female(insurance_records) #39.5

average_charge = calc_average_charge(charges) #13270.4
average_male_charge = calc_average_charge_male(insurance_records) #13956.75
average_female_charge = calc_average_charge_female(insurance_records) #12569.57
average_smoker_charge, average_non_smoker_charge = calc_average_smoker_charge() #32050.23, 8434.26
smoker_non_smoker_charge_diff = average_smoker_charge - average_non_smoker_charge #23615.96

counted_locations = count_locations(regions)

