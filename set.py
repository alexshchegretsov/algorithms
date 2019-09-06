"""

E = ((A\B)n(C\D))u((D\A)n(B\C))
\ - symmetric difference >>> ^
n - intersection         >>> &
u - union                >>> |
"""
A = set('0123456789')
B = set('02468')
C = set('12345')
D = set('56789')

a = A.symmetric_difference(B).intersection(C.symmetric_difference(D))
b = D.symmetric_difference(A).intersection(B.symmetric_difference(C))
# print(a.union(b))

print(((A^B) & (C^D)) | ((D^A) & (B^C)) == a | b)
