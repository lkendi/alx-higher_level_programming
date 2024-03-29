#include "lists.h"
#include <stdio.h>
#include <stdlib.h>

/**
 * check_cycle - checks if a singly linked list has a cycle
 * @list: pointer to the head node of the linked list
 * Return: 0 if there is no cycle, 1 if there is a cycle
 */
int check_cycle(listint_t *list)
{
    listint_t *slow, *fast;

    if (list == NULL)
        return (0);

    slow = list;
    fast = list;
    /*Fast moves 2 steps each time, slow moves 1 step each time*/
    /*If there is a cycle, both pointers will meet at some point*/
    while (fast != NULL && fast->next != NULL)
    {
        slow = slow->next;
        fast = fast->next->next;
        if (slow == fast)
            return (1);
    }
    return (0);
}