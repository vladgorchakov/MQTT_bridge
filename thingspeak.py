import socket
import requests


class Channel:
    def __init__(self, api_key, connection) -> None:
        self.__host = "https://api.thingspeak.com/"
        self.__api_key = api_key
        self.__update_url = f'{self.__host}update?api_key={api_key}' # + '&' + 'field'
        self.__fields = {} #channels
        self.connection = connection

    
    @staticmethod
    def check_sending(data) -> bool:
        try:
            num_get = int(str(data).split('\n')[-1])
        except:
            return False
        else:
            if num_get != 0:
                print(f'number of request: {num_get}')
                return True
            else:
                return False
    
    
    def __send(self, url):
        try:
            data = self.connection.get(url)
        except:
            return False
        else:
            print(f'status code: {data.status_code}')
            if data.status_code==200:
                return self.check_sending(data.text)
            
    
    def show_status(self, status):
        if status:
            print('message delivered: Yes')
        else:
            print('message delivered: No')


    def write_field(self, value: float, field_id: int) -> None:
        url = self.__update_url + f'&field{field_id}={value}'
        
        self.show_status(self.__send(url))
            
    
    def write_fields(self, data:dict):
        url = self.__update_url
        for field, value in data.items():
            url += f'&field{field}={value}'
            
        self.show_status(self.__send(url))
        


def main():
	pass
     
        
if __name__=='__main__':
    main()
