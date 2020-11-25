from django import forms
from django.shortcuts import render, redirect
from django.views.generic import FormView

from dev_test.main.models import Order


class CreateOrderForm(forms.ModelForm):
    """
    The form to create a new order
    """
    def clean(self):

        return self.cleaned_data

    class Meta:
        model = Order
        fields = {'amount_paid', 'product'}


class CreateOrder(FormView):
    """
    The view to create a new order
    """
    template_name = 'create_order.jinja'
    title = 'Create Order'
    form_class = CreateOrderForm

    def form_valid(self, form):
        order = form.save()
        return redirect('order-confirmation', pk=order.pk)


def order_confirmation(request, pk):
    """
    The confirmation page after making a successful order
    """
    order = Order.objects.get(id=pk)
    # Get change here and display on the view
    print(order.amount_paid)
    total = change(order.amount_paid)

    return render(request, 'order_confirmation.jinja', context={'title': 'Order Confirmation', 'order': order, 'change': total})

def change(amount):

    denominations = [50, 20, 10, 5, 2, 1, .5, .2, .1, .05, .02, .01]
    changeReturned = {}
    changeDue = amount
    
    for i in denominations:
        if changeDue >= i:
            changeReturned[i] = changeDue // i
            changeDue = changeDue - i
    
    print(changeReturned)
    
    return(changeReturned)
    
