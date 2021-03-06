from django.shortcuts import render, get_object_or_404, render_to_response, redirect
from django import forms
from django.utils.translation import ugettext
import django_filters
from django_filters.filterset import ORDER_BY_FIELD
# Create your views here.

from .forms import ZooarchForm, QnispForm
from zooarch.models import Zooarch, Qnisp #, Zooarchsamples
from filters.views import FilterMixin


# Create your views here.
def createzooarch(request):
    if request.method == "POST":
        form = ZooarchForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            #post.user = request.user
            #post.datetime = datetime.datetime.now()

            post.save()
            return redirect('allzooarch')
    else:
        form = ZooarchForm()
    return render(request, 'zooarch/create_zooarch.html', {'form': form})


def editzooarch(request, pk):
    post = get_object_or_404(Zooarch, pk=pk)
    if request.method == "POST":
        form = ZooarchForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            #post.user = request.user
            #post.datetime = datetime.datetime.now()
            post.save()
            return redirect('allzooarch')
            #, pk=post.pk)
    else:
        form = ZooarchForm(instance=post)
    return render(request, 'zooarch/create_zooarch.html', {'form': form})


# def detailzooarch(request):
#     pass




def removeqnisp(request, pk):
    Qnisp.objects.get(pk=pk).delete()
    return redirect('/zooarch/qnisp')

class ZooarchFilterForm(forms.ModelForm):
    class Meta:
        model = Zooarch
        fields = (
        'sample_id',
        'area_easting',
        'area_northing',
        'context_number',
        'sample_number',
        'material',
        'specific_material',
        'exterior_color_hue',
        'exterior_color_lightness_value',
        'exterior_color_chroma',
        'interior_color_hue',
        'interior_color_lightness_value',
        'interior_color_chroma',
        'weight_kilograms',
        'sample_description',
        'category',
        'subcategory',
        'count',
        'current_location',
        'recovery_type',
        'problems',
        'image_files',
        'number_3d_files',
        'chronology',
        'analysis_request',
        'detailed_sample_description',
        'bureaucratic_status',
        'subjective_significance',
        'museum_inventory_number',
        'bureaucratic_status_identifier',

        )



class ZooarchFilter(django_filters.FilterSet):

    # def __init__(self, data={}, *args, **kwargs):
    #     super(ZooarchFilterForm, self).__init__(data, *args, **kwargs)  # NOQA
    #     try:
    #         self.fields[ORDER_BY_FIELD].widget.attrs = {
    #             'onchange': "this.form.submit();",
    #         }
    #     except KeyError:
    #         pass

    class Meta:
        form = ZooarchFilterForm
        model = Zooarch
        fields = [
        'sample_id',
        'area_easting',
        'area_northing',
        'context_number',
        'sample_number',
        'material',
        'specific_material',
        'exterior_color_hue',
        'exterior_color_lightness_value',
        'exterior_color_chroma',
        'interior_color_hue',
        'interior_color_lightness_value',
        'interior_color_chroma',
        'weight_kilograms',
        'sample_description',
        'category',
        'subcategory',
        'count',
        'current_location',
        'recovery_type',
        'problems',
        'image_files',
        'number_3d_files',
        'chronology',
        'analysis_request',
        'detailed_sample_description',
        'bureaucratic_status',
        'subjective_significance',
        'museum_inventory_number',
        'bureaucratic_status_identifier',

        ]
        order_by = (
            ('sample_id', ugettext("A-Z")),
            ('-sample_id', ugettext("Z-A")),
        )

class ZooarchListView(FilterMixin, django_filters.views.FilterView):
    model = Zooarch
    paginate_by = 16
    filterset_class = ZooarchFilter
    def get_queryset(self, *atgs, **kwargs):
        object_list=Zooarch.objects.filter(material='Organic', specific_material='Bone')
        return object_list






# Create your views here.
def createqnisp(request):
    if request.method == "POST":
        form = QnispForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.created_by= request.user
            #post.datetime = datetime.datetime.now()

            post.save()
            return redirect('allqnisp')
    else:
        form = QnispForm()
    return render(request, 'qnisp/create_qnisp.html', {'form': form})


def editqnisp(request, pk):
    post = get_object_or_404(Qnisp, pk=pk)
    if request.method == "POST":
        form = QnispForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            #post.user = request.user
            #post.datetime = datetime.datetime.now()
            post.save()
            return redirect('allqnisp')
            #, pk=post.pk)
    else:
        form = QnispForm(instance=post)
    return render(request, 'qnisp/create_qnisp.html', {'form': form})


def detailqnisp(request, qnisp_id):
    detailqnisp = get_object_or_404(Qnisp, pk=qnisp_id)
    return render(request, 'qnisp/detailqnisp.html', {'qnisp':detailqnisp})

class QnispFilterForm(forms.ModelForm):
    class Meta:
        model = Qnisp
        fields = (
        'qnisp_id',
        'area_easting',
        'area_northing',
        'context_number',
        'sample_number',
        'collection_method',
        'mandible_with_teeth',
        'bt',
        'ss',
        'oc_tje',
        'ch',
        'oa',
        'equid',
        'cer',
        'lp',
        'meles',
        'pesc',
        'brd',
        'canis',
        'unio',
        'cerastoderma',
        'landsnail',
        'shell_other',
        'rodent',
        'comments',
        'ursus',
        'big_feline_lynx_size',
        )
        order_by = (
            ('collection_method', ugettext("A-Z")),
            ('-collection_method', ugettext("Z-A")),
        )

class QnispFilter(django_filters.FilterSet):

    class Meta:  # pylint: disable=C1001
        form = QnispFilterForm
        model = Qnisp
        fields = [
        'qnisp_id',
        'area_easting',
        'area_northing',
        'context_number',
        'sample_number',
        'collection_method',
        'mandible_with_teeth',
        'bt',
        'ss',
        'oc_tje',
        'ch',
        'oa',
        'equid',
        'cer',
        'lp',
        'meles',
        'pesc',
        'brd',
        'canis',
        'unio',
        'cerastoderma',
        'landsnail',
        'shell_other',
        'rodent',
        'comments',
        'ursus',
        'big_feline_lynx_size',
        ]




class QnispListView(FilterMixin, django_filters.views.FilterView):
    model = Qnisp
    paginate_by = 16
    filterset_class = QnispFilter


# class ZooarchsamplesFilterForm(forms.ModelForm):
#     class Meta:
#         model = Zooarchsamples
#         fields = (
#             'area_easting',
#             'area_northing',
#             'context_number',
#             'sample_number',
#             'element',
#             'portion',
#             'side',
#             'sex',
#             'fusion',
#             'taxonomic_description',
#             'age_estimation',
#             'tooth_wear',
#             'sample_id',
#             'status',
#         )


# class ZooarchsamplesListView(FilterMixin, django_filters.views.FilterView):
#     def get_queryset(self, *atgs, **kwargs):
#         object_list2=Zooarchsamples.objects.filter(material='Organic', specific_material='Bone')
#         return object_list2
#     model = Zooarchsamples

def detailzooarch(request, sample_id):
    detailzooarch = get_object_or_404(Zooarch, pk=sample_id)
    return render(request, 'zooarch/detailzooarch.html', {'zooarch':detailzooarch})



# def detailzooarch(request, sample_id):
#     detailzooarch = get_object_or_404(Zooarch, pk=sample_id)
#     return render(request, 'zooarch/detailzooarch.html', {'zooarch':detailzooarch})
#
# def detailqnisp(request, qnisp_id):
#     detailqnisp = get_object_or_404(Qnisp, pk=qnisp_id)
#     return render(request, 'qnisp/detailqnisp.html', {'qnisp':detailqnisp})
