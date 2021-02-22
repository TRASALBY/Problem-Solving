#include    <stdio.h>
#include    <string.h>
#include    <math.h>

int main(){

    int L;
    long long result = 0;
    char arr[51];
    char alpha[26];


    for(int i = 0; i<26; i++){
        alpha[i] = i + 97;
    }

    scanf("%d", &L);
    scanf("%s", arr);
    int n = strlen(arr);
    for(int i = 0; i<n;i++ ){
        for(int j = 0; j<26; j++){
            if(arr[i]==alpha[j]){
                result += pow(31,j);
            }
        }

    }

    printf("%d",result);

}