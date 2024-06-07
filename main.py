
from db import Database


def main() -> str:
    users = input("""
        1. Users >>>>
""")
    
    if users == '1':
        query = f"SELECT * FROM users;"
        print(*Database.connect(query, 'select'))
    else:
        print("Error!")
        return main()
    
if __name__ == '__main__':
    main()
