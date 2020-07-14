class Node:
  def __init__(self, value):
    self.left = None
    self.right = None
    self.value = value

class BinarySearchTree:
  def __init__(self):
    self.root = None

  def insert(self, value):
    newNode = Node(value)
    if self.root == None:
      self.root = newNode
    else:
      currentNode = self.root
      while(currentNode):
        if newNode.value < currentNode.value:
          if currentNode.left == None:
            currentNode.left = newNode
            return self
          else:
            currentNode = currentNode.left
        else:
          if currentNode.right == None:
            currentNode.right = newNode
            return self
          else:
            currentNode = currentNode.right 

  def lookup(self, value):
    if self.root == None:
      return False

    currentNode = self.root
    while(currentNode):
      if value == currentNode.value:
        return currentNode
      if value < currentNode.value:
        currentNode = currentNode.left
      else:
        currentNode = currentNode.right
    return False

  # def remove(self, value):


tree = BinarySearchTree();
tree.insert(9)
tree.insert(4)
tree.insert(6)
tree.insert(20)
tree.insert(170)
tree.insert(15)
tree.insert(1)

tree.lookup(213)
tree.lookup(1)
tree.lookup(9)
tree.lookup(0)


#     9
#  4     20
#1  6  15  170

# print(tree.root.value)
# print(tree.root.left.value)
# print(tree.root.right.value)
# print(tree.root.left.left.value)
# print(tree.root.left.right.value)
# print(tree.root.right.left.value)
# print(tree.root.right.right.value)