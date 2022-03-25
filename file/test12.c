
int main() {
int arr1[5] = {1,2,3,4,5};
int arr2[5] = {5,4,3,2,1};
int arr3[10];
int count = 0;
float x = 0.0;
bool flag = false;
for(int i=0;i<10;i++) {
count++;
if(count < 5) {
arr3[i]=arr[i];
if(count*25 == 50) {
flag = true;
}
if(flag) {
while(x < 43) {
x++;
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
