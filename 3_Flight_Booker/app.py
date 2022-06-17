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
    return gr.TextArea.update(visible=True, value=message)

def remove_message():
    """Clears and removes message display."""
    return gr.TextArea.update(visible=False, value="")

def check_date(flight_type: str, start_date: str, return_date: str):
    """If the date is updated, checks format and updates button."""
    state = True
    try:
        d1 = datetime.strptime(start_date, "%d.%m.%Y")
        if flight_type == "return flight":
            d2 = datetime.strptime(return_date, "%d.%m.%Y")
            if d1 > d2: 
                state = False
    # When date input format is wrong
    except Exception:
        state = False
    return gr.Button.update(visible=state)

TODAY = datetime.now().strftime("%d.%m.%Y")

with gr.Blocks() as demo:
    gr.Markdown(
        """# Flight Booker
        """
    )
    with gr.Column():
        flight_type = gr.Dropdown(["one-way flight", "return flight"], value="one-way flight", show_label=False)
        start_date = gr.Textbox(TODAY, max_lines=1, placeholder="dd.mm.yyyy", show_label=False)
        return_date = gr.Textbox("", max_lines=1, placeholder="dd.mm.yyyy", show_label=False, interactive=False)
        button = gr.Button("Book")
        message = gr.Textbox(max_lines=1, visible=False, interactive=False, show_label=False)

        flight_type.change(return_state, flight_type, return_date)
        flight_type.change(check_date, [flight_type, start_date, return_date], button)
        flight_type.change(remove_message, [], message)

        start_date.change(check_date, [flight_type, start_date, return_date], button)
        start_date.change(remove_message, [], message)

        return_date.change(check_date, [flight_type, start_date, return_date], button)
        return_date.change(remove_message, [], message)

        button.click(display_message, [flight_type, start_date, return_date], message)

if __name__ == "__main__":
    demo.launch()