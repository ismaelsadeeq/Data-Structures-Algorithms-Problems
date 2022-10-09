#include "linked.h"

/**
 * main - Function to run the code
 *
 * Return: No return
 */
int main()
{
	node_d *new_node;
	size_t length;
	int array[] = {23, 434, 765, 534, 34, 3, 3564, 32, 97, 23, 73};

	length = sizeof(array) / sizeof(array[0]);
	printf("\nCreating a doubly linked list...\n");
	new_node = create_circularly_linked_list(array, length);
	printf("\nPrinting a doubly linked list...\n");
	print_circularly_linked_list(new_node);
	printf("\nPrinting after deleting the last node in a ");
	printf("circularly linked list...\n");
	delete_last_node_circularly_linked_list(new_node);
	print_circularly_linked_list(new_node);
	printf("\nFreeing a doubly linked list...\n");
	free_circularly_linked_list(new_node);

	return (0);
}
