import re
import os
from pathlib import Path

if os.path.isfile('results/new.txt') :
    open('results/new.txt', "w").close()  ##Have to clear the file if it already exists before using it

def store_on_files(data, file_name):
    ##Store data in file named `file_name`
    if data:
        try:
            with open(file_name, "a", encoding='utf-8') as f:
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
            return remove_time_stamp(result)
        except:
            return ' '

issue_details = dict()

def data_storage_func():
    dir = './data/GitHubData/IssueContent' ##enter directory address
    for filename in os.listdir(dir):
        f = os.path.join(dir, filename)
        if os.path.isfile(f):
            with open(f,'r', encoding='utf-8') as file:
                s=file.read()
                res=regexify(s)
                if res == 'None':
                    issue_details['issue_content_console_path'] = 'N/A'
                else:
                    issue_details['issue_content_console_path'] = './results/new.txt'

                store_on_files(res, 'results/new.txt') #Enter result file and use in loop to prevent unexplained behaviour
                


if __name__ == '__main__':
	data_storage_func()