from django.shortcuts import render, redirect
from random import randint
from datetime import datetime

# Create your views here.
def index(request):
  if not 'logs' in request.session:
    request.session['logs'] = []
  if not 'gold' in request.session:
    request.session['gold'] = 0
  return render(request, 'index.html')

def process_gold(request, location):
  goldMap = {'farm': [10,20], 'cave': [5,10], 'house': [2,5], 'casino': [-50,50]}
  bounds = goldMap[location]
  result = randint(bounds[0], bounds[1])
  request.session['gold'] += result
  log = {
    'amount': abs(result),
    'isGain': result >= 0,
    'location': location,
    'time': datetime.now().strftime('%H:%M %p %d/%m/%y')
  }
  request.session['logs'].insert(0, log)
  return redirect(index)

def reset(request):
  request.session.clear()
  return redirect('/')
