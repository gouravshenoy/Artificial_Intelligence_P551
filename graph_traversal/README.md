## Graph Travesals

### Description
This program implements different graph traversal algorithms such as BFS, DFS, Iterative Deepening to find the path between a source and destination.

### Requirements

To execute the program, you need an input file that describes a map in the following format:

    Oradea Zerind 71
    Oradea Sibiu 151
    Zerind Arad 75
    ...

Sample input files can be found in the folder:

    graph_traversal/data/


### Usage

Program help menu can be found using the [-h] or [--help] option:

    python graph_traversal.py -h
    usage: graph_traversal.py [-h] [--file FILE]

    optional arguments:
      -h, --help   show this help message and exit
      --file FILE  Input file specifying paths


### Sample Output

Program run using data/romania.txt file as input for BFS, DFS:

    Enter source city: arad
    Enter destination city: bucharest
    Enter the search technique (BFS/DFS/Iterative Deepening): dfs
    Reached destination, Path = arad,sibiu,rimnicu,piteshi,bucharest, Cost = 418


    Enter source city: arad
    Enter destination city: bucharest
    Enter the search technique (BFS/DFS/Iterative Deepening): bfs
    Reached destination, Path = arad,sibiu,fagaras,bucharest, Cost = 450