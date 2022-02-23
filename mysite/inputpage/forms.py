from django import forms


class LeaveForm(forms.Form):
    from_email = forms.EmailField(required=True, widget=forms.TextInput(
        attrs={
            'style': 'width: 400px',
            'class': 'basicAutoComplete',
            'data-url': "/domain/email_autocomplete/"
        }))


# class LeaveForm(forms.Form):
#     leave_list = (
#         ('Casual Leave', 'Casual Leave'),
#         ('Sick Leave', 'Sick Leave')
#     )
#     from_email = forms.EmailField(required=True, widget=forms.TextInput(attrs={'style': 'width: 400px'}))
#     start_date = end_date = forms.CharField(widget=forms.TextInput(attrs={'type': 'date', 'style': 'width: 175px'}))
#     leave_type = forms.ChoiceField(choices=leave_list, widget=forms.Select(attrs={'style': 'width: 400px'}))
#     comments = forms.CharField(required=True, widget=forms.Textarea(attrs={'style': 'width: 400px; height: 247px'}))

#     def clean_from_email(self):
#         data = self.cleaned_data['from_email']
#         if "@testdomain.com" not in data:
#             raise forms.ValidationError("Must be @testdomain.com")
#         return data