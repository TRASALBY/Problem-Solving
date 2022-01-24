#include <stdio.h>

int main(){
    int x, y, w, h;
    int arr[4];
    int min = 1000;

    scanf("%d %d %d %d", &x, &y, &w, &h);

    arr[0] = h - y;
    arr[1] = y;
    arr[2] = w - x;
    arr[3] = x;

    for(int i = 0; i< 4; i++){
        if(min>=arr[i]){
            min = arr[i];
        }
    }
    printf("%d", min);

}