from vector import Vector

v = Vector(['-7.579', '-7.88'])
w = Vector(['22.737', '23.64'])

print "Is Parallel: ", v.is_parallel_to(w)
print "Is Orthogonal: ", v.is_orthogonal_to(w)

v = Vector([-2.029, 9.97, 4.172])
w = Vector([-9.231, -6.639, -7.245])

print "Is Parallel: ", v.is_parallel_to(w)
print "Is Orthogonal: ", v.is_orthogonal_to(w)

v = Vector([-2.328, -7.284, -1.214])
w = Vector([-1.821, 1.072, -2.94])

print "Is Parallel: ", v.is_parallel_to(w)
print "Is Orthogonal: ", v.is_orthogonal_to(w)

v = Vector([2.118, 4.827])
w = Vector([0, 0])

print "Is Parallel: ", v.is_parallel_to(w)
print "Is Orthogonal: ", v.is_orthogonal_to(w)