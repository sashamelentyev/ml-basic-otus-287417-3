def make_id(s: str) -> str:
    if len(s) > 8:
        return s

    r = 8 - len(s)

    return "0" * r + s


seq = 1
step = 0

users = {}
data = []
id = ""

while True:
    inp = input()
    if len(inp) == 0:
        break

    step += 1

    if step == 1 or step == 2:
        data.append(inp.__str__().title())

    elif step == 3:
        try:
            age = int(inp)
            if age < 18 or age > 60:
                print("Возраст должен быть от 18 до 60 включительно")
                break

            data.append(age)
        except ValueError:
            print("Возраст должен быть числом")
            break

    elif step == 4:
        try:
            int(inp)
        except ValueError:
            print("Идентификатор должен быть числом")
            break

        id = make_id(inp)

    if step % 4 == 0:
        if users.get(id) is not None:
            print("Идентификатор уже существует")
            break

        users[id] = data

        step = 0
        data = []

for id, data in users.items():
    print(id, "|", data[0], "|", data[1], "|", data[2])
