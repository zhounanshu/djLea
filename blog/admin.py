#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.contrib import admin
from .models import Post

# 注册模型，使模型在admin上可见
admin.site.register(Post)
