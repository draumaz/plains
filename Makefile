FILE0 = "c0_splash"
FILE1 = "c1_areas"
FILE2 = "c1_cave_subs"
FILE3 = "c1_txt"
FILE4 = "glob_vis"
FILE5 = "savesys"
FILE6 = "screen_manip"
FILE7 = "main"

all: dir_create obj_build compile cleanup

dir_create:
	@mkdir \
	-p \
	./build

obj_build:
	@echo "CC	$(FILE0).o"
	@$(CC) $(CFLAGS) -Wall -c ./src/base/$(FILE0).c -o ./build/$(FILE0).o
	@echo "CC	$(FILE1).o"
	@$(CC) $(CFLAGS) -Wall -c ./src/base/$(FILE1).c -o ./build/$(FILE1).o
	@echo "CC	$(FILE2)"
	@$(CC) $(CFLAGS) -Wall -c ./src/base/$(FILE2).c -o ./build/$(FILE2).o
	@echo "CC	$(FILE3).o"
	@$(CC) $(CFLAGS) -Wall -c ./src/base/$(FILE3).c -o ./build/$(FILE3).o
	@echo "CC	$(FILE4).o"
	@$(CC) $(CFLAGS) -Wall -c ./src/base/$(FILE4).c -o ./build/$(FILE4).o
	@echo "CC	$(FILE5).o"
	@$(CC) $(CFLAGS) -Wall -c ./src/base/$(FILE5).c -o ./build/$(FILE5).o
	@echo "CC	$(FILE6).o"
	@$(CC) $(CFLAGS) -Wall -c ./src/base/$(FILE6).c -o ./build/$(FILE6).o
	@echo "CC	$(FILE7).o"
	@$(CC) $(CFLAGS) -Wall -c ./src/base/$(FILE7).c -o ./build/$(FILE7).o

compile:
	@echo -en "Compiling binary..."
	@cd ./build && $(CC) $(CFLAGS) -Wall -lncurses -lm \
	-ltinfo \
	c0_splash.o c1_areas.o c1_txt.o c1_cave_subs.o glob_vis.o savesys.o screen_manip.o main.o \
	-o ../plains-debug
	@echo -e "DONE -> ./plains-debug"

cleanup:
	@rm -rf ./build
