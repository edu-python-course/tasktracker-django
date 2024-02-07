"""
Tasks application forms

"""

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from django import forms
from django.contrib.auth import get_user_model

from tasks.models import TaskModel


class TaskModelForm(forms.ModelForm):
    assignee = forms.ModelChoiceField(
        required=False,
        queryset=get_user_model().objects
        .exclude(is_superuser=True)
        .exclude(is_active=False)
    )

    class Meta:
        model = TaskModel
        fields = ("summary", "completed", "description", "assignee")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = "post"
        self.helper.form_class = "w-75 m-auto form-task"
        self.helper.attrs["aria-label"] = "TaskForm"
        self.helper.add_input(
            Submit("cancel", "Submit", css_class="w-100 mt-3")
        )
