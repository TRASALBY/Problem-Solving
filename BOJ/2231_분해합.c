#include    <stdio.h>

int main(){
    int n;
    int x;
    int sum;

    scanf("%d", &n);

    for(int i = 0; i<n;i++){
        
        x = i;
        sum = 0;
        while (x!=0)
        {
            sum += x %10;
            x = x/10;
 
        }
        sum = sum + i;
        if(sum == n){
            printf("%d", i);
            return 0;
        }
    }
    printf("0");
    return 0;
}