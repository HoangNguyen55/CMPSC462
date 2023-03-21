class BinaryTree():
    def __init__(self, items: list) -> None:
        self.items = items
        self.root: Node
        self._create_tree()
        
    def _create_tree(self):
        self.root = Node(self.items[0])
        for i in self.items[1:]:
            self.root.insert(i)

    def insert(self, val: int):
        self.items.append(val)
        self.root.insert(val)

    def in_order_traversal(self):
        self.root.in_order_traversal()

    def pre_order_traversal(self):
        self.root.pre_order_traversal()

    def post_order_traversal(self):
        self.root.post_order_traversal()

    def delete(self, val):
        try:
            self.items.pop(self.items.index(val))
            self._create_tree()
        except:
            print("Cannot remove value that is not there")

    def find(self, val):
        node: Node = self.root
        while node != None:
            if val < node.data:
                node = node.left
            elif val > node.data:
                node = node.right
            elif val == node.data:
                return node

        return None

class Node:
    def __init__(self, data: int, parent: 'Node' = None) -> None:
        self.data = data
        self.left: 'Node' = None
        self.right: 'Node' = None
    
    def in_order_traversal(self):
        if self.left != None:
            self.left.in_order_traversal()
        print(self.data)
        if self.right != None:
            self.right.in_order_traversal()

    def pre_order_traversal(self):
        print(self.data)
        if self.left != None:
            self.left.in_order_traversal()
        if self.right != None:
            self.right.in_order_traversal()

    def post_order_traversal(self):

        if self.left != None:
            self.left.in_order_traversal()
        if self.right != None:
            self.right.in_order_traversal()
        print(self.data)

    def insert(self, data: int):
        if data <= self.data:
            if self.left != None:
                self.left.insert(data)
            else:
                self.left = Node(data, self)
        else:
            if self.right != None:
                self.right.insert(data)
            else:
                self.right = Node(data, self)




t = BinaryTree([5, 1, 4, 6, 2, 3, 7, 8, 0])
t.insert(10)
f = t.find(10)
print(f"{f = }\n{f.data = }")
t.in_order_traversal()
t.delete(5)
t.delete(8)
t.delete(3)
print("-"*10)
t.in_order_traversal()