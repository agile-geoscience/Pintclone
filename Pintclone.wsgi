import os

os.environ['PATH'] = "/home/ubuntu/torch/install/bin:/home/ubuntu/bin:/home/ubuntu/.local/bin:/home/ubuntu/torch/install/bin:/home/ubuntu/anaconda3/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/usr/local/games:/snap/bin"

os.environ['LUA_PATH'] = "/home/ubuntu/rando/?.lua;/home/ubuntu/.luarocks/share/lua/5.1/?.lua;/home/ubuntu/.luarocks/share/lua/5.1/?/init.lua;/home/ubuntu/torch/install/share/lua/5.1/?.lua;/home/ubuntu/torch/install/share/lua/5.1/?/init.lua;./?.lua;/home/ubuntu/torch/install/share/luajit-2.1.0-beta1/?.lua;/usr/local/share/lua/5.1/?.lua;/usr/local/share/lua/5.1/?/init.lua"

os.environ['LUA_CPATH'] = "/home/ubuntu/torch/install/lib/?.so;/home/ubuntu/.luarocks/lib/lua/5.1/?.so;/home/ubuntu/torch/install/lib/lua/5.1/?.so;./?.so;/usr/local/lib/lua/5.1/?.so;/usr/local/lib/lua/5.1/loadall.so"

os.environ['DYLD_LIBRARY_PATH'] = "/home/ubuntu/torch/install/lib:/home/ubuntu/torch/install/lib"

os.environ['LD_LIBRARY_PATH'] = "/home/ubuntu/torch/install/lib:/home/ubuntu/torch/install/lib"

from Pinclone import application

