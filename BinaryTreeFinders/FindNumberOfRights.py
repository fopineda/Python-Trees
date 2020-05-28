# solution
def findNumberOfRights(root):
    rightList = []
    postOrderTraversal(root, rightList)
    return len(rightList)


def postOrderTraversal(root, rightList):
    if not root:
        return

    if root.right:
        rightList.append(root.right.value)
    
    postOrderTraversal(root.left, rightList)
    postOrderTraversal(root.right, rightList)
    

def checkAnswer(developerAnswer, moduleAnswer):
    return developerAnswer == moduleAnswer

def main():
    from binarytree import tree,bst,heap # https://pypi.org/project/binarytree/
    root = tree(height=3)
    print(root)
    print(findNumberOfRights(root))
    # print(checkAnswer(findNumberOfLefts(root), root.size - root.leaf_count))



if __name__ == '__main__':
    main()
