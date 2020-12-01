class Gym_Class:
    def __init__(self, name, capacity, fill_up_occupancy, size_of_class, id=None):
        self.name = name
        self._capacity = capacity
        self.members = []
        self.fill_up_occupancy = fill_up_occupancy
        self.size_of_class = 0
        self.id = id

    # Need to increment number of members joining class and then stop when limit reached
    
    def get_capacity(self):
        return self._capacity

    def free_spaces(self):
        return self._capacity - len(self.members)

    def add_to_size_of_class(self, occupancy):
        self.size_of_class += occupancy

    def book_in_member(self, member):
        if self.free_spaces() <= 30 and member.wants_to_attend(self.fill_up_occupancy):
            member.fill(self.fill_up_occupancy)
            self.size_of_class += self.fill_up_occupancy
            self.members.append(member)







   