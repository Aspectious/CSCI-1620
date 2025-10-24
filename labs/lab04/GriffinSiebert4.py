import re;
import csv;

def main() -> None:

    # Reads input data from file
    #
    inputFile = open('input.txt', 'r');
    addresses = [];
    dictbook = {};
    for line in inputFile:
        if (re.match(r"(From )", line)):

            # Cleans up the strings and splits it into an array we can use with data
            line = line.strip();
            line = line.replace("  ", " ");
            line = line.replace("From ", "");
            line = line.split(" ");
            addresses.append(line);
        elif (re.match(r"(From: )", line)):
            line = line.strip();
            line = line.replace("From: ", "");
            if line not in dictbook:
                dictbook[line] = 1;
            else:
                dictbook[line] += 1;
    inputFile.close();


    # Writes input data to files
    #
    csvfile = open('output.csv', 'w',newline='');
    header = ["Email","Day","Date","Month","Year","Time"]
    writer = csv.writer(csvfile)
    writer.writerow(header)
    for arr in addresses:
        # why did you truncate leading zeros for the time in the sample csv file
        # now i have to do this to make it match perfectly
        if (arr[4].startswith("0")):
            arr[4] = arr[4].replace("0", "",1);
        changedarr = [arr[0],arr[1],arr[3],arr[2],arr[5],arr[4]];
        writer.writerow(changedarr);
    csvfile.close();

    # TODO: VALUES FOR LJUST
    # I did the math on it perfectly so it will do the whitespace calculations every time
    # ljust by 41 on each entry (NOT 40 SOMEHOW)
    # print 49 dashes for bottom line
    outfile = open('output.txt', "w");
    outfile.write("Email".ljust(41, " ") + "- Count\n");
    total = 0;
    for key in dictbook:
        total += dictbook[key];
        outfile.write(key.ljust(41, " ") + "- " + str(dictbook[key]) + "\n");

    outfile.write("".ljust(49, "-") + "\n");
    outfile.write("Total emails".ljust(41, " ") + "- " + str(total) + "");
    outfile.close();









if "__main__" == __name__:
    main();