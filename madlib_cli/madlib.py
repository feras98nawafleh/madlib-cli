import re

def open_template(Filepath):
  # open text file using Filepath
   with open(Filepath)as file:
     return file.read()

def parse_template(text):
  # parse the opened template file
  x = re.findall(r'{(.*?)}',text)
  y = tuple(x)
  x = re.sub(r'{(.*?)}',"{}",text)

  return x, y


def correction(file,inputs):
    # make the template in the correct form with input from user
    correctForm = file.format(*inputs)
    return correctForm

def writeNewFile(content):
    # put content to a new file
    with open('assets/video_game_result.txt', 'w') as video_game:
        video_game.write(content)


if __name__=="__main__":

    print(
    """
    ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
                Welcome to madlib-cli, a CLI based game to enter Adjectives and nouns and it will be showed with names you choose.
     +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    """
    )
    words = open_template("assets/video_game.txt")
    output = re.findall(r'{(.*?)}',words)

    wantedWords = []
    for i in output:
        userInput = input(f'Please enter a {i} ')
        wantedWords.append(userInput)


    wantedWords1 = tuple(wantedWords)
    print(wantedWords1)

    modifiedText = re.sub(r'{(.*?)}',"{}",words)

    print(modifiedText)

    print(correction(modifiedText,wantedWords1))
    
    writeNewFile(correction(modifiedText,wantedWords1))
