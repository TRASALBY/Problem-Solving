#include    <stdio.h>

int main(){

    int arr[15][15] = {0};

    int t;
    int q, n;

    scanf("%d", &t);
    for(int i = 0; i<15; i++){
        arr[0][i] = i+1;
    }

    for(int i = 1; i<15; i++){
        for(int j = 0; j <15; j++){
            for(int k = 0; k <= j; k++){
            arr[i][j] += arr[i-1][k];
            }
        }

    }

    for (int i = 0; i < t; i++)
    {
        scanf("%d", &q);
        scanf("%d", &n);

        printf("%d\n", arr[q][n-1]);

    }
    

}

