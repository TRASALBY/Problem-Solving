#include	<stdio.h>
#include	<string.h>

int main() {
	char s[1000001];
	scanf_s("%[^\n]s", s,sizeof(s));
	int cnt = 0;

	int len = strlen(s);
	if (s[0] != ' ')
		cnt++;
	for (int i = 0; i < len; i++) {

		if (s[i] == ' ') {
			cnt++;
		}
	}
	if (s[len-1] == ' ')
		cnt--;
	printf("%d", cnt);

	
}