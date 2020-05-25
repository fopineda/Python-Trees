# solution that counts nodes instead of edges
def findMinDepthOfBSTByNodes(root):
    if not root:
        return 0
    
    if not root.left and not root.right:
        return 1

    if not root.left:
        return findMinDepthOfBSTByNodes(root.right) + 1

    if not root.right:
        return findMinDepthOfBSTByNodes(root.left) + 1

    return min(findMinDepthOfBSTByNodes(root.left), findMinDepthOfBSTByNodes(root.right)) + 1

def checkAnswer(developerAnswer, moduleAnswer):
    return developerAnswer == moduleAnswer

def main():
    from binarytree import tree,bst,heap, Node # https://pypi.org/project/binarytree/
    root = bst(height=3, is_perfect=True)
    # root = Node(1) 
    # root.left = Node(2) 
    # root.right = Node(3) 
    # root.left.left = Node(4) 
    # root.left.right = Node(5)
    # root.right.right = Node(10)
    # root.right.right.left = Node(11)

    # add 1 to module answer because module counts edges (N) and solution counts nodes (N+1)
    print(root)
    print(findMinDepthOfBSTByNodes(root), root.min_leaf_depth + 1)
    print(checkAnswer(findMinDepthOfBSTByNodes(root), root.min_leaf_depth + 1))


if __name__ == '__main__':
    main()
