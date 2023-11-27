class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    def __str__(self):
        if self.left and self.right:
            return f"({self.left} {self.value} {self.right})"
        return str(self.value)
    
    def depth(self):
        left = self.left.depth() if self.left else 0
        right = self.right.depth() if self.right else 0
        return max(left, right) + 1