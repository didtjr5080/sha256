import module
from flask import Flask
from markupsafe import escape


app = Flask(__name__)

# module.make_key()

# module.get_key()



@app.route("/encoding/<word>") # 127.0.0.1/encoding/<word>에 접속하면 "word"를 암호화해줌
def encoding(word):
    a = module.encoding(word)
    return f'{escape(a)}'

@app.route("/decoding/<word>") # 127.0.0.1/encoding/<word>에 접속하면 "word"를 복호화해줌
def decoding(word):
    a = module.denoding(word)
    return f'{escape(a)}'


@app.route("/getkey") # 키 불러오기
def getkey():
    a = module.get_key()
    return f'{escape(a)}'

# a = 'kyu'

# b = module.encoding(a)

# c = module.denoding(b)

# print(a==c)


if __name__ == "__main__":
    app.run(port=5000)