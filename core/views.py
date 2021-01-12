from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from .models import Transaction
from django.contrib.auth.decorators import login_required

# Create your views here.


@login_required(login_url='login_view')
def home(request):
    # user = User.objects.get(username='admin')
    user = request.user
    # print(user.transactions.all())
    transactions = user.transactions.all()
    balance = 0
    prev_balances = []
    for transaction in transactions:
        if transaction.transaction_type == 'credit':
            balance += transaction.amount
            prev_balances.append(balance)
        else:
            balance -= transaction.amount
            prev_balances.append(balance)
    print(balance)
    print(prev_balances)
    transactions = zip(transactions, prev_balances)
    return render(request, 'core/home.html', {'balance': balance, 'transactions': transactions})


@login_required(login_url='login_view')
def credit(request):
    # user = User.objects.get(username='admin')
    user = request.user
    if request.POST:
        amount = request.POST['amount']
        description = request.POST['description']
        transac_date = request.POST['date']
        new_transactions = Transaction(user=user, amount=amount, transaction_type='credit', description=description, date=transac_date)
        new_transactions.save()
        return redirect('home')
    return redirect('home')


@login_required(login_url='login_view')
def debit(request):
    # user = User.objects.get(username='admin')
    user = request.user
    if request.POST:
        amount = request.POST['amount']
        description = request.POST['description']
        transac_date = request.POST['date']
        new_transactions = Transaction(user=user, amount=amount, transaction_type='debit', description=description, date=transac_date)
        new_transactions.save()
        return redirect('home')
    return redirect('home')


@login_required(login_url='login_view')
def delete(request, id):
    transaction = get_object_or_404(Transaction, id=id)
    transaction.delete()
    return redirect('home')
