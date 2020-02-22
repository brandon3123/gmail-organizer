from __future__ import print_function


class Messages:

    @staticmethod
    def getAllMessages(service):
        results = service.users().messages().list(userId='me').execute()
        return results
