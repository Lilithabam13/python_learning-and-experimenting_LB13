x = [1,2,3,4,5]
z = x[0:4]
y = sum(x[0:2+1])
print(y)
print(z)

import platform

os_system = platform.system()
os_version = platform.version()
os_release = platform.release()
print(os_system)
print(os_version)
print(os_release)