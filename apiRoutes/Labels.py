from apiRoutes.ApiRoute import ApiRoute


class Labels(ApiRoute):

    def get_all_labels(self):
        return self.api().list(userId='me').execute()['labels']

    def get_label(self, id):
        return self.api().get(userId='me', id=id).execute()

    def create_label(self, name):
        label = self.label_json(name)
        return self.api().create(userId='me', body=label).execute()

    def create_label_with_color(self, name, bg_color, text_color):
        color = self.color_json(bg_color, text_color)
        label = self.label_json(name, color)
        return self.api().create(userId='me', body=label).execute()

    def api(self):
        return super().gmail_api().users().labels()

    def label_json(self,
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

    def color_json(self, bg_color=None, text_color=None):
        return {
                'textColor': text_color,
                'backgroundColor': bg_color,
            }
