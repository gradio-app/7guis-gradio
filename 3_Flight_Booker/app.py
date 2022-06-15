import gradio as gr
from datetime import datetime


def update_return_visibility(flight_type: str):
    """Changes visibility of the returning date, depending on flight type."""
    if flight_type == "return flight":
        visible = True
    else:
        visible = False
    return gr.Textbox.update(visible=visible)


def on_click(flight_type: str, start_date: str, return_date: str):
    """If Book button is clicked displays message."""
    if flight_type == "one-way flight":
        message = f"You have booked a {flight_type} flight on {start_date}"
    else:
        message = f"You have booked a {flight_type} flight starting on {start_date} and returning on {return_date}"
    return gr.TextArea.update(value=message)


def update_date(flight_type: str, start_date: str, return_date: str):
    """Changing the date values. Any change to dates also clear out the message."""
    button_visible = True
    try:
        d1 = datetime.strptime(start_date, "%d.%m.%Y")
        if flight_type == "return flight":
            d2 = datetime.strptime(return_date, "%d.%m.%Y")
            if d1 > d2: 
                button_visible = False
    except Exception: # Exception is raised by datetime.strptime when input format is wrong
        button_visible = False

    return gr.Button.update(visible=button_visible), gr.TextArea.update(value="")


################################
# main demo
################################

TODAY = datetime.now().strftime("%d.%m.%Y")

with gr.Blocks() as demo:
    gr.Markdown(
        """# Flight Booking
        """
    )
    with gr.Column():
        flight_type = gr.Dropdown(["one-way flight", "return flight"], value="return flight", show_label=False)
        start_date = gr.Textbox(TODAY, max_lines=1, placeholder="dd.mm.yyyy", show_label=False)
        return_date = gr.Textbox(TODAY, max_lines=1, placeholder="dd.mm.yyyy", show_label=False) # supposed to be turned off / not visible initially, but keeping it on for now
        button = gr.Button("Book")
        message = gr.Textbox(max_lines=1, visible=True, show_label=False)

        flight_type.change(update_return_visibility, flight_type, return_date)
        start_date.change(update_date, [flight_type, start_date, return_date], [button, message])
        return_date.change(update_date, [flight_type, start_date, return_date], [button, message])
        button.click(on_click, [flight_type, start_date, return_date], message)


if __name__ == "__main__":
    demo.launch()
