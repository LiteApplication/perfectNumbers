# include <stdio.h>
char checkPerfect(int number) {
    int i = 1, somme = 0;
    for (i=1;i<number;i++) {
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
    
}