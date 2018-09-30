#include "types.h"
#include "user.h"
#include "fcntl.h"

#define N 14641000
#define MAX_PROC 26

void processo(long bilhetes, char nome){
    int pid = fork(bilhetes);

    if (pid > 0)
        while(1) printf(1, "%c;%d\n", nome, bilhetes);
}

int main(void) {
    for(int i = 1; i <= MAX_PROC; i++)
        processo(i * i * i * i, i + 64);
    exit();
    return 0;
}
