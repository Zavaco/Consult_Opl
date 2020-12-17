from modeltranslation.translator import translator, TranslationOptions
from .models import Teacher, Navbar


class NavbarTranslationOptions(TranslationOptions):
    fields = ('home', 'about')


translator.register(Navbar, NavbarTranslationOptions)