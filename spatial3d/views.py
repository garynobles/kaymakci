from django.shortcuts import render, get_object_or_404, render_to_response, redirect
from django import forms
from django.utils.translation import ugettext
import django_filters
from django_filters.filterset import ORDER_BY_FIELD
# Create your views here.

from .forms import PhotobatchForm
from spatial3d.models import Photobatch
from filters.views import FilterMixin

# Create your views here.
def createphotobatch(request):
    if request.method == "POST":
        form = PhotobatchForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            #post.user = request.user
            #post.datetime = datetime.datetime.now()

            post.save()
            return redirect('allphotobatch')
    else:
        form = PhotobatchForm()
    return render(request, 'photobatch/create_photobatch.html', {'form': form})


def editphotobatch(request, pk):
    post = get_object_or_404(Photobatch, pk=pk)
    if request.method == "POST":
        form = PhotobatchForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.created_by = request.user
            #post.modified_by = request.user
            post.datetime = datetime.datetime.now()
            post.save()
            return redirect('allphotobatch')
            #, pk=post.pk)
    else:
        form = PhotobatchForm(instance=post)
    return render(request, 'photobatch/create_photobatch.html', {'form': form})

def detailphotobatch(request, id):
    detailphotobatch = get_object_or_404(Photobatch, pk=id)
    return render(request, 'photobatch/detailphotobatch.html', {'detailphotobatch':detailphotobatch})

class PhotobatchFilterForm(forms.ModelForm):
    class Meta:
        model = Photobatch
        fields = (
        'photobatch_id',
        'prefix',
        'area_easting',
        'area_northing',
        'context_number',
        'number_of_photos',
        'number_targets',
        'processed_on',
        'processed_by',
        'camera_model',
        'imported_photoscan',

        'aligned',
        'align_accuracy',
        'align_pair_selection',
        'align_keypoint_limit',
        'align_tiepoint_limit',
        'detected_targets',
        'target_type',
        'target_tolerance',
        'target_origional_error',
        'target_optimised_error',
        'dense_pointcloud',
        'mesh',
        'mesh_type',
        'mesh_face_count',
        'mesh_interpolation',

		'texture',
        'texture_defaults',
        'dem',
        'dem_coordinate_system',
        'dem_source_data',
        'dem_interpolation',
        'orthomosaic',
        'orthomosaic_type',
        'orthomosaic_pixel_size',
        'export_points',
        'export_points_filename',
        'export_points_offsets',

		'export_report_pdf',
        'export_orthophoto',
        'export_dem',
        'export_dem_pixel_size',
        'export_dem_geodatabase',
        'folder_processed',
        'processing_notes',
        #'image',
        #'created_timestamp',
        'created_by'
        )

class PhotobatchFilter(django_filters.FilterSet):

    class Meta:  # pylint: disable=C1001
        form = PhotobatchFilterForm
        model = Photobatch
        fields = [
        'photobatch_id',
        'prefix',
        'area_easting',
        'area_northing',
        'context_number',
        'number_of_photos',
        'number_targets',
        'processed_on',
        'processed_by',
        'camera_model',
        'imported_photoscan',

        'aligned',
        'align_accuracy',
        'align_pair_selection',
        'align_keypoint_limit',
        'align_tiepoint_limit',
        'detected_targets',
        'target_type',
        'target_tolerance',
        'target_origional_error',
        'target_optimised_error',
        'dense_pointcloud',
        'mesh',
        'mesh_type',
        'mesh_face_count',
        'mesh_interpolation',

		'texture',
        'texture_defaults',
        'dem',
        'dem_coordinate_system',
        'dem_source_data',
        'dem_interpolation',
        'orthomosaic',
        'orthomosaic_type',
        'orthomosaic_pixel_size',
        'export_points',
        'export_points_filename',
        'export_points_offsets',

		'export_report_pdf',
        'export_orthophoto',
        'export_dem',
        'export_dem_pixel_size',
        'export_dem_geodatabase',
        'folder_processed',
        'processing_notes',
        #'image',
        #'created_timestamp',
        'created_by'


        ]
        order_by = (
            ('sample_number', ugettext("A-Z")),
            ('-sample_number', ugettext("Z-A")),
        )

class PhotobatchListView(FilterMixin, django_filters.views.FilterView):
    def get_queryset(self, *atgs, **kwargs):
        object_list=Photobatch.objects.filter(material='Ceramic')
        return object_list
    model = Photobatch
    paginate_by = 16
    filterset_class = PhotobatchFilter
