inputKey1 = input()
inputKey2 = input()

safePassWord = {
  "key": "H",
  "key2": "4567"
}

def getPassword(key1,key2):
  if key1 == safePassWord.get("key") and key2 == safePassWord.get("key2"):
    print("safe unlocked")
  elif key1 == safePassWord.get("key") and key2 != safePassWord.get("key2"):
    print("safe locked - change digit")
  elif key1 != safePassWord.get("key") and key2 == safePassWord.get("key2"):
    print("safe locked - change char")
  else:
    print("safe locked")
    
getPassword(inputKey1,inputKey2)

