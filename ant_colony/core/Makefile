CC=clang++
CFLAGS=-std=c++17 -stdlib=libc++
OBJ=ant_colony_main.o
FILES=ant_colony_main.cpp ant.cpp colony.cpp simulator.cpp world.cpp

ant_colony: ant_colony_main.cpp
	$(CC) $(CFLAGS) $(FILES) -o $(OBJ) --debug
