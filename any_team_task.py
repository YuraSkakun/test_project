s = '4e6f7720776520617265206c6f6f6b696e6720666f7220a48656164206f66204d6f62696c6520456e67696e656572696e67a50726f64756374204f776e657220666f72204d6f62696c65207465616da5465616d204c656164204261636b2d656e642028507974686f6e29a4d6964646c6520507974686f6e20646576a4a756e696f72204d616e75616c205141a4665656c206672656520746f20636f6e74616374206f75722072656372756974696e67207465616d20666f722064657461696c73206f722073656e6420796f7572204356a416e6e6120a54656c656772616d204062617262657261736174616ea4f6b73616e6120a54656c656772616d2040726f78795f66697265'

s1 = 'f0 9f 92 b8 48 69 20 42 72 61 69 6e 79 2c 20 63 75 72 72 65 6e 74 6c 79 20 49 27 6d 20 73 65 65 6b 69 6e 67 20 73 70 65 63 69 61 6c 69 73 74 73 20 66 6f 72 20 46 69 6e 54 65 63 68 20 70 72 6f 6a 65 63 74 73 20 69 6e 20 4b 79 69 76 20 f0 9f 87 ba f0 9f 87 a6 3a 0a 0a e2 99 a1 20 4f 70 65 6e 20 70 6f 73 69 74 69 6f 6e 73 20 e2 99 a1 0a f0 9f 94 a5 f0 9f 94 a5 42 61 63 6b 2d 65 6e 64 20 54 65 61 6d 20 4c 65 61 64 20 28 50 79 74 68 6f 6e 29 0a f0 9f 94 a5 f0 9f 94 a5 55 58 20 64 65 73 69 67 6e 65 72 0a f0 9f 94 a5 53 65 6e 69 6f 72 20 42 6f 74 20 64 65 76 65 6c 6f 70 65 72 0a f0 9f 94 a5 53 65 6e 69 6f 72 20 50 79 74 68 6f 6e 20 64 65 76 65 6c 6f 70 65 72 0a e2 80 a2 20 43 75 73 74 6f 6d 65 72 20 73 75 70 70 6f 72 74 20 61 67 65 6e 74 20 42 32 43 0a e2 80 a2 20 4d 69 64 64 6c 65 20 42 75 73 69 6e 65 73 73 20 41 6e 61 6c 79 73 74 0a e2 80 a2 20 4d 69 64 64 6c 65 20 50 79 74 68 6f 6e 20 64 65 76 65 6c 6f 70 65 72 20 28 70 61 79 6d 65 6e 74 20 73 79 73 74 65 6d 73 20 69 6e 74 65 67 72 61 74 69 6f 6e 29 0a 0a f0 9f 92 8c 20 46 65 65 6c 20 66 72 65 65 20 74 6f 20 63 6f 6e 74 61 63 74 20 6d 65 20 66 6f 72 20 64 65 74 61 69 6c 73 20 6f 72 20 73 65 6e 64 20 79 6f 75 72 20 43 56 0a 45 6d 61 69 6c 3a 20 73 61 74 61 6e 40 6a 63 61 73 68 2e 63 6f 0a 54 47 3a 20 74 2e 6d 65 2f 42 61 72 62 65 72 61 53 61 74 61 6e'
print(len(s))
l = len(s)
print(s[0], type(s[0]), s[0] + s[1])

l1 = len(s1)
s1_list = [('0x' + i) for i in s1.split(" ")]
print(s1_list)

s_list = [('0x' + s[i] + s[i+1]) for i in range(l) if i%2==0]
print((s_list))

for s_l in s_list:
    print(chr(int(s_l, 16)), end="")
print('#########################################')
for s_l in s1_list:
    print(chr(int(s_l, 16)), end="")



# sByte = bytearray.fromhex(s)
# sResult = sByte.decode("utf-16")
# print(sResult)

# s_str = ''.join(s_list)
# print(s_str)
# print(type(s_str))

# print(s_bytes.decode('utf-8'))