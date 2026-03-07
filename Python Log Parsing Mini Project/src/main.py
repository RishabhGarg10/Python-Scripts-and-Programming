#step 1 : Read the file
#step 2 : extract information like ip adresses, request failed vs successful
#step 3 : save output into csv, excel file
#step 4 : sending email with file

import re
import pandas as pd

my_logfile = open("logs/serverlogs", "r")

ip = r'^\d+\.\d+\.\d+\.\d+'
status = r'"\s(\d{3})'
data_tf = r'\s\d{3}\s(\d+)\s'


def fetch(logfile):
    ip_list = []
    status_list = []
    data_tf_list = []

    for lf in logfile:
        ip_re = re.search(ip, lf)
        ip_list.append(ip_re.group())
    
        status_re = re.search(status, lf)
        status_list.append(status_re.group(1))
    
        data_tf_re = re.search(data_tf, lf)
        data_tf_list.append(data_tf_re.group(1))

    report = {
        "ip": ip_list,
        "status": status_list,
        "data_tf": data_tf_list
    }    
    return report

df_1 = pd.DataFrame(fetch(my_logfile))
print(df_1.head())   

def convert_csv(df):
    df.to_csv("report/serverlogs_report.csv", index=False)

csv_file = convert_csv(df_1)    
print(csv_file)