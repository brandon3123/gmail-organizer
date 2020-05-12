from __future__ import print_function
from apiRoutes.Messages import Messages
from apiRoutes.Labels import Labels

messages_api = Messages()
labels_api = Labels()


def main():

    results = messages_api.get_all_messages()

    # for message in results['messages']:
    #     messagesData = messages_api.get_message(message['id'])
        # print(messagesData)


    # test_label = labels_api.create_label('test')

    # print(test_label)

    # all_labels = labels_api.get_all_labels()

    # for label in all_labels['labels']:
    #     print(labels_api.get_label(label['id']))

if __name__ == '__main__':
    main()