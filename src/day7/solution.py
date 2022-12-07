"""
https://adventofcode.com/2022/day/7

>>> test_input_str = '''$ cd /
... $ ls
... dir a
... 14848514 b.txt
... 8504156 c.dat
... dir d
... $ cd a
... $ ls
... dir e
... 29116 f
... 2557 g
... 62596 h.lst
... $ cd e
... $ ls
... 584 i
... $ cd ..
... $ cd ..
... $ cd d
... $ ls
... 4060174 j
... 8033020 d.log
... 5626152 d.ext
... 7214296 k'''
>>> main(test_input_str)
95437
24933642
>>> main()
1770595
2195372
"""

import re


def input_provider(input_str=None):
    if input_str:
        for s in input_str.split("\n"):
            yield s
    else:
        with open("input.txt", "r") as f:
            for ll in f:
                yield ll.rstrip()


def traverse(d):
    for _, v in d.items():
        if type(v) is dict:
            yield from traverse(v)
        else:
            yield v


def get_dir_sizes(t, max_dir_size=None, min_dir_size=None):
    if max_dir_size and min_dir_size:
        raise ValueError("Max or min size, not both")
    for _, v in t.items():
        if type(v) is dict:
            s = sum(traverse(v))
            if max_dir_size:
                if s <= max_dir_size:
                    yield s
            elif min_dir_size:
                if s >= min_dir_size:
                    yield s
            else:
                yield s
            yield from get_dir_sizes(
                v, max_dir_size=max_dir_size, min_dir_size=min_dir_size
            )


def main(input_str=None):
    ls_mode = False
    size_buf = 0
    tree = {}
    current_element = tree
    elements_in_path = []

    for line in input_provider(input_str):
        if ls_mode:
            size = re.search(r"\d+", line)
            size_buf += int(size[0] if size else 0)
            current_element["size"] = size_buf
        if line == "$ ls":
            ls_mode = True
            size_buf = 0
        elif line[:4] == "$ cd":
            ls_mode = False
            size_buf = 0
            dir_name = line[5:]
            if dir_name == '..':
                elements_in_path.pop()
                current_element = elements_in_path[-1]
                continue
            val = current_element.get(dir_name)
            if val is None:
                current_element[dir_name] = {}
            elements_in_path.append(current_element.get(dir_name))
            current_element = current_element[dir_name]



    # Part 1 solution
    print(sum(get_dir_sizes(tree, max_dir_size=100000)))

    # Part 2 solution
    total_space = 70000000
    needed_free_space = 30000000
    current_space = max(get_dir_sizes(tree))
    needed_space_to_free_up = current_space - (total_space - needed_free_space)
    print(min(get_dir_sizes(tree, min_dir_size=needed_space_to_free_up)))


if __name__ == "__main__":
    import doctest
    doctest.testmod()
