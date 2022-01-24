#include <stdio.h>
#include <stdlib.h>
int main() {
	char s1[4], s2[4];
	scanf_s("%s %s", s1, sizeof(s1), s2,sizeof(s2));
	char temp = ' ';
	temp = s1[0];
	s1[0] = s1[2];
	s1[2] = temp;

	temp = s2[0];
	s2[0] = s2[2];
	s2[2] = temp;

	for (int i = 0; i < 3; i++) {
		if (s1[i] > s2[i]) {
			printf("%s", s1);
			break;
		}
		else if (s1[i] < s2[i]) {
			printf("%s", s2);
			break;
		}
		else
			continue;
		
	}
}

