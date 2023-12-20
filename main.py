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
# Initialization and data loading remains the same...

def simulate_delivery_process(trucks, all_packages, address_to_index, distanceData, hashTable):
    while any(package.status != 'delivered' for package in all_packages):
        for truck in trucks:
            truck.load_truck_with_priorities(all_packages)

            if not truck.truckPackages:
                continue

            truck.truckAddressListAndDistanceMatrix(address_to_index, distanceData)
            if not truck.truckDistanceMatrix:
                continue

            optimized_route, _ = twoOpt(truck.truckDistanceMatrix)
            truck.truckPackagesBestTour = [truck.truckPackages[i] for i in optimized_route]

            delivered_package_ids = truckDeliverPackagesBestTour(truck, address_to_index, distanceData, hashTable)

            # Unload delivered packages
            for package_id in delivered_package_ids:
                truck.unload_package(package_id)

            all_packages = hashTable.get_all_packages()

            undelivered_packages = [pkg for pkg in all_packages if pkg.status != 'delivered']
            if not undelivered_packages:
                break

            truck.load_truck_with_priorities(undelivered_packages)
            truck.current_time += datetime.timedelta(hours=1)

    for truck in trucks:
        truck.display_truck_info()


# Call the simulation function
simulate_delivery_process([truck1, truck2], all_packages, address_to_index, distanceData, hash_table)

# # After the simulation, you can print the results
# for truck in [truck1, truck2]:
#     truck.display_truck_info()
#     print(f"Truck {truck.truck_id} finished deliveries at: {truck.current_time}")
