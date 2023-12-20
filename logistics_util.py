import datetime

# Calculate the total distance of a given tour based on the truck's distance matrix
def twoOptDistance(tour, distance_matrix):
    total_distance = 0
    for i in range(len(tour) - 1):
        total_distance += distance_matrix[tour[i]][tour[i + 1]]
    total_distance += distance_matrix[tour[-1]][tour[0]]  # Return to starting point
    return total_distance

# Implement the 2-opt algorithm to find the best tour
def twoOpt(distance_matrix):
    # Start with a random tour
    num_locations = len(distance_matrix)
    tour = list(range(num_locations))
    best_distance = twoOptDistance(tour, distance_matrix)

    improvement = True
    while improvement:
        improvement = False
        for i in range(1, num_locations - 1):
            for j in range(i + 1, num_locations):
                new_tour = tour[:i] + tour[i:j + 1][::-1] + tour[j + 1:]
                new_distance = twoOptDistance(new_tour, distance_matrix)
                if new_distance < best_distance:
                    tour = new_tour
                    best_distance = new_distance
                    improvement = True
        if not improvement:
            break
    return tour, best_distance

# Find the distance between two addresses in the distanceData matrix
def distanceBetween(address1, address2, address_to_index, distanceData):
    index1 = address_to_index[address1]
    index2 = address_to_index[address2]
     # Get the distance from index1 to index2
    distance = distanceData[index1][index2]
     # If the distance is 0.0 (assuming this represents an empty value), try the opposite
    if distance == 0.0 and index1 != index2:  # We check index1 != index2 to avoid self-distances which are correctly 0.0
        distance = distanceData[index2][index1]
    return distance

def truckDeliverPackagesBestTour(truck, address_to_index, distanceData, hashTable):
    total_miles = 0
    delivered_package_ids = []

    for i in range(len(truck.truckPackagesBestTour) - 1):
        package = truck.truckPackagesBestTour[i]
        next_package = truck.truckPackagesBestTour[i + 1]

        address1 = package.address
        address2 = next_package.address

        distance = distanceBetween(address1, address2, address_to_index, distanceData)
        delivery_time = timeToDeliver(distance)

        total_miles += distance
        truck.current_time += delivery_time

        hashTable.update_package_status(package.package_id, "delivered", truck.current_time)
        delivered_package_ids.append(package.package_id)

    print(f"Total miles traveled by Truck {truck.truck_id}: {total_miles}")
    return delivered_package_ids


# Update the delivery status of each package and calculate the time taken for delivery
def timeToDeliver(distance):
    hours = distance / 18  # Truck speed is 18 mph
    return datetime.timedelta(hours=hours)
