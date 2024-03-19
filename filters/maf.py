# this file implements a moving average filter for any raw sensor values. 

class MovingAverageFilter:
    def __init__(self, window_size):
        self.window_size = window_size
        self.window = []
    
    def add(self, value):
        self.window.append(value)
        if len(self.window) > self.window_size:
            self.window.pop(0)
    
    def get_average(self):
        return sum(self.window) / len(self.window)
