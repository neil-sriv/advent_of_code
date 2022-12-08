from pathlib import Path
from pprint import pprint
from typing import Dict, List, Tuple

import ipdb
from anytree import Node, RenderTree

TOTAL_DISK_SPACE = 70_000_000
UNUSED_SPACE = 30_000_000

dir_path = Path(__file__).resolve().parent
with open(f"{dir_path}/day7_input.txt") as file:
	data = file.read().splitlines()


def build_tree(data: List[str]) -> Tuple[Node, Dict[str, Node]]:
	root = Node(name="root", size=0, type="folder", filepath="/root")
	folders: Dict[str, Node] = {'/root': root}
	current_folder = root
	for line in data[1:]:
		words = line.split(" ")
		first, second = words[0:2]
		match first:
			case "$":
				if second == "cd":
					third = words[2]
					if third == "..":
						current_folder = current_folder.parent
					else:
						folder_path = f"{current_folder.filepath}/{third}"
						current_folder = folders[folder_path]
			case "dir":
				folder_path = f"{current_folder.filepath}/{second}"
				folders[folder_path] = Node(name=second, filepath=folder_path, size=0, type="folder", parent=current_folder)
			case _:
				Node(name=second, size=int(first), type="file", parent=current_folder)
	return root, folders

def _compute_sizes(root: Node, small_sizes: List[Node]):
	# print(f"Start computing size of {root.name}")
	if not root.children:
		return 0
	total_size = 0
	for node in root.children:
		if node.type =="folder":
			total_size+=_compute_sizes(node, small_sizes)
		else:
			total_size+=node.size
	root.size = total_size
	# print(f"Node {root.name} has size: {root.size}")
	if root.size <= 100_000:
		small_sizes.append(root)
	return root.size

def _find_smallest_large_enough(folders: Dict[str, Node], space: int) -> Node:
	smallest = folders['/root']
	# pprint(folders.keys())
	for _, node in folders.items():
		if node.size < space:
			continue
		if node.size < smallest.size:
			smallest = node
	return smallest

root_node, folders = build_tree(data)
small = list()
_compute_sizes(root_node, small)
smallest_node = _find_smallest_large_enough(folders, UNUSED_SPACE-(TOTAL_DISK_SPACE-folders['/root'].size))
# print(sum([node.size for node in small]))
print(smallest_node)
# print(RenderTree(root_node))