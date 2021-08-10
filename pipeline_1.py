import kfp.compiler as com
from steps_hua.s01_components import plus_inputs_step_generator,minus_inputs_step_generator


# Define a pipeline and create a task from a component:
def my_pipeline(x: int, y: int):
    valuse_ = plus_inputs_step_generator(x, y)
    result_ = minus_inputs_step_generator(valuse_.outputs['sum'])


com.Compiler().compile(
    pipeline_func=my_pipeline,
    package_path='pipeline.yaml')