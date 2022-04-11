import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

tree = {}
arr = []
while True:
    try:
        new_node = int(input())
        arr.append(new_node)
        tree[new_node] = ['','']
    except:
        break

def make_tree(root,target):

    if tree[root][0] != '' and target <= root:
        make_tree(tree[root][0],target)

    elif tree[root][1] != '' and target > root:
        make_tree(tree[root][1],target)

    elif tree[root][1] == '' and target > root:
            tree[root][1] = target

    elif tree[root][0] == '' and target <= root:
            tree[root][0] = target

def postorder(root):
    if root != '':
        postorder(tree[root][0])
        postorder(tree[root][1])
        print(root)

for i in range(1,len(arr)):
    make_tree(arr[0],arr[i])
postorder(arr[0])


