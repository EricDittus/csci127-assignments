#include<iostream>
using std::cout;
using std::endl;
int main(){
  int a, b, c, min, max;

  std::cout << "Pick a number from 0 to 99, inclusive.\n";
  std::cin >> a;
  min = 0;
  max = 99;

  b = (max + min/2);

  std::cout << "Is your number " << b << "?" << std::endl;
    std::cout << "Input:" << std::endl;
    std::cout << "-1: My number is lower, you're bad at this." << std::endl;
    std::cout << "1: My number is higher, you're still bad at this." << std::endl;
    std::cout << "0: You Got It! Wow, that was amazing!" << std::endl;
    std::cin >> c;

  while(c != 0){
     /*b = min + (rand() % static_cast<int>(max - min + 1));*/

    if(c = -1){
      max = b;

    }
    else{
      min = b;
    }
    b = (max + min)/2;
    std::cout << "Is your number " << b << "?" << std::endl;
    std::cout << "Input:" << std::endl;
    std::cout << "-1: My number is lower, you're bad at this." << std::endl;
    std::cout << "1: My number is higher, you're still bad at this." << std::endl;
    std::cout << "0: You Got It! Wow, that was amazing!" << std::endl;
    std::cin >> c;
  }
  std::cout << "Congrats to me!" << std::endl;
  return 0;
}
