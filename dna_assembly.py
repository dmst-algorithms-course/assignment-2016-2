import os
import argparse

parser = argparse.ArgumentParser()

parser.add_argument("g", help="name of input file")

args = parser.parse_args()

f = open(args.g)

line1 = f.readline()
line1= line1.strip()
k = len(line1)

z = {}                    # pinakas geitniasis
x = 0
g = {}

f = open(args.g)

counter1 = 0            # metraei ta z

for line in f:

    line2 = line.strip()
    letters = list(line2)

    s1 = ""
    l1 = []
    l2 = []

    for i in range(0, k-1):
        s1 = s1 + letters[i]
        l1.append(letters[i])
    s2 = ""
    for i in range(1, k):
        s2 = s2 + letters[i]
        l2.append(letters[i])

    if s1 not in g:
        g[s1] = l1
    if x == 0:
        first = s1
        x = 1


    if s2 not in g:
        g[s2] = l2

    if (s1, s2) in z:
        z[( s1, s2)] = z[( s1, s2)] + 1
    else:
        z[( s1, s2)] = 1
    counter1 = counter1 + 1

q = 0


dna = []
dna.append(first)
current = 'qq'

counter2 = 0                    # metraei poses fores allaxe to current, stamataei i epanalipsi otan counter1 == counter2
while first != current and counter1 != counter2:

    if q == 0:
        current = first
        q = q + 1

    for key in g:


        if key != current and (current, key) in z:

            if z[( current, key)] != 0:
                z[( current, key)] = z[( current, key)] -1
                current = key
                dna.append(key)
                counter2 = counter2 + 1

                if current == first:
                    break



flag = 0
l = []



while counter2 != counter1:

    dna2 = list(dna)
    for i in dna2:
        first = i
        current = 'qq'
        stop = False
        if counter1 == counter2:
            break
        l = []
        

       
        while stop == False and counter1 != counter2:
           
            stop = True
            n = 0
            while current != first:

                if n == 0 :
                    current = first
                    n =1

                for key in g:
                 
                    
                    if current != key and (current , key) in z:

                        if z[( current, key )] != 0 :
                            z[( current, key )] = z[( current, key )] -1

                            current = key
                            l.append(key)
                            counter2 = counter2 + 1

                            stop = False
                            if current == first or counter1 == counter2:
                                break

    
        length = len(l)
        if length > 1:
            index = dna.index(first)

            for p in range(0 , length):
                element = l.pop()
                dna.insert(index + 1, element)



s = ''



o = len(dna)
for i in range(1, o):
	s = s + g[dna[i]][k-2]


print(s)



os.system('pause')
