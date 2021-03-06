# AUTO-GENERATED by tools/checkspecs.py - DO NOT EDIT
from __future__ import unicode_literals
from ..preprocess import AutoTLRC


def test_AutoTLRC_inputs():
    input_map = dict(args=dict(argstr='%s',
    ),
    base=dict(argstr='-base %s',
    mandatory=True,
    ),
    environ=dict(nohash=True,
    usedefault=True,
    ),
    ignore_exception=dict(deprecated='1.0.0',
    nohash=True,
    usedefault=True,
    ),
    in_file=dict(argstr='-input %s',
    copyfile=False,
    mandatory=True,
    ),
    no_ss=dict(argstr='-no_ss',
    ),
    outputtype=dict(),
    terminal_output=dict(deprecated='1.0.0',
    nohash=True,
    ),
    )
    inputs = AutoTLRC.input_spec()

    for key, metadata in list(input_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(inputs.traits()[key], metakey) == value


def test_AutoTLRC_outputs():
    output_map = dict(out_file=dict(),
    )
    outputs = AutoTLRC.output_spec()

    for key, metadata in list(output_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(outputs.traits()[key], metakey) == value
