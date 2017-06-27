#python 2

import sys

class Dis_Set(object):
    
    def __init__(self, number_of_elements, number_of_rows):
        self.parent = range(number_of_elements)
        self.rank = number_of_rows
        
    def __str__(self):
        return "parent: " + str(self.parent) +"\nrank: " + str(self.rank)
    
    def find(self, i):
        #print "i:", i, "parent[i]", self.parent[i]
        if i != self.parent[i]:
            #print "we are here"
            self.parent[i] = self.find(self.parent[i])
            #print self.parent
        return self.parent[i]
    
    def get_rank(self):
        return self.rank

    def union(self, i, j):
        global maximum
        i_id = self.find(i)
        j_id = self.find(j)
        if i_id == j_id:
            return
        else:
            self.parent[j_id] = i_id
            self.rank[i_id] += self.rank[j_id]
            self.rank[j_id] = 0
            if self.rank[i_id] > maximum:
                maximum = self.rank[i_id]
            #if self.rank[i_id] == self.rank[j_id]:
            #    self.rank[j_id] = self.rank[j_id] + 1
        #print max(self.rank)

dis_set = Dis_Set(5, [1]*5)
print dis_set
