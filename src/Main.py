"""script for for main"""
import CSP
import Maze
import sys

if __name__ == "__main__":
    print("hello world")
    file = str(sys.argv[1])

    with open(file) as f:
        lines = f.readlines()
    lines = [l.strip() for l in lines]

    dim = len(lines[0])
    dim2 = len(lines)
    print(dim)
    print(dim2)
    graph = ""
    for l in lines:
        graph = graph + l
