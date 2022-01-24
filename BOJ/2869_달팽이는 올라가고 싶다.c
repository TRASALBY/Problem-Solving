#include    <stdio.h>

int main(){
{
	int A, B, V;
	int day;
	scanf("%d %d %d", &A, &B, &V);


	if (((V-B) % (A - B)) == 0)
	{
		day = (V-B) / (A - B);
	}
	else
	{
		day = (V-B) / (A - B) + 1;
	}
	printf("%d", day);
	return 0;
}