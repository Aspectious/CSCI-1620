import os.path;
import re;

def main():


    # File and Path Logic / Handling
    # Should provide both infile and outfile
    infile = ""
    filevalid = False
    while not filevalid:
        temppath = "./files/" + input("Input file name: ").strip()

        try:
            tempfile = open(temppath);
            filevalid = True;
            infile = temppath
            tempfile.close()
        except:
            print("File does not exist!")

    outfile = ""
    filevalid = False
    promp = "Output file name: "
    while filevalid == False:
        # I wasn't sure if I were to prompt the user or not for the initial output file name,
        # But the examples are highlighted in red which implies user input.
        # I went ahead and handled it anyway under that implication.
        temppath = "./files/" + input(promp).strip();

        if os.path.isfile(temppath):
            promp2 = "Overwrite existing file? (y/n): "
            ansgood = False
            while ansgood == False:
                resp = input(promp2).strip().lower()
                if (resp.startswith("y") or resp.startswith("n")):
                    ansgood = True;
                else:
                    promp2 = "Enter (y/n):"
            if (resp.startswith("n")):
                promp = "New output file name: "
                filevalid = False;
            else:
                filevalid = True;
                outfile = temppath;
        else:
            filevalid = True;
            outfile = temppath;


    # Data Handling
    valfile = open(infile, "r")
    output = open(outfile, "w")
    output.write("Email,Time,Confidence\n")
    values = [[],[],[]]
    for line in valfile:
        if (line.startswith("From: ")):
            values[0].append(line.strip().replace("From: ", ""))
        if (line.startswith("X-DSPAM-Processed: ")):
            drgxfmt = "[0-9]{2}:[0-9]{2}:[0-9]{2}"
            match = re.search(drgxfmt, line)
            timeval = match.group(0)
            if (re.match("0[0-9]:[0-9]{2}:[0-9]{2}",timeval)):
                timeval = timeval[1:] # Removes the leading zero from some times for an unknown reason
            values[1].append(timeval)

        if (line.startswith("X-DSPAM-Confidence: ")):
            confidence = line.strip().replace("X-DSPAM-Confidence: ", "")
            values[2].append(float(confidence))

    if (len(values[0]) == 0):
        print("No Confidence values present!")
    else:
        for i in range(len(values[0])):
            csvstr = f"{values[0][i]},{values[1][i]},{values[2][i]}\n"
            output.write(csvstr)
        avgtxt = f',Average,{sum(values[2])/len(values[2]):.4f}\n'
        output.write(avgtxt)
        print("Data stored!")

    valfile.close()
    output.close()








if __name__ == "__main__":
    main()
