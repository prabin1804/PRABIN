import subprocess

data= subprocess.check_output(['netsh','wlan','show','profiles']).decode('utf-8',errors="backslashreplace").split('\n')
profiles =[i.split(":"),[1][1:-1] fori in data if "All User profile" in i]

for i in profile:
    results =subprocess.check_output(['netsh','wlan','show','profile',i,'key=clear']).decode('utf-8',errors="backslashreplace").split('\n')
    results = [b.spilt(":"),[1][1:-1] for i in results if "key Content" in b]
    try:
        print ("{:<30}| {:<}".format(i,results[0]))
        except IndexError:
            print ("{:<30}| {:<}".format(i,"None"))
            input("")