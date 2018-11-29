#include <iostream>

int main()
{
  int i = 20;

  if (i > 10){
    std::cout << "i is greater than 10\n";
    std::cout << "more stuff not in the if statement\n";
  }

  if (i < 10){
    std::cout << "i is less than 10\n";
    std::cout << "more stuff not in the if statement\n";
  }
/*
  if (i > 10){
    std::cout << "i is greater than 10\n";
    std::cout << "with a second statement\n";
  }

  if (i > 10){
    std::cout << "i is greater than 10\n";
    std::cout << "with a second statement\n";
  }

  if (i > 10){
    std::cout << "i is greater with an else\n";
  } else {

  } else {

  } else {

  }
    std::cout << "with a second statement\n";
  }
*/

  return 0;
}
