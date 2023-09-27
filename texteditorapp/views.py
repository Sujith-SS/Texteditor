from django.shortcuts import render
from .forms import TextEditorForm
from .models import SavedText

def text_editor(request):
    if request.method == 'POST':
        form = TextEditorForm(request.POST)
        if form.is_valid():
            font_family = form.cleaned_data['font_family']
            font_size = form.cleaned_data['font_size']
            editor_content = form.cleaned_data['editor']

            # Save data to the database
            saved_text = SavedText(font_family=font_family, font_size=font_size, content=editor_content)
            saved_text.save()

            return render(request, 'index.html', {'form': form, 'success_message': 'Text saved successfully.'})

    else:
        form = TextEditorForm()

    return render(request, 'index.html', {'form': form})
