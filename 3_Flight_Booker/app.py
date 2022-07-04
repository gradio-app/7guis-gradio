import gradio as gr
from datetime import datetime

def return_state(flight_type: str):
    """Changes interactivity of the returning date Textbox depending on flight type."""
    state = flight_type == "return flight"
    return gr.Textbox.update(value="", interactive=state)

def display_message(flight_type: str, start_date: str, return_date: str):
    """If the book button is clicked, displays a message."""
    if flight_type == "one-way flight":
        message = f"You have booked a {flight_type} on {start_date}."
    else:
        message = f"You have booked a {flight_type} starting on {start_date} and returning on {return_date}."
    return gr.TextArea.update(message, visible=True)

def remove_message():
    """Clears and removes message display."""
    return gr.TextArea.update("", visible=False)

def validate_date(date: str):
    """Extracts date from string."""
    valid = True
    try:
        date = datetime.strptime(date, "%d.%m.%Y")
    except Exception:
        valid = False
    return date, valid

def check_date(flight_type: str, start_date: str, return_date: str):
    """If the date is updated, checks format, and updates button and warning."""
    state, v2 = True, True
    
    d1, v1 = validate_date(start_date)
    if flight_type == "return flight":
        d2, v2 = validate_date(return_date)
        state = d1 <= d2 if v1 and v2 else False
    else:
        state = v1
    
    return (
        gr.Button.update(visible=state),
        gr.HighlightedText.update(visible=not v1),
        gr.HighlightedText.update(visible=not v2)
    )


TODAY = datetime.now().strftime("%d.%m.%Y")
DATE_HINT = "dd.mm.yyyy"

with gr.Blocks() as demo:
    gr.Markdown(
        """# Flight Booker
        """
    )
    with gr.Column():
        flight_type = gr.Dropdown(["one-way flight", "return flight"], value="one-way flight", show_label=False)
        with gr.Row():
            
            start_date = gr.Textbox(TODAY, max_lines=1, placeholder=DATE_HINT, show_label=False).style()
            start_status = gr.HighlightedText([(DATE_HINT, "X")], show_label=False, visible=False).style(color_map={"X": "red"})

        with gr.Row():
            return_date = gr.Textbox("", max_lines=1, placeholder=DATE_HINT, show_label=False, interactive=False)
            return_status = gr.HighlightedText([(DATE_HINT, "X")], show_label=False, visible=False).style(color_map={"X": "red"})
        button = gr.Button("Book")
        message = gr.Textbox(max_lines=1, visible=False, interactive=False, show_label=False)

        flight_type.change(return_state, flight_type, return_date)
        flight_type.change(check_date, [flight_type, start_date, return_date], [button, start_status, return_status])
        flight_type.change(remove_message, [], message)

        start_date.change(check_date, [flight_type, start_date, return_date], [button, start_status, return_status])
        start_date.change(remove_message, [], message)

        return_date.change(check_date, [flight_type, start_date, return_date], [button, start_status, return_status])
        return_date.change(remove_message, [], message)

        button.click(display_message, [flight_type, start_date, return_date], message)

if __name__ == "__main__":
    demo.launch()