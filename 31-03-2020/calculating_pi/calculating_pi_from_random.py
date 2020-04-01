import random
import math


class Point(object):
    def __init__(self):
        self.x = random.random()
        self.y = random.random()
        self.calculate_distance_from_origin()

    def calculate_distance_from_origin(self):
        self.distance_from_origin = math.sqrt(math.pow(self.x, 2) + math.pow(self.y, 2))
        
    def is_inside_semi_circle(self):
        return self.distance_from_origin <= 1 
    
    def print(self):
        print("( "+ str(self.x) + ", " + str(self.y) + ")")

class Bag(object):
    def __init__(self, number_of_points):
        self.points = []
        self.number_of_points = number_of_points
        self.porpotion = 0
        for i in range(number_of_points):
            self.points.append(Point())
        self.calculate_porpotion()
    ''' 
    Returns the porpotion of points inside the semi-circle
    '''
    def calculate_porpotion(self):
        self.porpotion = sum([p.is_inside_semi_circle() for p in self.points]) / self.number_of_points

    def print_points(self):
        for p in self.points:
            p.print()


class PiCalculator(object):
    def __init__(self):
        self.bags = []
        self.pi = 0
    def calculate_pi(self):
        sum_of_porpotions = 0
        for b in self.bags:
            sum_of_porpotions = sum_of_porpotions + b.porpotion
        self.pi = 4 * (sum_of_porpotions / len(self.bags))

if __name__ == "__main__":
    calculator = PiCalculator()
    calculator.bags.append(Bag(1000000))
    calculator.bags.append(Bag(1000000))
    calculator.bags.append(Bag(1000000))
    calculator.bags.append(Bag(1000000))
    calculator.bags.append(Bag(1000000))

    
    calculator.calculate_pi()
    print(calculator.pi)