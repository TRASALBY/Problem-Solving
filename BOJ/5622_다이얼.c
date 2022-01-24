#include	<stdio.h>
#include	<string.h>
int main() {
	char s[16];

	scanf_s("%s", s, sizeof(s));
	int len = strlen(s);
	int cnt = 0;

	for (int i = 0; i < len; i++) {
		if (s[i] >= 'A' && s[i] <= 'C') {
			cnt = cnt + 3;
			continue;
		}
		if (s[i] >= 'D' && s[i] <= 'F') {
			cnt = cnt + 4;
			continue;
		}
		if (s[i] >= 'G' && s[i] <= 'I') {
			cnt = cnt + 5;
			continue;
		}
		if (s[i] >= 'J' && s[i] <= 'L') {
			cnt = cnt + 6;
			continue;
		}
		if (s[i] >= 'M' && s[i] <= 'O') {
			cnt = cnt + 7;
			continue;
		}
		if (s[i] >= 'P' && s[i] <= 'S') {
			cnt = cnt +8;
			continue;
		}
		if (s[i] >= 'T' && s[i] <= 'V') {
			cnt = cnt + 9;
			continue;
		}
		if (s[i] >= 'W' && s[i] <= 'Z') {
			cnt = cnt + 10;
			continue;
		}
	}
	printf("%d", cnt);
}