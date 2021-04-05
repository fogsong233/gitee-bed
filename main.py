from giteebed.pic import Pic

if __name__ == '__main__':
    print(Pic(token = "your token",
              owner = "your name",
              repo = "your repo").upload_with_time_path(file_path = r"file path"))

