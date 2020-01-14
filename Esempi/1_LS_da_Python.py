import subprocess as s

s.run(["dir", "-l", "/dev/null"], capture_output=True)