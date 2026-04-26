from django import forms

class FeedbackForm(forms.Form):
    subject = forms.CharField(
        label='Тема',
        max_length=100,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Тема сообщения'})
    )
    email = forms.EmailField(
        label='Ваш Email',
        widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'name@example.com'})
    )
    text = forms.CharField(
        label='Сообщение',
        widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 5, 'placeholder': 'Ваш вопрос или предложение...'})
    )