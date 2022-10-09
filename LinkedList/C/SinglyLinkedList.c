#include "linked.h"

/**
 * main - Test run the code
 *
 * Return: 0
 */

int main()
{
	int array[] = {1, 2, 3, 4, 6, 7, 9};
	size_t length;
	node_t *new_list;

	length = sizeof(array) / sizeof(array[0]);
	new_list = create_linked_list(array, length);
	printf("Printing the singly linked list after created...\n");
	print_linked_list(new_list);
 	delete_last_node_singly_linked_list(new_list);
	printf("\nPrinting the last node after the last node is deleted...\n");
	print_linked_list(new_list);
	free_linked_list(new_list);
	return (0);
}
