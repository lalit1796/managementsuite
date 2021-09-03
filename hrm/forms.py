from django import forms
from hrm.models import Job, Candidate


class jobForm(forms.ModelForm):
    class Meta:
        model = Job
        fields = '__all__'
        
            
            
class newCandidateForm(forms.ModelForm):
    class Meta:
        model = Candidate
        fields = '__all__'
        