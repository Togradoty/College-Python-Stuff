def main():
    
    #gets the file name from the user
    filename = input("Enter the name of the file here: ")
    
    #opens the file and only reads it
    infile = open(filename, "r")
    
    #starts at line number one
    line_number = 1
    
    #reads every line in the file starting at 1
    for line in infile:
        print(f"{line_number}: {line.strip()}")
        line_number += 1
    
    #closes file once done
    infile.close()

if __name__ == "__main__":
    main()

