# import os

# with open("server.log", "w") as f:
#     f.write("INFO: Server started successfully\n")
#     f.write("ERROR: Database connection failed\n")
#     f.write("WARNING: Memory usage above 80%\n")
#     f.write("ERROR: Unauthorized access attempt\n")

# with open("server.log", "a") as f:
#     f.write("INFO: User logged in")
# try: 
#     with open("server.log", "r") as f:
#         lines = f.readlines()  # readlines krky aik list milti hy

#         for line in lines:
#             if "ERROR" in line:
#                 print(line.strip())

# except FileNotFoundError:
#     print("File mot found")


# # for reading multiple lines: lines = f.readlines()
# # OR
# # for line in f:
#         # print(line.strip())

import os

class LogManager:
    def __init__ (self, filepath):
        self.filepath=filepath

    def add_log(self, level, message):
        with open(self.filepath,"a") as f:
            f.write(f"[{level}], {message}\n")


    def read_all(self):
        try:
            with open(self.filepath,"r") as f:
                lines = f.readlines()
                for line in lines:
                    print(line.strip())
        except FileNotFoundError:
            print("file not found")

    def filter_by_level(self, level):
        try:
            with open(self.filepath,"r") as f:
                lines = f.readlines()
                for line in lines:
                    if level in line:
                        print(line.strip())
        except FileNotFoundError:
            print("file not found")