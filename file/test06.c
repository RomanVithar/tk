int main() {
  int count = 10;
  int count2 = 10;
  while(count) {
    while(count2 != 5){
      count = count - 2;
      if(count == 6) {
        break;
      }
    }
  count = count - 1;
  }
  return 0;
}
