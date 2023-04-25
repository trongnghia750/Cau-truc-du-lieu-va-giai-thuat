

class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None
        self.prev = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            current_node = self.head
            while current_node.next is not None:
                current_node = current_node.next
            current_node.next = new_node
            new_node.prev = current_node

    def remove(self, data):
        if self.head is None:
            return

        if self.head.data == data:
            self.head = self.head.next
            self.head.prev = None
            return

        current_node = self.head
        while current_node.next is not None:
            if current_node.next.data == data:
                current_node.next = current_node.next.next
                if current_node.next is not None:
                    current_node.next.prev = current_node
                return
            current_node = current_node.next

    def display(self):
        current_node = self.head
        while current_node is not None:
            print(current_node.data)
            current_node = current_node.next
a= int(input('Nhap a='))
b= int(input('Nhap b='))
c= int(input('Nhap c='))
d= int(input('Nhap phan tu can xoa='))
my_list = DoublyLinkedList()
my_list.append(a)
my_list.append(b)
my_list.append(c)
print("danh sach phan tu")
my_list.display()
print("kết quả:\n")
my_list.remove(d)
my_list.display()