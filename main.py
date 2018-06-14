import os

import gen
import concat
import visu

if(__name__ == "__main__"):
    print("Generating optimal solutions...")
    gen.main()
    print("done.\n Concatenating files...")
    concat.main()
    print("done.\n Creating visualization...")
    visu.main()
    print("done.\n Cleaning up...")

    for i in range(256):
        os.remove(str(i) + ".txt")

    print("done.\n Generated files visualization.png and all.txt\n")
