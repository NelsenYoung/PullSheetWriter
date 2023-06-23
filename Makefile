# Makefile for Read_CSV

CC = g++ -std=c++14
CFLAGS = -g

#rules.
all: Read_CSV

#
#

coil.o: coil.cpp coil.h
	$(CC) -c $(CFLAGS) coil.cpp 

Read_CSV.o: Read_CSV.cpp coil.h
	$(CC) -c $(CFLAGS) Read_CSV.cpp

Read_CSV: Read_CSV.o coil.o
	$(CC) -o Read_CSV Read_CSV.o coil.o

clean:
	rm -f *.o *~ core Read_CSV