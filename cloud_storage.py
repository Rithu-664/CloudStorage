import dropbox

class TransferData:
    def __init__(self, access_token):
        self.access_token = access_token

    def uploadFiles(self, fileFrom, fileTo):
        dbx = dropbox.Dropbox(self.access_token)


        f = open(fileFrom, 'rb')
        dbx.files_upload(f.read(), fileTo)

def main():
    access_token = 'zYq6MPJ7vfIAAAAAAAAAAb5Eatb5ePl7IbM6r0Pa1PQAkvOnNcucYKnwXL8vc9Pd'
    transferData = TransferData(access_token)

    fileFrom = input("Enter the file path to transfer : -")
    fileTo = input("enter the full path to upload to dropbox:- ")

    transferData.uploadFiles(fileFrom, fileTo)
    print("file has been moved")


main()