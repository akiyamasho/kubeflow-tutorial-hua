import kfp.components as comp
from typing import NamedTuple


def plus_inputs(x: int, y: int) -> NamedTuple(
    'ExampleOutputs', [('sum', int)]):
    sum_ = x + y

    from collections import namedtuple
    divmod_output = namedtuple('MyDivmodOutput',
                               ['sum'])
    return divmod_output(sum_)


def minus_inputs(z: int) -> int:
    return z - 6


plus_inputs_step_generator = comp.func_to_container_op(
    func=plus_inputs
    #     output_component_file='component.yaml', # This is optional. It saves the component spec for future use.
    #     base_image='python:3.7',
    #     packages_to_install=['numpy==1.1.4']
)

minus_inputs_step_generator = comp.func_to_container_op(
    func=minus_inputs
)
