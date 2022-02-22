SRC_PFX = "./src/base"
BUILD_PFX = "./build"
SRCS := c0_splash c1_areas c1_cave_subs c1_hill_subs c1_txt glob_vis savesys screen_manip main

all: dir_create obj_build compile cleanup

dir_create:
	@mkdir \
	-pv \
	./build

obj_build:
	$(foreach obj, $(SRCS), echo "CC      $(BUILD_PFX)/$(obj).o" && $(CC) $(CFLAGS) -Wall -c $(SRC_PFX)/$(obj).c -o $(BUILD_PFX)/$(obj).o;)

compile:
	cd $(BUILD_PFX) && \
	$(CC) $(CFLAGS) -Wall -lncurses -lm \
	-ltinfo \
	$(foreach obj, $(SRCS), $(obj).o) \
	-o ../plains-debug

cleanup:
	rm -rf $(BUILD_PFX)
