#include    <stdio.h>

int main(){
    int a, b, n;
    int temp;

    a = 0;
    b = 1;
    scanf("%d", &n);


    for(int i = 0; i < n; i++){
        temp = a;
        a = a + b;
        b = temp;
    }

    printf("%d", a);
}