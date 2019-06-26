import os
import sys

import pydiff

fnames=[]

def getchangeline(a,b,f):
    deletionlist=[]
    addlist=[]
    result = pydiff.diff(a, b, f)
    filename_list=None
    if len(result) > 0:
        for one in result:
            if one.status == -1 and (not one.val.strip()==""):
                deletionlist.append(one)
            elif one.status == 1and (not one.val.strip()==""):
                addlist.append(one)
        delete = [m for m in deletionlist]
        for j in delete:
            for add in addlist:
                if j.val.strip() == add.val.strip():
                    deletionlist.remove(j)
                    addlist.remove(add)
                    break
        flag=True
        # for add in addlist:
        #     if "if" in add.val:
        #         flag=True
        if flag:
            filename_deletionlist = f +"$Del "
            filename_addlist = "$ADD "
            # if len(addlist)>0  and len(addlist)<10 and len(deletionlist)<10:
            if len(addlist) > 0:
                for item_ in deletionlist:
                    item = item_.col
                    filename_deletionlist = filename_deletionlist + str(item) + " "
                for item_2 in addlist:
                    item2 = item_2.col
                    filename_addlist = filename_addlist + str(item2) + " "
                filename_deletionlist = filename_deletionlist.strip(" ")
                filename_addlist = filename_addlist.strip(" ")

                filename_list = filename_deletionlist +filename_addlist
                # print(filename_list)

            else:
                pass
                # print(f + "  addlist length deletion length 这里不合格")
                # print(len(addlist), len(deletionlist))
    return filename_list

if __name__ == '__main__':
    basedir=r"C:\Users\troye sivan\Desktop\GithubDATA\bufferC\javafiles"
    for i in range(2009,2019):
        year=str(i)
        new_javafile=os.path.join(basedir,"new_files/"+year)
        old_javafile=os.path.join(basedir,"old_files/"+year)
        last_line=0
        for root,dirs,files in os.walk(new_javafile):
            i=0
            length=len(files)
            for f in files:
                # if f=="02f192f92a9ce566abab3622074a0ae096017d38.java":
                i=i+1
                if i<=last_line:
                    pass
                else:
                    # if f.endswith("java"):
                        try:
                            with open(os.path.join(root,f), "r", encoding='UTF-8') as f_new:
                                file_new = f_new.read()
                            with open(os.path.join(root,f).replace("new","old") ,"r", encoding='UTF-8') as f_old:
                                file_old = f_old.read()
                                a = file_old
                                b = file_new
                                result = getchangeline(a, b, f)
                                storepath=os.path.join(basedir,"changeline_"+year)
                                if not result == None:
                                    with open(storepath, "a", encoding="utf-8") as f:
                                        f.write(result)
                                        f.write("\n")
                                        f.flush()
                        except UnicodeDecodeError as e:
                            pass
                        except FileNotFoundError as e:
                            pass
                # print("\r%s%% |%d" % (int(i % length), length,int( * '#'), end="")
                print("\r%s%% |%d" % (int((i*100)/ length), length), end="")
                sys.stdout.flush()

