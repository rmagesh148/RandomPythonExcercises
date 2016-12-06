import json
import math
import operator

class Origin(object):
    """
    input: x, y (Integer Values)
    return: None
    """
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Solution(object):
    def __init__(self):
        pass

    def __getEuclideanDistance__(self, coordinates_data, origin):
        """
        method: finds the euclidean distance and stores in a dictionary
        input: coordinates_data -> Dict containing key as the id and value as the data points from Json
        origin -> Origin is the point with x and y (Integer type)
        return: None
        """
        sorted_distance = {}
        distance = {}
        for key, value in coordinates_data.iteritems():
            point = value.split(',')
            sqr=((origin.x - int(point[0])))**2 + ((origin.y - int(point[1])))**2 
            distance[key]= math.sqrt(sqr)
            sorted_distance = sorted(distance.items(),key = operator.itemgetter(1))
        for key in sorted_distance:
            print coordinates_data[key[0]]
            
    def result(self, origin):
        """
        method: Prints the value closest to the origin point
        Input: Origin(Integer) values of x and y
        return: None
        """
        json_data = open("coordinates.json").read()
        json_coordinates = json.loads(json_data) #Change this input file 
        
        coordinates_data = {}
        
        for data in json_coordinates:
            coordinates_data[data['id']] = data['value']
        self.__getEuclideanDistance__(coordinates_data, origin)

x_value = int(input("Please enter the origin value X-Coordinate:"))
y_value = int(input("Please enter the origin value Y-Coordinate:"))

origin = Origin(x_value, y_value)

solution = Solution()

solution.result(origin)
