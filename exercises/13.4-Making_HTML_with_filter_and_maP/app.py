all_colors = [
	{"label": 'Red', "sexy": True},
	{"label": 'Pink', "sexy": False},
	{"label": 'Orange', "sexy": True},
	{"label": 'Brown', "sexy": False},
	{"label": 'Pink', "sexy": True},
	{"label": 'Violet', "sexy": True},
	{"label": 'Purple', "sexy": False},
]

# Your code here
def generate_li(item):
    return '<li>' + item["label"] + '</li>'

def filter_colors(color):
    return color["sexy"] == True

sexy_colors = list(filter(filter_colors, all_colors))
li_sexy_colors = list(map(generate_li, sexy_colors))
print(li_sexy_colors)

