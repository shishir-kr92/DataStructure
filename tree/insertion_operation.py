class Node:
	def __init__(self, key):
		self.left = None
		self.right = None
		self.key = key

def inorder_transversal(tree):
	if not tree:
		return 
	inorder_transversal(tree.left)
	print(tree.key, end = " ")
	inorder_transversal(tree.right)

def insert(tree, key):
	q = [tree]

	while(len(q)):
		temp = q[0]
		q.pop(0)

		if not temp.left:
			temp.left = Node(key)
			break
		else:
			q.append(temp.left)

		if not temp.right:
			temp.right = Node(key)
			break
		else:
			q.append(temp.right)


if __name__ == "__main__":
	root = Node(10)
	
	root.left = Node(11)
	root.right = Node(9)

	root.left.left = Node(7)

	root.right.left = Node(15)
	root.right.right = Node(8)
	print("inorder transversal")
	inorder_transversal(root)
	print()
	insert(root, 12)
	inorder_transversal(root)
	print()


