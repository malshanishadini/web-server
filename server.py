import socket

host = '127.0.0.1' 
port = 8888
folder = 'abc'

socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

print("Starting server on "+ host + ":" + str(port))

socket.bind((host,port))  

socket.listen(1) 

while True:
    connection,address = socket.accept() 

    try: 
        request = connection.recv(1024).decode() 
        print(request)
        if not request:
            continue
            
    except Exception as e:
        print("Request Error" + str(e))
        break

    try:
        request_file = request.split(' ')[1] 
        request_file = request_file.split('?')[0]  

        if request_file == "/": 
            request_file = "/index.html" 

        f_path = folder + request_file
        f_type = request_file.split('.')[1]
        
        file = open(f_path, 'rb') 
        response = file.read()
        file.close()
            
        print('File-Path: ' , f_path)
        print('File-Type: ' , f_type)

        header = 'HTTP/1.1 200 OK\n Connection:close\n'  
        
        if f_type == 'html':
            header += 'Content-Type: text/html\n\n'
        elif f_type == 'png':
            header += 'Content-Type: image/png\n\n'
        elif f_type == 'jpg' or f_type == 'jpeg':
            header += 'Content-Type: image/jpeg\n\n'
        elif f_type == 'pdf':
            header += 'Content-Type: application/pdf\n\n'

    except Exception as e:
        header = 'HTTP/1.1 404 Not Found\n Connection:close\n\n'
        response = "<h1>Error 404: File not found</h1>".encode()
 
    last_response = header.encode()  
    last_response += response
    
    connection.send(last_response) 
    connection.close() 
    


