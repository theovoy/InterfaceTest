import time
import hashlib
import encrypt_aes_p
#timestamp=str(int(round(time.time() * 1000)))
vcode='TC007'
secret='71526121fa9c4fae8616c225c87d0eca'
class Token:

    def gettoken(self,time):
        data=secret+'&'+vcode+'&'+time
        encryptdata=encrypt_aes_p.encrypt(data,secret)
        token=hashlib.md5(encryptdata.encode('utf8')).hexdigest()
        print(time)
        print(token)
        return token

if __name__ == "__main__":
    token=Token()
    eg=token.gettoken(str(int(round(time.time() * 1000))))