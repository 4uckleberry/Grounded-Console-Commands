import json

def load_json_data():
    with open('commands.json', 'r') as f:
        data = json.load(f)
    categories = {}
    for drop in data['drops']:
        categories[drop['description']] = drop['members']
    commands = data['commands']
    category_drop = list(categories.keys())
    return data, categories, commands, category_drop

def copy_final(root, sample_entry, category_type, quantity_entry):
    root.clipboard_clear()
    multiple_sample = sample_entry.get()
    if category_type.get() == 'Cheats':
        pass
    else:
        for i in range(int(quantity_entry.get()) - 1):
            multiple_sample = multiple_sample + '|' + sample_entry.get()
    root.clipboard_append(multiple_sample)

def category_select_match(event, categories, category_type, selectionCombo):
    cat_type = category_type.get()
    if cat_type in categories:
        selectionCombo['values'] = categories[cat_type]
        selectionCombo.set('')
    else:
        selectionCombo['values'] = []
        selectionCombo.set('')

def callback(eventObject, selection_type, commands, sample):
    selected_item = selection_type.get()
    command = commands.get(selected_item, '')
    sample.set(command)