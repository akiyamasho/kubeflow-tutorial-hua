from kfp.components import func_to_container_op
import kfp.dsl as dsl
import kfp.compiler as com

from typing import NamedTuple


@func_to_container_op
def plus_inputs(x: int, y: int) -> NamedTuple(
    'ExampleOutputs', [('sum', int)]):
    sum_ = x + y

    from collections import namedtuple
    divmod_output = namedtuple('MyDivmodOutput',
                               ['sum'])
    return divmod_output(sum_)


@func_to_container_op
def minus_inputs(z: int) -> int:
    return z - 6


@func_to_container_op
def minus_inputs_2(z: int) -> int:
    return z - 1


## Conditional execution
def my_pipeline(x: int, y: int):
    valuse_ = plus_inputs(x,y)
    with dsl.Condition(valuse_.output > 5):
        result_ = minus_inputs(valuse_.outputs['sum'])
    with dsl.Condition(valuse_.output <= 5):
        result_ = minus_inputs_2(valuse_.outputs['sum'])
com.Compiler().compile(
    pipeline_func=my_pipeline,
    package_path='pipeline.tar.gz')