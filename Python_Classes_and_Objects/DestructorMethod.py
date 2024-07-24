class FileHandler:
    def __init__(self, filename):
        self.filename = filename
        self.file = open(self.filename, 'r')
    def read_data(self):
        return self.file.read()
    def __del__(self):
        print("Inside __Del()__ method...") #To check if this method is called.
        self.file.close()
file_obj = FileHandler('sample.txt')
print(file_obj.read_data())