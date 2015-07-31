from collections import deque
from Graph import Graph

class Breadth_First_Search():
    def __init__(self, G, s):
        self.marked = [False] * G.get_Vertices()
        self.edge_to = [None] * G.get_Vertices()        
        self.s = s
        self.cnt = 0
    ##distance is a dictionary, {each vertice: distance from this vertice to the starting point}
        self.distance = {} 
        for vertice in G.adj:
            self.distance[vertice] = 'inf'            
        self.bfs(G, s)
        
    def __str__(self):
        pass

    def bfs(self, G, v):        
        self.marked[v] = True
        self.distance[v] = 0        
        queue = deque([])
        queue.append(v)       
        while len(queue):
            print 'the current queue is: ', queue
            x = queue.popleft()
            for w in G.adj[x]:
                if not self.marked[w]:
                    self.marked[w] = True
                    queue.append(w)
                    self.edge_to[w] = x
                    self.distance[w] = self.distance[x] + 1
                    
    ## path from the starting point to the point v
    def path_to(self, v):
        path = []
        if self.edge_to[v] == None:
            return None
        while v is not self.s:
            path.append(v)
            v = self.edge_to[v]
        path.append(self.s)
        return path
    
    ## print the distance for each vertice in the graph to the starting point
    def show_distance(self):
        print ''
        for vertice in self.distance:
            print 'distance from ' + str(vertice) + ' to ' +str(self.s) + ': '\
                  + str(self.distance[vertice])

    ## print the paths for each vertice in the graph to the starting point
    def show_path_to(self, G):
        print ''
        for vertice in G.get_adj_list():            
            if self.path_to(vertice) == None:
                print 'From '+ str(self.s) + ' to ' +str(vertice) + ': ', 'None'
            else:
                path = self.path_to(vertice)
                path.reverse()
                print 'From '+ str(self.s) + ' to ' +str(vertice) + ': ', path       

   
def main():
    try:
        filename = raw_input('Please input the file name: ')
        G = Graph(filename)
        print G
    except:
        print 'Canot open the file: ' + filename
    try:
        vertice = raw_input('please input the vertice: ')
        BFS = Breadth_First_Search(G, int(vertice))    
        BFS.show_path_to(G)
        BFS.show_distance()
    except:
        print 'ERROR'

          
    
if __name__ == '__main__':
    main()
        
    
