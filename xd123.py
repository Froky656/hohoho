i = int(input("Четырёхзначное число:")) #123

j = i/10 #12.3
k = int(j) #12
l = j - k #0.3
h = l*10 #3
N = round(h)#ТОЧНО 3

j1 = k/10 #1.2
k1 = int(j1) #1
l1 = j1 - k1 #0.2
h1 = l1*10 #2
N1 = round(h1) #ТОЧНО 2

j2 = k1/10
k2 = int(j2)
l2 = j2 - k2
h2 = l2*10
N2 = round(h2)

j3 = k2/10
k3 = int(j3)
l3 = j3 - k3
h3 = l3*10
N3 = round(h3)

print(N3,N2,N1,N)

