import random

def animal_rand(): # todo give 3 results instead of 1
    animal_list = ['cat', 'dog', 'gecko', 'snake', 'unicorn', 'goat', 'sheep', 'deer', 'cow', 'mole', 'mole rat', 'vulture', 'hawk', 'raven', 'corvid', 'axolotl', 'zebra', 'tiger', 'lion', 'panther', 'saber tooth tiger', 'thylacine', 'hyena', 'tasmanian devil', 'mouse', 'rat', 'shrew', 'bat', 'chameleon', 'mongoose', 'mink', 'cobra', 'koala', 'horse', 'wolf', 'fox', 'numbat', 'pika', 'rock hyrax', 'hamster', 'bear', 'owl', 'moose', 'shark', 'ferret', 'siberian ferret', 'porcupine', 'hedgehog', 'bandicoot', 'skunk', 'pine martin', 'squirrel', 'pig', 'warthog', 'platypus', 'duck', 'goose', 'dragon', 'wyvern', 'anteater', 'tapir', 'degu', 'donkey', 'rabbit', 'capybara', 'dinosaur', 'chimera', 'moon bear', 'polar bear', 'red panda', 'beaver', 'crocodile', 'panda', 'dingo', 'maned-wolf', 'sphinx cat', 'scottish fold cat', 'kangaroo', 'elephant', 'hippo', 'parrot', 'budgie']
    animal = random.choice(animal_list)
    print('Prompt: ', animal)

def gore_prompt():
    gore_list = ['blood', 'cannibalism', 'intestines', 'surgery', 'knife', 'slit throat', 'nosebleed', 'teeth', 'burn victim', 'ribs', 'bones', 'self-harm', 'smoking', 'body horror', 'rot', 'plant overgrowth', 'fungus', 'trypophobia', 'acid burns', 'schizophrenia', 'bdsm', 'piercings', 'eyes', 'siamese twins', 'amputee', 'post-surgery', 'cultist ritualism', 'sliced off', 'needles', 'gas mask', 'blisters', 'guts', 'zombie', 'halloween costume', 'decay', 'scars', 'stitches', 'thorns', 'extra limbs', 'bruised', 'tourniquete', 'bugs', 'sickness', 'impaled', '80s horror movie fanart', 'insanity', 'arrows', 'roadkill', 'dissection', 'crystals', 'rabies', 'tumors', 'blind', 'medical', 'eye trauma', 'butcher', 'lacerations', 'skinned alive']
    gore = random.choice(gore_list)
    print('Prompt: ', gore)

def palette_gen(): # todo study up on the syntax used for this function
        # Define color groups based on color theory and popular themes
    color_groups = {
        "primary": ["#FF0000", "#00FF00", "#0000FF"],  # Red, Green, Blue
        "analogous": ["#FF5733", "#FF8D33", "#FFBD33"],  # Warm colors
        "complementary": ["#FF0000", "#00FFFF"],  # Red and Cyan
        "triadic": ["#FF0000", "#00FF00", "#0000FF"],  # Red, Green, Blue
        "split_complementary": ["#FF0000", "#00FFFF", "#0000FF"],  # Red, Cyan, Blue
        "tetradic": ["#FF0000", "#00FF00", "#0000FF", "#FFFF00"],  # Red, Green, Blue, Yellow
        "square": ["#FF0000", "#00FF00", "#0000FF", "#FFFF00"],  # Red, Green, Blue, Yellow
        "solarized_dark": ["#073642", "#586e75", "#657b83", "#839496", "#93a1a1", "#eee8d5", "#dc322f", "#b58900", "#859900", "#268bd2", "#2aa198", "#d33682"],
        "dracula": ["#282a36", "#44475a", "#f8f8f2", "#6272a4", "#8be9fd", "#50fa7b", "#ffb86c", "#ff79c6", "#bd93f9", "#ff5555", "#f1fa8c"],
        "tokyo_night": ["#1a1b26", "#c0caf5", "#7aa2f7", "#9ece6a", "#ff9e64", "#ff75a0", "#bb9af7", "#f7768e", "#e0af68"],
        "gruvbox_dark": ["#282828", "#ebdbb2", "#fb4934", "#b8bb26", "#fabd2f", "#83a598", "#d3869b", "#8ec07c", "#fe8019"],
        "zenburn": ["#3F3F3F", "#DCDCCC", "#D0D0D0", "#DCDCCC", "#CC9393", "#F0DFAF", "#8CD0D3", "#D0BF8F"],
        "monokai": ["#272822", "#F8F8F2", "#66D9EF", "#A6E22E", "#F92672", "#FD971F", "#75715E", "#F8F8F2"],
        "nord": ["#2e3440", "#d8dee9", "#3b4252", "#4c566a", "#5e81ac", "#88c0d0", "#a3be8c", "#ebcb8b", "#bf616a", "#b48ead"],
        "flat_remix": ["#2C3E50", "#E74C3C", "#3498DB", "#1ABC9C", "#F1C40F", "#9B59B6", "#34495E"],
        "kyli0x": ["#1C1C1C", "#F8F8F2", "#FF79C6", "#50FA7B", "#FFB86C", "#BD93F9", "#FF5555"],
        "adapta": ["#2E3440", "#D8DEE9", "#4C566A", "#5E81AC", "#88C0D0", "#A3BE8C", "#BF616A", "#D19A66"],
        "dusklight": ["#F8F8F2", "#282A36", "#6272A4", "#8BE9FD", "#50FA7B", "#FFB86C", "#FF79C6"]
        }

        # Randomly select a color theory type
    theory_type = random.choice(list(color_groups.keys()))
    selected_colors = random.sample(color_groups[theory_type], k=random.randint(3, 5))  # Pick 3 to 5 colors

        # Print the color palette
    print(f"\nGenerated {theory_type.replace('_', ' ').capitalize()} Color Palette:")
    for color in selected_colors:
            # Print color sample
        print(f"\033[48;2;{int(color[1:3], 16)};{int(color[3:5], 16)};{int(color[5:7], 16)}m  \033[0m {color}")


def ocs_prompt():
    oc_prompt_list = ['newest', 'oldest', 'grumpiest', 'most wholesome', '']
    oc_activity_list = ['eating', 'dressing-up']
    oc1 = random.choice(oc_prompt_list)
    oc2 = random.choice(oc_activity_list)
    print('Prompt: ', oc1, oc2)

def prompt():
    prompt_list = ['winter', 'summer', 'spring', 'magic', 'fanart', 'pokemon', 'feral art', 'anthro', 'depressed', 'neopets']
    prompts = random.choice(prompt_list)
    print('Prompt: ', prompts)

def error_handling():
    print("Error! You have typed something wrong. ")

def menu():
    print('This small program will help you get ideas during art block, it suggests what to draw by giving you prompts. \nChoose between options 1 to 5 then press enter. \n')
    while True:
        try:
                x = int(input(" 1. Animal randomizer \n 2. Gore prompts  \n 3. Palette generator \n 4. OC prompts -- WIP !!! \n 5. Regular prompts "))
                if x == 1:
                    animal_rand()
                elif x == 2:
                    gore_prompt()
                elif x == 3:
                    palette_gen()
                elif x == 4:
                    ocs_prompt()
                elif x == 5:
                    prompt()
                else:
                    error_handling()
        except ValueError:
                print('Please enter a valid number (1 - 5)! ')

menu()