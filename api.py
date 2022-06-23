import shutil
from_directory = r"C:\ProgramData\Jenkins\.jenkins\workspace\jenkinspipeline\WebApplication1\bin"
to_directory = r"C:\ProgramData\Jenkins\.jenkins\workspace\jenkinspipeline\PROD\bin"

shutil.copytree(from_directory, to_directory)
