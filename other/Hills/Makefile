CXX=		g++
#CXXFLAGS=	-g -std=c++98
CXXFLAGS=	-g -Wall -std=c++98
#CXXFLAGS=	-g -Wall -w -lSDL2 -lSDL2_image -lncurses -std=c++98
#CXXFLAGS=	-g -Wall -w -lSDL2 -lSDL2_image -std=c++98
SHELL=		bash
#PROGRAMS=	AliceGame BoardFolding
PROGRAMS=	jgraph

#all:	AliceGame BoardFolding
all:	jgraph

#AliceGame:	AliceGame.cpp AliceGame_TEST.cpp
#	$(CXX) $(CXXFLAGS) -o $@ $^

jgraph:	jgraph.cpp
#jgraph:	jgraphTest.cpp
#jgraph:	jGraph.cpp
	$(CXX) $(CXXFLAGS) -o $@ $^

.PHONY:		clean

clean:
	rm -f $(PROGRAMS)
