__author__ = 'Gaurav-PC'

import os
import argparse
from queue import Queue


class Graph_Node:
    """
    Class represents node in a graph
    """
    def __init__(self, name, path, cost, visited):
        self.name = name
        self.path = path
        self.cost = cost
        self.visited = visited


class Path_Finder:
    """
    Class performing elementry traversal
    """
    def __init__(self, ip_file):
        self.ip_file = ip_file
        print('Input File: ' + ip_file)

    @classmethod
    def create_graph(self, ip_file):
        """
        Method to create a graph based on the input file
        :param ip_file:
        :return: map_dict
        """
        # our graph dict
        graph_dict = {}

        # read input graph file
        with open(ip_file) as fp:
            for line in fp:
                line = line.rstrip()
                cities = line.split(' ')
                city_1 = cities[0].lower()
                city_2 = cities[1].lower()
                cost = int(cities[2])

                # Add city_2 as a neighbor of city_1
                try:
                    graph_dict[city_1][city_2] = cost
                except Exception as ex:
                    graph_dict[city_1] = {city_2: cost}

                # Add city_1 as a neighbor of city_2
                try:
                    graph_dict[city_2][city_1] = cost
                except Exception as ex:
                    graph_dict[city_2] = {city_1: cost}

            print(graph_dict)
        # file closes
        return graph_dict

    def find_path(self, origin, destination, algorithm):
        """
        Method finds the path/route from source to destination
        using the requested search technique algorithm.
        :param origin:
        :param destination:
        :param algorithm:
        :return:
        """

        graph_dict = self.create_graph(self.ip_file)

        try:
            # check if source & destination cities exist
            if bool(graph_dict[origin]) is False or \
                    bool(graph_dict[destination] is False):
                raise Exception

            if algorithm == 'bfs':
                self.bfs_search(origin=origin,
                                destination=destination,
                                graph_dict=graph_dict)
            else:
                print('Invalid Search Entered!')

        except Exception as ex:
            print('Something went wrong with the search. Try again!')
            return

    @classmethod
    def bfs_search(self, origin, destination, graph_dict):
        """
        Method performs Breadth First Search (BFS)
        using queues
        :param origin:
        :param destination:
        :return:
        """

        # Basic data structures required for BFS
        queue = Queue()
        visited_list = []

        # create a node
        node = Graph_Node(name=origin,
                          path=origin,
                          cost=0,
                          visited=True)

        # enqueue city node
        queue.put(node)

        # perform till queue is empty
        while queue.empty() is False:
            current_node = queue.get()
            city_name = current_node.name
            current_path = current_node.path
            current_cost = current_node.cost

            # add to visited list
            visited_list.append(city_name)

            # check if goal state
            if city_name == destination:
                print("Reached destination, Path = " + current_path + ', Cost = ' + str(current_cost))
                return

            # get neighbouring cities
            neighbors = graph_dict[city_name]
            for city, cost in neighbors.iteritems():
                # check if city is already visited
                if city in visited_list:
                    continue

                # if not, create a new node & enqueue
                node = Graph_Node(name=city,
                                  path=current_path + ',' + city,
                                  cost=(current_cost + cost),
                                  visited=False)
                # enque node
                queue.put(node)
                # end-for-loop
        # end-while-loop

        return None


if __name__ == '__main__':
    # define the arg parser
    parser = argparse.ArgumentParser()
    parser.add_argument('--file', help='Input file specifying paths')
    args = parser.parse_args()

    # read the commandline argument
    ip_file = args.file
    ip_file = os.path.realpath(
        os.path.expanduser(ip_file))

    # get user input
    origin = raw_input("Enter source city: ")
    destination = raw_input("Enter destination city: ")
    algorithm = raw_input("Enter the search technique (BFS/DFS/Iterative Deepening): ")

    # call the class method
    path_finder = Path_Finder(ip_file)
    path_finder.find_path(origin=origin.lower(),
                          destination=destination.lower(),
                          algorithm=algorithm.lower())
