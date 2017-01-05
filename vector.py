import math
"""Import the math module"""

class Vector(object):
    """This object represents a vector"""
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

    def __eq__(self, v_vector):
        return self.coordinates == v_vector.coordinates

    def __add__(self, v_vector):
        result_coordinates = [x+y for x, y in zip(self.coordinates, v_vector.coordinates)]
        return Vector(result_coordinates)

    def __sub__(self, v_vector):
        result_coordinates = [x-y for x, y in zip(self.coordinates, v_vector.coordinates)]
        return Vector(result_coordinates)

    def times_scalar(self, scale):
        """Calculates the scalar multiplier of the vector by scale"""
        result_coordinates = [x * scale for x in self.coordinates]
        return Vector(result_coordinates)

    def magnitude(self):
        """Calculates the magnitude of the vector"""
        coordinates_squared = [x**2 for x in self.coordinates]
        return math.sqrt(sum(coordinates_squared))

    def normalized(self):
        """Calculcate the normal (direction) of the vector"""
        try:
            magnitude = self.magnitude()
            return self.times_scalar(1.0/magnitude)

        except ZeroDivisionError:
            raise Exception('Cannot normalize the zero vector')

    def dot_product(self, v_vector):
        """Calculates the dot product of the vector and v_vector"""
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

V = Vector([-0.221, 7.437])
print "The magnitude of", V, "is", V.magnitude()

V = Vector([8.813, -1.331, -6.247])
print "The magnitude of", V, "is", V.magnitude()

V = Vector([5.581, -2.136])
print "The direction of", V, "is", V.normalized()

V = Vector([1.996, 3.108, -4.554])
print "The normal vector of", V, "is", V.normalized()

V = Vector([0, 0, 0])
print "The normal vector of", V, "is", V.normalized()
