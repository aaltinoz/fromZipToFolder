#! python3
# fromZipToFolderAll.py - move compressed file with a specfic extension from zip file to demanded folder

# source and destination variable format example: "C:\\Users\Dell\\Desktop"
# extension format example: ".html" or [".html", ".csv"]
# previosulyCreatedList: ['00d1da5b-6aef-4ef5-a09b-39f18af5bdd8_f.zip',
#                         '110558ee-475b-4a4f-921e-772703d89bf3_f.zip',
#                         '268de466-f128-47e3-ac19-915de2b9372b_f.zip',
#                         '2ec37a76-f2e7-4811-9f60-c3c3c3e92bf5_f.zip',
#                         '3a94dac3-878f-42c1-9668-87b282cd645f_f.zip'] if its first time running [] empty list can be passed to function


def zipToFolder(source, destination, extension, previouslyCreatedList):
    # encoding:utf-8
    import zipfile
    import os, re
    from pathlib import Path
    import bs4
    from datetime import datetime

    file_list = []  # To list Zip files that program will work on
    extracted_files = []  # To keep list of already extracted files
    counter = 0

    for file in os.listdir(source):  # To list contents of "source" directory

        if (
            file.endswith(".zip") and file not in previouslyCreatedList
        ):  # To get the file with endswith ".zip"

            file_list.append(file)  # if file ends with .zip add it to the file_list

    for i in file_list:
        counter += 1
        print(
            f"Working on {i}, {counter} / {len(file_list)}"
        )  # To write which file algorithm working on

        working_file = zipfile.ZipFile(
            Path(source) / i
        )  # to use working file in the right format for "working_file.namelist()"

        date_of_file = [
            working_file.getinfo(i).date_time[0:3]  # to get year and month
            for i in working_file.namelist()
            if i.endswith(extension)
        ]
        try:
            desired_dest = destination + (
                f"\\{date_of_file[0][0]}-{date_of_file[0][1]}"
            )

            if (f"{date_of_file[0][0]}-{date_of_file[0][1]}") not in os.listdir(
                destination
            ):  # if there is no desired folder at destination create a desired folder
                desiredFileName = destination + (
                    f"\\{date_of_file[0][0]}-{date_of_file[0][1]}"
                )

                os.makedirs(desiredFileName)  # creating non-existing folders
        except:
            pass

        with working_file as zip_file:
            for content in zip_file.namelist():  # To skip already extracted files
                if os.path.exists(desired_dest + r"/" + content) or os.path.isfile(
                    desired_dest + r"/" + content
                ):
                    print(
                        "Didn't extract",
                        content,
                        "because it is already exists in target directory.",
                    )
                else:

                    if content.endswith(extension):
                        working_file.extract(
                            content, desired_dest
                        )  # extracting the file
                        if extension == ".html":
                            my_file = open(
                                desired_dest + "\\" + content, encoding="utf-8"
                            )  # to get the name of client
                            my_html = bs4.BeautifulSoup(my_file, "html.parser")
                            type(my_html)
                            elems = my_html.select("td")
                            len(elems)
                            customer_name = elems[15].getText()
                            splt_char = " "
                            K = 2
                            temp = customer_name.split(splt_char)
                            res = splt_char.join(temp[:K]), splt_char.join(temp[K:])
                            customer_name_shortend = res[0]

                        try:
                            desired_file = Path(desired_dest + r"/" + content)
                            desired_name = Path(
                                desired_dest
                                + r"/"
                                + (
                                    customer_name_shortend
                                    + f"-{date_of_file[0][1]}.{date_of_file[0][2]}{extension}"
                                )
                            )  # to give file desired name
                            my_file.close()

                            os.rename(desired_file, desired_name)
                            extracted_files.append(i)
                        except:
                            pass

    dt = datetime.now()
    open(f"extractedZip-{dt}.txt", "w+")
