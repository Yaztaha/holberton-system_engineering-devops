#include <stdio.h>
#include <unistd.h>
#include <sys/types.h>
#include <stdlib.h>
/**
 * infinite_while - creates an infinite while
 * Return: does not return
 */
int infinite_while(void)
{
	while (1)
	{
		sleep(1);
	}
	return (0);
}
/**
 * main - Program that 5 zombies processes.
 * Return: void
 */
int main(void)
{
	int i = 0;
	int pid = 0;

	for (i = 0; i < 5; i++)
	{
		pid = fork();
		if (pid > 0)
			printf("Zombie process created, PID: %i\n", pid);
		else
			exit(0);
	}
	infinite_while();
	return(0);
}
