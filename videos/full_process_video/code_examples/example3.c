#include <stdio.h>
#include <unistd.h>
#include <stdlib.h>

int main(void) {
    int pid;
    
    // pid equals fork but if it is -1 exit
    if ((pid = fork()) == -1) {
        printf("Error in fork");
        exit(1);
    }
    if (pid == 0) {
        printf("I am the child process\n");
        // do error checking for execve

        if (execve("another_program", NULL, NULL) == -1) {
            fprintf(stderr, "Error in execve\n");
            exit(1);
        }

    } else {
        printf("Sleeping\n");
        sleep(1);
        printf("I am the parent process\n");
    }

    return 0;
}