import menus
from ProcessLoopFor import ProcessLoop


def main():
    is_running = True
    while is_running:
        is_running = menus.menu()

if __name__ == '__main__':
    main()
