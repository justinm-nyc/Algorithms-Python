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

  # def lookup(self, value):

  # def remove(self, value):


tree = BinarySearchTree();
tree.insert(9)
tree.insert(4)
tree.insert(6)
tree.insert(20)
tree.insert(170)
tree.insert(15)
tree.insert(1)


#     9
#  4     20
#1  6  15  170
