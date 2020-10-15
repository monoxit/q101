# -*- coding: utf-8 -*-
import re

path = '/etc/dphys-swapfile'

print('スワップ容量を増やします')

try:
    with open(path) as f:
        content = f.read()

except Exception as e:
    print('ファイルが開けません', path, e)
    quit()

changed_content = re.sub(r'(CONF_SWAPSIZE=)\d+', r'\g<1>1024', content, flags=re.DOTALL)

with open(path, mode='w') as f:
    f.write(changed_content)

print(path,'のスワップ容量を正常に変更しました。')