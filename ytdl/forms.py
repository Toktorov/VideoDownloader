from django import forms


class DownloadForm(forms.Form):
    url = forms.CharField(widget=forms.TextInput(attrs={ 'placeholder': 'Вставьте сюда ссылку на видео' }), label=False)