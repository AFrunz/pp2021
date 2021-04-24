# from django import forms
#
# class Feedback(forms.Form):
#     class Meta:
#

#
# class IndexForm(forms.Form):
#     Choise_country = (("Russia", 1,), ("Germany", 2,))
#     country = forms.CharField(max_length=20, )
#     city = forms.CharField(max_length=20)
#     theme = forms.Select(choices=Choise_country)
#     keywords = forms.CharField(max_length=20)
#     money_ot = forms.FloatField()
#     money_do = forms.FloatField()
#     date_ot = forms.DateField()
#     date_do = forms.DateField()
#
#     class Meta:
#         fields = ['country', 'city', 'theme', 'keywords', 'money_ot', 'money_do', 'date_ot', 'date_do']
#         widgets = {
#             "country": forms.TextInput(attrs={
#                 "class": "search_txt"}),
#             "city": forms.TextInput(attrs={
#                 "class": "search_txt"}),
#             "theme": forms.Select(attrs={
#                 "class": "search_txt"}),
#             "keywords": forms.TextInput(attrs={
#                 "class": "search_txt",
#                 "type": "text",
#                 "placeholder": "Найти",
#                 "value": ""}),
#             "money_ot": forms.TextInput(attrs={
#                 "class": "search_txt", "type": "number",
#                 "placeholder": "От",
#                 "value": ""}),
#             "money_do": forms.TextInput(attrs={
#                 "class": "search_txt", "type": "number",
#                 "placeholder": "До",
#                 "value": ""}),
#             "date_ot": forms.DateInput(attrs={
#                 "class": "search_txt"}),
#             "date_do": forms.DateInput(attrs={
#                 "class": "search_txt"})
#         }