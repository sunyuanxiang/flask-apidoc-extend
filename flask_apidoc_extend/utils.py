import platform
import subprocess


def apidoc_cmd():
    apidoc = 'apidoc'
    sys = platform.system()
    if sys == 'Windows':
        p = subprocess.Popen(['where', 'apidoc.cmd'],shell=True, stdout=subprocess.PIPE)
        stdout = p.communicate()[0]
        apidoc = stdout.decode('utf-8').split()[0]
    return apidoc
