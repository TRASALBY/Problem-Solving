#include	<stdio.h>
#include	<string.h>

int main() {
	int n;
	int cnt = 0;
	int cnt2 = 0;
	int len;
	char s[101];
	scanf_s("%d", &n);

	for (int k = 0; k < n; k++) {
		scanf_s("%s", s, sizeof(s));
		len = strlen(s);
		for (int i = 0; i < len; i++) {

			for (int j = i + 1; j < len; j++) {
				if (s[i] == s[j]) {
					if ( j == i + 1) {
						cnt++;
						continue;
					}
					else
					{
						break;
					}
				}
			}
			if (cnt != 0)
				cnt2++;
			cnt = 0;
		}
}
	printf("%d", cnt2);
}