from django.core.exceptions import ValidationError

class ContainsLetterValidator:
    def validate(self,password,user=None):
        if not any(char.isalpha() for char in password):
            raise ValidationError('Le mot de doit contenir une lettre',code='password_no_letters')
        
    def get_help_text(self):
        return 'votre mot de passe doit contenir au moins une lettre'
    
class ContainsNumberValidator:
    def validate(self,password,user=None):
        if not any(char.is_digit() for char in password):
            raise ValidationError(code='password_no_letters')
        
    def get_help_text(self):
        return "Votre mot de passe doit contenir au moins un chiffre"