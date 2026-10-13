"""
🎓 VocaQuiz - 콘솔 & 학습용 파이썬 영단어 퀴즈 프로그램
=============================================================
주요 기능:
1. 4지 선다형 영단어 퀴즈 (랜덤 출제)
2. 실시간 정답 확인 및 점수 계산
3. 오답 단어 자동 수집 및 오답노트 복습 기능
4. 단어장 조회 및 나만의 단어 추가 기능
=============================================================
"""

import random
import time

# 1. 기본 영단어 데이터베이스 (단어, 뜻, 품사, 예문)
DEFAULT_WORD_BANK = [
    {
        "word": "appreciate",
        "meaning": "감사하다, 진가를 인정하다",
        "part": "동사",
        "example": "I really appreciate your kind help."
    },
    {
        "word": "convenient",
        "meaning": "편리한, 사용하기 쉬운",
        "part": "형용사",
        "example": "This subway station is very convenient."
    },
    {
        "word": "essential",
        "meaning": "필수적인, 본질적인",
        "part": "형용사",
        "example": "Water is essential for all living things."
    },
    {
        "word": "generous",
        "meaning": "관대한, 후한, 아낌없는",
        "part": "형용사",
        "example": "He is always generous to people in need."
    },
    {
        "word": "hesitate",
        "meaning": "망설이다, 주저하다",
        "part": "동사",
        "example": "Don't hesitate to ask if you have questions."
    },
    {
        "word": "opportunity",
        "meaning": "기회",
        "part": "명사",
        "example": "Don't miss this wonderful opportunity."
    },
    {
        "word": "concentrate",
        "meaning": "집중하다, 전념하다",
        "part": "동사",
        "example": "Please be quiet so I can concentrate."
    },
    {
        "word": "accommodate",
        "meaning": "수용하다, 편의를 제공하다",
        "part": "동사",
        "example": "The hotel can accommodate up to 500 guests."
    },
    {
        "word": "comprehensive",
        "meaning": "포괄적인, 종합적인",
        "part": "형용사",
        "example": "We conducted a comprehensive review of the plan."
    },
    {
        "word": "implement",
        "meaning": "실행하다, 이행하다",
        "part": "동사",
        "example": "The company decided to implement new security policies."
    },
    {
        "word": "vulnerable",
        "meaning": "취약한, 상처받기 쉬운",
        "part": "형용사",
        "example": "Small businesses are vulnerable to economic shocks."
    },
    {
        "word": "mandatory",
        "meaning": "의무적인, 법에 정해진",
        "part": "형용사",
        "example": "Wearing a helmet is mandatory for cyclists."
    }
]

word_bank = list(DEFAULT_WORD_BANK)
wrong_notes = []


def run_quiz(custom_words=None):
    """4지선다 영단어 퀴즈 실행 함수"""
    target_pool = custom_words if custom_words else word_bank

    if len(target_pool) < 4:
        print("\n⚠️ 퀴즈를 진행하려면 최소 4개 이상의 단어가 필요합니다!")
        return

    print("\n" + "=" * 50)
    print("🎯 영단어 4지선다 퀴즈를 시작합니다!")
    print("=" * 50)

    try:
        q_count = int(input(f"몇 문제를 푸시겠습니까? (최대 {len(target_pool)}개): ") or "5")
    except ValueError:
        q_count = 5

    q_count = min(q_count, len(target_pool))
    quiz_questions = random.sample(target_pool, q_count)

    score = 0
    streak = 0
    session_wrong = []

    for i, target in enumerate(quiz_questions, 1):
        print(f"\n[문제 {i} / {q_count}] 🔥 연속 정답: {streak}")
        print(f"👉 단어: \033[1;36m{target['word']}\033[0m ({target['part']})")

        # 오답 보기 3개 무작위 추출
        other_meanings = [w["meaning"] for w in word_bank if w["word"] != target["word"]]
        wrong_options = random.sample(other_meanings, 3)

        # 4개 보기 조합 및 셔플
        options = wrong_options + [target["meaning"]]
        random.shuffle(options)
        correct_num = options.index(target["meaning"]) + 1

        for idx, opt in enumerate(options, 1):
            print(f"   ({idx}) {opt}")

        # 정답 입력받기
        while True:
            choice = input("\n정답 번호를 입력하세요 (1~4): ").strip()
            if choice in ["1", "2", "3", "4"]:
                break
            print("1, 2, 3, 4 중 하나를 입력해주세요.")

        if int(choice) == correct_num:
            streak += 1
            score += 1
            print("✅ \033[1;32m정답입니다!\033[0m")
        else:
            streak = 0
            print(f"❌ \033[1;31m오답입니다!\033[0m 정답은 ({correct_num})번 '{target['meaning']}' 입니다.")
            # 오답노트에 추가
            if target not in wrong_notes:
                wrong_notes.append(target)
            session_wrong.append(target)

        # 예문 학습
        print(f"   💡 예문: {target['example']}")
        time.sleep(0.5)

    # 결과 리포트
    print("\n" + "=" * 50)
    print("🎉 퀴즈 종료! 결과 발표")
    print(f"📊 맞힌 개수: {score} / {q_count}개")
    accuracy = (score / q_count) * 100
    print(f"🎯 정답률: {accuracy:.1f}%")

    if accuracy == 100:
        print("🏆 만점입니다! 완벽하게 마스터하셨네요!")
    elif accuracy >= 80:
        print("👏 대단해요! 뛰어난 어휘력입니다.")
    else:
        print("💪 조금 더 복습하면 완벽해질 거예요!")

    print("=" * 50)


def view_wrong_notes():
    """오답노트 확인 및 재도전"""
    if not wrong_notes:
        print("\n🎉 현재 오답노트가 비어있습니다! 틀린 단어가 없습니다.")
        return

    print("\n" + "=" * 50)
    print(f"❌ 오답노트 (총 {len(wrong_notes)}단어)")
    print("=" * 50)
    for i, w in enumerate(wrong_notes, 1):
        print(f"{i}. {w['word']} ({w['part']}): {w['meaning']}")
        print(f"   예문: {w['example']}")

    retry = input("\n오답 단어들로만 재시험을 보시겠습니까? (y/n): ").strip().lower()
    if retry == "y":
        run_quiz(custom_words=wrong_notes)


def view_all_words():
    """전체 단어 목록 보기"""
    print("\n" + "=" * 50)
    print(f"📚 전체 단어장 목록 (총 {len(word_bank)}개)")
    print("=" * 50)
    for i, w in enumerate(word_bank, 1):
        print(f"{i:2d}. {w['word']:<15} : {w['meaning']}")


def add_custom_word():
    """나만의 단어 추가"""
    print("\n" + "=" * 50)
    print("➕ 새로운 영단어 등록")
    print("=" * 50)
    word = input("영어 단어 입력: ").strip()
    if not word:
        print("단어가 입력되지 않았습니다.")
        return
    meaning = input("한국어 뜻 입력: ").strip()
    part = input("품사 입력 (예: 명사, 동사, 형용사): ").strip() or "명사"
    example = input("예문 입력 (생략 가능): ").strip() or "예문이 등록되지 않았습니다."

    word_bank.append({
        "word": word,
        "meaning": meaning,
        "part": part,
        "example": example
    })
    print(f"\n✅ '{word}' 단어가 단어장에 성공적으로 추가되었습니다!")


def main():
    while True:
        print("\n========================================================")
        print("🎓 VocaQuiz - 영단어 퀴즈 & 학습 프로그램")
        print("========================================================")
        print("1. 🎯 4지선다 영단어 퀴즈 시작")
        print(f"2. ❌ 오답노트 확인 및 복습 (틀린 단어 {len(wrong_notes)}개)")
        print("3. 📚 전체 단어장 보기")
        print("4. ➕ 나만의 영단어 추가하기")
        print("0. 🚪 종료")
        print("========================================================")

        choice = input("원하는 메뉴 번호를 선택하세요: ").strip()

        if choice == "1":
            run_quiz()
        elif choice == "2":
            view_wrong_notes()
        elif choice == "3":
            view_all_words()
        elif choice == "4":
            add_custom_word()
        elif choice == "0":
            print("\n👋 VocaQuiz 프로그램을 종료합니다. 열공하세요!")
            break
        else:
            print("\n올바른 번호를 입력해주세요.")


if __name__ == "__main__":
    main()
