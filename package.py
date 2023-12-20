class Package:
    def __init__(self, package_id, address, city, state, zip, deadline, weight, status, special_notes, delivery_time):
        self.package_id = package_id
        self.address = address
        self.city = city
        self.state = state
        self.zip = zip
        self.deadline = deadline
        self.weight = float(weight)
        self.status = status
        self.special_notes = special_notes if special_notes is not None else ""       
        self.delivery_time = delivery_time


    def __repr__(self):
        return (f"Package ID: {self.package_id}, Address: {self.address}, City: {self.city}, "
                f"Zip: {self.zip}, Deadline: {self.deadline}, Weight: {self.weight}, "
                f"Status: {self.status}, Special Notes: {self.special_notes}" +
                (f", Delivery Time: {self.delivery_time}" if self.delivery_time else ""))
