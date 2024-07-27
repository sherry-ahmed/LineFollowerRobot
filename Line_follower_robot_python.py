import socket


HOST = '192.168.133.16'  # Server IP address
PORT = 8080



def process_data(data):
    a1 = 80
    a2 = 80
    processed_data= (0,0,0,0)
    if (data[0]==0 and data[1]==0 and data[2]==1 and data[3]==0 and data[4]==0):
        processed_data= (a1,0,a2,0)
    elif (data[0]==0 and data[1]==0 and data[2]==1 and data[3]==1 and data[4]==0):
        processed_data= (a1,0,0,0)
    elif (data[0]==0 and data[1]==1 and data[2]==1 and data[3]==0 and data[4]==0):
        processed_data= (0,0,a2,0)
    elif (data[0]==0 and data[1]==0 and data[2]==0 and data[3]==1 and data[4]==0):
        processed_data= (a1,0,0,0)
    elif (data[0]==0 and data[1]==1 and data[2]==0 and data[3]==0 and data[4]==0):
        processed_data= (0,0,a2,0)
    elif (data[0]==1 and data[1]==1 and data[2]==1 and data[3]==1 and data[4]==1):
        processed_data= (a1,0,a2,0)    
    elif (data[0]==0 and data[1]==0 and data[2]==1 and data[3]==0 and data[4]==1):
        processed_data= (0,0,a2,0)
    elif (data[0]==1 and data[1]==0 and data[2]==0 and data[3]==0 and data[4]==0):
        processed_data= (0,0,a2,0)
    elif (data[0]==0 and data[1]==0 and data[2]==0 and data[3]==0 and data[4]==1):
        processed_data= (a1,0,0,0)
    elif (data[0]==1 and data[1]==0 and data[2]==1 and data[3]==0 and data[4]==0):
        processed_data= (0,0,a2,0) 
    elif (data[0]==0 and data[1]==1 and data[2]==1 and data[3]==1 and data[4]==0):
        processed_data= (a1,0,a2,0) 
    elif (data[0]==0 and data[1]==0 and data[2]==0 and data[3]==0 and data[4]==0):
        processed_data= (a1,0,a2,0) 
    elif (data[0]==0 and data[1]==1 and data[2]==0 and data[3]==1 and data[4]==0):
        processed_data= (a1,0,a2,0)
    elif (data[0]==1 and data[1]==0 and data[2]==0 and data[3]==0 and data[4]==1):
        processed_data= (a1,0,a2,0)
    elif (data[0]==1 and data[1]==0 and data[2]==0 and data[3]==1 and data[4]==1):
        processed_data= (a1,0,0,0)
    elif (data[0]==1 and data[1]==0 and data[2]==1 and data[3]==0 and data[4]==1):
        processed_data= (a1,0,a2,0) 
    elif (data[0]==0 and data[1]==1 and data[2]==1 and data[3]==1 and data[4]==0):
        processed_data= (a1,0,0,0) 
    elif (data[0]==1 and data[1]==1 and data[2]==0 and data[3]==0 and data[4]==1):
        processed_data= (a1,0,a2,0)
    elif (data[0]==0 and data[1]==1 and data[2]==1 and data[3]==1 and data[4]==1):
        processed_data= (a1,0,a2,0)
    elif (data[0]==1 and data[1]==1 and data[2]==1 and data[3]==0 and data[4]==1):
        processed_data= (a1,0,a2,0)
    elif (data[0]==0 and data[1]==1 and data[2]==0 and data[3]==0 and data[4]==1):
        processed_data= (a1,0,a2,0)
    elif (data[0]==1 and data[1]==0 and data[2]==0 and data[3]==1 and data[4]==0):
        processed_data= (a1,0,a2,0)
    elif (data[0]==1 and data[1]==0 and data[2]==1 and data[3]==1 and data[4]==1):
        processed_data= (a1,0,a2,0)
    elif (data[0]==1 and data[1]==1  and data[2]==0 and data[3]==0 and data[4]==0):
        processed_data= (a1,0,a2,0)
    elif (data[0]==1 and data[1]==1  and data[2]==1 and data[3]==1 and data[4]==1):
        processed_data = (a1,0,a2,0)
    elif (data[0]==0 and data[1]==0  and data[2]==0 and data[3]==1 and data[4]==1):
        processed_data = (a1,0,a2,0) 
    print(processed_data)       
    return processed_data

def run_server():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
        server_socket.bind((HOST, PORT))
        server_socket.listen()

        print(f"Server is listening on {HOST}:{PORT}")

        while True:
            connection, address = server_socket.accept()
            with connection:
                print(f"Connected to {address}")

                while True:
                    data = connection.recv(1024)
                    if not data:
                        print("Connection closed.")
                        break

                    cleaned_data = data.decode('utf-8').strip()
                    sensor_data = cleaned_data.split(',')
                    
                    if len(sensor_data) > 4:
                        sensor_data = sensor_data[:5] 
                        sensor_data = [int(value) for value in sensor_data]
                        print("Received Sensor Data:", sensor_data)

                        # Process the data
                        processed_data = process_data(sensor_data)                        
                        # Convert processed_data to string before sending
                        processed_data_str = ','.join(map(str, processed_data))
                        connection.send((processed_data_str + '\n').encode())


run_server()

'''
elif(data[4]==1):
            while data[0] != 1:
                processed_data = (a1, 0, 0, 0)
'''