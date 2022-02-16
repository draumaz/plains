plains:
	gcc -Wall -lncurses -lm -ltinfo ./src/base/main.c ./src/base/landing_site_test.c ./src/base/screen_manip.c \
		-o ./plains-debug
