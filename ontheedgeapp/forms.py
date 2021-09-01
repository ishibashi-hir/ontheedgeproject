from django import forms
from .models import ResultCategory, TaskCategory, \
    Item, Grade, Task, Inspection, PicRecord

class ResultCategoryForm(forms.ModelForm):
    class Meta:
        model = ResultCategory
        fields = ['resultcategory']

class TaskCategoryForm(forms.ModelForm):
    class Meta:
        model = TaskCategory
        fields = ['taskcategory']

class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ['itemname']

class GradeForm(forms.ModelForm):
    class Meta:
        model = Grade
        fields = ['gradename']

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['taskcategory',
                'tasknum',
                'lot',
                'impdate',
                'item',
                'itemsize',
                'grade',
                'taskdate',
                'memo']

class InspectionForm(forms.ModelForm):
    class Meta:
        model = Inspection
        fields = ['task', 
                'resultcategory',
                'picpath', 
                'author']

class PicRecordForm(forms.ModelForm):
    class Meta:
        model = PicRecord
        fields = ['inspection',
                'x1', 
                'y1', 
                'x2', 
                'y2', 
                'gaus',
                'thrh']

class ImageForm(forms.Form):
    #default='C:\\Users\\AWadmin\\Desktop\\rd\\ontheedge03project\\static\\img\\original.png' 
    file = forms.ImageField(label='画像ファイルを選択')