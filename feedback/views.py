from django.contrib import messages
from django.http import HttpResponseRedirect
from django.shortcuts import render
from feedback.forms import AnonymousFeedbackForm, FeedbackForm

def leave_feedback(request):
    if request.user.is_authenticated:
        form = FeedbackForm(request.POST or None)
    else:
        form = AnonymousFeedbackForm(request.POST or None)
    if form.is_valid():
        feedback = form.save(commit=False)
        if request.user.is_anonymous:
            feedback.user = None
        else:
            feedback.user = request.user
        feedback.save()
        messages.add_message(request, messages.SUCCESS,
                             'Your feedback was submitted.')
        return HttpResponseRedirect(request.POST.get('next',
                                    request.META.get('HTTP_REFERER', '/')))
    return render(request, 'feedback/feedback_form.html', {'feedback_form': form})
