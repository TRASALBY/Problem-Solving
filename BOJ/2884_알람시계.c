#include <stdio.h>

int main() {
	int h, m;

	scanf_s("%d %d", &h, &m);
	m = m - 45;
	if (m < 0) {
		h -= 1;
		m += 60;
	}
	if (h < 0) {
		h += 24;
	}
	printf("%d %d", h, m);
}