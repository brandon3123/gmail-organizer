from __future__ import print_function
from services.EmailSortingService import EmailSortingService
from services.LabelService import LabelService
from enums.Email import Email
from services.MessageService import MessageService

label_service = LabelService()
sorting_service = EmailSortingService()
message_service = MessageService()

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
    # sorting_service.delete_emails_from(TO_DELETE_FROM)
    # sorting_service.delete_promotions()

    sorting_service.sort_job_postings()
    sorting_service.sort_amazon_orders()
    sorting_service.sort_rentals()
    sorting_service.delete_promotions()
    sorting_service.delete_social()

if __name__ == '__main__':
    main()