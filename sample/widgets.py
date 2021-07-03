from django.forms.widgets import HiddenInput
from django_filters.widgets import RangeWidget

class CustomRangeWidget(RangeWidget):
    template_name = 'forms/widgets/range-slider.html'

    def __init__(self, attrs=None):
        widgets = (HiddenInput(), HiddenInput())
        super(RangeWidget, self).__init__(widgets, attrs)

    def get_context(self, name, value, attrs):
        ctx = super().get_context(name, value, attrs)
        cur_min, cur_max = value
        if cur_min is None:
            cur_min = ctx['widget']['attrs']['data-range_min']
        if cur_max is None:
            cur_max = ctx['widget']['attrs']['data-range_max']
        ctx['widget']['attrs'].update({'data-cur_min':cur_min,
                                        'data-cur_max':cur_max})
        base_id = ctx['widget']['attrs']['id']
        for swx, subwidget in enumerate(ctx['widget']['subwidgets']):
            subwidget['attrs']['id'] = base_id + "_" + self.suffixes[swx]
        ctx['widget']['value_text'] = "{} - {}".format(cur_min,cur_max)
        return ctx
