#include "SymmetricTree.h"

/**
 * newNode - utility function to create new node
 * @key: value used to make operation on the node
 * Return: returns pointer to a new node
 */
Node *newNode(int key)
{
       	Node *temp = malloc(sizeof(Node));
	temp->key = key;
	temp->left = temp->right = NULL;
	return (temp);
}

/**
 * isMirror - checks if two trees are mirror of each other
 * @root1: pointer to root node of the first tree
 * @root2: pointer to root node of the second tree
 * Return: return true if both trees are empty or mirror
 * otherwise returns false
 */
bool isMirror(Node *root1, Node *root2)
{
	if (root1 == NULL && root2 == NULL)
		return true;

	if (root1 && root2 && root1->key == root2->key)
		return isMirror(root1->left, root2->right)
		&& isMirror(root1->right, root2->left);

	return false;
}

/**
 * isSymmetric - checks if a tree mirror of itself
 * @root: pointer to root node of the tree
 * Return: return true if a tree is mirror of itself
 */
bool isSymmetric(Node *root)
{
	return isMirror(root, root);
}
