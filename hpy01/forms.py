# coding:utf-8
# @author huangpingyi
from django import forms


class ArticleForm(forms.Form):
    title = forms.CharField(max_length=255, min_length=5)
    summary = forms.CharField(max_length=255, min_length=5)
    category_id = forms.IntegerField()
    head_img = forms.ImageField()
    content = forms.CharField(min_length=10)