months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December",
]


def main():
    date = get_date()


def get_date():
    while True:
        try:
            fecha = input("Date: ").strip().title()
            if "," in fecha:
                day = fecha.split(" ")[1].removesuffix(",")
                month = fecha.split(" ")[0]
                year = fecha.split(" ")[2]
                if int(day) > 31:
                    raise ValueError
                print(f"{year}-{months.index(month)+1:02}-{day.zfill(2)}")
                break
            elif "/" in fecha:
                day = fecha.split("/")[1]
                month = fecha.split("/")[0]
                year = fecha.split("/")[2]
                if int(day) > 31 or int(month) > 12:
                    raise ValueError
                print(f"{year}-{month.zfill(2)}-{day.zfill(2)}")
                break
        except EOFError:
            break
        except ValueError:
            pass


main()
