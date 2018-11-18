from . import models
from tagpuanApp.models import Category, Landmark
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm


class RegistrationForm(UserCreationForm):
    username = forms.CharField(required=True, label="Username", widget=forms.TextInput(
        attrs={'class': 'form-control form-group',
               'placeholder': 'username'})
        )

    email = forms.EmailField(required=True, label="Email", widget=forms.TextInput(
        attrs={'class': 'form-control form-group',
               'placeholder': 'email'})
        )

    password1 = forms.CharField(label="Password", widget=forms.PasswordInput(
        attrs={'class': 'form-control form-group',
               'name': 'password',
               'id': 'password',
               'placeholder': 'Enter your password'})
        )

    password2 = forms.CharField(label="Password confirmation", widget=forms.PasswordInput(
        attrs={'class': 'form-control form-group',
               'name': 'password',
               'id': 'password',
               'placeholder': 'Confirm password'})
        )

    first_name = forms.CharField(required=True, label="First name", widget=forms.TextInput(
        attrs={'class': 'form-control form-group',
               'placeholder': 'first name'})
        )

    last_name = forms.CharField(required=True, label="Last name", widget=forms.TextInput(
        attrs={'class': 'form-control form-group',
               'placeholder': 'last name'})
        )

    class Meta:
        model = User
        fields = (
            'username',
            'first_name',
            'last_name',
            'email',
            'password1',
            'password2'
        )

    def save(self, commit=True):
        user = super(RegistrationForm, self).save(commit=False)
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.email = self.cleaned_data['email']

        if (commit):
            user.save()

        return user




# After registering, satisfying default fields in built-in User model
# Create User Profile consisting of contact no. and date of birth
class CreateUserProfile(forms.ModelForm):
    date_of_birth = forms.CharField(label="Date of birth", widget=forms.TextInput(
        attrs={'class': 'form-control form-group',
               'placeholder': 'YYYY-MM-DD',
               'type': 'date',
               'required pattern': '[0-9]{4}-[0-9]{2}-[0-9]{2}'})
        )

    phone_number = forms.CharField(required=True, label="Contact no", widget=forms.TextInput(
        attrs={'class': 'form-control form-group',
               'placeholder': '+639999999999 format'})
        )


    class Meta:
        model = models.UserProfile
        fields = ('date_of_birth', 'phone_number')
        exclude = ('user',)




class LoginForm(AuthenticationForm):
    username = forms.CharField(required=True, label="Username", widget=forms.TextInput(
        attrs={'class': 'form-control form-group',
               'placeholder': 'username'})
        )

    password = forms.CharField(label="Password", widget=forms.PasswordInput(
        attrs={'class': 'form-control form-group',
               'name': 'password',
               'id': 'password',
               'placeholder': 'Enter your password'})
        )

    class Meta:
        fields = ('username', 'password')





class AddPostForm(forms.ModelForm):
    title = forms.CharField(required=True, label="Title", widget=forms.TextInput(
        attrs={'class': 'form-control form-group',})
        )

    post = forms.CharField(label="Post", widget=forms.Textarea(
        attrs={'class': 'form-control form-group', })
        )

    image = forms.ImageField(label="Upload image")

    category = forms.ModelChoiceField(queryset=Category.objects.order_by('category'), required=True)
    landmark = forms.ModelChoiceField(queryset=Landmark.objects.order_by('landmark'), required=True)

    POST_TYPE_CHOICES = (('Lost', 'Lost'), ('Found', 'Found'))
    post_type = forms.ChoiceField(required=True, widget=forms.RadioSelect(), choices=POST_TYPE_CHOICES)

    tags = forms.CharField(max_length=200, required=True, label="Tags", widget=forms.TextInput(
        attrs={'class': 'form-control form-group',
               'placeholder': 'Tags are comma separated, no spaces'})
                            )

    class Meta:
        model = models.Post
        fields = ('title', 'post', 'image', 'category', 'landmark', 'post_type', 'tags')
        exclude = ('post_id', 'post_timestamp',)