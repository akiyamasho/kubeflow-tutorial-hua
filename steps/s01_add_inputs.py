import kfp.components as comp

# You can also use this step as a template!


def add_inputs(x: int, y: int) -> int:
    return x + y
    
add_inputs_step_generator = comp.func_to_container_op(
    func=add_inputs
)
