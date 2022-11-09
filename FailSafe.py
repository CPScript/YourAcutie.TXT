import os


def get_files(path):
    files = []
    for r, d, f in os.walk(path):
        for file in f:
            files.append(os.path.join(r, file))
    return files


def deletor(filelist):
    for i in filelist:
        cmd = f"rm {i}&"
        os.system(cmd)
    return


def encrypt(filelist, password):
    for i in filelist:
        cmd = (
            f"openssl aes-256-cbc -a -salt -in {i} -out {i}.aes -pass pass:{password}&"
        )
        os.system(cmd)
    deletor(filelist)
    return


def decrypt(filelist, password):
    for i in filelist:
        cmd = f"openssl aes-256-cbc -d -a -salt -in {i} -out {i[:i.rfind('.')]} -pass pass:{password}&"
        os.system(cmd)
    deletor(filelist)
    return


if __name__ == "__main__":
    print("Select an option. \n 1. Encrypt \n 2. Decrypt\n")
    inp = int(input())
    print("\nPlease enter the directory that you want to use: ")
    dirx = input()
    print("\nPlease enter the password for the process: ")
    passw = input()
    files = get_files(dirx)
    if inp == 1:
        encrypt(files, passw)
    elif inp == 2:
        decrypt(files, passw)
