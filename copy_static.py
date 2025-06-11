import os
import shutil

def recursive_copy(src_path, dst_path):
    if not os.path.exists(dst_path):
        os.makedirs(dst_path)

    for item in os.listdir(src_path):
        s_item = os.path.join(src_path, item)
        d_item = os.path.join(dst_path, item)

        if os.path.isdir(s_item):
            recursive_copy(s_item, d_item)
        else:
            print(f"Copying {s_item} to {d_item}")
            shutil.copy2(s_item, d_item)

def copy_static_files(src, dst):
    src = "static"
    dst = "public"

    if os.path.exists(dst):
        shutil.rmtree(dst)
    os.makedirs(dst)

    recursive_copy(src, dst)

