from __future__ import print_function
from apiRoutes.Messages import Messages
from apiRoutes.Labels import Labels
from services.LabelService import LabelService
from services.MessageService import MessageService

messages_api = Messages()
labels_api = Labels()
message_service = MessageService()
label_service = LabelService()



def main():

    # results = messages_api.get_all_messages()
    message_service.sort_transfers()

    # label_service.create_label('test')


    # for message in results['messages']:
    #     messagesData = messages_api.get_message(message['id'])
    #     print(messagesData)

    # print(results['messages'])

    # test_label = labels_api.create_label('test')

    # print(test_label)

    # all_labels = labels_api.get_all_labels()

    # for label in all_labels['labels']:
    #     print(labels_api.get_label(label['id']))

    # messages_api.add_labels('172006893e87aea4', [test_label['id']])

if __name__ == '__main__':
    main()