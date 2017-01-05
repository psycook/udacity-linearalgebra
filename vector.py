import math

class Vector(object):
    def __init__(self, coordinates):
        try:
            if not coordinates:
                raise ValueError
            self.coordinates = tuple(coordinates)
            self.dimension = len(coordinates)

        except ValueError:
            raise ValueError('The coordinates must be nonempty')

        except TypeError:
            raise TypeError('The coordinates must be an iterable')


    def __str__(self):
        return 'Vector: {}'.format(self.coordinates)


    def __eq__(self, v):
        return self.coordinates == v.coordinates

    def __add__(self, v):
        result_coordinates = [x+y for x, y in zip(self.coordinates, v.coordinates)]
        return Vector(result_coordinates)

    def __sub__(self, v):
        result_coordinates = [x-y for x,y in zip(self.coordinates, v.coordinates)]
        return Vector(result_coordinates)

    def times_scalar(self, scale):
        result_coordinates = [x * scale for x in self.coordinates]
        return Vector(result_coordinates)

    def magnitude(self):
        coordinates_squared = [x**2 for x in self.coordinates]  
        return math.sqrt(sum(coordinates_squared))

    def normalized(self):
        try:
            magnitude = self.magnitude()
            return self.times_scalar(1.0/magnitude)
        
        except ZeroDivisionError:
            raise Exception('Cannot normalize the zero vector')  

    def dot_product(self, v):
        dot_product = 0.0

        return dot_product

# Tutorial 1
#
#v = Vector([8.218,-9.341])
#w = Vector([-1.129, 2.111])
#result_vector = v + w
#print "The resulting addition vector is ", result_vector

#v = Vector([7.119, 8.215])
#w = Vector([-8.223, 0.878])
#result_vector = v - w
#print "The resulting subtraction vector is ", result_vector

#v = Vector([1.671,-1.012,-0.318])
#scale = 7.41
#print "The resulting scalar multiplication is ", result_vector
#result_vector = v.times_scalar(scale)

v = Vector([-0.221,7.437])
print "The magnitude of", v, "is", v.magnitude()

v = Vector([8.813,-1.331,-6.247])
print "The magnitude of", v, "is", v.magnitude()

v = Vector([5.581, -2.136])
print "The direction of",v,"is", v.normalized()

v = Vector([1.996,3.108,-4.554])
print "The normal vector of",v,"is", v.normalized()

v = Vector([0,0,0])
print "The normal vector of",v,"is", v.normalized()