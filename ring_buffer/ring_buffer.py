from doubly_linked_list import DoublyLinkedList


class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = None
        self.storage = DoublyLinkedList()

    def append(self, item):
        # if theres still storage space
        if self.storage.length < self.capacity:
            self.storage.add_to_tail(item)
            self.current = self.storage.head
        # if the list is full start overwriting from the head
        elif self.storage.length == self.capacity:
            # while the head isnt none
            if self.current:
                print("current",self.current.value)
                # make the new item the new head
                print(f"making {item} the new head")
                self.storage.add_to_head(item)
                # remove the previous head
                print(f"removing {self.storage.head.next.value}")
                self.storage.head.next.delete()
                # make the next node the new head
                print(f"making {self.storage.head.next.value} the new head")
                self.current = self.storage.head.next
                print("current",self.current.value)
            

            



    def get(self):
        # Note:  This is the only [] allowed
        list_buffer_contents = []
        head = self.storage.head
        while head is not None:
            list_buffer_contents.append(head.value)
            head = head.next
        

        return list_buffer_contents

# ----------------Stretch Goal-------------------


class ArrayRingBuffer:
    def __init__(self, capacity):
        pass

    def append(self, item):
        pass

    def get(self):
        pass


buf = RingBuffer(3)
buf.append(1)
buf.append(2)
buf.append(3)
print(buf.get())
buf.append(4)
print(buf.get())

buf.append(5)
print(buf.get())
