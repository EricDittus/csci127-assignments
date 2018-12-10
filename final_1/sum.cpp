#include <iostream>

int sum;

int sumofsquares(int a, int b){
  int sum = 0;
  for(int i = a; i<=b; i++){
    sum = sum + (i^2);
  }
  return sum;
}

int main()
{
  std::cout << "sumofsquares function test:\n\n";
  std::cout << "Range 1 to 10\n";
  std::cout << sumofsquares(1,10) << std::endl;
  std::cout << "Range 3 to 5\n";
  std::cout << sumofsquares(3,5) << std::endl;
  std::cout << "Range 20 to 21\n";
  std::cout << sumofsquares(20,21) << std::endl;
}
