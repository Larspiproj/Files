#include <stdio.h>
#include <string.h>
#include <errno.h>
#include <stdlib.h>
#include <wiringPi.h>

#define STAGE_1 29

volatile int eventCounter = 0;

void myInterrupt(void) {
	eventCounter++;
}

int main (void) {
	if (wiringPiSetup() < 0) {
		fprintf(stderr, "Unable to setup wiringPi: %s\n", strerror(errno));
		return 1;
	}

	if (wiringPiISR(STAGE_1, INT_EDGE_BOTH, &myInterrupt) < 0) {
		fprintf(stderr, "Unable to setup ISR: %s\n", strerror(errno));
		return 1;
	}

	while (1) {
		printf("%d\n", eventCounter),
		eventCounter = 0;
		delay(10000);
	}

	return 0;
}
