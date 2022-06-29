
int main() {
int [5]arr1;
int [5]arr2;
int [10]arr3;
int count = 0;
float x = 0.0;
bool flag = false;
for(int i=0;i<10;i = i+1) {
count = count - 1;
if(count < 5) {
arr3[i]=arr[i];
if(count*25 == 50) {
flag = true;
}
if(flag) {
while(x < 43) {
x = x+1;
if (x > 5) {
x = x * 1.1 + 7;
}
}
}
} else {
arr3[i]=arr[i-5];
}
}
return 0;
}
