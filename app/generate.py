from src import get_data

generate = input("Do you want to generate new dataset? (y/n): ")

if(generate=='y'):
    get_data.main()
