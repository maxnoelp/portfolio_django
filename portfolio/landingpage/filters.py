import django_filters
from django_filters import ChoiceFilter

from portfolio.landingpage.models import CodeProjects
from portfolio.landingpage.utils import CODE_LANGUAGE


class ProjectTagsFilter(django_filters.FilterSet):
    filtered_tags = ChoiceFilter(
        choices=CODE_LANGUAGE,
        field_name="tag",
        label="Tag",
        empty_label="All Tags",
    )

    class Meta:
        model = CodeProjects
        fields = ["tag"]
