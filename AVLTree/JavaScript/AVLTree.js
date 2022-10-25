// Class to create node
class Node {
    constructor(num) {
        this.value = num;
        this.height = 1;
        this.left = null;
        this.right = null;
    }
}
  
// Class to create AVL Tree
class AVLTree {
    constructor() {
        let root = null;

        //get height of node
        this.height = (N) => {
            if (N === null) {
                return 0;
            }

            return N.height;
        };

        //rotations:
        //right rotation
        this.rightRotation = (b) => {
            let a = b.left;
            let c = a.right;
            a.right = b;
            b.left = c;
            b.height = Math.max(this.height(b.left), this.height(b.right)) + 1;
            a.height = Math.max(this.height(a.left), this.height(a.right)) + 1;
            return a;
        };

        //left rotation
        this.leftRotation = (a) => {
            let b = a.right;
            let c = b.left;
            b.left = a;
            a.right = c;
            a.height = Math.max(this.height(a.left), this.height(a.right)) + 1;
            b.height = Math.max(this.height(b.left), this.height(b.right)) + 1;
            return b;
        };

        // get the balance factor of node
        this.balanceFactorGetter = (N) => {
            if (N == null) {
                return 0;
            }

            return this.height(N.left) - this.height(N.right);
        };


        // function to help in node insertion
        const nodeInserter = (node, number) => {

            // find the position and insert node
            if (node === null) {
                return (new Node(number));
            }

            if (number < node.value) {
                node.left = nodeInserter(node.left, number);
            } else if (number > node.value) {
                node.right = nodeInserter(node.right, number);
            } else {
                return node;
            }

            // update the balance factor of each node
            node.height = 1 + Math.max(this.height(node.left), this.height(node.right));

            let balanceFactor = this.balanceFactorGetter(node);

            //balance AVL Tree
            if (balanceFactor > 1) {
                if (number < node.left.value) {
                    return this.rightRotation(node);
                } 
                else if (number > node.left.value) {
                    node.left = this.leftRotation(node.left);
                    return this.rightRotation(node);
                }
            }

            if (balanceFactor < -1) {
                if (number > node.right.value) {
                    return this.leftRotation(node);
                } 
                else if (number < node.right.value) {
                    node.right = this.rightRotation(node.right);
                    return this.leftRotation(node);
                }
            }

            return node;
        };

        // insert a node
        this.insertNode = (number) => {
            root = nodeInserter(root, number);
        };

        //get node with minimum value
        this.mimumValueNode = (node) => {
            let current = node;
            while (current.left !== null) {
                current = current.left;
            }
            return current;
        };

        // delete helper
        const nodeDeleter = (root, number) => {

            // find the particular node and delete it
            if (root == null) {
                return root;
            }
            if (number < root.value) {
                root.left = nodeDeleter(root.left, number);
            } 
            else if (number > root.value) {
                root.right = nodeDeleter(root.right, number);
            } 
            else {
                if ((root.left === null) || (root.right === null)) {
                    let temp = null;
                    if (temp == root.left) {
                        temp = root.right;
                    } 
                    else {
                        temp = root.left;
                    }

                    if (temp == null) {
                        temp = root;
                        root = null;
                    } 
                    else {
                        root = temp;
                    }
                } 
                else {
                    let temp = this.mimumValueNode(root.right);
                    root.value = temp.value;
                    root.right = nodeDeleter(root.right, temp.value);
                }
            }
            if (root == null) {
                return root;
            }

            // Update the balance factor of each node 
            root.height = Math.max(this.height(root.left), this.height(root.right)) + 1;

            let balanceFactor = this.balanceFactorGetter(root);
            
            //balance AVL Tree
            if (balanceFactor > 1) {
                if (this.balanceFactorGetter(root.left) >= 0) {
                    return this.rightRotation(root);
                } 
                else {
                    root.left = this.leftRotation(root.left);
                    return this.rightRotation(root);
                }
            }
            if (balanceFactor < -1) {
                if (this.balanceFactorGetter(root.right) <= 0) {
                    return this.leftRotation(root);
                } 
                else {
                    root.right = this.rightRotation(root.right);
                    return this.leftRotation(root);
                }
            }
            return root;
        };

        //node deletion
        this.deleteNode = (number) => {
            root = nodeDeleter(root, number);
        };

        // print the tree 
        this.printTreeOrder = () => {
            treeOrder(root);
        };

        const treeOrder = (node) => {
            if (node) {
                console.log(node.value);
                treeOrder(node.left);
                treeOrder(node.right);
            }
        };
    }
}


  //test
  var tree = new AVLTree();
  tree.insertNode(40);
  tree.insertNode(32);
  tree.insertNode(43);
  tree.insertNode(8);
  tree.insertNode(27);
  tree.insertNode(65);
  tree.insertNode(8);
  tree.insertNode();
  tree.printTreeOrder();
  tree.deleteNode(13);
  //console.log("After Deleting");
  tree.printTreeOrder();
  