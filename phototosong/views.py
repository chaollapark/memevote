from django.shortcuts import render, redirect
from .forms import MemeUploadForm  # Use your MemeUploadForm
from django.contrib import messages

def upload_photo(request):
    if request.method == 'POST':
        form = MemeUploadForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Photo uploaded successfully!')
            return redirect('upload_photo')  # Redirect to the same page after successful upload
    else:
        form = MemeUploadForm()

    return render(request, 'phototosong/upload_photo.html', {'form': form})
