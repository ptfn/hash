import hashlib
s = input("Введите число ")
print("Выберите алгоритм хеширования ")
hash1 = input("md5(m)/SHA(s)")
if hash1 =='':
  print('error')
else:
  if hash1 == "m":
    m = hashlib.md5(str(s).encode("ascii")).hexdigest()
    print ("md5:",m)
  if hash1 == "s":
    sha = input("sha-1(1)/sha-256(2)/sha-512(3)")
    if sha == "1" :
      sha1 = hashlib.sha1(str(s).encode("ascii")).hexdigest()
      print ("sha1:",sha1)
    if sha == "2" :
      sha2 = hashlib.sha256(str(s).encode("ascii")).hexdigest()
      print ("sha256:",sha2)
    if sha == "3" :
      sha3 = hashlib.sha512(str(s).encode("ascii")).hexdigest()
      print ("sha384:",sha3)
