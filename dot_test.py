from vector import Vector


v = Vector([7.887, 4.138])
w = Vector([-8.802, 6.776])

print v.dot(w)

v = Vector([-5.955, -4.904, -1.874])
w = Vector([-4.496, -8.755, 7.103])

print v.dot(w)

v = Vector([3.183, -7.627])
w = Vector([-2.668, 5.319 ])

print v.angle_with(w)

v = Vector([7.35, 0.221, 5.188])
w = Vector([2.751, 8.259, 3.985])

print v.angle_with(w, in_degrees=True)

