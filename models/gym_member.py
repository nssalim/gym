class Gym_Member:
    def __init__(self, first_name, last_name, age, phone_number, email, id=None):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.phone_number = phone_number
        self.email = email 
        self.membership = []
        self.id = id

    # Need to control what is in imput fields
    # name should be text
    # age should be up to a 3 digit number
    # phone number a set 11 digit number
    # email should have check for @ symbol 
    # membership should be premium or standard

    def full_name(self, gym_member):
        return gym_member.first_name == self.first_name and gym_member.last_name == self.last_name

    def wants_to_attend(self, occupancy):
        return self.membership >= occupancy

    def fill(self, occupancy):
        self.membership -= occupancy
    
    def number_of_gym_members(self):
        return len(self.members)

    def book_in_members(self, members):
        if self.free_spaces() >= len(members):
            for member in members:
                self.book_in_member(member)

    def check_out_member(self, member):
        self.members.remove(member)



    