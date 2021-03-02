#include    <stdio.h>
#include    <string.h>

void sort(char(*x)[51], int num, int *len);

int main(){
    int n;
    int len[20000]
    scanf("%d", &n);

    char* arr[20000];
    

    for(int i = 0; i < n; i++){
        scanf("%s", arr[i]);
        len[i] = strlen(arr[i]);
    }
    sort(arr, n, len);
    for(int i = 0; i < n; i++){
        printf("%s", arr[i]);
    }


}

void sort(char(*x)[51], int num, int *len){
    char tmp[51];
    for(int i = 0; i < num; i++){
        for(int j = 0; j < num - i - 1; j++){
            if(*len[i] > *len[j]){
                strcpy( tmp, *(x+j) );
				strcpy( *(x+j), *(x+j+1));
				strcpy( *(x+j+1), tmp );
            }
        }
    }
}