from turtle import update
import gradio as gr
from datetime import datetime


def update_return_visibility(flight_type: str):
    visible = True if flight_type == "return flight" else False
    return gr.Textbox.update(visible=visible)
        
def update_day(flight_type: str, start_day: str, return_day: str):
    try:
        d1 = datetime.strptime(start_day, "%d.%m.%Y")
        if flight_type == "return flight":
            d2 = datetime.strptime(return_day, "%d.%m.%Y")
    except Exception as e:
        print(f"Could not retrieve date: {e}")
        return gr.Button.update(visible=False)
    
    if flight_type == "return flight" and d1 > d2:
        print("Start day > returning date")
        return gr.Button.update(visible=False)
        
    print("All checks passed turning on button.")    
    return gr.Button.update(visible=True)



with gr.Blocks() as demo:
    with gr.Column():
        flight_type = gr.Dropdown(["one-way flight", "return flight"], value="one-way flight", type="value", show_label=False)
        today = datetime.now().strftime("%d.%m.%Y")
        start_day = gr.Textbox(today, max_lines=1, placeholder="dd.mm.yyyy", show_label=False)
        return_day = gr.Textbox(today, max_lines=1, placeholder="dd.mm.yyyy", show_label=False, visible=False)
        button = gr.Button("Book")

        flight_type.change(update_return_visibility, flight_type, return_day)

        start_day.change(update_day, [flight_type, start_day, return_day], button)
        return_day.change(update_day, [flight_type, start_day, return_day], button)


if __name__ == "__main__":
    demo.launch()
