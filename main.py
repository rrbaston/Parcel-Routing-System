import random
from hash_table import HashTable
from package import Package
from truck import Truck
from data_loader import (
    loadDistanceData,
    loadAddressData, 
    loadPackageData,
    displayDistanceData,
    displayAddressData
)
from logistics_util import (
    twoOptDistance,
    twoOpt,
    distanceBetween,
    truckDeliverPackagesBestTour,
    timeToDeliver
)


hash_table = HashTable(size=10)  # Create a HashTable instance
loadPackageData(hash_table, '/Users/rodrigo/Documents/repos/Parcel-Routing-System/WGUPS-package-v2.csv') # Load HashTable with package data
# hash_table.display()

distanceData = loadDistanceData('/Users/rodrigo/Documents/repos/Parcel-Routing-System/WGUPS-distance-matrix.csv') # Load distance matrix data
# displayDistanceData(distanceData)
addressData, address_to_index = loadAddressData('/Users/rodrigo/Documents/repos/Parcel-Routing-System/WGUPS-address.csv') # Load address data
# displayAddressData(addressData)

# Create trucks with capacity
truck1 = Truck(1, 16)
truck2 = Truck(2, 16)

# Manually load packages onto trucks
# Here, we randomly assign packages to trucks for demonstration purposes
package_list = [1,2,3,4,5,6,7,8,9,10]

random.shuffle(package_list)
for package in package_list:
    if len(truck1.truckPackages) < truck1.capacity:
        truck1.load_package(package)
    else:
        truck2.load_package(package)

# For each truck, create distance matrix and optimize route
for truck in [truck1, truck2]:
    truck.truckAddressListAndDistanceMatrix(address_to_index, distanceData)
    optimized_route, _ = twoOpt(truck.truckDistanceMatrix)
    truck.truckPackagesBestTour = [truck.truckPackages[i] for i in optimized_route]

    # Simulate package delivery
    truckDeliverPackagesBestTour(truck, address_to_index, distanceData, hash_table)

    # Display truck information
    truck.display_truck_info()






#Test
# address1 = "1060 Dalton Ave S"  # Replace with the actual address
# address2 = "195 W Oakland Ave"  # Replace with the actual address
# distance = get_distance_between(address1, address2, address_to_index, distanceData)
# print(f"The distance between {address1} and {address2} is {distance} miles.")


