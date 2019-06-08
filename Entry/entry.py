import sys
import os
from DES.app import big_des
from GOST.app import Gost
from Serpent.app import Serpent

modules = {
    # 'DES': big_des,
    'GOST': {
        'bytes': 8,
        'module': Gost,
        'round_amount': 16
    },
    'Serpent': {
        'bytes': 16,
        'module': Serpent,
        'round_amount': 32
    }
}

def main_app():
    try:
        check()
    except Exception as e:
        print(e)


def check():
    cipher = sys.argv[1]
    regime = sys.argv[2]
    file_path = sys.argv[3]
    file_path_enc = sys.argv[4]


    if len(sys.argv) < 6:
        error = "python entry.py [cipher name] [regime] [file_path] [file_path_enc] [key]"
        raise Exception(error)
    elif cipher not in modules:
        if cipher == "--help":
            error = "python entry.py [cipher name] [regime] [file_path] [file_path_enc] [key]"
            raise Exception(error)
        else:
            error = "Wrong name of cipher! --help to see the manual"
            raise Exception(error)
    elif regime != "enc" and regime != "dec":
        error = "Wrong regime! --help to see the manual"
        raise Exception(error)
    elif os.path.isfile(file_path) == False:
        error = "Wrong path to file! --help to see the manual"
        raise Exception(error)
    elif os.path.exists(file_path_enc) == False:
        error = "Wrong path to directory! --help to see the manual"
        raise Exception(error)

    try:
        key = int(sys.argv[5])
    except ValueError:
        error = "key must be int!"
        raise Exception(error)


    new_cipher = modules[sys.argv[1]]['module']
    print(new_cipher)

    new_cipher.Enc_file(file_path, file_path_enc, file_path_enc)
    print("3")

if __name__ == "__main__":
    main_app()

