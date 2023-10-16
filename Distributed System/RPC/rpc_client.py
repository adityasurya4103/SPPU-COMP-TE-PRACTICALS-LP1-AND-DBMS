import xmlrpc.client

def main():
    # Create an XML-RPC client
    proxy = xmlrpc.client.ServerProxy("http://localhost:8000/RPC2")

    # Call remote methods
    result_add = proxy.add(5, 3)
    result_subtract = proxy.subtract(10, 4)

    print(f"Addition result: {result_add}")
    print(f"Subtraction result: {result_subtract}")

if __name__ == "__main__":
    main()
