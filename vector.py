import math

class Vector(object):
    """This object represents a vector"""

    CANNOT_NORMALISZE_ZERO_VECTOR_MSG = 'Cannot normalize a zero vector'

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
            raise Exception(self.CANNOT_NORMALISZE_ZERO_VECTOR_MSG)

    def dot_product(self, v_vector):
        """Calculates the dot product of this vector and v_vector"""
        coordinates_multiplied = [x*y for x, y in zip(self.coordinates, v_vector.coordinates)]
        return sum(coordinates_multiplied)

    def angle_of(self, v_vector, in_degrees=False):
        """Calculates the angle between two vectors"""
        try:
            dot_product = self.dot_product(v_vector)
            magnitude_self = self.magnitude()
            magnitude_v_vector = v_vector.magnitude()
            if in_degrees:
                return math.degrees(math.acos(dot_product/(magnitude_self*magnitude_v_vector)))
            else:
                return math.acos(dot_product/(magnitude_self*magnitude_v_vector))

        except Exception as error:
            if str(error) == self.CANNOT_NORMALISZE_ZERO_VECTOR_MSG:
                raise Exception("Cannot compute an angle with zero vector")
            else:
                raise error

# ADDING, SUBTRACTING AND SCALAR MULTIPLICATION

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

# MAGNITUDE AND DIRECTION

#V = Vector([-0.221, 7.437])
#print "The magnitude of", V, "is", V.magnitude()

#print "The magnitude of", V, "is", V.magnitude()
#V = Vector([8.813, -1.331, -6.247])

#V = Vector([5.581, -2.136])
#print "The direction of", V, "is", V.normalized()

#V = Vector([1.996, 3.108, -4.554])
#print "The normal vector of", V, "is", V.normalized()

#V = Vector([0, 0, 0])
#print "The normal vector of", V, "is", V.normalized()

V = Vector([7.887, 4.138])
W = Vector([-8.802, 6.776])
print "The dot product of ", V, "and", W, "is", V.dot_product(W)

V = Vector([-5.955, -4.904, -1.874])
W = Vector([-4.496, -8.755, 7.103])
print "The dot product of ", V, "and", W, "is", V.dot_product(W)

V = Vector([3.183, -7.627])
W = Vector([-2.668, 5.319])
print "The angle between ", V, "and", W, "is", V.angle_of(W, False)

V = Vector([7.35, 0.221, 5.188])
W = Vector([2.751, 8.259, 3.985])
print "The angle between ", V, "and", W, "is", V.angle_of(W, True)
