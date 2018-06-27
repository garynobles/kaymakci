from django.shortcuts import render

# Create your views here.
def allqnisp(request):
    # qnisp_list = Qnisp.objects.all()
    # filtered_qs = filters.QnispFilter(request.GET, queryset=qnisp_list).qs
    # paginator = Paginator(filtered_qs, 10)
    #
    # page = request.GET.get('page')
    # try:
    #     response = paginator.page(page)
    # except PageNotAnInteger:
    #     response = paginator.page(1)
    # except EmptyPage:
    #     response = paginator.page(paginator.num_pages)
    return render(request,'qnisp/allqnisp.html')
    #,{'response': response})
