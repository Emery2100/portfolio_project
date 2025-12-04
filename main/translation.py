from modeltranslation.translator import register, TranslationOptions
from .models import Skill, Education, Project

@register(Skill)
class SkillTranslationOptions(TranslationOptions):
    fields = ('name', 'level')

@register(Education)
class EducationTranslationOptions(TranslationOptions):
    fields = ('degree', 'institution', 'description')

@register(Project)
class ProjectTranslationOptions(TranslationOptions):
    fields = ('title', 'summary')
