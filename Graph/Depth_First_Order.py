''' This program is used for find the topological order of a given graph'''
''' And also, it provides the reversed topological list of a graph, which will be useful
    in the KosarajuSCC program to find out the strongly connected components (SCC)'''


##the first 'Graph' represents 'Graph.py',
##the second 'Graph' is the class name of 'Graph'
from collections import deque
from Digraph import Digraph
class Depth_First_Order():
    def __init__(self, G):

        self.marked = [False] * G.get_Vertices()
        #self.s = s ##s is the starting point of the depth first search
        self.cnt = 0
        #self.pre_queue = deque([])
        #self.post_queue = deque([])
        self.in_stack = []
        self.post_stack = [] ##ni hou xu

        self.topo_order(G)

    def __str__(self):
        pass

    def is_marked(self, v):
        return self.marked[v]
## the pre_queue records the order when the vertice was first pushed into the dfs stack
## the post_queue records the order when the vertice was done and returned
    def dfs(self, G, v):        
        self.marked[v] = True
        self.cnt += 1
        self.in_stack.append(v) ##when the v was called, put it in the stack
        print 'the vertices in the stack are: ' + str(self.in_stack)
        
        #self.pre_queue.append(v)
        #print self.pre_queue
        for w in G.get_adj_list()[v]:
            
            if not self.marked[w]:
                self.dfs(G, w)
                
              
        #self.post_queue.append(v)
        self.post_stack.append(v)

        ##when the vertice v was done, remove it from the stack       
        self.in_stack.remove(v)

       

    def get_cnt(self):
        return self.cnt
    
                
## find the topological list of the graph G, return the topological order list
    def topo_order(self, G):
        for v in G.get_adj_list():
            if not self.marked[v]:
                self.dfs(G, v)
    
               
    def topo_list(self):
        x = self.post_stack[::-1]
        return x

    def show_topo_order(self):
        s = ''
        for i in range(len(self.post_stack) - 1, -1, -1):
            
            s += str(self.post_stack[i])
            if i > 0:
                s += ' -> '
        print s
    

    
def main():
    filename = raw_input('input the graph path: ')
    G = Digraph(filename)
    print 'The adjacent table of the input Graph is: \n'
    print G

    print ''
    #Start_point = raw_input('input the start point: ')
    DFS = Depth_First_Order(G)
    print '\nThe order used for the SCC search of orininal G is:: '
    print DFS.topo_list()
    print '\nThe toplocical order the the graph is: '
    DFS.show_topo_order()
    
    print '----------------the reversed G------------------'
    print G.reverse()
    DFS = Depth_First_Order(G.reverse())
    print '\nThe order used for the SCC of reversed G is: '
    print DFS.topo_list()
    print '\nThe toplocical order the the reversed graph is: '
    DFS.show_topo_order()



if __name__ == '__main__':
    main()

        
        
        
    
