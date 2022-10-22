from cryptography.fernet import Fernet
import pickle
import sys

keys = dict()

keys["car_00"] = Fernet.generate_key()
keys["car_01"] = Fernet.generate_key()
keys["car_02"] = Fernet.generate_key()
keys["car_03"] = Fernet.generate_key()

f = open("keys.pkl", "wb")
pickle.dump(keys, f)

print(keys)