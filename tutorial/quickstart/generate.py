def seri(model, fields):
    return f"class {model}Serializer(serializers.HyperlinkedModelSerializer):\n\tclass Meta:\n\t\tmodel \n = models.{model}\n\t\tfields = {fields}"

def viewset(model):
    return f"class {model}ViewSet(viewsets.ModelViewSet):\n\tqueryset = models.{model}.objects.all()\n\tserializer_class = serializers.{model}Serializer"


obj_list = list()

with open("models.py", "r") as file:
    all_text = file.readlines()
    for index, line in enumerate(all_text):
        if line.startswith("class"):
            model = line[len("class") + 1 : line.index("(")]
            fields = ["url"]
            i = 1
            next_line = all_text[index + i].strip()
            while not next_line.startswith("class"):
                try:
                    fields.append(next_line[0 : next_line.index(" =")])
                except ValueError:
                    pass
                i += 1
                next_line = all_text[index + i].strip()
            obj_list.append((model, fields))

with open("view_out.txt", "w") as output:
    for obj in obj_list:
        output.write(viewset(obj[0]))
        output.write("\n\n")

with open("serial_out.txt", "w") as output:
    for obj in obj_list:
        output.write(seri(obj[0], obj[1]))
        output.write("\n\n")

with open("model_list.txt", "w") as output:
    for obj in obj_list:
        output.write(obj[0])
        output.write("\n\n")
