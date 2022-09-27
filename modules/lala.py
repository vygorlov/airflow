import os


def lala():
    path = os.environ.get('PROJECT_PATH', '.')
    print("lala")
    print(f'{path}/data/train')


if __name__ == '__main__':
    lala()