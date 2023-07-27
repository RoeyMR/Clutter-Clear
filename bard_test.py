from bardapi import Bard


class File:
    def __init__(self, filename):
        self.tags = []
        self.filename = filename
        with open(filename, "r") as f:
            self.content = f.read()

    def get_tags(self):
        answer = bard.get_answer("""please list a few tags that represents the following file.
         Make sure that your answer includes only the tags, sepperated by "tag:".
          Do not include in your answer words other then the tags that represent the file!
           Do not explain the tags and do not present write text before and after the tags!. The file is: """ + self.content)
        content = answer["content"]
        first_appearance = content.find("```")
        tags = content[first_appearance + 3: content.find("```", first_appearance+3)-1]
        self.tags = tags.split("\ntag: ")
        self.tags = self.tags[1:] if self.tags[0] == "" else None



token = "ZAjDT7t7GsX6Hl6R1bsT5SSamnClgmCGbqMtpyKbIooFZKlc8j_614hjoZObVa6Vz2ClFA."
bard = Bard(token=token)

file1 = File(r"C:\Users\roeym\PycharmProjects\Clutter-Clear\test folder\HelloWorld.txt")
file1.get_tags()
print(file1.tags)




