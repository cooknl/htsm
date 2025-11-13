# /// script
# requires-python = ">=3.12"
# dependencies = [
#     "marimo[mcp,recommended]",
#     "mcp==1.18.0",
#     "numpy==2.2.6",
# ]
# ///

import marimo

__generated_with = "0.17.7"
app = marimo.App(auto_download=["html"])


@app.cell
def _():
    # Standard marimo cell for imports.
    import marimo as mo
    from numpy import arcsin, arctan, sqrt, sin, cos
    import math
    return arcsin, arctan, cos, math, mo, sin, sqrt


@app.cell
def _(
    get_state,
    mo,
    number_b,
    number_r,
    number_s,
    number_t,
    number_θ,
    target_selector,
):
    # Display cell - number inputs only
    _state = get_state()

    mo.vstack([
        mo.md("### Interactive Calculator"),
        target_selector,
        mo.md("---"),
        # θ row
        mo.hstack([
            number_θ if _state["output_target"] != "θ" else mo.md(f"θ: {_state['θ']['value']:.2f}"),
            mo.md(f"{_state['θ']['units']}")
        ], justify="start"),
        # b row  
        mo.hstack([
            number_b if _state["output_target"] != "b" else mo.md(f"b: {_state['b']['value']:.2f}"),
            mo.md(f"{_state['b']['units']}")
        ], justify="start"),
        # t row
        mo.hstack([
            number_t if _state["output_target"] != "t" else mo.md(f"t: {_state['t']['value']:.2f}"),
            mo.md(f"{_state['t']['units']}")
        ], justify="start"),
        # s row
        mo.hstack([
            number_s if _state["output_target"] != "s" else mo.md(f"s: {_state['s']['value']:.2f}"),
            mo.md(f"{_state['s']['units']} ground")
        ], justify="start"),
        # r row
        mo.hstack([
            number_r if _state["output_target"] != "r" else mo.md(f"r: {_state['r']['value']:.2f}"),
            mo.md(f"{_state['r']['units']}")
        ], justify="start"),
    ])
    return


@app.cell
def _(get_state, handle_slider_change, mo):
    # ALL UI ELEMENTS CREATION - NUMBERS ONLY VERSION
    _state = get_state()

    def make_number_handler(param_name):
        """Create a proper closure for the number handler"""
        print(f"Creating handler for parameter: {param_name}")  # Debug line
        def handler(value):
            print(f"Handler called for {param_name}: {value}")  # Debug line
            return handle_slider_change(param_name, value)
        return handler

    print("Creating ALL number input elements with consistent state...")

    # Create ALL number inputs (replacing sliders)
    number_θ = mo.ui.number(
        value=_state["θ"]["value"],
        start=_state["θ"]["start"],
        stop=_state["θ"]["stop"],
        step=_state["θ"]["step"],
        label=f"θ:",
        debounce=True,
        on_change=make_number_handler("θ"),
    ).style({"width": "120px"})

    number_b = mo.ui.number(
        value=_state["b"]["value"],
        start=_state["b"]["start"],
        stop=_state["b"]["stop"],
        step=_state["b"]["step"],
        label=f"b:",
        debounce=True,
        on_change=make_number_handler("b"),
    ).style({"width": "120px"})

    number_t = mo.ui.number(
        value=_state["t"]["value"],
        start=_state["t"]["start"],
        stop=_state["t"]["stop"],
        step=_state["t"]["step"],
        label=f"t:",
        debounce=True,
        on_change=make_number_handler("t"),
    ).style({"width": "120px"})

    number_s = mo.ui.number(
        value=_state["s"]["value"],
        start=_state["s"]["start"],
        stop=_state["s"]["stop"],
        step=_state["s"]["step"],
        label=f"s:",
        debounce=True,
        on_change=make_number_handler("s"),
    ).style({"width": "120px"})

    number_r = mo.ui.number(
        value=_state["r"]["value"],
        start=_state["r"]["start"],
        stop=_state["r"]["stop"],
        step=_state["r"]["step"],
        label=f"r:",
        debounce=True,
        on_change=make_number_handler("r"),
    ).style({"width": "120px"})

    print("All number input elements created with current state values")
    return number_b, number_r, number_s, number_t, number_θ


@app.cell
def __init__(mo):
    """
    Cell 1: Initialize State.
    Sets default values and unpacks the state getter and setter.
    """

    KNOTS2MPS = 0.5144444444
    MPS2KNOTS = 1.9438444924

    FEET2METERS = 0.3048
    METERS2FEET = 3.28083989501

    initial_state_dict =     {
            "θ": {"value": 5.0, "start": 0.1, "stop": 90.0, "step": 0.1, "units": "degrees"},
            "b": {"value": 5.0, "start": 0.5, "stop": 100.0, "step": 0.5, "units": "feet"},
            "t": {"value": 5.0, "start": 0.1, "stop": 10.0, "step": 0.1, "units": "seconds"},
            "s": {"value": 5.0, "start": 5.0, "stop": 300.0, "step": 5.0, "units": "knots"},
            "r": {"value": 5.0, "start": 1.0, "stop": 100.0, "step": 1.0, "units": "feet"},
            "output_target": "θ",
        }


    get_state, set_state = mo.state( initial_state_dict )
    return FEET2METERS, KNOTS2MPS, METERS2FEET, MPS2KNOTS, get_state, set_state


@app.cell
def calculation_functions(
    FEET2METERS,
    KNOTS2MPS,
    METERS2FEET,
    MPS2KNOTS,
    arcsin,
    arctan,
    cos,
    math,
    sin,
    sqrt,
):
    """
    Cell 2: Define Calculation Functions.
    Each function calculates one slider's value based on the other four.
    """


    def abort_angle(buffer=4.0, time=4.0, speed=1.0, radius=1.0):
        _buffer = buffer * FEET2METERS
        _speed = speed * KNOTS2MPS
        _radius = radius * FEET2METERS
        return math.degrees(
            float(
                arctan(_radius / (time * _speed))
                + arcsin((_buffer - _radius) / sqrt(_radius**2 + (time * _speed) ** 2))
            )
        )


    def abort_buffer(angle=abort_angle(), time=4.0, speed=1.0, radius=1.0):
        _angle = math.radians(angle)
        _speed = speed * KNOTS2MPS
        _radius = radius * FEET2METERS
        return METERS2FEET * float(
            time * _speed * sin(_angle) + _radius * (1 - cos(_angle))
        )


    def time_margin(angle=abort_angle(), buffer=4.0, speed=1.0, radius=1.0):
        _angle = math.radians(angle)
        _buffer = buffer * FEET2METERS
        _speed = speed * KNOTS2MPS
        _radius = radius * FEET2METERS
        return float((_buffer + _radius * (cos(_angle) - 1)) / (_speed * sin(_angle)))


    def abort_speed(angle=abort_angle(), buffer=4.0, time=4.0, radius=1.0):
        _angle = math.radians(angle)
        _buffer = buffer * FEET2METERS
        _radius = radius * FEET2METERS
        return MPS2KNOTS * float(
            (_buffer + _radius * (cos(_angle) - 1)) / (time * sin(_angle))
        )


    def abort_radius(angle=abort_angle(), buffer=4.0, time=4.0, speed=1.0):
        _angle = math.radians(angle)
        _buffer = buffer * FEET2METERS
        _speed = speed * KNOTS2MPS
        return METERS2FEET * float(
            (time * _speed * sin(_angle) - _buffer) / (cos(_angle) - 1)
        )


    # Store functions in a dictionary for easy lookup
    FUNCTIONS = {
        "θ": abort_angle,
        "b": abort_buffer,
        "t": time_margin,
        "s": abort_speed,
        "r": abort_radius,
    }
    return (FUNCTIONS,)


@app.cell
def _(get_state):
    # Helper to clamp values to the slider's range
    def clamp(value, target):
        _start = get_state()[target]["start"]
        _stop = get_state()[target]["stop"]
        return max(_start, min(_stop, value))
    return (clamp,)


@app.cell
def state_handlers(FUNCTIONS, clamp, get_state, set_state):
    """
    Cell 3: Define State-Update Handlers.
    These functions manage the core logic of updating slider values.
    """


    def handle_slider_change(slider_name, new_value):
        """
        Called when any slider is moved.
        Updates the moved slider AND the output slider.
        """
        # Get the dictionary that holds the entire app state
        current_state_dict = get_state()
        target = current_state_dict["output_target"]

        # Create a snapshot of the *next* state of all values
        next_inputs = current_state_dict.copy()
        next_inputs[slider_name]["value"] = new_value



        # If the moved slider isn't the output, re-calculate the output's value
        if slider_name != target:
            calc_function = FUNCTIONS[target]
            args = [
                next_inputs[p]["value"] for p in ["θ", "b", "t", "s", "r"] if p != target
            ]
            new_output_value = clamp(calc_function(*args), target)


        # Get a copy of the old state, apply updates, and set it back
        new_state_dict = current_state_dict.copy()
        new_state_dict[target]["value"] = new_output_value
        set_state(new_state_dict)


    def handle_target_change(new_target):
        """
        Called when the radio button is changed.
        Re-calculates the value of the new output slider.
        """
        current_state_dict = get_state()
        calc_function = FUNCTIONS[new_target]

        print(new_target)
        args = [
            current_state_dict[p]["value"]
            for p in ["θ", "b", "t", "s", "r"]
            if p != new_target
        ]

        new_output_value = clamp(calc_function(*args), new_target)

        # Get a copy, apply updates, and set the whole dict back
        new_state_dict = current_state_dict.copy()
        new_state_dict["output_target"] = new_target
        new_state_dict[new_target]["value"] = new_output_value

        set_state(new_state_dict)
    return handle_slider_change, handle_target_change


@app.cell
def _(get_state, handle_target_change, mo):
    # UI element to select the output
    target_selector = mo.ui.radio(
        options=["θ", "b", "t", "s", "r"],
        # Bind the radio's value to a key in the state dictionary
        value=get_state()["output_target"],
        on_change=handle_target_change,
        label="Select Output Slider:",
    )
    return (target_selector,)


@app.cell
def _(get_state, handle_slider_change, mo):
    _name = "θ"
    _state = get_state()


    slider_θ = mo.ui.slider(
        start=_state[_name]["start"],
        stop=_state[_name]["stop"],
        step=_state[_name]["step"],
        # Bind the slider's value to a key in the state dictionary
        value=get_state()[_name]["value"],
        label=f"Slider {_name}:",
        on_change=lambda v: handle_slider_change(_name, v),
        # Dynamically disable the slider if it's the output target
        disabled=(get_state()["output_target"] == _name),
    )
    return (slider_θ,)


@app.cell
def _(get_state, handle_slider_change, mo):
    _name = "b"
    _state = get_state()

    slider_b = mo.ui.slider(
        start=_state[_name]["start"],
        stop=_state[_name]["stop"],
        step=_state[_name]["step"],
        # Bind the slider's value to a key in the state dictionary
        value=_state[_name]["value"],
        label=f"Slider {_name}:",
        on_change=lambda v: handle_slider_change(_name, v),
        # Dynamically disable the slider if it's the output target
        disabled=(get_state()["output_target"] == _name),
    )
    return (slider_b,)


@app.cell
def _(get_state, handle_slider_change, mo):
    _name = "t"
    _state = get_state()


    slider_t = mo.ui.slider(
        start=_state[_name]["start"],
        stop=_state[_name]["stop"],
        step=_state[_name]["step"],
        # Bind the slider's value to a key in the state dictionary
        value=get_state()[_name]["value"],
        label=f"Slider {_name}:",
        on_change=lambda v: handle_slider_change(_name, v),
        # Dynamically disable the slider if it's the output target
        disabled=(get_state()["output_target"] == _name),
    )
    return (slider_t,)


@app.cell
def _(get_state, handle_slider_change, mo):
    _name = "s"
    _state = get_state()


    slider_s = mo.ui.slider(
        start=_state[_name]["start"],
        stop=_state[_name]["stop"],
        step=_state[_name]["step"],
        # Bind the slider's value to a key in the state dictionary
        value=get_state()[_name]["value"],
        label=f"Slider {_name}:",
        on_change=lambda v: handle_slider_change(_name, v),
        # Dynamically disable the slider if it's the output target
        disabled=(get_state()["output_target"] == _name),
    )
    return (slider_s,)


@app.cell
def _(get_state, handle_slider_change, mo):
    _name = "r"
    _state = get_state()


    slider_r = mo.ui.slider(
        start=_state[_name]["start"],
        stop=_state[_name]["stop"],
        step=_state[_name]["step"],
        # Bind the slider's value to a key in the state dictionary
        value=get_state()[_name]["value"],
        label=f"Slider {_name}:",
        on_change=lambda v: handle_slider_change(_name, v),
        # Dynamically disable the slider if it's the output target
        disabled=(get_state()["output_target"] == _name),
    )
    return (slider_r,)


@app.cell
def _(
    get_state,
    mo,
    slider_b,
    slider_r,
    slider_s,
    slider_t,
    slider_θ,
    target_selector,
):
    # Display all the UI elements
    _state = get_state()

    mo.vstack(
        [
            mo.md("### Interactive Slider Calculator"),
            target_selector,
            mo.md("---"),
            mo.hstack(
                [slider_θ, mo.md(f"{slider_θ.value:0.4} {_state['θ']['units']}")], justify="start"
            ),
            mo.hstack(
                [slider_b, mo.md(f"{slider_b.value:0.4} {_state['b']['units']}")], justify="start"
            ),
            mo.hstack(
                [slider_t, mo.md(f"{slider_t.value:0.4} {_state['t']['units']}")], justify="start"
            ),
            mo.hstack(
                [slider_s, mo.md(f"{slider_s.value:0.4} {_state['s']['units']} ground")],
                justify="start",
            ),
            mo.hstack(
                [slider_r, mo.md(f"{slider_r.value:0.4} {_state['r']['units']}")], justify="start"
            ),
        ]
    )
    return


if __name__ == "__main__":
    app.run()
