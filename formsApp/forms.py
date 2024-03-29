from django import forms
from django.core import validators

class UserRegistrationForm(forms.Form):
    GENDER = [
        ('male', 'MALE'),
        ('female', 'FEMALE')

    ] #list of tuples
    # django validators refrence https://docs.djangoproject.com/en/2.2/ref/validators/
    firstName = forms.CharField(widget=forms.TextInput, required=True, validators=[validators.MinLengthValidator(5), validators.MaxLengthValidator(20)])
    lastName = forms.CharField(widget=forms.TextInput, required=True, validators=[validators.MinLengthValidator(5), validators.MaxLengthValidator(20)])
    email = forms.CharField(widget=forms.TextInput, required=False, validators=[validators.EmailValidator])
    gender = forms.CharField(widget=forms.Select(choices=GENDER))
    password = forms.CharField(widget=forms.PasswordInput, validators=[validators.MinLengthValidator(5), validators.MaxLengthValidator(20)])

    ''' 
    # custom error message for each field individually
    def clean_firstName(self):
        inputFirstName = self.cleaned_data['firstName']
        if len(inputFirstName) > 20:
            raise forms.ValidationError('the max length of firstname must be <= 20 chars')
        return inputFirstName

    # custom error message for each field individually
    def clean_email(self):
        inputEmail = self.cleaned_data['email']
        if inputEmail.find('@') == -1:
            raise forms.ValidationError('invalid email address')
        return inputEmail

    #single error message for all fields
    def clean(self):  # overrifr the clean meathion in the clean calls
        user_cleaned_data = super().clean()
        inputFirstName = user_cleaned_data['firstName']
        inputLastName = user_cleaned_data['lastName']
        inputEmail = user_cleaned_data['email']
        if len(inputFirstName) > 20 or len(inputLastName) > 20:
            raise forms.ValidationError('the max length of firstname or lastname must be <= 20 chars')
        if inputEmail.find('@') == -1:
            raise forms.ValidationError('invalid email address')
        return user_cleaned_data
    '''


