import dropbox

class CloudStore:
    def __init__(self,access_token):
        self.access_token = access_token

    def upload_file(self,file_from,file_to):
        dbx= dropbox.Dropbox(self.access_token)

        with open(file_from,'rb') as f:
            dbx.files_upload(f.read(), file_to)

def main():
    access_token = 'sl.Ay7C2qbZyTYyXOFkmGsqkGz-qmWdUCWHOepKbFG42ZFNtG4NnPw9LiAmAUqM5yNoPblS4fMt7krRFbTOPvgXbT7Y18luypIvUD_HHLuaEsJFCfFSHs_SVJrryetJsyvpvascJH8'
    transferData =CloudStore(access_token)
    file_from = 'test.txt'
    file_to = '/test_dropbox/test.txt'
    transferData.upload_file(file_from,file_to)
main()