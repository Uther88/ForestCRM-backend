from django import forms

from . import models


class DriverTaskForm(forms.ModelForm):
    arrival = forms.DateTimeField(input_formats=["%a %b %d %Y %H:%M:%S", '%Y-%m-%dT%H:%M:%S'])
    departure = forms.DateTimeField(input_formats=["%a %b %d %Y %H:%M:%S", '%Y-%m-%dT%H:%M:%S'])
    
    class Meta:
        model = models.DriverTask
        fields = '__all__'


class WayBillForm(forms.ModelForm):

    class Meta:
        model = models.Waybill
        exclude = ['fuel_distribution']

    def __init__(self, *args, **kwargs):
        super(WayBillForm, self).__init__(*args, **kwargs)
        self.fields['date'].input_formats = ['%a %b %d %Y', '%Y-%m-%d']
        self.fields['period_from'].input_formats = ['%a %b %d %Y', '%Y-%m-%d']
        self.fields['period_to'].input_formats = ['%a %b %d %Y', '%Y-%m-%d']
        self.fields['dep_date'].input_formats = ["%a %b %d %Y %H:%M:%S", '%Y-%m-%dT%H:%M:%S']
        self.fields['dep_fact'].input_formats = ["%a %b %d %Y %H:%M:%S", '%Y-%m-%dT%H:%M:%S']
        self.fields['ret_date'].input_formats = ["%a %b %d %Y %H:%M:%S", '%Y-%m-%dT%H:%M:%S']
        self.fields['ret_fact'].input_formats = ["%a %b %d %Y %H:%M:%S", '%Y-%m-%dT%H:%M:%S']


# Outfits
class OutfitForm(forms.ModelForm):
    class Meta:
        model = models.Outfit
        exclude = ['fuel_distribution', 'act_spisanya', 'recycling_list']

    def __init__(self, *args, **kwargs):
        super(OutfitForm, self).__init__(*args, **kwargs)
        self.fields['begin'].input_formats = ['%a %b %d %Y', '%Y-%m-%d']
        self.fields['end'].input_formats = ['%a %b %d %Y', '%Y-%m-%d']


class OutfitWorkForm(forms.ModelForm):
    class Meta:
        model = models.OutfitWork
        fields = '__all__'


class OutfitTableForm(forms.ModelForm):
    class Meta:
        model = models.OutfitTable
        fields = '__all__'


class OutfitPostingForm(forms.ModelForm):
    class Meta:
        model = models.OutfitPosting
        fields = '__all__'


class OutfitExpenseForm(forms.ModelForm):
    class Meta:
        model = models.OutfitExpense
        fields = '__all__'


# Tractor RegForm

class TractorRegFormWorkForm(forms.ModelForm):
    class Meta:
        model = models.TractorRegFormWork
        exclude = ['fuel_distribution']

    def __init__(self, *args, **kwargs):
        super(TractorRegFormWorkForm, self).__init__(*args, **kwargs)
        self.fields['date'].input_formats = ['%a %b %d %Y', '%Y-%m-%d']


class TractorRegFormForm(forms.ModelForm):
    class Meta:
        model = models.TractorRegForm
        fields = '__all__'
        
    def __init__(self, *args, **kwargs):
        super(TractorRegFormForm, self).__init__(*args, **kwargs)
        self.fields['date'].input_formats = ['%a %b %d %Y', '%Y-%m-%d']


class SvodnayaZapisForm(forms.ModelForm):
    class Meta:
        model = models.SvodnayaZapis
        fields = '__all__'

class SvodnayaVedomostForm(forms.ModelForm):
    class Meta:
        model = models.SvodnayaVedomost
        exclude = ['created_date', 'conducted']

    def __init__(self, *args, **kwargs):
        super(SvodnayaVedomostForm, self).__init__(*args, **kwargs)
        self.fields['date'].input_formats = ['%a %b %d %Y', '%Y-%m-%d']


class NakopitelnayaVedomostForm(forms.ModelForm):
    class Meta:
        model = models.NakopitelnayaVedomost
        exclude = ['created_date', 'conducted']

    def __init__(self, *args, **kwargs):
        super(NakopitelnayaVedomostForm, self).__init__(*args, **kwargs)
        self.fields['date'].input_formats = ['%a %b %d %Y', '%Y-%m-%d']


class WorkTimeEntryForm(forms.ModelForm):
    class Meta:
        model = models.WorkTimeEntry
        fields = '__all__'


class WorkTimeTableForm(forms.ModelForm):
    class Meta:
        model = models.WorkTimeTable
        exclude = ['created_date']

    def __init__(self, *args, **kwargs):
        super(WorkTimeTableForm, self).__init__(*args, **kwargs)
        self.fields['date'].input_formats = ['%a %b %d %Y', '%Y-%m-%d']


class ForestArrivalReportForm(forms.ModelForm):
    class Meta:
        model = models.ForestArrivalReport
        exclude = ['created_date']

    def __init__(self, *args, **kwargs):
        super(ForestArrivalReportForm, self).__init__(*args, **kwargs)
        self.fields['date'].input_formats = ['%a %b %d %Y', '%Y-%m-%d']


class RecyclingListForm(forms.ModelForm):
    class Meta:
        model = models.RecyclingList
        exclude = ['created_date']

    def __init__(self, *args, **kwargs):
        super(RecyclingListForm, self).__init__(*args, **kwargs)
        self.fields['date'].input_formats = ['%a %b %d %Y', '%Y-%m-%d']


class HandoutForm(forms.ModelForm):

    class Meta:
        model = models.Handout
        exclude = ['created_date']

    def __init__(self, *args, **kwargs):
        super(HandoutForm, self).__init__(*args, **kwargs)
        self.fields['date'].input_formats = ['%a %b %d %Y', '%Y-%m-%d']


class FuelDistributionForm(forms.ModelForm):

    class Meta:
        model = models.FuelDistribution
        exclude = ['created_date']

    def __init__(self, *args, **kwargs):
        super(FuelDistributionForm, self).__init__(*args, **kwargs)
        self.fields['date'].input_formats = ['%a %b %d %Y', '%Y-%m-%d']


class ActSpisanyaForm(forms.ModelForm):

    class Meta:
        model = models.ActSpisanya
        exclude = ['created_date']

    def __init__(self, *args, **kwargs):
        super(ActSpisanyaForm, self).__init__(*args, **kwargs)
        self.fields['date'].input_formats = ['%a %b %d %Y', '%Y-%m-%d']