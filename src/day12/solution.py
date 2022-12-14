"""
https://adventofcode.com/2022/day/12

>>> test_input_str = '''Sabqponm
... abcryxxl
... accszExk
... acctuvwj
... abdefghi'''
>>> main(test_input_str)
31
29
>>> main()
408
399
"""



from typing import Generator
import queue

START = "S"
END = "E"

def input_provider(input_str: str = None) -> Generator[str, None, None]:
    if input_str:
        for s in input_str.split("\n"):
            yield s
    else:
        with open("input.txt", "r") as f:
            for line in f:
                yield line.rstrip()


class Vertex:
    coords: (int, int)
    parent = None
    explored = False

    def __init__(self, row, column):
        self.coords = row, column

    def __repr__(self):
        return "{} {}".format(self.__class__, self.coords)


def get_adjacent_vertices(vertex, out_grid, in_grid) -> [Vertex]:
    moves = [
        (1, 0),   # down
        (0, -1),  # left
        (-1, 0),  # up
        (0, 1),   # right
    ]
    res = []
    for move in moves:
        row, column = map(sum, zip(vertex.coords, move))
        if row < 0 or column < 0 or row >= len(out_grid) or column >= len(out_grid[-1]):
            continue
        new_move_smb = in_grid[row][column]
        current_smb = in_grid[vertex.coords[0]][vertex.coords[1]]
        if new_move_smb == "S":
            new_move_smb = "a"
        if new_move_smb == "E":
            new_move_smb = "z"
        if current_smb == "S":
            current_smb = "a"
        if current_smb == "E":
            current_smb = "z"

        if ord(new_move_smb) - ord(current_smb) > 1:
            continue

        res.append(out_grid[row][column])

    return res

def main(input_str: str = None) -> None:
    """Solve the problem using breadth-first search (BFS)"""
    
    in_grid = []
    for line in input_provider(input_str):
        in_grid.append(line)

    out_grid = []
    for r in range(len(in_grid)):
        out_grid.append([])
        for c in range(len(in_grid[-1])):
            out_grid[r].append(Vertex(r, c))

    start = None
    vertices_a: [Vertex] = []
    for r in range(len(in_grid)):
        for c in range(len(in_grid[-1])):
            if in_grid[r][c] == START:
                start = r, c
            elif in_grid[r][c] == "a":
                vertices_a.append(out_grid[r][c])

    vertices_a.append(out_grid[start[0]][start[1]])
    q = queue.Queue()
    counters = []

    for vertex_a in vertices_a:
        for r in range(len(out_grid)):
            for c in range(len(out_grid[-1])):
                out_grid[r][c].parent = None
                out_grid[r][c].explored = False

        vertex_a.explored = True
        q.queue.clear()
        q.put_nowait(vertex_a)
        end_vertex = None

        while not q.empty():
            vertex = q.get_nowait()
            if in_grid[vertex.coords[0]][vertex.coords[1]] == END:
                end_vertex = vertex
                break

            for v in get_adjacent_vertices(vertex, out_grid, in_grid):
                if v.explored:
                    continue
                v.explored = True
                v.parent = vertex
                q.put_nowait(v)

        if end_vertex is None:
            # Did not find the path to the end point from the given start point
            continue

        # Traceback the shortest path from the End to the Start
        counter = 0
        v: Vertex = end_vertex
        while True:
            if v.parent is None:
                break
            v = v.parent
            counter += 1

        counters.append(counter)

    print(counters[-1])        # part 1 answer
    print(min(counters[:-1]))  # part 2 answer


if __name__ == "__main__":
    import doctest
    doctest.testmod()
