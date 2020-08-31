class WeatherTracker(object):

    def __init__(self):
        self.sum = 0
        self.count = 0

    def insert_temperature(self, temperature):
        self.sum+= temperature
        self.count +=1

    def get_average_temperature(self):
        return self.sum/self.count

tracker = WeatherTracker()
tracker.insert_temperature(3)
tracker.insert_temperature(6)
result = tracker.get_average_temperature()
print (result)