# 1. 영어 -> 한글 2. 한글 -> 영어 ---> 둘중 하나 선택해서 시작
# 종료 라고 입력 받기 전까지는 계속 입력받은 값은 번역해서 출력
# 변역기에 넣어 놓지 않은 입력값이 들어오면 모르는 값이라는 말을 출력
# 안녕, 잘가, 너의 이름은 뭐니, 점심 먹었니, 너가 다니는 학교는 어디니, 난 용산고등학교 다녀
# 번역하는 부분은 함수로 구현


def Trans(langcode, comm):
    kor = ("안녕", "잘가", "너의 이름은 뭐니", "점심 먹었니", "너가 다니는 학교는 어디니", "난 용산고등학교 다녀")
    eng = ["hello", "bye", "what is your name", "did you have lunch", "where is your school",
           "I go to Yongsan high school"]
    try:
        if langcode == 1:
            return kor[eng.index(comm)]
        elif langcode == 2:
            return eng[kor.index(comm)]
    except ValueError:
        return "사전에 없습니다."


try:
    lang = int(input("1. 영한사전\n2. 한영사전\nInput : "))
    while True:
        word = input("\nInput : ")
        if word == "종료":
            break
        elif lang == 1 or 2:
            print(Trans(lang, word))
        else:
            print("다시 입력 해 주세요")
except:
    print("ERROR!!")
