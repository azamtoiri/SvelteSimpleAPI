from django.http import FileResponse, Http404
from django.shortcuts import get_object_or_404

from .models import SveltePage


def get_svelte_page(request, name):
    try:
        page = get_object_or_404(SveltePage, name=name)
        return FileResponse(page.template.open(), content_type='application/octet-stream')
    except Exception as e:
        raise Http404("Template not found")
