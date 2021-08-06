import kfp.dsl as dsl

# NOTE: You can copy-paste this pipeline as a template! :D

@dsl.pipeline(
    name="Tutorial pipeline",
    description="Add the inputs then multiple by 4"    
)
def basic_pipeline(
    x: int,
    y: int
):
    pass
