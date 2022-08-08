from django.forms import ModelForm, ChoiceField, ModelChoiceField

from .models import Group, Teacher


class GroupForm(ModelForm):
    class Meta:
        model = Group
        fields = '__all__'

    def __init__(self, *args, teachers_list=None, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['teacher'] = ModelChoiceField(queryset=Teacher.objects.filter(id__in=teachers_list))
