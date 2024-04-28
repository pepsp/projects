fileName = input("File name: ").casefold().strip()
ext = fileName.split(".")[-1]

match ext:
    case "jpg" | "jpeg":
        print("image/jpeg")
    case "gif" | "png":
        print("image/" + ext)
    case "pdf" | "zip":
        print("application/" + ext)
    case "txt":
        print("text/plain")
    case _:
        print("application/octet-stream")
