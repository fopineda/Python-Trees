# solution
def findNumberOfLefts(root):
    leftList = []
    postOrderTraversal(root, leftList)
    return leftList


def postOrderTraversal(root, leftList):
    if not root:
        return

    if root.left:
        leftList.append(root.left.value)
    
    postOrderTraversal(root.left, leftList)
    postOrderTraversal(root.right, leftList)
    

def checkAnswer(developerAnswer, moduleAnswer):
    return developerAnswer == moduleAnswer

def main():
    from binarytree import tree,bst,heap # https://pypi.org/project/binarytree/
    root = bst(height=3)
    print(root)

    print(findNumberOfLefts(root))
    # print(checkAnswer(findNumberOfLefts(root), root.size - root.leaf_count))



if __name__ == '__main__':
    main()
