# include <stdio.h>
#include <time.h>

char checkPerfect(unsigned long long int number) {
    unsigned long long int i = 1, somme = 0;
    unsigned long long int top = number / 2 + 1;
    for (i=1;i<top;i++) {
        if (number % i == 0) {
            somme += i;
        }
    }
    if (number == somme) {
        return 1;
    }else
    {
        return 0;
    }
    
}
int main() {
    clock_t begin = clock();
    unsigned long long int MIN = 0;
    unsigned long long int MAX = 0;
    clock_t end = 0;
    double time_spent = 0;
    unsigned long long int i = 0;
    int percent = 0;
    printf("MIN = ");
    scanf("%llu",&MIN);
    printf("MAX = ");
    scanf("%llu",&MAX);
    i = MIN;
    #pragma omp parallel for schedule(dynamic) reduction(+ : primes)
    printf("Starting...\n");
    for (i = MIN;i<MAX+1;i++) {
        percent = (100*i + MAX/2)/MAX;
        printf("%d%% Processing %llu\r", percent, i);
        if (checkPerfect(i)) {
            printf("Found %llu                     \n",i);
        }
    }
    end = clock();
    time_spent = (double)(end - begin) / CLOCKS_PER_SEC;
    printf("Done : %llu numbers checked in %fs.\n\n", MAX+1 - MIN, time_spent);
    return 0;
}