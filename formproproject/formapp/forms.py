from django import forms


class StudentForm(forms.Form):
          sname=forms.CharField(label='Enter Studnt Name',max_length=30)
          sage=forms.IntegerField(label='Enter Student Age')
          smobile=forms.IntegerField(label='Enter Student Mobile')
