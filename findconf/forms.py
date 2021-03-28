from django.forms import ModelForm

class IndexForm(ModelForm):
    class Meta:
        fields = ['country']