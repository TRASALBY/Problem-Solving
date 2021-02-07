#include    <stdio.h>

int main(){
    int N, F;
    int remainder;          //나머지

    scanf("%d %d", &N, &F);

    remainder = N % 100;

    N -= remainder;
    for(int i = 0; i<=99; i++){
        N += i;
        remainder = N % F; 
        if(remainder == 0){
            if(i<10){
                printf("0%d", i);
                break;
            }
            else{
                printf("%d", i);
                break;
            }
        }
        N-=i;
    }

    return 0;
}