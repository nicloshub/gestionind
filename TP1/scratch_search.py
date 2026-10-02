with open(r'C:\Program Files\draw.io\resources\app.asar', 'rb') as f:
    content = f.read()

pos = 0
for _ in range(5):
    pos = content.find(b'data:image/png,', pos + 1)
    if pos == -1: break
    print("Found at:", pos)
    print(content[pos-50:pos+200].decode('latin1', errors='ignore'))
    print("---")
