from src.controller import Controller

def run():
    agent = Controller()
    while True:
        query = input("\nYou: ")
        if query.lower() in ["quit", "exit"]:
            break
        answer = agent.handle_query(query)
        print(f"\nAgent: {answer}")

if __name__ == "__main__":
    run()
