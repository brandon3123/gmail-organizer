from __future__ import print_function
from apiRoutes.Messages import Messages

# If modifying these scopes, delete the file token.pickle.
SCOPES = ['https://www.googleapis.com/auth/gmail.readonly']


def main():
    messages_api = Messages()

    results = messages_api.get_all_messages()
    print(results)

    for message in results:
        # messages_api.get_message(message['id'])
        print(message['id'])

if __name__ == '__main__':
    main()