FILE0 = "c0_splash"
FILE1 = "c1_areas"
FILE2 = "c1_cave_subs"
FILE3 = "c1_txt"
FILE4 = "glob_vis"
FILE5 = "savesys"
FILE6 = "screen_manip"
FILE7 = "main"

SRC_PFX = "./src/base"
BUILD_PFX = "./build"

all: dir_create obj_build compile cleanup

dir_create:
	@mkdir \
	-p \
	./build

obj_build:
	@echo "  CC	 $(BUILD_PFX)/$(FILE0).o"
	@$(CC) $(CFLAGS) -Wall -c $(SRC_PFX)/$(FILE0).c -o $(BUILD_PFX)/$(FILE0).o
	@echo "  CC	 $(BUILD_PFX)/$(FILE1).o"
	@$(CC) $(CFLAGS) -Wall -c $(SRC_PFX)/$(FILE1).c -o $(BUILD_PFX)/$(FILE1).o
	@echo "  CC	 $(BUILD_PFX)/$(FILE2).o"
	@$(CC) $(CFLAGS) -Wall -c $(SRC_PFX)/$(FILE2).c -o $(BUILD_PFX)/$(FILE2).o
	@echo "  CC	 $(BUILD_PFX)/$(FILE3).o"
	@$(CC) $(CFLAGS) -Wall -c $(SRC_PFX)/$(FILE3).c -o $(BUILD_PFX)/$(FILE3).o
	@echo "  CC	 $(BUILD_PFX)/$(FILE4).o"
	@$(CC) $(CFLAGS) -Wall -c $(SRC_PFX)/$(FILE4).c -o $(BUILD_PFX)/$(FILE4).o
	@echo "  CC	 $(BUILD_PFX)/$(FILE5).o"
	@$(CC) $(CFLAGS) -Wall -c $(SRC_PFX)/$(FILE5).c -o $(BUILD_PFX)/$(FILE5).o
	@echo "  CC	 $(BUILD_PFX)/$(FILE6).o"
	@$(CC) $(CFLAGS) -Wall -c $(SRC_PFX)/$(FILE6).c -o $(BUILD_PFX)/$(FILE6).o
	@echo "  CC	 $(BUILD_PFX)/$(FILE7).o"
	@$(CC) $(CFLAGS) -Wall -c $(SRC_PFX)/$(FILE7).c -o $(BUILD_PFX)/$(FILE7).o

compile:
	@cd $(BUILD_PFX) && $(CC) $(CFLAGS) -Wall -lncurses -lm \
	-ltinfo \
	c0_splash.o c1_areas.o c1_txt.o c1_cave_subs.o glob_vis.o savesys.o screen_manip.o main.o \
	-o ../plains-debug
	@echo -e "\n-> ./plains-debug\n"

cleanup:
	@rm -rf ./build
