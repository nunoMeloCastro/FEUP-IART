#import imp

from tracemalloc import start
from maps import *
from utils import *
from ai import *
from moves import *
from time import *
from stats import *
import matplotlib.pyplot as plt

"""
This file is only for testing and graphs, to test run python3 stats.py
You can change the values of the heuristics in the lines marked with (+)
"""


def stats(pt, s):
    p = globals()[pt]

    start_dfs = time()
    dfs(start, goal, p, s)
    end_dfs = time()
    time_dfs = float(end_dfs-start_dfs)

    # Greedy
    start_greedy = time()
    ans = greedy(start, goal, p, s, "man")  # (+)
    end_greedy = time()
    time_greedy = float(end_greedy-start_greedy)
    #print("Time Greedy: ",time_greedy)
    # print(ans)

    # BFS
    start_bfs = time()
    bfs(start, goal, p)
    end_bfs = time()
    time_bfs = float(end_bfs-start_bfs)

    # A*
    start_astar = time()
    aStar(start, goal, p, s, "man")
    end_astar = time()
    time_astar = float(end_astar-start_astar)
    # print("Time A*: ",time_astar) #(+)

    #print("Greedy ",getCostGreedy()," A*",getCostAstar())

    TimeEfficiency(time_dfs, time_bfs, time_greedy, time_astar, s)
    SpaceEfficiency(getCostDfs(), getCostBfs(),
                    getCostGreedy(), getCostAstar(), s)
    return

# creating the dataset


def TimeEfficiency(time_dfs, time_bfs, time_greedy, time_astar, stepsRequired):
    data = {'Greedy': time_greedy,
            'A*': time_astar, 'DFS': time_dfs, 'BFS': time_bfs}
    courses = list(data.keys())
    values = list(data.values())

    fig = plt.figure(figsize=(8, 4))

    # creating the bar plot
    plt.bar(courses, values, color='green',
            width=0.5)

    plt.xlabel("Algorithm")
    plt.ylabel("Time to find solution")
    plt.title("Time efficiency of Algorithms with " +
              str(stepsRequired)+" steps")
    plt.show()
    return


def SpaceEfficiency(space_dfs, space_bfs, space_greedy, space_astar, stepsRequired):
    data = {'Greedy': space_greedy,
            'A*': space_astar, 'DFS': space_dfs, 'BFS': space_bfs}
    courses = list(data.keys())
    values = list(data.values())

    fig = plt.figure(figsize=(8, 4))

    # creating the bar plot
    plt.bar(courses, values, color='green',
            width=0.5)

    plt.xlabel("Algorithm")
    plt.ylabel("Iterations to find solution")
    plt.title("Space efficiency of Algorithms with " +
              str(stepsRequired)+" steps")
    plt.show()
    return


def main():
    mapOption = str(input("Enter Map Number: "))
    mapOption = "p"+mapOption
    s = int(input("Enter Answer Size: "))
    stats(mapOption, s)
    exit()


main()

#auxiliar function
"""
def heuristic():
        labels = ['Euclidean', 'Manhattan', 'Chebyshev']
        astar_means = [0.025,0.028,0.29]
        greedy_means = [0.018,0.012,0.12]

        x = np.arange(len(labels))  # the label locations
        width = 0.35  # the width of the bars

        fig, ax = plt.subplots()
        rects1 = ax.bar(x - width/2, astar_means, width, label='A*')
        rects2 = ax.bar(x + width/2, greedy_means, width, label='Greedy')

        # Add some text for labels, title and custom x-axis tick labels, etc.
        ax.set_ylabel('Time to find solution')
        ax.set_title("Time efficiency of Algorithms with 7 steps")
        ax.set_xticks(x, labels)
        ax.legend()

        ax.bar_label(rects1, padding=3)
        ax.bar_label(rects2, padding=3)

        fig.tight_layout()

        plt.show()

heuristic()
"""
