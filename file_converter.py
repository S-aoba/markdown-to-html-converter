import sys
import markdown

input_path = sys.argv[2]
output_path = sys.argv[3]

content = ""

command = sys.argv[1]

if command == "markdown":
    with open(input_path, "r") as f:
        content = f.read()

    with open(output_path, "w") as f:
        html = markdown.markdown(content)
        f.write(html)

else:
    print("コマンドが正しくありません。再度入力し直してください。")