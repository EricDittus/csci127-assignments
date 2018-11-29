# include <iostream>

int main()
{
  long int x;
  int i;
  int some_variable = 10 , another_variable;
  double d;
  char c;

  c = 'z';

  i = 20;

  i = i + some_variable;
  d = i;

  i = i /4.2;

  std::cout << "i = " << "\n";

  d = d/4.2;
  std::cout << "d = "<< d << "\n";

  std::cout << true << "\n";
  std::cout << false << "\n";
  std::cout << (i >100) << "\n";
  std::cout << (i <100)) << "\n";

  std::cout << "Please enter a number:";
  std::cin << i;
  return 0;
}
