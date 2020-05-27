# solution
def findNumberOfParents(root):
    parentList = []
    postOrderTraversal(root, parentList)
    return len(parentList)
def postOrderTraversal(root, parentList):
    if not root:
        return
    
    postOrderTraversal(root.left, parentList)
    postOrderTraversal(root.right, parentList)
    if (root.left and root.right) or (not root.left and root.right) or (root.left and not root.right):
        # print(root.value)
        parentList.append(root.value)
    

def checkAnswer(developerAnswer, moduleAnswer):
    return developerAnswer == moduleAnswer

def main():
    from binarytree import tree,bst,heap # https://pypi.org/project/binarytree/
    root = tree(height=3)
    print(root)
    print(findNumberOfParents(root))
    print(checkAnswer(findNumberOfParents(root), root.size - root.leaf_count))



if __name__ == '__main__':
    main()
