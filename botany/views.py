from django.shortcuts import render, get_object_or_404, render_to_response, redirect
from botany.models import Botany, Fraction, FractionComposition, FractionMaterialsPresent


# Create your views here.
def allbotany(request):
    botany = Botany.objects.all()
    fraction = Fraction.objects.all()
    fractioncomposition = FractionComposition.objects.all()
    fractionmaterialspresent = FractionMaterialsPresent.objects.all()
    return render(request, 'botany/allbotany.html',
    {'botany':botany,
    'fraction':fraction,
    'fractioncomposition':fractioncomposition,
    'fractionmaterialspresent':fractionmaterialspresent
    })

# def detail(request, blog_id):
#     detailblog = get_object_or_404(Blog, pk=blog_id)
#     return render(request, 'blog/detail.html', {'blog':detailblog})


def allfraction(request):
    fraction = Fraction.objects
    return render(request, 'fraction/allfraction.html', {'fraction':fraction})
