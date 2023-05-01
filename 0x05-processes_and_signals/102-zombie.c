#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
/*
 * main:Write a C program that creates 5 zombie processes.
 * infinite_while: returns 0
 *
 *
 */
int infinite_while(void)
{
	while (1)
	{
		sleep(1);
	}
	return (0);
}
int main(void)
{
	pid_t pid;
	int i;

	for (i = 0; i < 5; i++)
	{
		pid = fork();

		if (pid == 0)
		{
			exit(0);
		}
		else if (pid > 0)
		{
			printf("Zombie process created, PID: %d\n", pid);
		}
		else
		{
			fprintf(stderr, "Fork failed\n");
			return (1);
		}
	}
	infinite_while();
	return (0);
}
