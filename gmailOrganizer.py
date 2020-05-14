from __future__ import print_function
from services.EmailSortingService import EmailSortingService


sorting_service = EmailSortingService()


def main():

    # results = messages_api.get_all_messages()
    sorting_service.sort_money_transfers()

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