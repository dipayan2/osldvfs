# OBJS = profile_dvfs.o ols_scheduler.o cpuclock.o gpuclock.o memclock.o
OBJS = test_code.o cpuclock.o memclock.o gpuclock.o
# HEADER = ols_scheduler.h cpuclock.h gpuclock.h memclock.h
HEADER = cpuclock.h memclock.h gpuclock.h
# OUT = profile_dvfs
OUT = test_code
CXX = g++
CXXFLAGS = -g -O2 -Wall -Wextra -pedantic 

all : $(OBJS)
	$(CXX) $(CXXFLAGS) $(OBJS) -o $(OUT) -pthread

# profile_dvfs.o : profile_dvfs.cpp $(HEADER)
# 	$(CXX) $(CXXFLAGS) -c profile_dvfs.cpp -pthread

# ols_scheduler.o : ols_scheduler.cpp $(HEADER)
# 	$(CXX) $(CXXFLAGS) -c ols_scheduler.cpp -pthread

test_code.o : test_code.cpp $(HEADER)
	@echo "Needs to be in Jetson TX2"
	$(CXX) $(CXXFLAGS) -c test_code.cpp -pthread

cpuclock.o : cpuclock.cpp cpuclock.h
	@echo "Needs to be in Jetson TX2"
	$(CXX) $(CXXFLAGS) -c cpuclock.cpp -pthread

gpuclock.o : gpuclock.cpp gpuclock.h
	@echo "Needs to be in Jetson TX2"
	$(CXX) $(CXXFLAGS) -c gpuclock.cpp -pthread

memclock.o : memclock.cpp memclock.h
	@echo "Needs to be in Jetson TX2"
	$(CXX) $(CXXFLAGS) -c memclock.cpp -pthread

clean:
	rm -f $(OBJS) $(OUT)
