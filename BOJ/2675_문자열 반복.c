#include	<stdio.h>
#include	<string.h>

int main() {
	char s[20];
	int n, cnt;
	scanf_s("%d", &n);
	for (int i = 0; i < n; i++) {
		scanf_s("%d", &cnt);
		scanf_s("%s", s,sizeof(s));
		for (int j = 0; j < strlen(s); j++) {
			for (int k = 0; k < cnt; k++) {
				printf("%c", s[j]);
			}
		}
		printf("\n");
	}
}