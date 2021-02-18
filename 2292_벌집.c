#include    <stdio.h>

int main(){
    int n;
    int count;
    scanf("%d", &n);

    count = 1;

    if(n != 1){

        for(int i = 0; ;i++){
            if(count >= n){
                printf("%d", i);
                break;
            }
            count += i * 6;
        }
    }
    else{
        printf("1");
    
    }



    //2~7       2
    //8~19      3
    //20~37     4
    //38~61     5
    
}