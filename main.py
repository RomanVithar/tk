import program


def main():
    prog = '''
    int main()
    {
        int a = 4;
        string d = "fdsf";
        printf(d);
        string in_str = scanf();
        int [3]arr;
        int c = arr[2]; 
        return a;
    }

    '''
    program.execute(prog)

    # prog = mel_parser.parse(prog)
    # print(*prog.tree, sep=os.linesep)


if __name__ == "__main__":
    main()
