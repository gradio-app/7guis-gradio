import gradio as gr
import numpy as np
import re

dummy_data = [["Alice", "Springs"], ["Max", "Brown"]]

def fetch_data():
    """Fetch data from the data store. 
    In this case it's just an numpy array
    NOTE: This should happen at page load."""
    return dummy_data

def create_item(name, surname):
    """Create an item in the data store"""
    dummy_data.append([name, surname])
    return dummy_data

def update_item(idx, name, surname):
    """Update an item in the data store"""
    idx = dummy_data.index([name, surname])
    dummy_data.insert(idx,)
    return dummy_data

def delete_item(name, surname):
    """Delete an item from the data store"""
    dummy_data.remove([name, surname])
    return dummy_data

def filter_prefix(prefix):
    """Return all the item whoes surnames starting with prefix
    else return an empty list"""
    return [x for x in dummy_data[:,1] if re.search(f"^{prefix}", x)]

with gr.Blocks() as demo:

    fetch_btn = gr.Button("Fetch Data")
    out = gr.Dataframe(
            headers=["Name", "Surname"],
            datatype=["str", "str"],
            col_count=(2, "fixed"),
        )

    fetch_btn.click(fetch_data, None, out)
    
    filter_prefix = gr.Text(label="Filter prefix")
    with gr.Row():
        with gr.Column():
            name = gr.Text(label="Name")
            surname = gr.Text(label="Surname")
    with gr.Row():
        create_btn = gr.Button("Create")
        update_btn = gr.Button("Update")
        delete_btn = gr.Button("Delete")
    
    create_btn.click(create_item, [name, surname], out)
    update_btn.click(update_item, [name, surname], out)
    delete_btn.click(delete_item, [name, surname], out)

if __name__ == "__main__":
    demo.launch()
