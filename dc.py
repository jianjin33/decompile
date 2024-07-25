import os
import sys


sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), 'dc_dex')))
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), 'dc_res')))
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), 'dc_clean')))

from dc_dex import decompile_dex
from dc_res import decompile_res_smali
from dc_clean import clean

if __name__ == "__main__":
    clean()
    decompile_dex()
    decompile_res_smali()