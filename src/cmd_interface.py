import subprocess
import shlex

def exec_command(command_line):
    if "icacls" in command_line:
        return

    args = shlex.split(command_line)
    process = subprocess.Popen(args, stdout=subprocess.PIPE, shell=True)
    output, error = process.communicate()
    return output.decode('cp866')

# import os
# import ctypes
# import re

# # https://docs.python.org/2/library/commands.html


# class CmdInterface:
    
#     is_admin = False
#     current_dir = os.getcwd()

#     cd_pattern1 = re.compile('cd[ ]*\.\.')
#     cd_pattern2 = re.compile('cd[ ]*\\\\')
#     cd_pattern3 = re.compile('cd[ ]+(\w+[\w|\/]+)')

#     def __init__(self):
#         self.current_dir = os.getcwd()
#         self.is_admin = self.isAdmin()
        

#     def isAdmin(self):
#         try:
#             self.is_admin = (os.getuid() == 0)
#         except AttributeError:
#             self.is_admin = ctypes.windll.shell32.IsUserAnAdmin() != 0
#         return self.is_admin
    
#     def get_Dir(self):
#         return self.current_dir

#     def exec_command(self, command):
#         if self.cd_pattern1.match(command):
#             self.current_dir = "C:"
#         elif self.cd_pattern2.match(command):
#             self.current_dir = os.getcwd()
#         elif self.cd_pattern3.match(command):
#             self.current_dir = self.current_dir + "\\" + self.cd_pattern3.match(command).group(1)
#         else: 
#             os.chdir(self.current_dir)
#             result = os.system(command)
#             return result
        
# def command_test(command):

#     cd_pattern1 = re.compile('cd[ ]*\.\.')
#     cd_pattern2 = re.compile('cd[ ]*\\\\')
#     cd_pattern3 = re.compile('cd[ ]+(\w+[\w|\/]+)')

#     if cd_pattern1.match(command):
#         current_dir = "C:"
#     elif cd_pattern2.match(command):
#         current_dir = os.getcwd()
#     elif cd_pattern3.match(command):
#         current_dir = current_dir + "\\" + cd_pattern3.match(command).group(1)
#     else: 
#         result = ""
#         # os.chdir(current_dir)
#         print("0>")
#         # result = os.system(command)
#         print(os.system(command))
#         print("1>" + str(result))
#         return 0

# if __name__ == "__main__":

#     while True:
#         result = command_test(input("> "))

#         print("2> " + str(result))