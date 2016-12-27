from vector import Vector

v = Vector


a = v([1,2,3])
b = v([2,4,5])
c = v([1,2,3])
s = 4

print a

print a == b
print a== c

v1a = v([8.218, -9.341])
v1b = v([-1.129, 2.111])

v2a = v([7.119, 8.215])
v2b = v([-8.223, 0.878])

scalar = 7.41
v3a = v([1.671, -1.012, -0.318])

print v.plus(v1a, v1b)
print v.minus(v2a, v2b)
print v.times_scalar(v3a,scalar)

z = v([0,1,1])

unit=([0,0,0])
one=([1,1,1])
print v.magnitude(z)