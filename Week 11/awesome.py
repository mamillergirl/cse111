
def compute_circle_area(r):
    a = r* 3.14
    return a
def display_area(a):
    print(a)
def prompt_user_for_radius():
    r = int(input('Please enter a radius: '))
    return r
def main():
    r = prompt_user_for_radius()
    a = compute_circle_area(r)
    display_area(a)




main