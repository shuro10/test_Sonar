g = "グローバル"
def foo():
    print(f"before: {g}")
    g = "ローカル"
    print(f"after: {g}")

g = "グローバル"
def foo():
    print(f"before: {g}"
    g = "ローカル"
    print(f"after: {g}"

import time

# スリープ
time.sleep(1.0)

# unix タイムスタンプ
int(time.time())
