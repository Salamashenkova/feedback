from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from .forms import FeedbackForm
from django.contrib import messages

def feedback_view(request):
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            # Здесь вы можете обработать данные формы,
            # например, сохранить их в базе данных или отправить по email
            form.save()
            return render(request, 'feedback/thanks.html')  # Страница благодарности
    else:
        form = FeedbackForm()

    return render(request, 'feedback/feedback_form.html', {'form': form})