from django import forms
from post.models import Post


class NewPostForm(forms.ModelForm):
    caption = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "w-full !text-black placeholder:!text-black !bg-white !border-transparent focus:!border-transparent focus:!ring-transparent !font-normal !text-xl   dark:!text-white dark:placeholder:!text-white dark:!bg-slate-800",
                "placeholder": "What do you have in mind?",
                "rows": "6",
            }
        ),
        required=True,
    )
    tag = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "w-full !text-black placeholder:!text-black !bg-white !border-transparent focus:!border-transparent focus:!ring-transparent !font-normal !text-s   dark:!text-white dark:placeholder:!text-white dark:!bg-slate-800",
                "placeholder": "Tags - Separated by spaces",
                "rows": "6",
            }
        ),
        required=True,
    )
    picture = forms.ImageField(
        # widget=forms.TextInput(
        #     attrs={
        #         "type": "file",
        #         "name": "picture",
        #         "class": "hidden",
        #         "accept": "image/png, image/gif, image/jpeg",
        #         "id": "file",
        #     }
        # ),
        required=True,
    )

    class Meta:
        model = Post
        fields = ["caption", "tag", "picture"]
        # fields = fields = '__all__'
