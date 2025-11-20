import re
import typer

app = typer.Typer()

@app.command()
def regExRun(filename: str):
    input_text = open(f"files/{filename}", "r")
    output_text = input_text.read()
    output_file = open(f"files/output_{filename[:-4]}.txt", "w")

    # ask joe: should a backslash ever be in text?

    # trying to figure out how to remove a space then punctuation. for example if its
    # hi .i am
    # then it should remove " ." 
    patterns = ["[ \s][:\|.?/]", "&quot;", "&nbsp;", "&gt;", "&lt;", "&amp;", "~", "�?", "�", "\|", "[ \s][?]"]
    replaces = [" ", '"', " ", "", "", "&", " ", "", "", " ", " "]
    replaces_counter = 0

    for pat in patterns:
        #if pat in output_text:
        output_text = re.sub(pat, replaces[replaces_counter], output_text)
        replaces_counter += 1
        
    # having trouble with removing carets via regex despite using escape chars. workaround.
    output_text = output_text.replace("^", "")

    output_file.write(output_text)

    input_text.close()
    output_file.close()

if __name__ == "__main__":
    app()