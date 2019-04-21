import subprocess

res = subprocess.Popen('dir', shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

print(res.stdout.read().decode('gbk'))
if not res.stderr.read():
    print(res.stderr.read().decode('gbk')+ '1213')