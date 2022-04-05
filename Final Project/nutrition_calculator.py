import csv

#"Category","Description","Nutrient Data Bank Number","Data.Alpha Carotene","Data.Beta Carotene","Data.Beta Cryptoxanthin","Data.Carbohydrate","Data.Cholesterol","Data.Choline","Data.Fiber","Data.Lutein and Zeaxanthin","Data.Lycopene","Data.Niacin","Data.Protein","Data.Retinol","Data.Riboflavin","Data.Selenium","Data.Sugar Total","Data.Thiamin","Data.Water","Data.Fat.Monosaturated Fat","Data.Fat.Polysaturated Fat","Data.Fat.Saturated Fat","Data.Fat.Total Lipid","Data.Major Minerals.Calcium","Data.Major Minerals.Copper","Data.Major Minerals.Iron","Data.Major Minerals.Magnesium","Data.Major Minerals.Phosphorus","Data.Major Minerals.Potassium","Data.Major Minerals.Sodium","Data.Major Minerals.Zinc","Data.Vitamins.Vitamin A - RAE","Data.Vitamins.Vitamin B12","Data.Vitamins.Vitamin B6","Data.Vitamins.Vitamin C","Data.Vitamins.Vitamin E","Data.Vitamins.Vitamin K"] 
#  0            1                2                          3                   4                     5                        6                        7               8           9               10                          11              12          13              14              15              16              17                    18            19              20                          21                          22                          23                  24                              25                          26                          27                                  28                                      29                      30                          31                          32                              33                         34                       35                          36                      37

def create_food_dict_from_csv(filename):
    
    DESCRIPTION_INDEX = 1
    CARBOHYDRATE_INDEX = 6
    FIBER_INDEX = 9
    PROTEIN_INDEX = 13
    TOTAL_SUGAR_INDEX = 17
    SATURATED_FAT_INDEX = 22
    TOTAL_FAT = 23
    SODIUM_INDEX = 30
    CALCIUM_INDEX = 24
    IRON_INDEX = 26
    POTASSIUM_INDEX = 29 
    VITAMIN_A_INDEX = 32
    VITAMIN_B12_INDEX = 33
    VITAMIN_B6_INDEX = 34
    VITAMIN_C_INDEX = 35
    
    with open(filename, 'rt') as food_file:
        reader = csv.reader(food_file)
        next(reader)
        foods = {}
        for row_list in reader:
            food_item = {}
            
            keys = [
            'Carbohydrates', 
            'Protein',
            'Total Sugar',
            'Saturated Fat',
            'Total Fat',
            'Fiber',
            'Sodium',
            'Calcium',
            'Iron',
            'Potassium',
            'Vitamin A',
            'Vitamin B-12',
            'Vitamin B-6',
            'Vitamin C' 
               ]
            values = [
                float(row_list[CARBOHYDRATE_INDEX]), 
                float(row_list[PROTEIN_INDEX]), 
                float(row_list[TOTAL_SUGAR_INDEX]), 
                float(row_list[SATURATED_FAT_INDEX]), 
                float(row_list[TOTAL_FAT]), 
                float(row_list[FIBER_INDEX]), 
                float(row_list[SODIUM_INDEX]), 
                float(row_list[CALCIUM_INDEX]), 
                float(row_list[IRON_INDEX]),
                float(row_list[POTASSIUM_INDEX]),
                float(row_list[VITAMIN_A_INDEX]),
                float(row_list[VITAMIN_B12_INDEX]),
                float(row_list[VITAMIN_B6_INDEX]),
                float(row_list[VITAMIN_C_INDEX]) 
            ]

            for key, value in zip(keys, values):
                food_item[key] = value

            foods[row_list[DESCRIPTION_INDEX]] = food_item
    return foods
#figure out values needed so that the program can calculate your percent intake
def create_dv_list(profiles, name):
    user_info = profiles[name]
     
    Carbohydrates = user_info['Carbohydrate AMDR Range Grams']
    Protein = user_info['Protein AMDR Range Grams']
    Total_Fat = user_info['Fat AMDR Range Grams']
    saturated_fat_max_gram = user_info['Total Saturated Fat Grams']
   
    values = [
        Carbohydrates,
        Protein,
        Total_Fat,
        saturated_fat_max_gram,
        28,
        2300, 
        1300, 
        18,
        4700,
        900,
        2.4,
        1.7,
        90 ]
 
    return values
#find info for specific foods   
def get_food_info_from_dict(foods, description, portion):
    food_info = foods[description]
    for key in food_info:    
        food_info[key] *= portion
        food_info[key] = round(food_info[key], 2)
    
    return food_info
#calculate needed calories
def compute_eer(gender, age, weight, height, pal, pregnant, trimester,lactating, post_partem):
    
    if gender == 'Male' and age < 19 and age >= 9 :
        calories = 88.5 - 61.9 * age + pal * (26.7 * weight + 903 * height) +25
    elif gender == 'Male' and age >= 19:
        calories = 662 - 9.53 * age + pal * (15.91 * weight + 539.6 * height)
    elif gender == 'Female' and age < 19 and age >=9:
        calories = 135.3 - (30.8 * age) + pal * ((10.0 * weight) + (934 * height)) + 25
    elif gender == 'Female' and age >= 19:
        calories = 354 - 6.91 * age + pal * (9.36 * weight + 726 * height)
    if pregnant == True:
        if trimester == 2:
            calories = calories + 340
        elif trimester == 3:
            calories = calories + 452
    if lactating == True:
        if post_partem == 1:
            calories = calories + 330
        elif post_partem == 2:
            calories = calories + 400

    calories = round(calories)
    return calories

def prompt_gender():
    genders = ['Male', 'Female']
    gender = None
    while gender == None:
        try:
            gender = input('Enter gender (Male or Female):  ').capitalize()
            if gender not in genders :
                print(f"Error: Gender entered not valid")
                gender = None
        except ValueError as val_err:
            print("Error:", val_err)
    return gender
        

    
def prompt_number(phrase, number):
    value = None
    while value == None:
        try:
            value = int(input(phrase))
            if value < number:
                print(f"Error: This number is too low" \
                        f" Please enter a different number.")
                value = None
        except ValueError as val_err:
            print("Error:", val_err)
    return value

def prompt_activity_level():
    activity_levels = ['sedentary', 'low active', 'active', 'very active']
    
    activity_level = None
    while activity_level == None:
        try:
            activity_level = input('Enter activity level (sedentary, low active, active, very active):  ').lower()
            if activity_level not in activity_levels:
                print(f"Error: Activity level entered not valid")
                activity_level = None
        except ValueError as val_err:
            print("Error:", val_err)
    return activity_level

def prompt_if_pregnant_or_lacting(pregnant_or_lactating, gender, age):
    preg_or_lac = ''
    responses = ['yes', 'no']
    if gender == 'Female' and age >= 14:
        while preg_or_lac not in responses:
            preg_or_lac = input(f'Is this person {pregnant_or_lactating}? (yes or no)  ').lower()
        if preg_or_lac == 'yes': 
            preg_or_lac = True
        elif preg_or_lac == 'no':
            preg_or_lac = False
    else:
        preg_or_lac = False

    return preg_or_lac

def prompt_stage(phrase, total):
    stage = -1
    while stage < 1 or stage > total:
        stage = int(input(phrase))
    return stage

#put together all of the input into one dictionary to add it to profiles
def compile_user_info(profiles):
    #name as key for dictionary
    name = input('Enter name:  ').capitalize()
   
    # Gender
    gender = prompt_gender()
    # Age
    age = prompt_number('Enter age:  ', 9)
    # Weight
    pounds = prompt_number('Enter weight in pounds:  ', 0)
    weight = convert_value(pounds, 2.2046, 2)

    # Height
    inches = prompt_number('Enter height in inches:  ', 0 )
    height = convert_value(inches, 39.37, 2)
    # Activity Level
    activity_level = prompt_activity_level()
    # Find activity level number to calculate calories
   
    pal = find_pal_no(activity_level, age, gender)
    
    trimester = 0

    post_partem = 0

    pregnant = prompt_if_pregnant_or_lacting('pregnant', gender, age)
    if pregnant == True:
        trimester = prompt_stage('Enter trimester:  ', 3)
    lactating = prompt_if_pregnant_or_lacting('lactating', gender,age)
    if lactating == True:
        post_partem =  prompt_stage('Enter postpartem 1 or 2 (1: 0-6 months, 2:6-12 months):  ', 2)


    # Compute bmi
    bmi = round(compute_bmi(weight, height), 2)
    # Total Reccomended Calories
    eer = compute_eer(gender, age, weight, height, pal, pregnant, trimester, lactating, post_partem)
    
   

    #Lower Cal Carb
    Carbohydrates = []
    carbs_lower_cal = compute_amdr(eer, .45)
 
    #Upper Cal Carb
    carbs_upper_cal = compute_amdr(eer,.65)
   
    # Lower Gram Carb
    carbs_lower_gram = convert_value(carbs_lower_cal, 4, 0)
    Carbohydrates.append(carbs_lower_gram)
    # Upper Gram Carb
    carbs_upper_gram = convert_value(carbs_upper_cal, 4, 0)  
    Carbohydrates.append(carbs_upper_gram)
    Protein = []
    # Lower Cal Protein
    protein_lower_cal = compute_amdr(eer,.10)

    # Upper Cal Protein
    protein_upper_cal = compute_amdr(eer, .35)

    # Lower Gram Protein
    protein_lower_gram = convert_value(protein_lower_cal, 4, 0)
    Protein.append(protein_lower_gram)
    # Upper Gram Protein
    protein_upper_gram = convert_value(protein_upper_cal, 4, 0)
    Protein.append(protein_upper_gram)

    added_sugar_max_cal = compute_amdr(eer, .10)
    added_sugar_max_gram = convert_value(added_sugar_max_cal, 4, 0)

    saturated_fat_max_cal = compute_amdr(eer, .10)
    saturated_fat_max_gram = convert_value(saturated_fat_max_cal, 9, 0)

    
    Total_Fat = []
    # Lower Cal Fat
    fat_lower_cal = compute_amdr(eer,.20)

    # Upper Cal Fat
    fat_upper_cal = compute_amdr(eer, .35)

    # Lower Gram Fat
    fat_lower_gram = convert_value(fat_lower_cal, 9,0)
    Total_Fat.append(fat_lower_gram)
    # Upper Gram Fat
    fat_upper_gram = convert_value(fat_upper_cal,9, 0)
    Total_Fat.append(fat_upper_gram)
    #

    user_info_dict = {}
    keys = [
            'Gender', 
            'Age',
            'Weight',
            'Height',
            'Activity Level',
            'Pal',
            'Pregnant',
            'Trimester',
            'Lactating',
            'Postpartem',
            'BMI',
            'EER', 
            'Carbohydrate AMDR Range Grams',
            'Protein AMDR Range Grams',
            'Fat AMDR Range Grams',
            'Total Added Sugar Grams',
            'Total Saturated Fat Grams'
               ]
    values = [
        gender,
        age,
        weight,
        height,
        activity_level,
        pal,
        pregnant, 
        trimester, 
        lactating,
        post_partem,
        bmi,
        eer,
        Carbohydrates,
        Protein,
        Total_Fat,
        added_sugar_max_gram,
        saturated_fat_max_gram
       
    ]



    for key, value in zip(keys, values):
        user_info_dict[key] = value
    
    profiles[name] = user_info_dict
    return profiles

#convert between different types of measurement
def convert_value(original, base, decimal):
    new = original / base
    new =round(new, decimal)
    return new 




def compute_bmi(kg, meters):
    bmi = kg / (meters ** 2)
    return bmi

def find_pal_no(activity_level, age, gender):

    if activity_level == 'sedentary':
        pal = 1.0
    elif activity_level == 'low active' and gender == 'Male' and age >= 19:
        pal = 1.11
    elif activity_level == 'low active' and gender == 'Female' and age >= 19:
        pal = 1.12
    elif activity_level == 'low active' and gender == 'Male' and age in range(9, 19):
        pal = 1.13
    elif activity_level == 'low active' and gender == 'Female' and  age in range(9, 19):
        pal = 1.16
    elif activity_level == 'active' and gender == 'Male' and age >= 19:
        pal = 1.25
    elif activity_level == 'active' and gender == 'Female' and age >= 19:
        pal = 1.27
    elif activity_level == 'active' and gender == 'Male' and  age in range(9, 19):
        pal = 1.26
    elif activity_level == 'active' and gender == 'Female' and age in range(9, 19):
        pal = 1.31
    elif activity_level == 'very active' and gender == 'Male' and age >= 19:
        pal = 1.48
    elif activity_level == 'very active' and gender == 'Female' and age >= 19:
        pal = 1.45
    elif activity_level == 'very active' and gender == 'Male' and age in range(9, 19):
        pal = 1.42
    elif activity_level == 'very active' and gender == 'Female' and age in range(9, 19):
        pal = 1.56
    
    return pal

def compute_amdr(calories, percentage):
    amdr = calories * percentage
    amdr = round(amdr)
    return amdr


def calculate_food_intakes(dv_list, total_foods):
 
    carb_rec = dv_list[0]
    protein_rec = dv_list[1]
    fat_rec = dv_list[2]
    saturated_fat_rec = dv_list[3]
    fiber_rec = dv_list[4]
    sodium_rec = dv_list[5]
    calcium_rec = dv_list[6]
    iron_rec = dv_list[7]
    potassium_rec = dv_list[8]
    vitamin_a_rec = dv_list[9]
    vitamin_b12_rec = dv_list[10]
    vitamin_b6_rec = dv_list[11]
    vitamin_c_rec = dv_list[12]

    total_carb = 0
    total_protein = 0
    total_saturated_fat = 0
    total_fat = 0
    total_fiber = 0
    total_sodium = 0
    total_calcium = 0
    total_iron = 0
    total_potassium = 0
    total_vitamin_a = 0
    total_vitamin_b12 = 0
    total_vitamin_b6 = 0
    total_vitamin_c = 0
    
    for food_dict in total_foods:
        
        carb = food_dict['Carbohydrates']
        protein = food_dict['Protein']        
        saturated_fat = food_dict['Saturated Fat']
        fat = food_dict['Total Fat']
        fiber = food_dict['Fiber']
        sodium = food_dict['Sodium']
        calcium = food_dict['Calcium']
        iron = food_dict['Iron']
        potassium = food_dict['Potassium']
        vitamin_a = food_dict['Vitamin A']
        vitamin_b12 = food_dict['Vitamin B-12']
        vitamin_b6 = food_dict['Vitamin B-6']
        vitamin_c = food_dict['Vitamin C']
        total_carb += carb
        total_protein += protein
        total_saturated_fat += saturated_fat
        total_fat += fat
        total_fiber += fiber
        total_sodium += sodium
        total_calcium += calcium
        total_iron += iron
        total_potassium += potassium
        total_vitamin_a += vitamin_a
        total_vitamin_b12 += vitamin_b12
        total_vitamin_b6 += vitamin_b6
        total_vitamin_c += vitamin_c
    carb_lower_rec = carb_rec[0]
    carb_higher_rec = carb_rec[1]
    intake_carb = compare_intake_to_amdr(total_carb, carb_lower_rec, carb_higher_rec)
    protein_lower_rec = protein_rec[0]
    protein_higher_rec = protein_rec[1]
    intake_protein = compare_intake_to_amdr(total_protein, protein_lower_rec, protein_higher_rec)
    
    fat_lower_rec = fat_rec[0]
    fat_higher_rec = fat_rec[1]
    intake_fat = compare_intake_to_amdr(total_fat, fat_lower_rec, fat_higher_rec)

    intake_saturated_fat = calculate_percent_intake(total_saturated_fat , saturated_fat_rec)
    intake_fiber =  calculate_percent_intake(total_fiber,fiber_rec)
    intake_sodium = calculate_percent_intake(total_sodium ,sodium_rec)
    intake_calcium = calculate_percent_intake(total_calcium, calcium_rec)
    intake_iron = calculate_percent_intake(total_iron, iron_rec)
    intake_potassium = calculate_percent_intake(total_potassium, potassium_rec)
    intake_vitamin_a = calculate_percent_intake(total_vitamin_a, vitamin_a_rec)
    intake_vitamin_b12 = calculate_percent_intake(total_vitamin_b12 , vitamin_b12_rec)
    intake_vitamin_b6 = calculate_percent_intake(total_vitamin_b6, vitamin_b6_rec)
    intake_vitamin_c =  calculate_percent_intake(total_vitamin_c, vitamin_c_rec)

    food_intakes = {}
            
    keys = [
    'Carbohydrate Intake',
    'Protein Intake',
    'Total Fat Intake',
    'Saturated Fat Intake',
    'Fiber Intake',
    'Sodium Intake',
    'Calcium Intake',
    'Iron Intake',
    'Potassium Intake',
    'Vitamin A Intake',
    'Vitamin B-12 Intake',
    'Vitamin B-6 Intake',
    'Vitamin C Intake',
       ]
    values = [
        intake_carb,
        intake_protein,
        intake_fat,
        intake_saturated_fat,
        intake_fiber,
        intake_sodium,
        intake_calcium,
        intake_iron,
        intake_potassium,
        intake_vitamin_a,
        intake_vitamin_b12,
        intake_vitamin_b6,
        intake_vitamin_c]
        
    
    for key, value in zip(keys, values):
        food_intakes[key] = value

    return food_intakes

def calculate_percent_intake(total, rec):
    intake = total / rec 
    intake *= 100
    intake = round(intake, 1)
    return intake

def compare_intake_to_amdr(total,lower_rec, higher_rec):
    if total in range(lower_rec, higher_rec + 1):
        intake = 'within range'
    else:
        intake = 'not within range'
    return intake

def main():
    foods = create_food_dict_from_csv('food.csv')

    menu_selection = None
    profiles = {}
    profiles = compile_user_info(profiles)
    
    while menu_selection != 4:
        
        print(f'\nWelcome to the Nutrition Calculator\nChoose one of the following:\n1 - Create Another Profile\n2 - View Profile\n3 - Caluculate daily values for intake\n4 - Quit')
        menu_selection = int(input('Enter an option:  '))
        if menu_selection == 1:
            compile_user_info(profiles)
            print()
        elif menu_selection == 2:
            name = ''
            {'Gender': 'Female', 'Age': 18, 'Weight': 54.89, 'Height': 1.68, 'Activity Level': 'active', 'Pal': 1.31, 'Pregnant': False, 'Trimester': 0, 'Lactating': False, 'Postpartem': 0, 'BMI': 19.45, 'EER': 2381, 'Carbohydrate AMDR Range Grams': [268, 387], 'Protein AMDR Range Grams': [60, 208], 'Fat AMDR Range Grams': [53, 93], 'Total Added Sugar Grams': 60, 'Total Saturated Fat Grams': 26}
            while name not in profiles:
                name = input('Enter name:  ').capitalize()
            user_info_dict = profiles[name]

            if user_info_dict['Gender'] == 'Female' and user_info_dict['Pregnant'] == False and user_info_dict['Lactating'] == False and user_info_dict['Age'] >= 14:
                print(f'Information for {name}:\n{user_info_dict["Age"]} yr old non-pregnant non-lactating {user_info_dict["Gender"]}\n{user_info_dict["Weight"]} kg {user_info_dict["Height"]} meters\n{user_info_dict["BMI"]} BMI\n{user_info_dict["EER"]} required calorie estimate\n')
            elif user_info_dict['Gender'] == 'Female' and user_info_dict['Pregnant'] == True and user_info_dict['Lactating'] == False:
                print(f'Information for {name}:\n{user_info_dict["Age"]} yr old pregnant non-lactating {user_info_dict["Gender"]}\n{user_info_dict["Weight"]} kg {user_info_dict["Height"]} meters\n{user_info_dict["BMI"]} BMI\n{user_info_dict["EER"]} required calorie estimate\n')
            elif user_info_dict['Gender'] == 'Female' and user_info_dict['Pregnant'] == False and user_info_dict['Lactating'] == True:
                print(f'Information for {name}:\n{user_info_dict["Age"]} yr old non-pregnant lactating {user_info_dict["Gender"]}\n{user_info_dict["Weight"]} kg {user_info_dict["Height"]} meters\n{user_info_dict["BMI"]} BMI\n{user_info_dict["EER"]} required calorie estimate\n')
            else:
                print(f'Information for {name}:\n{user_info_dict["Age"]} yr old {user_info_dict["Gender"]}\n{user_info_dict["Weight"]} kg {user_info_dict["Height"]} meters\n{user_info_dict["BMI"]} BMI\n{user_info_dict["EER"]} required calorie estimate\n')

        elif menu_selection == 3:
            name = ''
            while name not in profiles:
                name = input('Enter name:  ').capitalize()

            dv = create_dv_list(profiles, name)

            total_foods_info = []

            continue_adding_foods = ''
            while continue_adding_foods != 'no':
                description = None
                while description == None:
                    description = input('Enter the exact description of the food:  ')
                    if description not in foods:
                        print('This description is not in the dictionary. Please enter another description')
                        description = None
                    
                portion = float(input('Enter how many servings:  '))
            
                food_info = get_food_info_from_dict(foods, description, portion)
                total_foods_info.append(food_info)
                
                continue_adding_foods = input('Would you like to keep adding foods(yes or no)?  ').lower()
            user_info_dict = profiles[name]
            
            food_intakes = calculate_food_intakes(dv, total_foods_info)
            
            print(f"Carbohydrate intake: {food_intakes['Carbohydrate Intake']} of AMDR\nProtein intake: {food_intakes['Protein Intake']} of AMDR\nFat intake: {food_intakes['Total Fat Intake']} of AMDR\nSaturated Fat Intake: {food_intakes['Saturated Fat Intake']}%\nFiber Intake: {food_intakes['Fiber Intake']}%\nSodium Intake:{food_intakes['Sodium Intake']}%\nCalcium Intake: {food_intakes['Calcium Intake']}%\nIron Intake: {food_intakes['Iron Intake']}%\nPotassium Intake: {food_intakes['Potassium Intake']}%\nVitamin A Intake: {food_intakes['Vitamin A Intake']}%\nVitamin B12 Intake: {food_intakes['Vitamin B-12 Intake']}%\nVitamin B-6 Intake: {food_intakes['Vitamin B-6 Intake']}%\nVitamin C Intake: {food_intakes['Vitamin C Intake']}%")


if __name__ == "__main__":
    main()


                              

           

         
           