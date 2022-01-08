from .csv import CSVHandler


def setup_test_values():
    csv_handler = CSVHandler.CSVHandler()
    csv_handler.create_files_folder_if_not_exists()

    with open("src/files/tracker.csv", "w") as f:
        f.write("start_date,start_time,stop_date,stop_time,work_hours,message\n"
                "\"Jan, 07 2022\",14:41:56,\"Jan, 07 2022\",14:42:56,00:01:00,\n"
                "\"Jan, 07 2022\",14:44:39,\"Jan, 07 2022\",14:44:42,00:00:03,My message\n"
                "\"Jan, 08 2022\",10:41:19,\"Jan, 08 2022\",14:45:56,00:04:47,Another message\n"
                "\"Jan, 08 2022\",10:54:29,\"Jan, 08 2022\",15:02:42,00:06:23,My second message\n"
                )


if __name__ == "__main__":
    setup_test_values()
