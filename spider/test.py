
import re

if __name__ == "__main__":
    # print(len('cd64af5c26eb4929ab06870978aeb32c'))
    string = "addContent('553c2189e7e845af9e636d287e7ee00c','97a061b4758c48b2ba0b43f59ea1fb9d','add','3901170101')"

    str2 = "viewTalk('caf2a9c2e51c45289ffdea670808c7a1','')"
    print(string)

    # res = re.findall(r"'\w{32}'",string)

    print(re.findall(r"'\w{32}'|''",string))  # 保证两种格式都能被正则到
    # print(res)