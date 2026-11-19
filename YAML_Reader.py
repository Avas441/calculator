
import re

def parse_hearth_yaml(file_path):
    data = {"hearth": {}}
    hearth = data["hearth"]
    current_list = None

    with open(file_path, "r") as file:
        for line in file:
            line = line.strip()

            if not line or line.startswith("#"):
                continue

            if line == "hearth:":
                continue

            if line.startswith("- "):
                if current_list is not None:
                    hearth[current_list].append(line[2:])
                continue

            if ":" in line:
                key, value = line.split(":", 1)
                key = key.strip()
                value = value.strip()

                if value:
                    hearth[key] = value
                    current_list = None
                else:
                    hearth[key] = []
                    current_list = key

    return data


def print_hearth_shape(file_path):

    # Parse YAML into a Python dictionary
    data = parse_hearth_yaml(file_path)

    hearth = data.get('hearth', {})

    print("--- Hearth Details ---")
    print(f"Color: {hearth.get('color')}")
    print(f"Shape: {hearth.get('shape')}")
    print("\nVisual Rendering (Top-Down):")

    encodding = hearth.get('encodding', [])

    for line_str in encodding:

        match = re.fullmatch(
            r'(\d+)space(\d+)shape', line_str
        )

        if match:
            spaces = int(match.group(1))
            shapes = int(match.group(2))

            print(
                " " * spaces +
                "\033[31m*\033[0m" * shapes
            )
        else:
            print(line_str)


if __name__ == "__main__":
    print_hearth_shape("hearth.yml")
