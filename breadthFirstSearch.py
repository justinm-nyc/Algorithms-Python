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

  def breadthFirstSearch(self):
    currentNode = self.root
    myList = []
    queue = []
    queue.append(currentNode)

    while(len(queue) > 0):
      currentNode = queue.pop(0)
      myList.append(currentNode.value)
      if(currentNode.left != None):
        queue.append(currentNode.left)
      if(currentNode.right != None):
        queue.append(currentNode.right)

    return myList

  def breadthFirstSearchRecursive(self, queue, myList):
    if (len(queue) == 0):
      return myList
    
    currentNode = queue.pop(0)
    myList.append(currentNode.value)
    if(currentNode.left != None):
      queue.append(currentNode.left)
    if(currentNode.right != None):
      queue.append(currentNode.right)

    return self.breadthFirstSearchRecursive(queue, myList)

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

tree.breadthFirstSearch()
tree.breadthFirstSearchRecursive([tree.root],[])

#     9
#  4     20
#1  6  15  170
