#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django import forms
from .models import Post, Comment


class PostForm(forms.ModelForm):
    class Meta:
        # 告诉django哪个模型会被用来创建此表单
        model = Post
        # 表单中出现的字段
        fields = ('title', 'text')


class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ('author', 'text',)
