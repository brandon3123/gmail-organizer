from apiRoutes.ApiRoute import ApiRoute


class LabelApi(ApiRoute):

    def get_all_labels(self):
        return self.__api().list(userId='me').execute()['labels']

    def get_label(self, id):
        return self.__api().get(userId='me', id=id).execute()

    def create_label(self, name):
        label = self.__label_json(name)
        return self.__api().create(userId='me', body=label).execute()

    def create_label_with_color(self, name, bg_color, text_color):
        color = self.__color_json(bg_color, text_color)
        label = self.__label_json(name, color)
        return self.__api().create(userId='me', body=label).execute()

    def __api(self):
        return super().gmail_api().users().labels()

    def __label_json(self,
                     label_name=None,
                     color=None):
        """Create Label object.

        Args:
          label_name: The name of the Label.
          message_visibility: Message list visibility, show/hide.
          label_visibility: Label list visibility, labelShow/labelHide.

        Returns:
          Created Label.
        """
        label = {
            'messageListVisibility': 'show',
            'name': label_name,
            'labelListVisibility': 'labelShow',
            'color': color
        }

        return label

    def __color_json(self, bg_color=None, text_color=None):
        return {
            'textColor': text_color,
            'backgroundColor': bg_color,
        }
