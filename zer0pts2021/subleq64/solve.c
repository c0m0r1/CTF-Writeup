#include <stdio.h>
#include <stdint.h>
#include <string.h>
#include <stdlib.h>
int64_t mem[100000];

#define DEBUG 0

void load(const char* fname)
{
    char tmp[100000];
    FILE* f = fopen(fname, "rt");
    fread(tmp, 100000, 1, f);
    char *pch = strtok(tmp, " ");
    int i = 0;
    while (pch != NULL)
    {
        mem[i] = strtoll(pch, NULL, 10);
        i++;
        pch = strtok(NULL, " ");
    }
    fclose(f);
}

int pc = 0;
int run = 1;

void run_one()
{
    int64_t a = mem[pc];
    int64_t b = mem[pc + 1];
    int64_t c = mem[pc + 2];

    if (DEBUG)
    {
        printf("%5d : %5lld %5lld %5lld  ", pc, a, b, c);
        printf("mem[a] : %-20lld  ", mem[a]);
        printf("mem[b] : %lld\n", mem[b]);
    }

    if(b == -1){
        putchar(mem[a] & 0xff);
        fflush(stdout);
    }
    else{
        mem[b] -= mem[a];
    }
    if (mem[b] <= 0)
        pc = c;
    else
        pc += 3;
    
    if(pc == -1) run = 0;
}

int main(int argc, char **argv)
{
    load(argv[1]);
    while (run)
    {
        run_one();
    }
}