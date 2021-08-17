import csv
import os.path


class FileUtil(object):
    """
    A class used to handle read and write to files.
    """

    @staticmethod
    def write_record_csv_file(file_name, header, record):
        """
        A function used to write records to a csv file.

        Parameters:
        file_name (string): the name of the file.
        header (string): the header required to write to the file.
        record (list): the data required to write to the file.
        """
        file_exists = os.path.isfile(file_name)
        with open(file_name, "a", newline="") as csv_file:
            # get writer object of the file
            csv_writer = csv.writer(csv_file)
            if not file_exists:
                csv_writer.writerow(header)  # file doesn't exist yet - write a header
            csv_writer.writerow(record)

    @staticmethod
    def read_record_csv_file(file_name):
        """
        A function used to read records from a csv file.

        Parameters:
        file_name (string): the name of the file.

        Returns:
        records (list of strings): contains the rows from the excel file.
        Exception if file not found.
        """
        file_exists = os.path.isfile(file_name)
        if file_exists:
            with open(file_name, "r") as csv_file:
                records = []
                # get reader object of the file
                csv_reader = csv.reader(csv_file)
                # iterate over each row in the file and add to the records list
                for row in csv_reader:
                    records.append(row)
                return records
        else:
            raise Exception("File not found")
