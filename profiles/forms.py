from django import forms
from .models import Profile


class ProfileForm(forms.ModelForm):
    # Handle documents as a textarea of URLs, one per line, in the form
    documents_text = forms.CharField(
        required=False,
        widget=forms.Textarea(attrs={"rows": 4}),
        help_text="One URL per line",
        label="Documents",
    )

    class Meta:
        model = Profile
        fields = [
            "name",
            "second_name",
            "last_name",
            "pfadi_name",
            "email",
            "phone_number",
            "level",
            "user",
            "img",
            "visible",
        ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self.instance and isinstance(self.instance.documents, list):
            self.fields["documents_text"].initial = "\n".join(self.instance.documents)

    def clean_documents_text(self):
        text = self.cleaned_data.get("documents_text", "")
        urls = []
        for line in text.splitlines():
            line = line.strip()
            if line:
                urls.append(line)
        return urls

    def save(self, commit=True):
        instance = super().save(commit=False)
        instance.documents = self.cleaned_data.get("documents_text", [])
        if commit:
            instance.save()
            self.save_m2m()
        return instance
