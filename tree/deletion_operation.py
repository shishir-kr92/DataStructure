class Node():
	def __init__(self, key):
		self.left = None
		self.right = None
		self.key = key

	def __str__(self):
		return f"{self.left}<---{self.key}--->{self.right}"

def inorder_transversal(root):
	if not root:
		return
	inorder_transversal(root.left)
	print(root.key, end=" ")
	inorder_transversal(root.right)

def delete_deepest(root, d_node):
	q = [root]

	while len(q):
		temp = q[0]
		q.pop(0)

		if temp is d_node:
			temp = None
			return
		if temp.left:
			if temp.left is d_node:
				temp.left = None
				return
			else:
				q.append(temp.left)

		if temp.right:
			if temp.right == d_node:
				temp.right = None
				return 
			else:
				q.append(temp.right)


def deletion(root, key):

	if not root:
		return 

	if root.left == None and root.right == None:
		if root.key == key:
			root = None

	q = [root]
	key_node = None

	# find the key node and the deepest node
	# last value stored in temp will be the
	# deepest node
	while len(q):

		temp = q[0]
		q.pop(0)

		if key == temp.key:
			key_node = temp

		if temp.left:
			q.append(temp.left)
		if temp.right:
			q.append(temp.right)
	
	if key_node:
		key_node.key = temp.key
		delete_deepest(root, temp)


if __name__ == "__main__":
	root = Node(10)
	
	root.left = Node(11)
	root.right = Node(9)

	root.left.left = Node(7)
	root.left.right = Node(12)

	root.right.left = Node(15)
	root.right.right = Node(8)
	print("inorder transversal")
	inorder_transversal(root)
	print()

	deletion(root, 11)
	inorder_transversal(root)

