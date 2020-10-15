# -*- coding: utf-8 -*-
from qiskit import IBMQ
import getpass

token = getpass.getpass('IBM Q Experience Token:')
IBMQ.save_account(token, overwrite=True)
print('トークンが保存されました:', token[:4],'***',token[-4:])
