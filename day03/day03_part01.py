import sys

RISE = 1
RUN = 3


def get_maze(input_file):
    maze = []
    with open(input_file, 'r') as f:
        for line in f.readlines():
            maze.append(line.strip('\n'))

    return maze


def is_tree(maze, i, j, maze_width):
    j = j % maze_width

    return maze[i][j] == '#'


def count_trees(maze):
    i, maze_height = 0, len(maze)
    j, maze_width = 0, len(maze[0])
    tree_count = 0

    while i < maze_height: 
        if is_tree(maze, i, j, maze_width):
            tree_count += 1

        i += RISE
        j += RUN

    return tree_count


def main():
    if(len(sys.argv) != 2):
        print("usage: python3 day03_part01.py maze_file")
        exit(-1)

    maze = get_maze(sys.argv[1])
    tree_count = count_trees(maze)

    print("there are {} trees".format(tree_count))


if __name__ == "__main__":
    main()
