#include <stdio.h>
#include <unistd.h>
#include <curses.h>

#define SAVE_LENGTH 21
#define SAVE_NAME "data.txt"

// BEGIN SAVE LEGEND //

// 0 ~ knife
// 1 ~ reset
// 2 ~ cave dialog loop
// 3 ~ bottle
// 4 ~ phone

// END SAVE LEGEND //

int * save_reader() {
	static int array[12];
	int i = 0;
	int x = 0;
	FILE *read_in = fopen(SAVE_NAME, "r");
	fscanf(read_in, "%d", &i);
	while (!feof (read_in)) {
		array[x] = i; x += 1;
		fscanf(read_in, "%d", &i);
	}
	return array;
}

int save_compare(int line, int num) {
	int ret;
	if (save_reader()[line] == num) {
		ret = 0;
	} else {
		ret = 1;
	}
	return ret;
}

void save_writer(int line, int state) {
	if (state < 0) { state = 0; }
	int * save_in = save_reader();
	FILE *read_out = fopen(SAVE_NAME, "w");
	for (int i = 0; i < SAVE_LENGTH; i++) {
		if (i == line) {
			fprintf(read_out, "%d\n", state);
		} else {
			fprintf(read_out, "%d\n", save_in[i]);
		}
	}
	fclose(read_out);
}

void save_generate() {
	FILE *generate = fopen(SAVE_NAME, "w");
	for (int i = 0; i < SAVE_LENGTH; i++) {
		fprintf(generate, "%d\n", 0);
	}
	fclose(generate);
}

void save_exists() {
	if (access(SAVE_NAME,F_OK) == -1) {
		save_generate();
	}
}

int save_ephemerance() {
	if (access(SAVE_NAME,F_OK) == -1) {
		return 0;
	} else {
		return 1;
	}
}