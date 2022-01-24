#include    <stdio.h>

int fact(int x);

int main(){
    int n, k;

    scanf("%d %d", &n, &k);

    printf("%d", fact(n)/(fact(k) * fact(n-k)));
}

int fact(int x){
    int result = 1;
    for(int i = 1 ; i <= x;i++){
        result *= i;
    }
    return result;
}