#include <iostream> 
#include <cstdlib> 

int main(int argc, char *argv[]) { 
    // Ensure correct number of arguments
    if (argc < 4) {
      std::cout << "Usage: tmovecheck file player move\n"
                          "Where: "
                          "file is the name of a file that contains the board configuration\n"
                          "       player is either B or W, indicating which player the agent should assume\n"
                          "       move is the move the player intends to execute" << std::endl  ;
      return 0 ;
     } 

    system("pwd") ;
    std::cout << "Hello world" << std::endl;

    return 0;
}
