# -*- coding: utf-8 -*-
from qiskit import IBMQ
from qiskit.providers.ibmq import least_busy

provider = IBMQ.load_account()
backends = provider.backends()
print('バックエンド一覧')
for backend in backends:
    print(backend.name())

print('5量子ビットの最も低負荷なバックエンド')
q5devices = provider.backends(filters=lambda x: x.configuration().n_qubits == 5
                                   and not x.configuration().simulator)
least_busy_backend = least_busy(q5devices)
print(least_busy_backend)
