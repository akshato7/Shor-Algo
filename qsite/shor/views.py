from django.http import JsonResponse
from django.shortcuts import render
import json

from qiskit import IBMQ
from qiskit.utils import QuantumInstance
from qiskit.algorithms import Shor
from qiskit.tools.monitor import job_monitor

IBMQ.enable_account('7645d95e54de3e21d9c435991554bd25bfbd98910be5abc5ef19ef724b115be8f06044c0cda02c8e50c73a0b2d53d092155b9ff51fcc147a067f094dbf6a0aa0')
provider = IBMQ.get_provider(hub='ibm-q')

def home(request):
    return render(request, 'index.html', {})

def factor(request):

    print(request.body)

    body_unicode = request.body.decode('utf-8')
    body = json.loads(body_unicode);

    device = body['device']
    number = int(body['number'])

    backend = provider.get_backend(device)

    factors = Shor(QuantumInstance(backend, shots=1, skip_qobj_validation=False)) #Function to run Shor's algorithm where 21 is the integer to be factored

    result_dict = factors.factor(N=number, a=2)
    result = result_dict.factors

    response = JsonResponse({'result': str(result)})
    return response