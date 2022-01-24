#include    <stdio.h>
#include    <math.h>

int main(){
    int line[3];
    int a, b, c;
    
    while(1){
        scanf("%d %d %d", &line[0], &line[1], &line[2]);
        if(line[0] == 0 && line[0] == 0 && line[0] == 0){
            break;
        }
        a = 30000;
        c = 0;
        for(int i = 0; i<3; i++){

            if(line[i]<a){
                a = line[i];
            }
            if(line[i]>c){
                c = line[i];
            }

        }
        for(int i = 0; i<3; i++){
            if(line[i]!= a && line[i] != c){
                b = line[i];
            }
        }

        if(pow(c,2) == pow(a,2) + pow(b,2)){
            printf("right\n");
        }
        else{
            printf("wrong\n");
        }
    }
    
}
