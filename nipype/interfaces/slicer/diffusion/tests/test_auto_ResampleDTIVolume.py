# AUTO-GENERATED by tools/checkspecs.py - DO NOT EDIT
from nipype.testing import assert_equal
from nipype.interfaces.slicer.diffusion.diffusion import ResampleDTIVolume
def test_ResampleDTIVolume_inputs():
    input_map = dict(origin=dict(argstr='--origin %s',
    ),
    correction=dict(argstr='--correction %s',
    ),
    defField=dict(argstr='--defField %s',
    ),
    window_function=dict(argstr='--window_function %s',
    ),
    image_center=dict(argstr='--image_center %s',
    ),
    transform_tensor_method=dict(argstr='--transform_tensor_method %s',
    ),
    size=dict(argstr='--size %s',
    sep=',',
    ),
    spline_order=dict(argstr='--spline_order %d',
    ),
    transform=dict(argstr='--transform %s',
    ),
    centered_transform=dict(argstr='--centered_transform ',
    ),
    transform_order=dict(argstr='--transform_order %s',
    ),
    Inverse_ITK_Transformation=dict(argstr='--Inverse_ITK_Transformation ',
    ),
    direction_matrix=dict(argstr='--direction_matrix %s',
    sep=',',
    ),
    interpolation=dict(argstr='--interpolation %s',
    ),
    ignore_exception=dict(nohash=True,
    usedefault=True,
    ),
    outputVolume=dict(position=-1,
    hash_files=False,
    argstr='%s',
    ),
    number_of_thread=dict(argstr='--number_of_thread %d',
    ),
    args=dict(argstr='%s',
    ),
    spacing=dict(argstr='--spacing %s',
    sep=',',
    ),
    hfieldtype=dict(argstr='--hfieldtype %s',
    ),
    rotation_point=dict(argstr='--rotation_point %s',
    ),
    terminal_output=dict(mandatory=True,
    nohash=True,
    ),
    notbulk=dict(argstr='--notbulk ',
    ),
    default_pixel_value=dict(argstr='--default_pixel_value %f',
    ),
    transform_matrix=dict(argstr='--transform_matrix %s',
    sep=',',
    ),
    Reference=dict(argstr='--Reference %s',
    ),
    transformationFile=dict(argstr='--transformationFile %s',
    ),
    environ=dict(nohash=True,
    usedefault=True,
    ),
    inputVolume=dict(position=-2,
    argstr='%s',
    ),
    spaceChange=dict(argstr='--spaceChange ',
    ),
    )
    inputs = ResampleDTIVolume.input_spec()

    for key, metadata in input_map.items():
        for metakey, value in metadata.items():
            yield assert_equal, getattr(inputs.traits()[key], metakey), value
def test_ResampleDTIVolume_outputs():
    output_map = dict(outputVolume=dict(position=-1,
    ),
    )
    outputs = ResampleDTIVolume.output_spec()

    for key, metadata in output_map.items():
        for metakey, value in metadata.items():
            yield assert_equal, getattr(outputs.traits()[key], metakey), value