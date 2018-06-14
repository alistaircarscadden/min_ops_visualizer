# Puts the data of 0...255.txt into all.txt

def write(f, t):
    for line in f:
        t.write(line)

def main():
    with open("all.txt", "w") as a:
        for i in range(256):
            with open(str(i) + ".txt", "r") as file:
                for line in file:
                    a.write(line)
					
if(__name__ == "__main__"):
    main()
