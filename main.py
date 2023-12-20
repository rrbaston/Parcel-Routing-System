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
import datetime


# hash_table = HashTable(size=10)  # Create a HashTable instance
# loadPackageData(hash_table, '/Users/rodrigo/Documents/repos/Parcel-Routing-System/WGUPS-package-v2.csv') # Load HashTable with package data
# # hash_table.display()

# distanceData = loadDistanceData('/Users/rodrigo/Documents/repos/Parcel-Routing-System/WGUPS-distance-matrix.csv') # Load distance matrix data
# # displayDistanceData(distanceData)
# addressData, address_to_index = loadAddressData('/Users/rodrigo/Documents/repos/Parcel-Routing-System/WGUPS-address.csv') # Load address data
# # displayAddressData(addressData)

# # Create trucks with capacity
# truck1 = Truck(1, 16, 8)
# truck2 = Truck(2, 16, 8)


# # For each truck, create distance matrix and optimize route
# for truck in [truck1, truck2]:
#     truck.truckAddressListAndDistanceMatrix(address_to_index, distanceData)
#     optimized_route, _ = twoOpt(truck.truckDistanceMatrix)
#     truck.truckPackagesBestTour = [truck.truckPackages[i] for i in optimized_route]

#     # Simulate package delivery
#     truckDeliverPackagesBestTour(truck, address_to_index, distanceData, hash_table)

#     # Display truck information
#     truck.display_truck_info()

# #Test
# # address1 = "1060 Dalton Ave S"  # Replace with the actual address
# # address2 = "195 W Oakland Ave"  # Replace with the actual address
# # distance = get_distance_between(address1, address2, address_to_index, distanceData)
# # print(f"The distance between {address1} and {address2} is {distance} miles.")






# Assuming your Truck class and logistics_util functions are already defined
# as provided in your previous messages.

# Initialize the hash table and load package data
hash_table = HashTable(size=10)
loadPackageData(hash_table, '/Users/rodrigo/Documents/repos/Parcel-Routing-System/WGUPS-package-v2.csv')

# Load distance matrix and address data
distanceData = loadDistanceData('/Users/rodrigo/Documents/repos/Parcel-Routing-System/WGUPS-distance-matrix.csv') # Load distance matrix data
addressData, address_to_index = loadAddressData('/Users/rodrigo/Documents/repos/Parcel-Routing-System/WGUPS-address.csv') # Load address data

# Set the start time for the trucks (e.g., 8:00 AM on a specific date)
start_time = datetime.datetime(2023, 12, 19, 8, 0)

# Create trucks with capacity and start time
truck1 = Truck(1, 16, start_time)
truck2 = Truck(2, 16, start_time)

# Get all packages from the hash table
all_packages = hash_table.get_all_packages()

# Function to simulate the delivery process
def simulate_delivery_process(trucks, all_packages, address_to_index, distanceData, hashTable):
    while any(package.status != 'delivered' for package in all_packages):
        for truck in trucks:
            # Load packages onto the truck based on priority
            truck.load_truck_with_priorities(all_packages)

            # Optimize the delivery route for the loaded packages
            optimized_route, _ = twoOpt(truck.truckDistanceMatrix)

            # Simulate delivery for the optimized route
            truckDeliverPackagesBestTour(truck, address_to_index, distanceData, hashTable)

            # Unload packages after delivery
            for package in truck.truckPackages:
                truck.unload_package(package.package_id)

            # Check for undelivered packages and reload the truck
            undelivered_packages = [pkg for pkg in all_packages if pkg.status != 'delivered']
            truck.load_truck_with_priorities(undelivered_packages)

            # Update the start time for the next round of deliveries
            truck.current_time += datetime.timedelta(hours=1)  # Assuming a 1-hour break

# Simulate the delivery process
simulate_delivery_process([truck1, truck2], all_packages, address_to_index, distanceData, hash_table)

# After the simulation, you can print the results
for truck in [truck1, truck2]:
    truck.display_truck_info()
    print(f"Truck {truck.truck_id} finished deliveries at: {truck.current_time}")
