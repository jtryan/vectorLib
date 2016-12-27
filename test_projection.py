from vector import Vector

v = Vector(['3.039', '1.879'])
w = Vector(['0.825', '2.036'])

print v.component_parallel_to(w)


v = Vector([-9.88, -3.264, -8.159])
w = Vector([-2.155, -9.353, -9.473])

print v.component_orthogonal_to(w)

v = Vector([3.009, -6.172, 3.692, -2.51])
w = Vector([6.404, -9.144, 2.759, 8.718])

vpar = v.component_parallel_to(w)
wpar = v.component_orthogonal_to(w)

print vpar
print wpar


v = Vector([8.462, 7.893, -8.187])
w = Vector([6.984, -5.975, 4.778])

print v.cross(w)


v = Vector([-8.987, -9.838, 5.031])
w = Vector([-4.268, -1.861, -8.866])

print v.area_parallelagram(w)

v = Vector([1.5, 9.547, 3.691])
w = Vector([-6.007, 0.124, 5.772])

print v.area_triangle(w)
