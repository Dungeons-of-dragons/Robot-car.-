# this file implements a median filter for any raw sensor values. 

class MedianFilter():
    def __init__(self, window_size):
        self.window_size = window_size
        self.window = []
    
    def add(self, value):
        self.window.append(value)
        if len(self.window) > self.window_size:
            self.window.pop(0)
    
    def get_median(self):
        return sorted(self.window)[len(self.window) // 2]

