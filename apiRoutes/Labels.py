from apiRoutes.ApiRoute import ApiRoute


def label_json(label_name, message_visibility='show', label_visibility='labelShow'):
    """Create Label object.

    Args:
      label_name: The name of the Label.
      message_visibility: Message list visibility, show/hide.
      label_visibility: Label list visibility, labelShow/labelHide.

    Returns:
      Created Label.
    """
    label = {'messageListVisibility': message_visibility,
             'name': label_name,
             'labelListVisibility': label_visibility}

    return label


class Labels(ApiRoute):

    def get_all_labels(self):
        return self.api().list(userId='me').execute()

    def get_label(self, id):
        return self.api().get(userId='me', id=id).execute()

    def create_label(self, name):
        label = label_json(name)
        return self.api().create(userId='me', body=label).execute()

    def api(self):
        return super().gmail_api().users().labels()
