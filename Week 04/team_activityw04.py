# Your program must compute the volume of all 12 can sizes.
# Your program must compute the surface area of all 12 can sizes.
# Your program must compute and print the storage efficiency of all 12 can sizes

import math 

names = ["#1 Picnic", "#1 Tall", "#2", "#2.5", "#3 Cylinder", "#5", "#6Z", "#8Z short", "#10", "#211", "#300", "#303"]
radiuses = [6.83, 7.78, 8.73, 10.32, 10.79, 13.02, 5.40, 6.83, 15.72, 6.83, 7.62, 8.10]
heights = [10.16, 11.91, 11.59, 11.91, 17.78, 14.29, 8.89, 7.62, 17.78, 12.38, 11.27, 11.11]
costs = [0.28, 0.43, 0.45, 0.61, 0.86, 0.83, 0.22, 0.26, 1.53, 0.34, 0.38, 0.42]

def main():
    for i in range(len(names)):
        name = names[i]
        radius = radiuses[i]
        height = heights[i]
        cost = costs[i]
        surf_area = compute_surface_area(radius, height)
        find_vol =  compute_volume(radius, height) 
        storage_efficency = compute_storage_efficiency(find_vol, surf_area )
        cost_efficiency = compute_cost_efficiency(find_vol, cost)
        highest_cost_effiency = -1
        if cost_efficiency > highest_cost_effiency:
            highest_cost_efficiency = cost_efficiency


        print (f"{name} {storage_efficency:.1f}, ${cost_efficiency:.2f}")
 
    print(f"The highest cost efficiency is {highest_cost_efficiency}")
def compute_volume(radius, height):
    volume = math.pi * (radius) ** 2 * (height)
    return volume 


def compute_surface_area(radius, height):
    surface_area = 2 * math.pi * radius * (radius + height)
    return surface_area


def compute_storage_efficiency(volume, surface_area):
    find_storage_eff = volume / surface_area 
    return find_storage_eff 


def compute_cost_efficiency(volume, cost):
    cost_efficiency = volume / cost
    return cost_efficiency


main()