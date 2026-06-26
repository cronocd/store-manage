from time import strftime
from datetime import date
import os

class History:
    
    DIRECTORY = '/home/testuser/Desktop/Coding/History'
    
    def check_folder(self, name_user):
        try:
            if os.path.isdir(self.DIRECTORY):
                self.start_close_file(name_user)
            else:
                os.mkdir(self.DIRECTORY)
                print('We created the directory')
                self.start_close_file(name_user)
        except Exception as e:
            print(f'An error occurred while we were trying create a directory: {e}')
            
            
    def start_close_file(self, name_user):
        now = strftime("%Y/%m/%d %I:%M:%S")
        file = f'{str(date.today())}.txt'
        road = f'{self.DIRECTORY}/{file}'
        
        try:
            if os.path.exists(road):
                with open(road, 'a') as FILE:
                    FILE.write(f'Hour to close: {now} By {name_user}')
            else:
                with open(road, 'a') as FILE:
                    FILE.write(f'Hour to started: {now} By {name_user}\n\n')
        except Exception as e:
            print(f'An error Occurred while we were trying to create a file: {e}')
                
    def log_sales(self, products, name_user):
        now = strftime("%Y/%m/%d %I:%M:%S")
        file = f'{str(date.today())}.txt'
        road = f'{self.DIRECTORY}/{file}'
        
        with open(road, 'a') as FILE:
            FILE.write(f'Product--------Quantity, By {name_user}\n')
            for product in products:
                FILE.write(f'{product[0]}---------{product[2]}, {now}\n')
                
        
        
        