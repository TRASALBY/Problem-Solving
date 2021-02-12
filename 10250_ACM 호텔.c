#include    <stdio.h>

int main(){
    int  w, h, n, t;
    int x, y;

    scanf("%d", &t);

    for(int i = 0; i < t; i++){
        scanf("%d %d %d", &h, &w, &n);
        y = n % h;
        x = n / h + 1;
        if(y == 0){
          y = h;
          x = x-1;
        }
        printf("%d\n", y*100 + x);
    }
}