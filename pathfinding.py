from collections import deque
from functools import lru_cache
import heapq
import math

class PathFinding:
    def __init__(self,game):
        self.game=game
        self.map=game.map.mini_map
        self.ways=[-1,0],[0,-1],[1,0],[0,1],[-1,-1],[1,-1],[1,1],[-1,1]
        self.graph={} 
        self.get_graph()


    @lru_cache
    def get_path(self,start,goal):
        self.visited=self.a_star(start,goal,self.graph)
        path=[goal]
        step=self.visited.get(goal,start)

        while step and step!=start:
            path.append(step)
            step=self.visited.get(step, start)
        return path[-1]

    def heuristic(self, p1, p2):
        return max(abs(p1[0] - p2[0]), abs(p1[1] - p2[1]))

    def a_star(self,start,goal,graph):
        pq = [(0, start)]
        visited={start:None}
        g_score = {start: 0}

        while pq:
            current_f, current_node = heapq.heappop(pq)
            if current_node==goal:
                break
            
            next_nodes = graph.get(current_node, [])

            for next_node in next_nodes:
                if next_node not in self.game.object_handler.npc_positions:
                    tentative_g_score = g_score[current_node] + 1
                    
                    if next_node not in g_score or tentative_g_score < g_score[next_node]:
                        g_score[next_node] = tentative_g_score
                        f_score = tentative_g_score + self.heuristic(next_node, goal)
                        heapq.heappush(pq, (f_score, next_node))
                        visited[next_node] = current_node

        return visited

        

    def get_next_nodes(self,x,y):
        return[(x+dx,y+dy)for dx,dy in self.ways if (x+dx,y+dy) not in self.game.map.world_map]
       

    def get_graph(self):
        for y,row in enumerate(self.map):
            for x,col in enumerate(row):
                if not col:
                    self.graph[(x,y)]=self.graph.get((x,y),[])+self.get_next_nodes(x,y)


    