import os
import time

git_repo_url = ("https://github.com/xmrig/xmrig")
cmd = ("git clone " + git_repo_url)
os.system(cmd)

cmd1 = ("mkdir /var/Make/")
cmd2 = ("mv xmrig /var/Make/")
cmd3 = ("mkdir /var/Make/xmrig/build/")
cmd4 = ("cd /var/Make/build/; cmake -DWITH_HWLOC=OFF ..")
cmd5 ("cd /var/make/xmrig/build/; make")
cmd_install = ("apt-get install git build-essential cmake libuv1-dev libmicrohttpd-dev libssl-dev -y")

os.system(cmd1)
os.system(cmd_install)
os.system(cmd2)
os.system(cmd3)
os.system(cmd4)
os.system(cmd5)
os.system("clear")
print("Programme Successfull")

