from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView

class RegisterView(CreateView):
    form_class = UserCreationForm
    template_name = 'auth/register.html'
    success_url = reverse_lazy('app1:list_records')

    def form_valid(self, form):
        response = super().form_valid(form)
        login(self.request, self.object)
        return response

class PasswordResetView(CreateView):
    template_name = 'auth/password_reset.html'
    success_url = reverse_lazy('auth:login')

    # password reset function
    def form_valid(self, form):
        form.save()
        return super().form_valid(form)
