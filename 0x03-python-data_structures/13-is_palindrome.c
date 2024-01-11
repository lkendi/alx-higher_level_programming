#include "lists.h"

int is_palindrome(listint_t **head)
{
	listint_t *ptr_slow = *head, *ptr_fast = *head;
	listint_t *prev = NULL, *current, *next;

	/*Handle empty and single-node lists*/
	if (*head == NULL || (*head)->next == NULL)
		return (1);

	/*Find the middle of the list*/
	while (ptr_fast != NULL && ptr_fast->next != NULL)
	{
		ptr_slow = ptr_slow->next;
		ptr_fast = ptr_fast->next->next;
	}
	/**
	* Reverse the second half of the list,
	* starting from the node after the middle node
	* and stopping before the middle node
	*/
	current = ptr_slow->next;
	while (current != NULL)
	{
		next = current->next;
		current->next = prev;
		prev = current;
		current = next;
	}

	/*Compare the first and second halves*/
	ptr_slow = *head;
	while (prev != NULL)
	{
		if (ptr_slow->n != prev->n)
		{
			return (0);
		}
		ptr_slow = ptr_slow->next;
		prev = prev->next;
	}
	return (1);
}
