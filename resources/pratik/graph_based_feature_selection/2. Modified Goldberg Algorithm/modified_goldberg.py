from __future__ import division
import numpy as np
import math


readfile = open("cluster0.txt", 'r')
read_content = readfile.read()
all_data = read_content.splitlines()
print len(all_data)
temp_list =  list(set(all_data))
gene_id = {}
gene_counter = 0
for i in temp_list:
	gene_id[gene_counter] = str(i)
	gene_counter += 1

n = len(temp_list)  # no. of vertices
print ("no. of vertices=%d" % (n))



network = np.zeros((n + 2, n))

readfile2 = open("full_interactions.txt", 'r')
read_content2 = readfile2.read()
all_data2 = read_content2.splitlines()



for lines in all_data2:
    values2 = lines.split('\t')
    temp_list = []
    for k in range(0,2):
        try:
            temp= gene_id.keys()[gene_id.values().index(values2[k])] 
        except ValueError:
            temp =-1
        temp_list.append(temp)


    if (-1 in temp_list):
        continue;
    else:
        i = temp_list[0]
        j = temp_list[1]
        network[i][j] = values2[2]
              
m = 0  # no. of edges
writefile = open("network_matrix.txt", 'w')
for i in range(0, n):
    for j in range(0, n):
        writefile.write(str(network[i][j]))
        m = m + math.ceil(network[i][j])
        writefile.write("\t")
    writefile.write("\n")



degree_list = {}
for i in range(0, n):
    sum = 0
    for j in range(0, n):
        sum = sum + math.ceil(network[i][j])
    degree_list[i] = sum
print degree_list
print ("no. of edges=%d" % (m))


def dsgfinder(gene_id):
    u = m
    l = 0
    n2 = len(gene_id)
    count = 0
    print n, n2
    while (u - l) >= float(1 / (n2 * (n2 - 1))):
        g = (u + l) / 2
        gene_id[n2] = "source"
        gene_id[n2 + 1] = "sink"

        for lines in all_data2:
            values2 = lines.split('\t')
            for i in range(0, n2):
                if (gene_id[i] == values2[1]):
                    for j in range(0, n2):
                        if (gene_id[j] == values2[0]):
                            network[i][j] = 1
                            break
                    break

        for j in range(0, n2):
            network[n2][j] = m
            network[n2 + 1][j] = m + 2 * g - degree_list[j]

        writefile = open("Goldberg_matrix.txt", 'w')
        for i in range(0, n2 + 2):
            for j in range(0, n2):
                writefile.write(str(network[i][j]))
                writefile.write("\t")
            writefile.write("\n")
        #print "n2##n", n2 ,n
        #ch = raw_input();

        # calculating max-min cut
        count += 1
        S = {}
        for s in range(1, count):
            S[s] = gene_id[s - 1]
        S[0] = "source"

        T_counter = 0
        T = {}
        for t in range(count - 1, n2 + 1):
            if gene_id[t] != "source":
                T[T_counter] = gene_id[t]
                T_counter += 1

        V2 = {}
        V2 = T
        V1 = {}
        for v in range(1, len(S)):
            V1[v - 1] = S[v]

        deg_vertex = 0
        V1_length = len(V1)
        print V1_length
        for i in range(0, V1_length):
            for j in range(0, n2):
                if (V1[i] == gene_id[j]):
                    deg_vertex = deg_vertex + degree_list[j]

        sum_1 = 0
        print deg_vertex
        for i in range(0, V1_length):
            for j in range(0, n2):
                if (V1[i] == gene_id[j]):
                    for k in range(0, len(V2)):
                        for l in range(0, n2):
                            if V2[k] == gene_id[l]:
                                if network[j][l] == 1:
                                    sum_1 = sum_1 + 1
                else:
                    continue

        print "sum=%d" % sum_1
        print "deg_vertex=%d" % deg_vertex
        # print "v1_length=%d" % V1_length
        # print "g=%d" % g
        print "n2@@@@n", n2, n
        print (V1)
        print (V2)

        try:
            D = (deg_vertex - sum_1) / (2 * V1_length)
            print ("d1=%d" % D)
        except ZeroDivisionError:
            D = 0

        min_cut = (m * n2) + V1_length * 2 * (g - D)
        print ("min_cut=%d" % min_cut)

        if len(S) == 1 and S[0] == "source":
            u = g
        else:
            l = g

    filename = "Densest subgraph cluster0_" + str(file_counter) + ".txt"
    writefile = open(filename, 'w+')
    for j in range(0, len(V1)):
        writefile.write(str(V1[j]))
        writefile.write("\n")

    # finding the hub genes

    if file_counter==0:
        writefile3 = open("HG5.txt",'w+')
        writefile2 = open('HG3.txt', 'w+')
        writefile4 = open('unique_genes_dsg.txt', 'w+')
    else:
        writefile3=open("HG5.txt",'a')
        writefile2 = open('HG3.txt', 'a')
        writefile4 = open('unique_genes_dsg.txt', 'a')

    container_set = set(open('unique_genes_dsg.txt','r').read().split())
    print container_set
    v_set = set(V1.values())
    print v_set
    remaining_unique_set = v_set - container_set
    container_set = container_set.union(remaining_unique_set)
    remaining_unique_list = list(remaining_unique_set)
    for i in remaining_unique_list:
        writefile4.write(str(i))
        writefile4.write("\n")

    print container_set
    print remaining_unique_set


    for i in range(0, len(V1)):
        total = 0
        for j in range(0, n):
            if V1[i] == gene_id[j]:
                for k in range(0, n):
                    total = total + network[j][k]
                break
            else:
                continue
        if total >= 3:
            writefile2.write(str(V1[i]))
            writefile2.write("\n")
        if total>= 5:
            writefile3.write((str(V1[i])))
            writefile3.write("\n")

    return len(V1)


# implementation of Goldberg Algorithm
stop_counter = 0
file_counter = 0
x=0
while stop_counter <= len(all_data):
    print "all_data",len(all_data)
    if file_counter == 2:
        exit()
    send_data = {}
    send_counter = 0
    for i in range(x, len(set(all_data))):
        send_data[send_counter] = gene_id[i]
        send_counter+=1
    print send_data
    print "send_counter", send_counter
    stop_counter = dsgfinder(send_data)
    x=x+stop_counter
    print stop_counter
    file_counter += 1
    print "x, file_counter", x, file_counter
