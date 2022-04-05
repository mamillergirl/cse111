from nutrition_calculator import compute_eer, compute_bmi, find_pal_no, compute_amdr, convert_value, get_food_info_from_dict, create_food_dict_from_csv, calculate_food_intakes
from pytest import approx
import pytest 




def test_compute_eer():
    assert compute_eer('Male', 13, 60.68, 1.48, 1.13, False, 0, False, 0) == approx(2650)
    assert compute_eer('Female', 15, 65.98, 1.56, 1.31, False, 0, False, 0) == approx(2471)
    assert compute_eer('Female', 25, 69.52, 1.67,  1.45, False, 0, False, 0) == approx(2883)
    assert compute_eer('Male', 20, 72.58, 1.78,  1.25, False, 0, False, 0) == approx(3115)
    assert compute_eer('Female', 25, 69.52, 1.67,  1.45, True, 1, False, 0) == approx(2883)
    assert compute_eer('Female', 25, 69.52, 1.67,  1.45, True, 2, False, 0) == approx(3223)
    assert compute_eer('Female', 25, 69.52, 1.67,  1.45, True, 3, False, 0) == approx(3335)
    assert compute_eer('Female', 25, 69.52, 1.67,  1.45, False, 0, True, 1) == approx(3213)
    assert compute_eer('Female', 25, 69.52, 1.67,  1.45, False, 0, True, 2) == approx(3283)

def test_find_pal_no():
    assert find_pal_no('sedentary', 20, 'Male') == 1.0
    assert find_pal_no('low active', 20, 'Male') == 1.11
    assert find_pal_no('low active', 20, 'Female') == 1.12
    assert find_pal_no('low active', 12, 'Male') == 1.13
    assert find_pal_no('low active', 16, 'Female') == 1.16
    assert find_pal_no('active', 20, 'Male') == 1.25
    assert find_pal_no('active', 20, 'Female') == 1.27
    assert find_pal_no('active', 13, 'Male') == 1.26
    assert find_pal_no('active', 15, 'Female') == 1.31
    assert find_pal_no('very active', 70, 'Male') == 1.48
    assert find_pal_no('very active', 40, 'Female') == 1.45
    assert find_pal_no('very active', 11, 'Male') == 1.42
    assert find_pal_no('very active', 9, 'Female') == 1.56

def test_compute_amdr():
    assert compute_amdr(2200.25, .10) == 220
    assert compute_amdr(1835.55, .35) == 642

def test_convert_value():
    assert convert_value(220, 4, 0) == 55
    assert convert_value(642, 9, 0) == 71
    assert convert_value(121, 2.2046, 2) == approx(54.89)
    assert convert_value(205, 2.2046, 2) == approx(92.99)
    assert convert_value(66, 39.37, 2) == approx(1.68)
    assert convert_value(75, 39.37, 2) == approx(1.91)



def test_compute_bmi():
    assert compute_bmi(75, 1.75) == approx(24.48979)
    assert compute_bmi(61.23, 1.63) == approx(23.04565)

def test_get_food_info_from_dict():
    foods = create_food_dict_from_csv('food.csv')
    assert get_food_info_from_dict(foods, 'Milk, human', 1) == {'Carbohydrates': 6.89, 'Protein': 1.03, 'Total Sugar': 6.89, 'Saturated Fat': 2.01, 'Total Fat': 4.38, 'Fiber': 0.00, 'Sodium': 17.0, 'Calcium': 32.0, 'Iron': 0.03, 'Potassium': 51.0, 'Vitamin A': 61.0, 'Vitamin B-12': 0.05, 'Vitamin B-6': 0.01, 'Vitamin C': 5.0}
    assert get_food_info_from_dict(foods, 'Milk, human', 2) == {'Carbohydrates': 13.78, 'Protein': 2.06, 'Total Sugar': 13.78, 'Saturated Fat': 4.02, 'Total Fat': 8.76, 'Fiber': 0.00, 'Sodium': 34.00, 'Calcium': 64.0, 'Iron': 0.06, 'Potassium': 102.0, 'Vitamin A': 122.0, 'Vitamin B-12': 0.10, 'Vitamin B-6': 0.02, 'Vitamin C': 10.0}

def test_calculate_food_intakes():
    assert calculate_food_intakes([[234, 339], [52, 182], [46, 81], 23, 28, 2300, 1300, 18, 4700, 900, 2.4, 1.7, 90], [{'Carbohydrates': 163.0, 'Protein': 16.4, 'Total Sugar': 1.2, 'Saturated Fat': 1.28, 'Total Fat': 5.6, 'Fiber': 8.4, 'Sodium': 652.0, 'Calcium': 22.0, 'Iron': 2.98, 'Potassium': 580.0, 'Vitamin A': 0.0, 'Vitamin B-12': 0.0, 'Vitamin B-6': 0.3, 'Vitamin C': 0.0}, {'Carbohydrates': 16.21, 'Protein': 7.86, 'Total Sugar': 1.78, 'Saturated Fat': 2.29, 'Total Fat': 8.04, 'Fiber': 2.8, 'Sodium': 322.0, 'Calcium': 83.0, 'Iron': 1.67, 'Potassium': 221.0, 'Vitamin A': 31.0, 'Vitamin B-12': 0.1, 'Vitamin B-6': 0.1, 'Vitamin C': 3.1}]) == {'Carbohydrate Intake': 'not within range', 'Protein Intake': 'not within range', 'Total Fat Intake': 'not within range', 'Saturated Fat Intake': 15.5, 'Fiber Intake': 40.0, 'Sodium Intake': 42.3, 'Calcium Intake': 8.1, 'Iron Intake': 25.8, 'Potassium Intake': 17.0, 'Vitamin A Intake': 3.4, 'Vitamin B-12 Intake': 4.2, 'Vitamin B-6 Intake': 23.5, 'Vitamin C Intake': 3.4}
    assert calculate_food_intakes([[232, 335], [52, 180], [46, 80], 23, 28, 2300, 1300, 18, 4700, 900, 2.4, 1.7, 90], [{'Carbohydrates': 50.45, 'Protein': 13.82, 'Total Sugar': 1.95, 'Saturated Fat': 3.46, 'Total Fat': 18.81, 'Fiber': 4.35, 'Sodium': 679.5, 'Calcium': 156.0, 'Iron': 3.71, 'Potassium': 232.5, 'Vitamin A': 45.0, 'Vitamin B-12': 0.27, 'Vitamin B-6': 0.21, 'Vitamin C': 0.0}]) == {'Carbohydrate Intake': 'not within range', 'Protein Intake': 'not within range', 'Total Fat Intake': 'not within range', 'Saturated Fat Intake': 15.0, 'Fiber Intake': 15.5, 'Sodium Intake': 29.5, 'Calcium Intake': 12.0, 'Iron Intake': 20.6, 'Potassium Intake': 4.9, 'Vitamin A Intake': 5.0, 'Vitamin B-12 Intake': 11.3, 'Vitamin B-6 Intake': 12.4, 'Vitamin C Intake': 0.0}

pytest.main(["-v", "--tb=line", "-rN", __file__])