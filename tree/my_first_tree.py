from node import Node


child1 = Node(2)
child2 = Node(3)

root = Node(1)
root.left=child1
root.right=child2

print(root)
l=[]
l.append(root)
print(l)
l.pop(0)
print(l)
