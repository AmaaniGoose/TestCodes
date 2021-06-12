import re
import os
from pathlib import Path

if os.path.isfile('results/new.txt') :
    open('results/new.txt', "w").close()  ##Have to clear the file if it already exists before using it

def store_on_fs(data, file_name):
    ##Store data in file named `file_name`
    if data:
        try:
            with open(file_name, "a") as f:
                f.write(str(data))
        except:
            return 

def remove_time_stamp(content):
    if not content:
        return content
    # Remove time stamp
    new_content = re.sub(r"\d{2}:\d{2}:\d{2}", "", content)
    new_content = re.sub(r"\[\d{4}-\d{2}-\d{2}.*?\]", "", new_content)
    return new_content


def regexify(s):
    pattern = "\`\`\`([\s\S]*?)\`\`\`"
    substring = re.findall(pattern, s)
    result=''.join(substring)
    if result:
        try:
            return result
        except:
            return ' '




directory = 'text_files' ##enter directory address


for filename in os.listdir(directory):
    f = os.path.join(directory, filename)
    if os.path.isfile(f):
        with open(f,'r') as file:
            s=file.read()
            res=regexify(s)
            print(res)
            store_on_fs(res, 'results/new.txt') #Enter result file and use in loop to prevent unexplained behaviour
