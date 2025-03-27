from ..models.grid import Grid
from ..models.frontier import QueueFrontier
from ..models.solution import NoSolution, Solution
from ..models.node import Node


class BreadthFirstSearch:
    @staticmethod
    def search(grid: Grid) -> Solution:
        """Find path between two points in a grid using Breadth First Search

        Args:
            grid (Grid): Grid of points
            
        Returns:
            Solution: Solution found
        """
        # Initialize a node with the initial position
        node = Node("", grid.start, 0)

        # Initialize the explored dictionary to be empty
        explored = {} 
        
        # Add the node to the explored dictionary
        explored[node.state] = True
        # aplicamos test objetivo
        if node.state == grid.end:
            return Solution(node, explored)
        
        #Inicializamos la frontera, en este caso es una Cola
        frontier=QueueFrontier()
        frontier.add(node)

        while True:
            #falla si frontera vacía
            if frontier.is_empty():
                return NoSolution(explored)
            #sacar nodo de frontera
            node=frontier.remove()
            print(node.state)
            successors=grid.get_neighbours(node.state)
            
            for a in successors:
                new_pos=successors[a]
                if new_pos not in explored:
                    n1=Node("",new_pos,grid.get_cost(new_pos)+ node.cost, node,a)
                    if n1.state == grid.end:
                        return Solution(n1,explored)
                    explored[new_pos]=True
                    frontier.add(n1)



        
        return NoSolution(explored)
