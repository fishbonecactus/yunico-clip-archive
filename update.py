import os,subprocess,sys

BASE=os.path.dirname(os.path.abspath(__file__))

def main():
    print("="*40)
    print("유니코 클립 업데이트")
    print("="*40)

    print("\n[clip_collector.py 실행]")
    r=subprocess.run([sys.executable,os.path.join(BASE,"clip_collector.py")])

    if r.returncode:
        print("clip_collector.py 오류 발생")
        exit(1)

    print("\n클립 업데이트 완료")

    if sys.stdin.isatty():
        input("엔터를 누르면 종료합니다.")

if __name__=="__main__":
    main()
