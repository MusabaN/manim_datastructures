#include <stdio.h>

int main(void) {
    int pid
    
    // pid equals fork but if it is -1 exit
    if ((pid = fork()) == -1) {
        printf("Error in fork")
        exit(1);
    }
    if (pid == 0) {
        printf("I am the child process\n");
    } else {
        printf("Sleeping")
        sleep(0.5);
        printf("I am the parent process\n");
    }
}