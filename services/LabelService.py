from apiRoutes.LabelApi import LabelApi
from enums.Color import Color

label_api = LabelApi()


class LabelService:

    def all_labels(self):
        return label_api.get_all_labels()

    def create_label(self, name):
        return label_api.create_label(name)

    def create_label_with_color(self, name, bg_color, text_color):
        return label_api.create_label_with_color(name, bg_color, text_color)

    def label_with_name(self, name):
        for label in self.all_labels():
            if label['name'] == name:
                return label
        return None

    def create_label_if_not_found(self,
                                  label_name,
                                  bg_color,
                                  text_color=Color.WHITE_GRAY.value):
        label = self.label_with_name(label_name)
        if label is None:
            label = self.create_label_with_color(label_name, bg_color, text_color)
        return label;

    def name(self, label):
        return label['name']

    def bg_color(self, label):
        return str(self.color(label)['backgroundColor'])

    def color(self, label):
        return label['color']

    def text_color(self, label):
        return str(self.color(label)['textColor'])
