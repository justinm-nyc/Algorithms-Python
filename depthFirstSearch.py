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

  def DFSInOrder(self):
    return self.traverseInOrder(self.root, [])

  def DFSPostOrder(self):
    return self.traversePostOrder(self.root, [])

  def DFSPreOrder(self):
    return self.traversePreOrder(self.root, [])
  
  def traverseInOrder(self, node, myList):
    if(node.left != None):
      self.traverseInOrder(node.left, myList)
    myList.append(node.value)
    if(node.right != None):
      self.traverseInOrder(node.right, myList)
    return myList

  def traversePreOrder(self, node, myList):
    myList.append(node.value)
    if(node.left != None):
      self.traversePreOrder(node.left, myList)
    if(node.right != None):
      self.traversePreOrder(node.right, myList)
    return myList


  def traversePostOrder(self, node, myList):
    if(node.left != None):
      self.traversePostOrder(node.left, myList)
    if(node.right != None):
      self.traversePostOrder(node.right, myList)
    myList.append(node.value)
    return myList


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

tree.DFSInOrder()
tree.DFSPreOrder()
tree.DFSPostOrder()


#     9
#  4     20
#1  6  15  170
