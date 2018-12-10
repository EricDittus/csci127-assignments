#include <iostream>
#include <math.h>
int a,b,c,r,disc;

int discriminant(int a, int b, int c){
    int disc = (b^2)-(4*a*c);
    return disc;
}

int quadsolve(int a, int b, int c){
  if(discriminant(a,b,c)>=0){
    int r = (sqrt(discriminant(a,b,c)) -(b))/(2*a);
    return r;
  }
  else{return 0;}
}

int main()
{
  std::cout << "discriminant function test:\n\n";
  std::cout << "a = 3, b = 5, c = 2\n";
  std::cout << discriminant(3,5,2) << std::endl;
  std::cout << "a = 1, b = -2, c = 20\n";
  std::cout << discriminant(1,-2,20) << std::endl;
  std::cout << "a = 0, b = -20, c = -200\n";
  std::cout << discriminant(0,-20,-200) << std::endl;

  std::cout << "quadsolve function test:\n\n";
  std::cout << "a = 3, b = -4, c = -5\n";
  std::cout << quadsolve(3,-4,-5) << std::endl;
  std::cout << "a = 1, b = -2, c = -20\n";
  std::cout << quadsolve(1,-2,-20) << std::endl;
  std::cout << "a = 0, b = -20, c = -200\n";
  std::cout << quadsolve(0,-20,-200) << std::endl;

}
