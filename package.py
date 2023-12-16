class Package:
    def __init__(self, package_id, address, city, zip_code, deadline, weight, status, delivery_time = None):
        self.package_id = package_id
        self.address = address
        self.city = city
        self.zip_code = zip_code
        self.deadline = deadline
        self.weight = weight
        if status not in ["at the hub", "en route", "delivered"]:
            raise ValueError("Invalid status. Status must be 'at the hub', 'en route', or 'delivered'.")
        self.status = status
        self.delivery_time = delivery_time if status == "delivered" else None

    def __repr__(self):
        return (f"{self.package_id}, {self.address}, {self.deadline}, {self.city}, "
                f"{self.zip_code}, {self.weight}, {self.status}" + (f", {self.delivery_time}" if self.delivery_time else "") + ")")