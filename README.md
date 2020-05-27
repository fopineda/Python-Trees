# Python-Trees
 Tree traversals, algorithms, and problems in Python.

## Installation
Python [binarytree](https://pypi.org/project/binarytree/)
module will need to be installed. 

Install stable version:
```bash
pip install binarytree
```
or

Install current Github version:
```bash
pip install -e git+git@github.com:joowani/binarytree.git@master#egg=binarytree
```

## Usage
Individual Python files can be ran using command. For example:

```bash
python3 Playground.py
```

## Description
### Binary Tree
Binary Trees only have rule and that is that each node has at most two child nodes.

Example:
```bash
cd BinarySearchTreeFinders/
```
```bash
python3 FindMax.py
```
Solutions found in this folder will only solve problems dealing with Binary Trees. This means that the code in the folder is technically formatted for the structure of Binary Trees.


### Binary Search Tree
Binary Search Trees (BST) are Binary Trees in which each node has a greater value than all children in its left subtree and a smaller value than all its children in the right subtree.
Example:
```bash
cd BinaryTreeFinders/
```
```bash
python3 FindAllParents.py
```
Solutions found in this folder will only solve problems dealing with Binary Search Trees. This means that the code in the folder is technically formatted for the structure of Binary Search Trees.

## Structure of Code
Typically, the files will have 2-3 (maybe 4) functions written out.

Take the FindAllParents.py file. It has a solution, solution helper, checker, and main function.

Solution and Solution helper functions:
```python
def findAllParents(root):
    parentList = []
    postOrderTraversal(root, parentList)
    return parentList
def postOrderTraversal(root, parentList):
    if not root:
        return
    
    postOrderTraversal(root.left, parentList)
    postOrderTraversal(root.right, parentList)
    if ((root.left and root.right) or (not root.left and root.right) or (root.left and not root.right)):
        parentList.append(root.value)
```

Check Answer function:
```python
def checkAnswer(developerAnswer, moduleAnswer):
    return developerAnswer == moduleAnswer
```

Main function: 
```python
def main():
    from binarytree import tree,bst,heap # https://pypi.org/project/binarytree/
    root = tree(height=3)
    print(root)
    print(findAllParents(root))
    # print(checkAnswer(findNumberOfParents(root), root.size - root.leaf_count))
```

Of course code calls the main function to activate the file:
```python
if __name__ == '__main__':
    main()
```

Lastly, code is a mixture of normal python syntax and [binarytree](https://pypi.org/project/binarytree/) module code. Documentation can be found [here](https://binarytree.readthedocs.io/en/latest/overview.html).
