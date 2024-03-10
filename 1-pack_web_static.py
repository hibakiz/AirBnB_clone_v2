#!/usr/bin/python3


import Fabric
from datetime import datetime
import os


def do_peak():
    """
    Genertates .tgz
    """
    env.local_dir = "~/AirBnB_clone_v2"
    now = datetime.now()
    filenmae = f"web_static_{now.strftime('%Y%m%d_%H%M%S')}.tgz"
    run("mkdir -p versions", pty=True)
    local(f"tar -cvzf versions/{filenmae} web_static/")
    return os.path.join(env.local_dir, "versions", filenmae)
