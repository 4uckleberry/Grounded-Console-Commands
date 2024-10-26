from tkinter import *
from tkinter import ttk

from .utils import callback, category_select_match, copy_final, load_json_data

def main():
    data, categories, commands, category_drop = load_json_data()
    
    root = Tk()
    root.title("Grounded Console Commands")
    root.resizable(False, False)
    root.geometry("800x180")
    
    dropdown_frame = ttk.Frame(root)
    
    catefory_frame = ttk.Frame(dropdown_frame)
    category_lbl = ttk.Label(catefory_frame, text="Select Category:")
    category_lbl.pack(pady=(0,3))
    
    category_type = StringVar()
    categorycb=ttk.Combobox(catefory_frame, width=30, textvariable=category_type)
    categorycb['values'] = category_drop
    categorycb['state'] = 'readonly'
    categorycb.current(0)
    categorycb.pack(padx=5, side=LEFT)
    catefory_frame.pack(side=LEFT)
    
    selection_frame = ttk.Frame(dropdown_frame)
    
    selection_lbl = ttk.Label(selection_frame, text="Select Item:")
    selection_lbl.pack(pady=(0,3))
    
    selection_type = StringVar()
    
    selectionCombo = ttk.Combobox(selection_frame, width=60, textvariable=selection_type)
    selectionCombo['state'] = 'readonly'
    selectionCombo.pack(padx=5)
    
    selection_frame.pack()
    dropdown_frame.pack(pady=(5,0))
    
    blueprint_lbl = ttk.Label(root, text="Sample Console Command")
    blueprint_lbl.pack(pady=(10,0))
    
    sample_frame = ttk.Frame(root)
    sample = StringVar()
    sample_entry = ttk.Entry(master=sample_frame, width=120, state='readonly', justify=CENTER, textvariable=sample)
    sample_entry.pack(side=LEFT)
    
    sample_frame.pack(pady=(5,5))
    
    quantity_frame = ttk.Frame(root)
    
    quantity_lbl = ttk.Label(quantity_frame, text="Quantity: ")
    quantity_lbl.pack(side=LEFT)
    
    quantity_entry = ttk.Entry(master=quantity_frame, justify=CENTER, width=10)
    quantity_entry.insert(0, 1)
    quantity_entry.pack(pady=(3,0))
    
    quantity_frame.pack()
    
    copy_button = ttk.Button(
        master=root, 
        width=20, 
        text="Copy to Clipboard", 
        command=lambda: copy_final(root, sample_entry, category_type, quantity_entry)
    )
    copy_button.pack(pady=(10,0))
    
    categorycb.bind('<<ComboboxSelected>>', lambda event: category_select_match(event, categories, category_type, selectionCombo))
    
    selectionCombo.bind("<<ComboboxSelected>>", lambda event: callback(event, selection_type, commands, sample))
    
    root.mainloop()