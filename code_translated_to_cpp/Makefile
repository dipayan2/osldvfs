OBJS = profile_dvfs.o ols_scheduler.o cpuclock.o gpuclock.o memclock.o
HEADER = ols_scheduler.h cpuclock.h gpuclock.h memclock.h
OUT = profile_dvfs
CXX = g++
CXXFLAGS = -g -O2 -Wall -Wextra -pedantic

all : $(OBJS)
	$(CXX) $(CXXFLAGS) $(OBJS) -o $(OUT) -pthread

profile_dvfs.o : profile_dvfs.cpp $(HEADER)
	$(CXX) $(CXXFLAGS) -c profile_dvfs.cpp -pthread

ols_scheduler.o : ols_scheduler.cpp $(HEADER)
	$(CXX) $(CXXFLAGS) -c ols_scheduler.cpp -pthread

cpuclock.o : cpuclock.cpp cpuclock.h
	$(CXX) $(CXXFLAGS) -c cpuclock.cpp -pthread

gpuclock.o : gpuclock.cpp gpuclock.h
	$(CXX) $(CXXFLAGS) -c gpuclock.cpp -pthread

memclock.o : memclock.cpp memclock.h
	$(CXX) $(CXXFLAGS) -c memclock.cpp -pthread

clean:
	rm -f $(OBJS) $(OUT)
