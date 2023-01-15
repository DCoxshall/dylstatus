from lib.render import render

print("{\"version\": 1}")
print("[[],")
while True:
    blocks = [{"full_text": "hello"}]
    render(blocks)
    import time
    time.sleep(0.125)
