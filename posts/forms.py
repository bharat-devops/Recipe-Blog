from django import forms
from django.contrib.flatpages.models import FlatPage
from tinymce.widgets import TinyMCE



# class TinyMCEWidget(TinyMCE):
# 	def use_required_attribute(self, *args):
# 		return False


class FlatPageForm(forms.ModelForm):

    content = forms.CharField(widget=TinyMCE(attrs={'cols': 80, 'rows': 30}))

    class Meta:
        model = FlatPage
