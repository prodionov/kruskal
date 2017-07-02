#python2

import sys
import math
import heapq


class Dis_Set(object):
    
    def __init__(self, number_of_elements, number_of_rows):
        self.parent = range(1, number_of_elements + 1)
        self.rank = number_of_rows
        
    def __str__(self):
        return "parent: " + str(self.parent) +"\nrank: " + str(self.rank)
    
    def find(self, i):
        #print "i:", i, "parent[i]", self.parent[i - 1]
        if i != self.parent[i - 1]:
            #print "we are here"
            self.parent[i - 1] = self.find(self.parent[i - 1])
            #print self.parent
        return self.parent[i - 1]
    
    def get_rank(self):
        return self.rank

    def union(self, i, j):
        i_id = self.find(i)
        j_id = self.find(j)
        if i_id == j_id:
            return
        else:
            self.parent[j_id - 1] = i_id
            self.rank[i_id - 1] += self.rank[j_id - 1]
            self.rank[j_id - 1] = 0


class Edge():

    def __init__(self, info):
        self.start = info[0]
        self.end = info[1]
        self.weight = info[2]

    def __str__(self):
        return str(self.start) + " " + str(self.end) + " " + str(self.weight)

ver_num = int(sys.stdin.readline())
maximum = ver_num
#ver_num = int(ver_num.strip('').split(' '))

class Coordinates():

    def __init__(self, coor):
        self.x1 = coor[0]
        self.x2 = coor[1]

    def __str__(self):
        return "x1- %s, x2 - %s" %(self.x1, self.x2)

    def dist(self, other):
        dist_sq = math.pow((self.x1 - other.x1),2) + math.pow((self.x2 - other.x2),2)
        return math.sqrt(dist_sq)



graph = {ver: set() for ver in range(1, ver_num + 1)}
coor_list = []
edge_list = []
heap = []
#test
a = Coordinates([0, 0])
b = Coordinates([1, 1])

#print Coordinates.dist(a, b)

for i in range(ver_num):
    coor = sys.stdin.readline()
    coor = Coordinates(map(int, coor.strip('').split(' ')))
    coor_list.append(coor)

#print coor_list

for x, coor_x in enumerate(coor_list, 1):
    for y, coor_y in enumerate(coor_list[x - 1:], x):
        if x == y:
            pass
        else:
            coor_x = coor_list[x-1]
            coor_y = coor_list[y-1]
            weight = Coordinates.dist(coor_x, coor_y)
            edge = Edge([x, y, weight])
            #edge_list.append(edge)
            new_entry = [edge.weight, edge]
            heapq.heappush(heap, new_entry)

#while heap:
#    #print heapq.heappop(heap)
#    #print edge
#

def kruskal(n):
    dis_set = Dis_Set(n, [1] * n)
    #print dis_set
    answer = 0
    while heap:
        [dist, edge] = heapq.heappop(heap)
        #print edge
        start = edge.start
        end = edge.end
        if dis_set.find(start) != dis_set.find(end):
            answer += edge.weight
            dis_set.union(start, end)
    return answer

print kruskal(ver_num)


















