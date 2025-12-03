from django.core.exceptions import ValidationError
from django.utils.translation import gettext as _

class ComplexityValidator:

    def validate(self,password , user =None):
        minimum_requirment = 1
        capitals =[char for char in password if char.isupper()]
        lowers = [char for char in password if char.islower()]
        numbers = [char for char in password if char.isdigit()]
        special = [char for char in password if char.isalnum()]


        if(len(capitals)<minimum_requirment or
           len(lowers)<minimum_requirment or
           len(numbers)<minimum_requirment or
           len(special)<minimum_requirment):
            raise ValidationError(_("You need at leas one uppercase"),code="You need atleast one uppercase ...")
        

class CharacterRepeatValidator:
    def validate(self , password ,user=None):
        for char in password:
            if char * 3 in password:
                raise ValidationError(
                    _("You can not repeat one character more than 2 times in succession"),
                    code="you cannot repeat one charact..."
                )