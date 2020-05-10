from __future__ import print_function
from apiRoutes.ApiRoute import ApiRoute


class Messages(ApiRoute):

    def get_all_messages(self):
        return self.messages_api().list(userId='me').execute()

    def get_message(self, id):
        return self.messages_api().get(id=id).execute()

    def messages_api(self):
        return super().gmail_api().users().messages()
