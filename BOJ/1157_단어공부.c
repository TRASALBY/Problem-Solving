#include <stdio.h>
#include <string.h>

int main() {
	char s[1000001] = "";
	int alpa[26] = { 0 };
	scanf_s("%s", s, sizeof(s));
	int max = -1;
	int cnt;
	
	for (int i = 0; i < strlen(s); i++) {
		if (s[i] >= 97)
			s[i] -= 32;
	}

	for (int i = 0; i < strlen(s); i++) {
		alpa[s[i] - 65]++;
	}
	for (int i = 0; i < sizeof(alpa)/4; i++) {
		if (alpa[i] > max) {
			cnt = i;
			max = alpa[i];
		}
	}
	for (int i = 0; i < sizeof(alpa)/4; i++) {
		if (i == cnt)
			continue;
		if (alpa[i] == max) {
			printf("?");
			return 0;
		}
	}
	printf("%c", cnt+65);
	return 0;
}
