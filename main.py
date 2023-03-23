from chatbot.gpt import GPT
from chatbot.langchain_memory import LangChainMemory
from chatbot.pinecone_store import PineconeStore
from chatbot.postgres_database import PostgresDatabase
from config import OPENAPI_KEY, PINECONE_API_KEY, DB_CREDENTIALS

def display_clients(clients):
    if not clients:
        print("No clients added.")
    else:
        for client_id, client_data in clients.items():
            print(f"{client_id}. {client_data['name']}")

def main():
    # Initialize components
    db = PostgresDatabase(DB_CREDENTIALS)
    pinecone_store = PineconeStore(PINECONE_API_KEY)
    langchain_memory = LangChainMemory()
    gpt = GPT(OPENAPI_KEY)

    while True:
        print("\nWhat do you want to do?")
        print("1. Use assistant")
        print("2. Add a client")
        print("3. Exit")
        choice = input("Enter your choice (1/2/3): ")

        if choice == "1":
            # Use assistant
            clients = db.load_clients()
            print("\nWhich client are you working on?")
            display_clients(clients)

            client_id = int(input("Enter the client ID: "))
            client_data = clients.get(client_id, None)

            if not client_data:
                print("Invalid client ID. Please try again.")
                continue

            while True:
                print("\nWhat do you want to do?")
                print("1. Run the assistant")
                print("2. Edit the master prompt")
                print("3. Go back")
                sub_choice = input("Enter your choice (1/2/3): ")

                if sub_choice == "1":
                    # Run the assistant
                    while True:
                        message = input("You: ")
                        if message.lower() == "exit":
                            break

                        # Load client context
                        context = db.load_client_context(client_id)

                        # Chat with GPT
                        response = gpt.chat(context, message)

                        # Update context and save it to the database
                        context.append({"role": "user", "content": message})
                        context.append({"role": "assistant", "content": response})
                        db.save_client_context(client_id, context)

                        print(f"Assistant: {response}")

                elif sub_choice == "2":
                    # Edit the master prompt
                    new_prompt = input("Enter the new master prompt: ")
                    client_data["master_prompt"] = new_prompt
                    db.save_client_context(client_id, context)

                elif sub_choice == "3":
                    break
                else:
                    print("Invalid choice. Please try again.")

        elif choice == "2":
            # Add a client
            client_name = input("What is the name of the client's business? ")
            master_prompt = input("What is my role, and what are the details of their product or service? ")

            new_client = {
                "name": client_name,
                "context": [{"role": "system", "content": master_prompt}]
            }
            db.add_client(new_client)

        elif choice == "3":
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()


    # TODO: Connect Render Database
    # TODO: Get it working
    # TODO: Figure out memory with langchain and wheather we need pinecone
    # TODO: Add contribution and license urls to Readme