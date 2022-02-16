plains:
	mkdir \
	-pv \
	./build
	$(CC) $(CFLAGS) -Wall -c ./src/base/landing_site_test.c -o ./build/landing_site_test.o
	$(CC) $(CFLAGS) -Wall -c ./src/base/screen_manip.c -o ./build/screen_manip.o
	$(CC) $(CFLAGS) -Wall -c ./src/base/main.c -o ./build/main.o
	cd ./build && $(CC) $(CFLAGS) -Wall -lncurses -lm \
	-ltinfo \
	landing_site_test.o screen_manip.o main.o \
	-o ./plains-debug
	rm -rf ./build
