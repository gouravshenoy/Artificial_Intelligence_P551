## Graph Travesals

### Description
This program implements different graph traversal algorithms such as BFS, DFS, Iterative Deepening to find the path between a source and destination.

### Requirements

To execute the program, you need an input file that describes a map in the following format:

    Oradea,Zerind,71
    Oradea,Sibiu,151
    Zerind,Arad,75
    ...

Sample input files can be found in the folder:

    graph_traversal/data/


### Usage

usage: graph_traversal.py [-h] FILE

positional arguments:
  FILE        Input file specifying graph (map) paths

optional arguments:
  -h, --help  show this help message and exit


### Sample Output

Program run using data/romania.txt file as input for BFS, DFS:

    $ python graph_traversal.py data/romania.txt
    Enter source city: arad
    Enter destination city: bucharest
    Enter the search technique (BFS/DFS/Iterative Deepening): bfs
    Reached destination, Path = [arad -> sibiu -> fagaras -> bucharest], Cost = 450
    ************** COMPLETE ****************

    Do you wish to re-run the program? (Yes/No): yes
    Enter source city: arad
    Enter destination city: bucharest
    Enter the search technique (BFS/DFS/Iterative Deepening): dfs
    Reached destination, Path = [arad -> sibiu -> rimnicu vilcea -> piteshi -> bucharest], Cost = 418
    ************** COMPLETE ****************

    Do you wish to re-run the program? (Yes/No): yes
    Enter source city: arad
    Enter destination city: bucharest
    Enter the search technique (BFS/DFS/Iterative Deepening): iterative deepening
    Reached destination, Path = [arad -> sibiu -> fagaras -> bucharest], Cost = 450, Iteration Level = 4
    ************** COMPLETE ****************

    Do you wish to re-run the program? (Yes/No): no
    Exiting Now!