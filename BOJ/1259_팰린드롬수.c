#include    <stdio.h>

int main(){
    int num = 1;
    int arr[5];
    int tmp;
    int len;

    while(1){
        scanf("%d", &num);
        if(num == 0){
            return 0;
        }
        tmp = num;
        for(int i = 0; tmp != 0; i ++){
            arr[i] = tmp % 10;
            tmp = tmp/10;
        }
        len = sizeof(arr);
        for(int i = 0; i < len /2; i++){
            if(arr[i] == arr[len-i]){
                if(i==(len/2)-1){
                    printf("yes");  
                }
                else{
                    continue;
                }

            }
            else{
                printf("no\n");
                break;
            }

        }
    }
    

}