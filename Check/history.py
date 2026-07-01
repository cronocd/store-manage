from time import strftime
from datetime import date
import os

class History:
    
    DIRECTORY = '/home/testuser/Desktop/Coding/History'
    
    def check_folder(self, name_user):
        try:
            os.makedirs(self.DIRECTORY, exist_ok=True)
            self.start_file(name_user)
        except Exception as e:
            print(f'An error occurred while we were trying create a directory: {e}')
            
            
    def start_file(self, name_user):
        now = strftime("%Y/%m/%d %I:%M:%S")
        file = f'{str(date.today())}.txt'
        road = f'{self.DIRECTORY}/{file}'
        
        try:
            with open(road, 'a') as FILE:
                FILE.write(f'\nHour to started: {now} By {name_user}\n\n')
        except Exception as e:
            print(f'An error Occurred while we were trying to create a file: {e}')
    
    def close_file(self, name_user):
        now = strftime("%Y/%m/%d %I:%M:%S")
        file = f'{str(date.today())}.txt'
        road = f'{self.DIRECTORY}/{file}'
        
        try:
            with open(road, 'a') as FILE:
                FILE.write(f'\nHour to close: {now} By {name_user}\n')
        except Exception as e:
            print(f'An error Occurred while we were trying to create a file: {e}')         
                    
    def log_sales(self, products, name_user, total):
        now = strftime("%Y/%m/%d %I:%M:%S")
        file = f'{str(date.today())}.txt'
        road = f'{self.DIRECTORY}/{file}'
        
        os.makedirs(self.DIRECTORY, exist_ok=True)
        with open(road, 'a') as FILE:
            FILE.write(f'\nProduct--------Quantity, By {name_user}\n')
            for product in products:
                FILE.write(f'{product[0]}---------{product[2]}, {now}\n')
            FILE.write(f'Total:......................{total}\n')
                
        
        
        