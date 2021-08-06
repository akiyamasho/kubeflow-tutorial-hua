import kfp.dsl as dsl
from steps.s01_add_inputs import (
    add_inputs_step_generator,
)  # we need the generator, not the function

# NOTE: You can copy-paste this pipeline as a template! :D
@dsl.pipeline(
    name="Tutorial pipeline", description="Add the inputs then multiple by 4"
)
def basic_pipeline(x: int, y: int):
    s01_add_inputs_step = add_inputs_step_generator(x=x, y=y)
