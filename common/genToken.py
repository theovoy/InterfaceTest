import time
import hashlib
import encrypt_aes_p
vcode_qa='TC001'
secret_qa='e291c6a536ec4257812d13f00acd26d8'
vcode='TC007'
secret='c818b80eb1284276b67f72bd766c2c9b'

class Token:
    def gettoken(self,time,env):
        if env =='p':
            data=secret+'&'+vcode+'&'+time
            encryptdata=encrypt_aes_p.encrypt(data,secret)
            token=hashlib.md5(encryptdata.encode('utf8')).hexdigest()
            print('线上')
            return token
        else:
            if env == 'qa':
                data=secret_qa+'&'+vcode_qa+'&'+time
                encryptdata=encrypt_aes_p.encrypt(data,secret_qa)
                token=hashlib.md5(encryptdata.encode('utf8')).hexdigest()
                print('qa')
                return token

            print('请输入正确环境')


if __name__ == "__main__":
    token=Token()
    timestamp=str(int(round(time.time() * 1000)))
    eg=token.gettoken(timestamp,'p')
    print(timestamp)
    print(eg)
    to='||##||'
    tt=hashlib.md5(to.encode('utf8')).hexdigest()
    print(tt)