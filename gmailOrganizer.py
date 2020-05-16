from __future__ import print_function
from services.EmailSortingService import EmailSortingService
from services.LabelService import LabelService
from enums.Email import Email

label_service = LabelService()
sorting_service = EmailSortingService()

TO_DELETE_FROM = [
    Email.LINKEDIN_DOMAIN.value,
    Email.SAIT_ALUMNI.value,
    Email.COURSERA_NO_REPLY.value,
    Email.TILE_NO_REPLY.value,
    Email.TURBO_TAX.value,
]

def main():

    # results = messages_api.get_all_messages()
    # sorting_service.sort_money_transfers()
    # sorting_service.sort_job_postings()
    # sorting_service.sort_amazon_orders()
    # label_service.create_label('test')
    sorting_service.delete_emails_from(TO_DELETE_FROM)
    # sorting_service.delete_promotions()

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