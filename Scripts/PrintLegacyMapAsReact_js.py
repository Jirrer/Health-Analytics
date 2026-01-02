from enum import Enum

class State(Enum):
    lookingForCounty = 1
    lookingForSVG = 2
    startingNew = 3


File_Location = "C:\Projects\health_analytics - legacy\old code\html\\map.html"

def main():
    content = getContent()
    counties = getCounties(content)
    proccessedCounties = proccessCounties(counties)
    printCounties(proccessedCounties)

def getContent():
    with open(File_Location, 'r') as file:
        return file.read()

def getCounties(content: str) -> list:
    lines, state = [], State.lookingForCounty

    name, svg = [], []

    index = 13

    while index < len(content) - 3:
        if state == State.lookingForCounty:
            if content[index] == '"':
                index += 5
                state = State.lookingForSVG
            else:
                name.append(content[index])
                index += 1

        elif state == State.lookingForSVG:
            if content[index] == '"':
                index += 17
                state = State.lookingForCounty
                lines.append((''.join(name), ''.join(svg)))
                name, svg = [], []
            else:
                svg.append(content[index])
                index += 1

    return lines

def proccessCounties(counties: list):
    output = []

    for county, svg in counties:
        output.append(f'<path\n\tclassName="{county}"\n\td="{svg}"\nonClick={{() => handleClick("{county}")}}\nstyle={{{{ cursor: "pointer" }}}}\n/>\n')

    return output

def printCounties(counties: list):
    for x in counties:
        print(x)
    

if __name__ == "__main__":
    main()