#include "linked.h"
/**
 * main - Funtion to test the doubly linked list
 *
 * Return: return 0
 */
int main()
{
	node_d *new_node;
	int array[] = {23, 564, 2, 4, 65, 23, 76};
	size_t length;

	length = sizeof(array) / sizeof(array[0]);
	printf("Creating a doubly linked list...\n");
	new_node = create_doubly_linked_list(array, length);
	printf("\nPrinting the doubly linked list...\n");
	print_doubly_linked_list(new_node);
	printf("\nPrinting the doubly linked list ");
	printf("after deleting the last node...\n");
	delete_last_node_doubly_linked_list(new_node);
	print_doubly_linked_list(new_node);
	printf("Freeing the doubly linked list...\n");
	free_doubly_linked_list(new_node);
	return (0);
}
