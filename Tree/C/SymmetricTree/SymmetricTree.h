#ifndef SYMMETRIC_TREE_H
#define SYMMETRIC_TREE_H

#include <stdbool.h>
#include <stdio.h>
#include <stdlib.h>

typedef struct Node {
    int key;
    struct Node *left, *right;
} Node;

Node* newNode(int key);
bool isMirror(Node *root1, Node *root2);
bool isSymmetric(Node* root);

#endif
