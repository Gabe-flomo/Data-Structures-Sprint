class Node:
  def __init__(self, value=None, next_node=None):
    # the value at this linked list node
    self.value = value
    # reference to the next node in the list
    self.next_node = next_node

  def get_value(self):
    return self.value

  def get_next(self):
    return self.next_node

  def set_next(self, new_next):
    # set this node's next_node reference to the passed in node
    self.next_node = new_next

class LinkedList:
  def __init__(self):
    # reference to the head of the list
    self.head = None

  def add_to_head(self, value):
    node = Node(value)
    if self.head is not None:
      node.set_next(self.head)
    
    self.head = node

  def contains(self, value):
    if not self.head:
      return False
    # get a reference to the node we're currently at; update this as we traverse the list
    current = self.head
    # check to see if we're at a valid node 
    while current:
      # return True if the current value we're looking at matches our target value
      if current.get_value() == value:
        return True
      # update our current node to the current node's next node
      current = current.get_next()
    # if we've gotten here, then the target node isn't in our list
    return False
  
  # reverse the pointers of each node
  # [1]->[2]->[3]->None
  # none<-[1]<-[2]<-[3]
  #
  # prev = none
  # current = head     == [1]
  # head = head.next  == [2]
  # [1] needs to point to none since it will be the new tail [none]<-[1] [2]->[3]->[none]
  # current.next = prev    (just like in a DLL)
  # prev = current     == [1]
  #
  # loop
  # 
  # prev = [1]
  # current = head     == [2]
  # head = head.next  == [3]
  # [2] needs to point to [1]
  # current.next = prev
  # prev = current
  #
  # loop
  def reverse_list(self):
    prev = None
    
    while self.head:
      # save the head as the current node
      current = self.head

      # make the new head the next value
      self.head = self.head.next_node

      # make the currents next node point to the node before it
      current.next_node = prev

      # make the previous node the old head
      prev = current

      
      

  def printlist(self):
    content = []
    head = self.head
    while head:
      content.append(head.value)
      head = head.next_node
    
    return content

ll = LinkedList()
ll.add_to_head(1)
ll.add_to_head(2)
ll.add_to_head(3)
#print(ll.printlist())
ll.reverse_list()
print(ll.printlist())