import subprocess

test = subprocess.run("apt-cache policy <app-name>", capture_output=True, text=True, shell=True)
test1 = test.stdout.splitlines()[1]
test2 = test.stdout.splitlines()[2]
print (test1.split()[1])


