from django import forms

"""
class CreateBookForm(forms.Form):

    your_name = forms.CharField(label='Your name', max_length=100)
    
    name = forms.CharField()
    age = forms.IntegerField()
    address = forms.CharField(required=False)
    gender = forms.ChoiceField(choices=(('M', 'Male'), ('F', 'Female')))

    class Meta:
        model = CreateBook
        fields = ('customer', 'car_id', 'book_start_date', 'book_end_date')

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('url', 'location', 'company')
"""