#include "lists.h"

/**
 * is_palindrome - checks if a singly linked list is a plaindrome
 * @head: pointer to the head node
 * Return: 0 if not a palindrome, 1 if it is a palindrome
*/

int is_palindrome(listint_t **head)
{
	listint_t *ptr;
	int count, center, i, queue[100];

	/*An empty list is considered a palindrome*/
	if (*head == NULL)
		return (1);
	/*Find the length of the list*/
	count = 0;
	ptr = *head;
	while (ptr != NULL)
	{
		ptr = ptr->next;
		count++;
	}
	/*List with an odd length cannot contain a palindrome*/
	if (count % 2 != 0)
		return (0);

	/*Find the center of the list*/
	center = count / 2;

	ptr = *head;
	for (i = 0; i < center; i++)
	{
		queue[i] = ptr->n;
		ptr = ptr->next;
		printf("\nQueue [%d]: %d", i, queue[i]);
	}
	for (i = center - 1; i >= 0; i--)
	{
		if (ptr->n == queue[i])
		{
			printf("\nQueue2 [%d]: %d", i, queue[i]);
			printf("\nPtr: %d", ptr->n);
			ptr = ptr->next;
		}
		else
			return (0);
	}
	return (1);
}
