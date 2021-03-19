class Gym_Member:
    def __init__(self, first_name, last_name, age, address, phone_no, email, premium, membership_no, is_active, id=None):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.address = address
        self.phone_no = phone_no
        self.email = email 
        self.premium = premium
        self.membership_no = membership_no
        self.is_active = is_active
        self.id = id

    def full_name(self):
        full_name = self.first_name + ' ' + self.last_name
        return full_name



    