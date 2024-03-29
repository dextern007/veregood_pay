from django.contrib import admin
from website.models import  *
# Register your models here.
from website.widgets import editor
from django import forms

class CascadeStyleInline(admin.StackedInline):
    model = CascadeStyle
    extra = 1

class JavaScriptInline(admin.StackedInline):
    model = JavaScript
    extra = 1

class MetaInline(admin.TabularInline):
    model = Meta
    extra = 1

class PageAdmin(admin.ModelAdmin):
    inlines = [CascadeStyleInline,JavaScriptInline,MetaInline]
    class Meta:
        model = Page



class SerializerInline(admin.TabularInline):
    model = JsonSerializer.api.through
    extra = 1

class FunctionInline(admin.TabularInline):
    model = CustomFuction.api.through
    extra = 1

class APIEditorForm(forms.ModelForm):
    model = Widget

    class Meta:
        fields = '__all__'
        widgets = {
            'content': editor.HtmlEditor(attrs={'style': 'width: 90%; height: 100%;'}),
        }

class ApiAdmin(admin.ModelAdmin):
    inlines = [SerializerInline,FunctionInline]
    form    = APIEditorForm
    class Meta:
        model = Api

class EditorForm(forms.ModelForm):
    model = Widget

    class Meta:
        fields = '__all__'
        widgets = {
            'content': editor.HtmlEditor(attrs={'style': 'width: 90%; height: 100%;'}),
        }



class WidgetAdmin(admin.ModelAdmin):
    form = EditorForm

class SerializerAdmin(admin.ModelAdmin):

    form    = EditorForm
    class Meta:
        model = JsonSerializer

class FunctionAdmin(admin.ModelAdmin):

    form    = EditorForm
    class Meta:
        model = CustomFuction

admin.site.register(Page,PageAdmin)
admin.site.register(Widget,WidgetAdmin)
admin.site.register(Api,ApiAdmin)
admin.site.register(JsonSerializer,SerializerAdmin)
admin.site.register(CustomFuction,FunctionAdmin)
admin.site.register(View)
