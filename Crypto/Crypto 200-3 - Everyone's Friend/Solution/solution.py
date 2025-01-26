p = 61
q = 53
n = 3233
e = 17
c = ["264","889","119","374","559","357","870","453","4ce","264","77","a5d","87a","170","77","87a","b5a","a5d","119","87a","87a","b5a","2b2","170","96c","70a","77","7aa","870","b5a","6ed","170","5ec"]
int_c = []
m = ""
print("- converting c to integers -\n")
for x in c:
    int_c.append(int(x, 16))

print("-finding phi(n) -\n")
phi_n = (p-1)*(q-1)

print("- finding mod inverse -\n")
# d is the inverse of e mod phi(n)
d = pow(e, -1, phi_n)

print("- decrypting c -\n")
for x in int_c:
    m += chr(pow(x, d, n))

print(m)
