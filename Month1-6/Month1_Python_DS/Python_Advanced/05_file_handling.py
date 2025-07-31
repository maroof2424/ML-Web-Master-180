def main():
    # Task 1
    lines = ['line1','line2','line3']
    with open('myfile.txt','w') as f:
        for line in lines:
            f.write(line+'\n')

    # Task2

    with open('myfile.txt','r') as f:
        print(f.read())


    # Task3

    with open('myfile.txt','a') as f:
        f.write("Appended Line\n")

if __name__ == "__main__":
    main()