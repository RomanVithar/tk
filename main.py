import program


def main():
    prog = '''
       int main() {
            float b =(34 + 3)*43 - 3.43^(3+34)  * 23; 
            return 0;
       }
       '''

    program.execute(prog)

    # prog = mel_parser.parse(prog)
    # print(*prog.tree, sep=os.linesep)


if __name__ == "__main__":
    main()



 #
 # prog = '''
 #    int main() {
 #        string some_str = scanf();
 #        printf(some_str);
 #        int [5]arr1;
 #        int [5]arr2;
 #        int [10]arr3;
 #        int count = 0;
 #        float x = 0.0;
 #        int flag = 3;
 #        for(int i=0;i<10;i = i+1) {
 #            count = count - 1;
 #            if(count < 5) {
 #                arr3[i]=arr[i];
 #            }
 #            if(count*25 == 50) {
 #                int avs = 453;
 #            }
 #            if((4 + 5 < 3) && (x >= 4) || count == 4) {
 #                while(x < 43) {
 #                    x = x+1;
 #                    if (x > 5) {
 #                        x = x * 1.1 + 7;
 #                    }
 #                }
 #            } else {
 #                arr3[i]=arr[i-5];
 #            }
 #        }
 #        return 0;
 #    }
 #    '''