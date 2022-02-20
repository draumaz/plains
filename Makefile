all: dir_create obj_build compile cleanup

dir_create:
	mkdir \
	-pv \
	./build

obj_build:
	$(CC) $(CFLAGS) -Wall -c ./src/base/c0_splash.c -o ./build/c0_splash.o
	$(CC) $(CFLAGS) -Wall -c ./src/base/c1_areas.c -o ./build/c1_areas.o
	$(CC) $(CFLAGS) -Wall -c ./src/base/c1_cave_subs.c -o ./build/c1_cave_subs.o
	$(CC) $(CFLAGS) -Wall -c ./src/base/c1_txt.c -o ./build/c1_txt.o
	$(CC) $(CFLAGS) -Wall -c ./src/base/glob_vis.c -o ./build/glob_vis.o
	$(CC) $(CFLAGS) -Wall -c ./src/base/savesys.c -o ./build/savesys.o
	$(CC) $(CFLAGS) -Wall -c ./src/base/screen_manip.c -o ./build/screen_manip.o
	$(CC) $(CFLAGS) -Wall -c ./src/base/main.c -o ./build/main.o

compile:
	cd ./build && $(CC) $(CFLAGS) -Wall -lncurses -lm \
	-ltinfo  \
	c0_splash.o c1_areas.o c1_txt.o c1_cave_subs.o glob_vis.o savesys.o screen_manip.o main.o \
	-o ../plains-debug

cleanup:
	rm -rf ./build