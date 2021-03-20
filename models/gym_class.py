class Gym_Class:
    def __init__(self, title, duration, capacity, intensity, difficulty, date, time, location, id=None):
        self.title = title
        self.duration = duration
        self.capacity = capacity
        self.intensity = intensity
        self.difficulty = difficulty
        self.date = date
        self.time = time
        self.location = location
        self.id = id

    def formatted_date(self):
        return self.date.strftime("%D/%M/%Y")

    def formatted_time(self):
        return self.time.strftime("%H/%M")








   