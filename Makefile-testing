SRC_PFX = "./src/base"
BUILD_PFX = "./build"

all: dir_create obj_build compile cleanup

dir_create:
	@mkdir \
	-pv \
	$(BUILD_PFX)

obj_build:
	$(CC) $(CFLAGS) -Wall -c $(SRC_PFX)/main.c -o $(BUILD_PFX)/main.o
	$(CC) $(CFLAGS) -Wall -c $(SRC_PFX)/savesys.c -o $(BUILD_PFX)/savesys.o
	$(CC) $(CFLAGS) -Wall -c $(SRC_PFX)/screen_manip.c -o $(BUILD_PFX)/screen_manip.o
	$(CC) $(CFLAGS) -Wall -c $(SRC_PFX)/glob_vis.c -o $(BUILD_PFX)/glob_vis.o
	$(CC) $(CFLAGS) -Wall -c $(SRC_PFX)/c0_splash.c -o $(BUILD_PFX)/c0_splash.o
	$(CC) $(CFLAGS) -Wall -c $(SRC_PFX)/c1_areas.c -o $(BUILD_PFX)/c1_areas.o
	$(CC) $(CFLAGS) -Wall -c $(SRC_PFX)/c1_cave_subs.c -o $(BUILD_PFX)/c1_cave_subs.o
	$(CC) $(CFLAGS) -Wall -c $(SRC_PFX)/c1_hill_subs.c -o $(BUILD_PFX)/c1_hill_subs.o
	$(CC) $(CFLAGS) -Wall -c $(SRC_PFX)/c1_txt.c -o $(BUILD_PFX)/c1_txt.o

compile:
	@echo "creating binary"
	@cd $(BUILD_PFX) && \
	$(CC) $(CFLAGS) -Wall -lncurses -lm \
	-ltinfo \
	main.o savesys.o screen_manip.o glob_vis.o c0_splash.o c1_areas.o c1_cave_subs.o c1_hill_subs.o c1_txt.o \
	-o ../plains-debug
	@echo "-> ./plains-debug"

cleanup:
	rm -rf $(BUILD_PFX)
