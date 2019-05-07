#!/usr/bin/env python
# -*- coding:utf-8 -*-

import os
import sys, getopt

def usage():
    print ("Usage:\tpython3 merge.py < output dir > [--hard]")

def get_target_dir(path):
    dir = os.path.basename(path)
    if dir == "":
        err_str = "Error: Undefine save dir"
        return False, err_str 

    basic_dir = os.path.dirname(path)
    if basic_dir == "":
        basic_dir = "./"

    try:
        process = os.popen("cd %s ; pwd" % basic_dir)
        os_dir = process.read().replace('\n', '')
        if os.path.exists(os_dir) == True:
            basic_dir = os_dir
        else:
            basic_dir = os.path.abspath(basic_dir)

        print("Basic:", basic_dir)
    except FileNotFoundError as err:
        return False, err

    final_dir = basic_dir + "/" + dir
    x_dir = os.path.exists(final_dir)
    if x_dir:
        select = input(("Warnning: %s directory already exists.\n\
continue execution may OVERWRITE the contents of %s directory, whether to change the saved directory:[new path|continue|exit]") % (final_dir, final_dir))
        if select == "continue":
            return True, final_dir
        elif select == "exit":
            os._exit(0)
        else:
            return get_target_dir(select)

    os.mkdir(final_dir)
    return True, final_dir

if __name__ == '__main__':
    pn = len(sys.argv)
    options = " -f "    # -f 存在则覆盖
    if pn != 2 and pn != 3:
        usage()
        os._exit(-1) 
    elif pn == 3:
        if sys.argv[2] != "--hard":
            usage()
            os.exit(-1)
    else:
        options += " -s "   # -s 建立软连接，

    if os.name == "posix":
        ret, dir = get_target_dir(sys.argv[1])
        if not ret:
            print(dir)
            os._exit(-1)
        else:
            print (("SAVE TO DIR: %s") % (dir))
           
        img_path = "./images/"
        img_path = os.path.abspath(img_path)
    
        print(os.getcwd())
        os.chdir(dir) # 先获取绝对路径， 再改变当前路径
        print(os.getcwd()) 

        img_counter = 0 
        dir_counter = 0
        dir_total = len(os.listdir(img_path))
        while dir_counter < dir_total:
            cur_img_dir = os.popen(("ls -d %s/%03d*") % (img_path, dir_counter)).read().replace('\n','')
            cur_img_counter = 0 

            try:
                cur_img_total = len(os.listdir(cur_img_dir))
            except FileNotFoundError as err:
                print(err)
                dir_counter += 1
                continue
                
            print(("DIR: %s MERGE LINK TO %s") % (os.path.basename(cur_img_dir), dir))
            while cur_img_counter < cur_img_total:
                img_file = os.popen(("ls -f %s/%06d*") % (cur_img_dir, cur_img_counter)).read().replace('\n','')
                suffix =  os.path.splitext(img_file)[-1]
                os.system(("ln %s %s %06d%s") % (options, img_file, img_counter, suffix)) 
                cur_img_counter += 1
                img_counter += 1
                print(("DIR %3d/%-3d IMAGE %6d/%-6d > %06d") % (dir_counter, dir_total, cur_img_counter, cur_img_total, img_counter))

            dir_counter += 1

            
