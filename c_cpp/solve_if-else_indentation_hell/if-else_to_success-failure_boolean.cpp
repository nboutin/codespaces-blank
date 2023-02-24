

bool func1();
bool func2();
bool func3();

int main(int argc, char **argv)
{
  bool success = func1();
  success &= func2();
  success &= func3();
}

bool func1()
{
  return true;
}

bool func2()
{
  return true;
}

bool func3()
{
  return true;
}
