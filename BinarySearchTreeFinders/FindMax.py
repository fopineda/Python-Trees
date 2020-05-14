# solution
def findMaxNodeOfBST(root):
    if not root.right:
        return root.value
    return findMaxNodeOfBST(root.right)

def checkAnswer(developerAnswer, moduleAnswer):
    return developerAnswer == moduleAnswer

def main():
    from binarytree import tree,bst,heap # https://pypi.org/project/binarytree/
    root = bst(height=3, is_perfect=True)
    print(root)
    print(checkAnswer(findMaxNodeOfBST(root), root.max_node_value))


if __name__ == '__main__':
    main()
