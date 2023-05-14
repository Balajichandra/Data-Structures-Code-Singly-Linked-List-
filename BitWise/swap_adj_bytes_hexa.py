n = 0x1234
res = (n<<8) & (0xff00) | (n>>8) & (0x00ff)
print("After swaping adjacent bytes:",res)