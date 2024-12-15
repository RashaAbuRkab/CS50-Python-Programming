name = input("File Name: ").strip().lower()
if '.' in name:
    suffix = name.rsplit('.', 1)[-1]
else:
    suffix = ""

match suffix:
    case "gif":
        print("image/gif")
    case "jpg" | "jpeg":
        print("image/jpeg")  # Explicitly output image/jpeg for both jpg and jpeg
    case "png":
        print("image/png")
    case "pdf":
        print("application/pdf")
    case "txt":
        print("text/plain")
    case "zip":
        print("application/zip")
    case _:
        print("application/octet-stream")
