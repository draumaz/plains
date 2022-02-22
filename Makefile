SRC_PFX = "./src/base"
BUILD_PFX = "./build"
SRCS := c0_splash c1_areas c1_cave_subs c1_hill_subs c1_txt glob_vis savesys screen_manip main

all: dir_create obj_build compile cleanup

dir_create:
	@mkdir \
	-pv \
	$(BUILD_PFX)

obj_build:
	@$(foreach OBJ, $(SRCS), echo " CC      $(BUILD_PFX)/$(OBJ).o" && $(CC) $(CFLAGS) -Wall -c $(SRC_PFX)/$(OBJ).c -o $(BUILD_PFX)/$(OBJ).o;)

compile:
	@cd $(BUILD_PFX) && \
	$(CC) $(CFLAGS) -Wall -lncurses -lm \
	-ltinfo \
	$(foreach OBJ, $(SRCS), $(OBJ).o) \
	-o ../plains-debug
	@echo "-> ./plains-debug"

cleanup:
	rm -rf $(BUILD_PFX)
