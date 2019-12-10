from src import get_data
import SimpleHTTPServer

generate = raw_input("Do you want to generate new dataset? (y/n): ")

if(generate=='y'):
    get_data.main()

# Implement auto starting server
