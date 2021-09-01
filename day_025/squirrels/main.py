
import pandas

file_name = "2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv"
output_file = "squirrel_colors_count.csv"

# count squirel by ""Primary Fur Color" and save new frame to csv

data = pandas.read_csv(file_name)

colors = data["Primary Fur Color"]

gray_count = len(colors[data["Primary Fur Color"] == "Gray"])
black_count = len(colors[data["Primary Fur Color"] == "Black"])
cinnamon_count = len(colors[data["Primary Fur Color"] == "Cinnamon"])


color_data = {
    "Fur color": ["Gray", "Black", "Cinnamon"],
    "Count": [gray_count, black_count, cinnamon_count]
}

pandas.DataFrame(color_data).to_csv(output_file)
