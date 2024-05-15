
class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

def insert(root, key):
    if root is None:
        return Node(key)
    else:
        if key < root.val:
            root.left = insert(root.left, key)
        else:
            root.right = insert(root.right, key)
    return root

def search (root, key):
    if root is None or root.val == key:
        return root
    if key < root.val:
        return search(root.left, key)
    return search(root.right, key)

def find_max (root):
    if root is None:
        return None
    elif root.right is None:
        return root
    else: 
        return find_max (root.right)
    
def find_min (root):
    if root is None:
        return None
    elif root.left is None:
        return root
    else:
        return find_min (root.left)
    
def sum_all (root):
    if root is None:
        return 0
    else:
        return root.val + sum_all(root.left) + sum_all(root.right)
    

# Test
root = Node(5)
root = insert(root, 3)
root = insert(root, 2)
root = insert(root, 4)
root = insert(root, 7)
root = insert(root, 6)
root = insert(root, 8)

# Пошук значення

max_val = find_max(root)
if max_val:
    print(f"Максимальне значення в дереві: {max_val.val}")
else:
    print("Дерево порожнє")

min_val = find_min (root) 
if min_val:
    print(f"Мінімальне значення в дереві: {min_val.val}")
else:
    print("Дерево порожнє")  

total = sum_all (root)
print(f"Сума всіх значень у дереві: {total}")
