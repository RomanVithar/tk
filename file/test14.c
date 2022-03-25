int f(int a) {
if(a == 1) {
return 1;
}
return a * f(a-1);
}

int main() {
int b = f(4);
return 0;
}
