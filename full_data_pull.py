import re
import csv

make = "Avigilon (ONVIF)"
model_list = ["1.3C-H4SL-D1", "2.0C-H4A-D1-B", "2.0C-H4A-DC2", "2.0C-H4M-D1",
              "2.0C-H4PTZ-DC30", "3.0C-H4A-D1-B", "3.0C-H4A-DC1", "3.0C-H4A-DC1-B",
              "3.0C-H4SL-D1", "3.0C-H4A-DO1-B", "24C-H4A-3MH-180", "2.0C-H5A-D1",
              "2.0C-H4PTZ-DP30", "2.0C-H5SL-D1", "3.0C-H5SL-D1", "4.0C-H5A-DO1",
              "6.0L-H4F-DO1-IR", "2.0C-H5A-PTZDC36", "5.0C-H5A-BO2-IR"]

new_file = input("What is the camera model? **Use Exact Casing and Symbols** ")
site_health_csv = "C:\\Users\\ADMIN-SURV\\Desktop\\data_pull\\IslandViewSiteHealth.csv"
file_path = "C:\\Users\\ADMIN-SURV\\Desktop\\data_pull\\"
filter_end_path = file_path + "filter_results\\" + new_file + ".txt"

output_txt_file = open(filter_end_path, 'w')
with open(site_health_csv, 'r') as fid:
    input_file = csv.reader(fid)
    for row in input_file:
        if row[0] == "Server Name":
            # skip first row
            continue
        if row[2] == make and row[3] == new_file:
            output_text = row[1] + " " + row[5] + " " + row[8]
            output_txt_file.write(output_text + "\n")
        # output_txt_file.close()
            dupe_file_path = "C:\\Users\\ADMIN-SURV\\Desktop\\data_pull\\filter_results\\"
            final_file_path = "C:\\Users\\ADMIN-SURV\\Desktop\\data_pull\\filter_results\\final\\"
            my_duplicates = new_file

            file_with_dupes = dupe_file_path + my_duplicates + ".txt"
            final_file = final_file_path + my_duplicates + "_final" + ".txt"

            openFile = open(file_with_dupes, "r")
            writeFile = open(final_file, "w")
            # Store traversed lines
            tmp = set()
            for row in openFile:
                # Check new line
                if row not in tmp:
                    writeFile.write(row)
                # Add new traversed line to tmp
                tmp.add(row)
            openFile.close()
    writeFile.close()
print("Scan Complete!")



