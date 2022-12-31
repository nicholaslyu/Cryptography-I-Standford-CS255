import base64
from Crypto.Util import Counter

from Crypto.Cipher import AES
import codecs
from Crypto.Util.Padding import unpad
CBS_CIPHERS=['4ca00ff4c898d61e1edbf1800618fb2828a226d160dad07883d04e008a7897ee2e4b7465d5290d0c0e6c6822236e1daafb94ffe0c5da05d9476be028ad7c1d81',
             '5b68629feb8606f9a6667670b75b38a5b4832d0f26e1ab7da33249de7d4afc48e713ac646ace36e872ad5fb8a512428a6e21364b0c374df45503473c5242a253']

CBS_KEYS = ['140b41b22a29beb4061bda66b6747e14',
            '140b41b22a29beb4061bda66b6747e14']

CTR_CIPHERS = ['69dda8455c7dd4254bf353b773304eec0ec7702330098ce7f7520d1cbbb20fc388d1b0adb5054dbd7370849dbf0b88d393f252e764f1f5f7ad97ef79d59ce29f5f51eeca32eabedd9afa9329',
               '770b80259ec33beb2561358a9f2dc617e46218c0a53cbeca695ae45faa8952aa0e311bde9d4e01726d3184c34451']

CTR_KEYS = ['36f18357be4dbd77f050515c73fcf9f2',
            '36f18357be4dbd77f050515c73fcf9f2']

def decode_to_bytes(hex_str):
    return codecs.decode(hex_str, 'hex')

def decrypt_cbs(key,cipher):
    iv = cipher[:16]
    obj = AES.new(key, AES.MODE_CBC,iv)
    decrypted = obj.decrypt(cipher[16:])
    pt = unpad(decrypted, AES.block_size)
    return pt
def decrypt_ctr(key, cypher):
    iv = cypher[:16]
    ct1 = cypher[16:]
    counter = int.from_bytes(iv[8:], "big")
    obj = AES.new(key, AES.MODE_CTR, initial_value=counter,nonce=iv[:8])
    return obj.decrypt(ct1)

def main():
    cbs_ciphers = [decode_to_bytes(str_) for str_ in CBS_CIPHERS]
    cbs_keys = [decode_to_bytes(str_) for str_ in CBS_KEYS]
    ctr_ciphers = [decode_to_bytes(str_) for str_ in CTR_CIPHERS]
    ctr_keys = [decode_to_bytes(str_) for str_ in CTR_KEYS]
    pt_cbs = []
    pt_ctr= []
    for i in range(len(ctr_keys)):
        pt_cbs.append(decrypt_cbs(cbs_keys[i],cbs_ciphers[i]))
        pt_ctr.append(decrypt_ctr(ctr_keys[i],ctr_ciphers[i]))
    print(pt_cbs)
    print(pt_ctr)

main()









