import gradio as gr

with gr.Blocks() as demo:
    gr.Markdown(
        """# Temperature Converter
        Update the temperature in either Celsius or Fahrenheit and press enter to get the other!
        """
    )

    with gr.Row():
        celsius = gr.Number(0, label="Celsius")
        fahrenheit = gr.Number(32, label="Fahrenheit")

        celsius.submit(lambda c: c * 9 / 5 + 32, celsius, fahrenheit)
        fahrenheit.submit(lambda f: (f - 32) * 5 / 9, fahrenheit, celsius)

if __name__ == "__main__":
    demo.launch()
